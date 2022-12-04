#from django.forms import ModelForm
from django import forms
from . models import Meetup, MyUser, Participant, Speaker
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, TextInput, CheckboxInput
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

class MeetupForm(forms.ModelForm):
     class Meta:
        model=Meetup
        fields=['title', 'from_date',  'to_date', 'meetup_time', 'description', 'organizer_email', 'location_address', 'activate','image',]
        
        widgets = {
            'meetup_date' : DatePickerInput(
                 attrs={
                    "placeholder": "Enter meetup description",
                    "class":"form-control"
                }
            ),
            'from_date' : DatePickerInput(),
            'to_date' : DatePickerInput(),
            'meetup_time':TimePickerInput(),
            'location_address':Textarea(
                attrs={
                    "placeholder": "Enter location address",
                    "class":"form-control"
                }
            ),
            'activate':CheckboxInput(
                attrs={
                    "class": "form-check form-switch",
                     "id":"mySwitch",

                }
            ), 
            'description':Textarea(
                
                attrs={
                    "placeholder": "Enter meetup description",
                    "class":"form-control"
                }
            ), 
            'title':TextInput(
                attrs={
                   "placeholder": "Enter title",
                   "class":"form-control"
                }
            ),
            
            'organizer_email':TextInput(
                attrs={
                   "placeholder": "Enter your email",
                   "class":"form-control"
                }
            ),
            'location_name':TextInput(
                attrs={
                   "placeholder": "Enter location name",
                   "class":"form-control"
                }
            )
           
        }
        
class RegForm(forms.ModelForm):
   class Meta:
      model=Participant
      fields=['email']
      widgets = {
           
            'email':TextInput(
                attrs={
                    "placeholder": "Enter your email",
                    "class":"form-control"
                }
            )
        }


class UserRegistrationForm(UserCreationForm):
   class Meta:
      model=MyUser
      fields=['name', 'username', 'email', 'password1', 'password2']
      widgets = {
            
            
            'name':TextInput(
                attrs={
                   "placeholder": "Enter name",
                   "class":"form-control"
                }
            ),
            'email':TextInput(
                attrs={
                   "placeholder": "Enter email",
                    "class":"form-control"
                }
            ),
            'username':TextInput(
                attrs={
                   "placeholder": "Enter username",
                    "class":"form-control"
                }
            ),
            'phone':TextInput(
                attrs={
                   "placeholder": "Enter phone",
                    "class":"form-control"
                }
            )
         }


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields =['name', 'email','phone', 'bio', 'image']
        widgets = {
            
            'bio':Textarea(
                attrs={
                    "placeholder": "Enter bio",
                    "class":"form-control"
                }
            ),
            'name':TextInput(
                attrs={
                   "placeholder": "Enter name",
                   "class":"form-control"
                }
            ),
            
            'email':TextInput(
                attrs={
                   "placeholder": "Enter your email",
                   "class":"form-control"
                }
            ),
            'phone':TextInput(
                attrs={
                   "placeholder": "Enter  phone no",
                   "class":"form-control"
                }
            )
           
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [ 'name', 'username', 'email', 'user_info', 'image', 'mobile_no', 'birth_day',]
        widgets = {
            'birth_day' : DatePickerInput(),
            'user_info':Textarea(
                attrs={
                    "placeholder": "Enter your bio",
                    "class":"form-control"
                }
            ), 
            'mobile_no':TextInput(
                
                attrs={
                    "placeholder": "Enter mobile no.",
                    "class":"form-control"
                }
            ), 
            'name':TextInput(
                attrs={
                   "placeholder": "Enter name",
                   "class":"form-control"
                }
            ),
            
            'email':TextInput(
                attrs={
                   "placeholder": "Enter your email",
                   "class":"form-control"
                }
            ),
            'username':TextInput(
                attrs={
                   "placeholder": "Enter username",
                   "class":"form-control",
                   "readonly":"readonly"
                }
            )
           
            
        }
