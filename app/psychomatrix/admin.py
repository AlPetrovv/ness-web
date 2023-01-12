from django.contrib import admin

from .models import PsychomatrixBaseContent, PsychomatrixAdditionalContent

admin.site.register(PsychomatrixBaseContent)
admin.site.register(PsychomatrixAdditionalContent)
