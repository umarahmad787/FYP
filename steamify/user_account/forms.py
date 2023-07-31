from django import forms
from user_account.models import Video
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['id', 'title', 'category', 'video_file']

        id = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))