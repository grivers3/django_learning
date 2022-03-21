from django.contrib import admin

from . import models
#from .models import Notes

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(models.Notes, NotesAdmin)
#admin.site.register(Notes, NotesAdmin)
