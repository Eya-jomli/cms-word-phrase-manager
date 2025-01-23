from django import forms
from .models import WordPhrase

class WordPhraseForm(forms.ModelForm):
    class Meta:
        model = WordPhrase
        fields = ['word_first_lang', 'word_second_lang', 'sentence_first_lang', 'sentence_second_lang']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['word_first_lang'].required = True
        self.fields['word_second_lang'].required = True