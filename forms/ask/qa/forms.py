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
    question = forms.IntegerField()
    
    def __init__ (self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)

    def clean_text(self):
        if not self.cleaned_data['text']:
            raise forms.ValidationError("text cannot be empty", code=1)
        return self.cleaned_data['text']
    
    def save(self, question_id):
        question_id = self.cleaned_data.pop('question')
        q = Question.objects.get(id=question_id)
        answer = Answer(question=q, **self.cleaned_data)
        answer.save()
        return answer
