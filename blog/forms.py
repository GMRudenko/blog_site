from django import forms

class CreateCommentForm(forms.Form):
    text=forms.CharField(max_length=140, min_length=1, help_text='Input text')

    