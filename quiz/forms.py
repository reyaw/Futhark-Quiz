from django import forms

CHOICES = ['A', 'B', 'C', 'D', ]


class QuestionForm(forms.Form):
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

