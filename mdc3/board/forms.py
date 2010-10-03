from django import forms
from mdc3.board.models import Thread, Post
from django.contrib.sites.models import Site

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('subject',)

    def clean_subject(self):
        subj = self.cleaned_data["subject"]
        subj = subj.strip()
        if subj  == '':
            raise forms.ValidationError("whitespace is not a subject")
        return subj
                    

class PostForm(forms.ModelForm):
    class Meta:
        auto_id = False
        model = Post
        fields = ('body',)

