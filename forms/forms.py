from django.forms import ModelForm, RadioSelect
from forms.models import Boolean, Default, ChoicesAndDefault, Choices


class BooleanForm(ModelForm):
    class Meta:
        model = Boolean
        fields = '__all__'


class RadioBooleanForm(ModelForm):
    class Meta:
        model = Boolean
        fields = '__all__'
        # only where null=true do we change the widget
        widgets = {
            'both_true': RadioSelect(),
            'null_true': RadioSelect(),
        }


class ChoicesForm(ModelForm):
    class Meta:
        model = Choices
        fields = '__all__'


class RadioChoicesForm(ModelForm):
    class Meta:
        model = Choices
        fields = '__all__'
        widgets = {
            'both_false': RadioSelect(),
            'both_true': RadioSelect(),
            'null_true': RadioSelect(),
            'blank_true': RadioSelect(),
        }



class DefaultForm(ModelForm):
    class Meta:
        model = Default
        fields = '__all__'


class RadioDefaultForm(ModelForm):
    class Meta:
        model = Default
        fields = '__all__'
        widgets = {
            'both_true': RadioSelect(),
            'null_true': RadioSelect(),
        }


class ChoicesDefaultForm(ModelForm):
    class Meta:
        model = ChoicesAndDefault
        fields = '__all__'


class RadioChoicesDefaultForm(ModelForm):
    class Meta:
        model = ChoicesAndDefault
        fields = '__all__'
        widgets = {
            'both_false': RadioSelect(),
            'both_true': RadioSelect(),
            'null_true': RadioSelect(),
            'blank_true': RadioSelect(),
        }
