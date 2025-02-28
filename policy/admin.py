from django.contrib import admin

from .models import PolicyPage


@admin.register(PolicyPage)
class AboutPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if PolicyPage.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False
