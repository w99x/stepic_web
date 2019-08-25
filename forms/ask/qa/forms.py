from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError("title cannot be empty", code=1)
        return "Title: " + title
    
    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError("write an answer text", code=1)
        return "Text: " + text        
    
    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = Question()
    
    def __init__ (self, *args, **kwargs):
        question = kwargs.pop('question')
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.question = question

    def clean_text(self):
        if not self.cleaned_data['text']:
            raise forms.ValidationError("text cannot be empty", code=1)
        return self.cleaned_data['text']
    
    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
