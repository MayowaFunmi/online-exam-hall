from django.contrib import admin
# Register your models here.
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sessions.models import Session

from . forms import CustomUserCreationForm, CustomUserChangeForm
from . models import CustomUser, Candidate, Examiner, CandidateProfile, ExaminerProfile, SchoolAdmin, Location


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'unique_id', 'status', 'first_name', 'last_name']
    list_filter = ['status']
    search_fields = ('status',)


class SessionAdmin(ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']

admin.site.register(Session, SessionAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Candidate)
admin.site.register(SchoolAdmin)
admin.site.register(CandidateProfile)
admin.site.register(Examiner)
admin.site.register(ExaminerProfile)
admin.site.register(Location)

admin.site.site_header = 'Exam Hall Admin Page'