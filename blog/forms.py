from django import forms


class CreateCommentForm(forms.Form):
    text = forms.CharField(max_length=140, min_length=1, widget=forms.Textarea)


class CreateMainPostForm(forms.Form):
    title = forms.CharField(max_length=140, min_length=1, widget=forms.Textarea)
    text = forms.CharField(max_length=1000, min_length=1, widget=forms.Textarea)
