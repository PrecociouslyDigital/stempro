from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from app.forms import CustomUserCreationForm, CustomUserChangeForm
from app.models import CustomUser, SubscribeEmail, Course, TutorActive, InvolvedActive, Program, RegisterActive, SubscribePresentation, Event, SignupEvent

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

class RegisterActiveAdmin(admin.ModelAdmin):
    list_display = ('active_name', 'who_register', 'type', 'register_date', 'is_paid')
    list_filter = ('active_name', 'type', 'register_date', 'is_paid')
    #change_list_template = 'admin/register_active.html'

class SubscribePresentationAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'cellphone', 'grade', 'wechat', 'schoolName')

class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'when', 'where', 'summary', 'capacity')

class SignupEventAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'event_name', 'number', 'register_date', 'is_paid')

admin.site.site_header = "StemPro Dashboard"
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SubscribeEmail)
admin.site.register(Course)
admin.site.register(TutorActive)
admin.site.register(InvolvedActive)
admin.site.register(Program)
admin.site.register(RegisterActive, RegisterActiveAdmin)
admin.site.register(SubscribePresentation, SubscribePresentationAdmin)
admin.site.register(Event, EventsAdmin)
admin.site.register(SignupEvent, SignupEventAdmin)

