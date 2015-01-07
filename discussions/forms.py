from ckeditor.widgets import CKEditorWidget
from django import forms
from discussions.models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'topic_comment']
        widgets = {
            'title':forms.TextInput(attrs={'placeholder': 'Type Topic Title'}),
            'topic_comment': forms.Textarea(attrs={'placeholder':'Comment...', 'rows':'4'}),
        }
        exclude = ('institution', 'category')

    #def save(self, commit=False):
    #    post = super(PostForm, self).save(commit=False)
    #    post.active = True
    #    if commit:
    #        post.save()
    #    return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.CharField(widget=CKEditorWidget())
        }
        exclude = ('topic',)