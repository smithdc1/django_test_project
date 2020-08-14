from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from forms.forms import (
    BooleanForm, RadioBooleanForm,
    ChoicesForm, RadioChoicesForm,
    DefaultForm, RadioDefaultForm,
    ChoicesDefaultForm, RadioChoicesDefaultForm
)
from .models import Boolean, ChoicesAndDefault, Choices, Default

def index(request):
    boolean_form = BooleanForm(request.POST or None)
    if "boolean_form" in request.POST:
        if boolean_form.is_valid():
            boolean_form.save()

    radio_boolean_form = RadioBooleanForm(request.POST or None)
    if "radio_boolean_form" in request.POST:
        if radio_boolean_form.is_valid():
            radio_boolean_form.save()

    choices_form = ChoicesForm(request.POST or None)
    if "choices_form" in request.POST:
        if choices_form.is_valid():
            choices_form.save()

    radio_choices_form = RadioChoicesForm(request.POST or None)
    if "radio_choices_form" in request.POST:
        if radio_choices_form.is_valid():
            radio_choices_form.save()

    default_form = DefaultForm(request.POST or None)
    if "default_form" in request.POST:
        if default_form.is_valid():
            default_form.save()

    radio_default_form = RadioDefaultForm(request.POST or None)
    if "radio_default_form" in request.POST:
        if radio_default_form.is_valid():
            radio_default_form.save()

    choices_default_form = ChoicesDefaultForm(request.POST or None)
    if "choices_default_form" in request.POST:
        if choices_default_form.is_valid():
            choices_default_form.save()

    radio_choices_default_form = RadioChoicesDefaultForm(request.POST or None)
    if "radio_choices_default_form" in request.POST:
        if radio_choices_default_form.is_valid():
            radio_choices_default_form.save()

    context = {
        "boolean_form": boolean_form,
        "radio_boolean_form": radio_boolean_form,
        "choices_form": choices_form,
        "radio_choices_form": radio_choices_form,
        "default_form": default_form,
        "radio_default_form": radio_default_form,
        "choices_default_form": choices_default_form,
        "radio_choices_default_form": radio_choices_default_form,
    }
    return render(request, 'forms/index.html', context)


def list_view(request):
    pass
