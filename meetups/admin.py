from django.contrib import admin
from . models import MyUser, Meetup, Speaker, Participant

# Register your models here.
class MeetupAdmin(admin.ModelAdmin):
    list_display=('title', 'organizer_email',)
    prepopulated_fields={'slug':('title',)}
admin.site.register(MyUser)
admin.site.register(Meetup,MeetupAdmin )
admin.site.register(Speaker)
admin.site.register(Participant)
