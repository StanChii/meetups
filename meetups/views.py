from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import MeetupForm, RegForm, UserRegistrationForm, SpeakerForm, ProfileForm
from django.contrib.auth import login, authenticate
from .models import Meetup, MyUser, Speaker
from django.contrib import messages
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

# Create your views here.
def loginPage(request):
    page='Login'
    if request.user.is_authenticated:
        return redirect('home')
    #when submit botti=on is pressed
    if request.method=='POST':  
        email = request.POST.get('email')
        email.lower()
        password = request.POST.get('password')
        try:
            user=MyUser.objects.get(email=email)  
        except:
            messages.error(request, 'email does not exist')
        user=authenticate(request, email=email, password=password)
        if user is not None:
          login(request, user)
          return redirect ('home')
        else:
          messages.error(request, 'Username OR password does not exist')
    context={'page':page}

    return render(request, 'meetups/login.html', context)
def index (request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    meetups=Meetup.objects.all()
    meetups=meetups.filter(
        Q(title__icontains=q)|
        Q(description__icontains=q)|
         Q(location__icontains=q)

        )
    count=meetups.count()
    return render(request, 'meetups/home.html', {'meetups':meetups, 'count':count })
def register(request):
    form=UserRegistrationForm()
    context={'form':form}
    if request.method=='POST':
        form=UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request, user)
            return redirect ('home') 
    return render(request, 'meetups/register.html', context)
def meetup_details(request, pk):
    try:
        meetup=Meetup.objects.get(pk=pk)
        if request.method=='GET':
            registration_form=RegForm()
        else:
            registration_form=RegForm(request.POST)
            if registration_form.is_valid():
                participant=registration_form.save()
                meetup.participant.add(participant)
                return redirect('comfirm-registration')
                
        return render(request, 'meetups/meetup_details.html', {'meetup':meetup, 'form':registration_form})
    
    except Exception as exc:
        return render(request, 'meetups/meetup_details.html')

   


class MeetupCreate(CreateView):
    model=Meetup
    form_class=MeetupForm
    success_url=reverse_lazy('home')
    template_name='meetups/meetup_form.html'
    def form_valid(self, form):
        form.instance.user=self.request.user
        form.instance.slug=form.instance.title.replace(' ', '-')
        return super(MeetupCreate, self).form_valid(form)

class MeetupUpdate(UpdateView):
    model=Meetup
    form_class=MeetupForm
    success_url=reverse_lazy('home')
    template_name='meetups/meetup_form.html'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(MeetupUpdate, self).form_valid(form)

class MeetupDelete(DeleteView):
    model=Meetup
    success_url=reverse_lazy('home')
    template_name='meetups/meetup_delete_form.html'

def comfirm_registration(request):
    return  render(request, 'meetups/comfirm_registration.html')


def user_meetups(request, pk):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    
    user_meetups=Meetup.objects.order_by('-create')
    user_meetups=Meetup.objects.filter(user=pk)

    meetups=user_meetups.filter(
        Q(title__icontains=q)
        
        ) 
    return render(request, 'meetups/user_meetups.html', {'meetups':meetups} )


def add_speakers(request, pk):
   # selected_meetup=Meetup.objects.get(slug=meetup_slug)
    try:
        selected_meetup=Meetup.objects.get(pk=pk)
        
        if request.method=='GET':
            add_speaker_form=SpeakerForm()
        else:
           
            add_speaker_form= SpeakerForm(request.POST, request.FILES)
            if add_speaker_form.is_valid():
                add_speaker_form.instance.user=request.user
                
                speaker=add_speaker_form.save(commit=False)
                add_speaker_form.instance.meetup_name=selected_meetup.title
                speaker=add_speaker_form.save()
                selected_meetup.meetup_speaker.add(speaker)
                return redirect('home')
              
        return render(request, 'meetups/add_speaker.html', {
         'meet_found':True,
         'meetup':selected_meetup,
         'page':False, 
         'form': add_speaker_form ,
         

          })    
   
    except Exception as exc:
     
        return render(request, 'meetups/add_speaker.html', {
         'meet_found':False,
         
     })


def user_speakers(request, pk):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    
 
    user_speakers=Speaker.objects.filter(
        Q(user=pk)&
        Q(name__icontains=q)|
        Q(meetup_name__icontains=q)
        
        ) 
    user_speakers=Speaker.objects.order_by('-id')
    count=user_speakers.count()
    
    return render(request, 'meetups/user_speakers.html', {'speakers':user_speakers, 'count':count} )

def participants(request, pk):
    meetup=Meetup.objects.get(id=pk)
    participants=meetup.participant.all()
    participants=participants.order_by('-id')
    count=participants.count()
    
    return render(request, 'meetups/participants.html', {'participants':participants, 'count':count} )

def profile(request, pk):
    page="Profile"
    user = request.user
    form = ProfileForm(instance=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.id)
    context={'form':form, 'page':page}
    return render(request, 'meetups/profile_form.html', context)