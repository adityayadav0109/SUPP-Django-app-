from django.contrib import admin
from main.models import Feedback
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'description')


admin.site.register(Feedback, FeedbackAdmin)

