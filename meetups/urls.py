from django.urls import path
from . import views
from .views import MeetupCreate, MeetupDelete, MeetupUpdate, loginPage
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path('login/', views.loginPage, name='login' ),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.index, name='home' ),
    path('register/', views.register, name='register' ),
    path('participants/<int:pk>', views.participants, name='participants' ),
    path('profile/<int:pk>', views.profile, name='profile' ),
    path('user-meetups/<int:pk>', views.user_meetups, name='user-meetups'),
    path('add-speakers/<int:pk>', views.add_speakers, name='add-speakers'),
    path('user-speakers/<int:pk>', views.user_speakers, name='user-speakers'),
    path('comfirm-registration', views.comfirm_registration, name='comfirm-registration' ),
    path('meetup-create/', MeetupCreate.as_view(), name='meetup-create' ),
    path('meetup-update/<int:pk>', MeetupUpdate.as_view(), name='meetup-update' ),
    path('meetup-delete/<int:pk>', MeetupDelete.as_view(), name='meetup-delete' ),
    path('meetup/<int:pk>', views.meetup_details, name='meetup-details' ),

]