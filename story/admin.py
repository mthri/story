from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry

from .models import Story, Tag


class CustomAdmin(admin.AdminSite):
    site_title = 'داستان من'
    site_header = site_title

admin_site = CustomAdmin()


@admin.register(User, site=admin_site)
class NewUserAdmin(UserAdmin):

    def get_readonly_fields(self, request, obj):
        return ('date_joined', 'last_login')


@admin.register(Story, site=admin_site)
class StoryAdmin(admin.ModelAdmin):
    search_fields = ('text', 'id', )
    list_filter = ('accept', )
    list_display = ('title', 'view', 'accept', )
    actions = ('accept_action', )
    readonly_fields = (
        'user', 'id', 'slug', 'title', 
        'preview', 'tags', 'text', 'view',
        'created_at', 'modified_at', 
    )

    @admin.display(description='تایید')
    def accept_action(self, request, obj):
        obj.update(accept=True)

    def has_add_permission(self, request):
        return False
    
    def save_model(self, request, obj, form, change):
        update_fields = []
        if change: 
            if form.initial['accept'] != form.cleaned_data['accept']:
                update_fields.append('accept')

        obj.save(update_fields=update_fields)


@admin.register(Tag, site=admin_site)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_filter = ('accept', )


@admin.register(LogEntry, site=admin_site)
class LogEntryAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False