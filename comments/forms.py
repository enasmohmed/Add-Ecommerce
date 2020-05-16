from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment','image')
        widgets = {
        'comment': forms.Textarea(attrs={'class':'form-control','placeholder':'Text',}),
        }
