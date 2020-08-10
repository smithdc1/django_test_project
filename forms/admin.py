from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Choices, ChoicesAndDefault, Boolean, Default

admin.site.register(Choices)
admin.site.register(ChoicesAndDefault)
admin.site.register(Boolean)
admin.site.register(Default)
