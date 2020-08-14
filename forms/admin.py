from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Choices, ChoicesAndDefault, Boolean, Default


class ChoicesAdmin(admin.ModelAdmin):
    pass


class BooleanAdmin(admin.ModelAdmin):
    pass


admin.site.register(Choices, ChoicesAdmin)
admin.site.register(ChoicesAndDefault)
admin.site.register(Boolean, BooleanAdmin)
admin.site.register(Default)
