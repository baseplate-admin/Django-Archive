from django import forms
from upload.models import MusicList
from soundcore.models import LibraryGenerator

# Create your forms here

class LibraryGeneratorForm(forms.ModelForm):
    class Meta:
        model = LibraryGenerator
        fields = ['musics']
        musics = forms.ModelMultipleChoiceField(
            queryset=MusicList.objects.all(),
            widget=forms.CheckboxSelectMultiple,
        )
