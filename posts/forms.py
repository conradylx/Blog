from django import forms
from tinymce import TinyMCE

from posts.models import Post, Comments


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCEWidget(
        attrs={'required': False, 'cols': 30, 'rows': 10}
    ))

    class Meta:
        model = Post
        fields = '__all__'


class CommentsForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-input',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '6'
    }))

    class Meta:
        model = Comments
        fields = ('user', 'content',)
