from django.contrib import admin

from philosophy.models import Thought


@admin.register(Thought)
class AdminThought(admin.ModelAdmin):
    list_display = [
        'title',
    ]
