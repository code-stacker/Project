from django import forms
from .models import Article
from quizSite.forms import MyForm



class PostForm(MyForm):
    title_attrs = {"placeholder":"Title", "autofocus":"autofocus", "class":"form-control"}
    content_attrs = {"placeholder":"Content", "class":"form-control"}
    title       = forms.CharField(widget=forms.TextInput(title_attrs), label="Title")
    content     = forms.CharField(widget=forms.Textarea(content_attrs), label="Content")
    class Meta:
        model = Article
        fields = ['title', 'content']