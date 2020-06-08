from django import forms
from .models import InputModel
# from .models import Location
#
# class LocationForm(forms.ModelForm):
#     class Meta:
#         model = Location
#         fields = "__all__"


class InputFormModel(forms.ModelForm):
    class Meta:
        model = InputModel
        fields = ('info', )

    def __init__(self, *args, **kwargs):
        super(InputFormModel, self).__init__(*args, **kwargs)
        self.fields['info'].widget = forms.TextInput(attrs={
            'id': 'info',
            'type': 'text',
            'name': 'cord',
            'style': "width:80%; font-size:26px;border-radius:10px;",
            'placeholder': 'Select a location on map!'})