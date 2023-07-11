from django import forms

from barter.models import ItemModel


class CreateAnnouncementForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '6'}))
    place = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(widget=forms.FileInput(
        attrs={
            'class': 'form-control form-control-sm',
            'id': 'formFileSm',
            'type': 'file',
        }
    ))

    class Meta:
        model = ItemModel
        fields = ('title', 'description', 'place', 'photo')
