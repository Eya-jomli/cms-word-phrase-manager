from django.db import models

class WordPhrase(models.Model):
    word_first_lang = models.CharField(max_length=255) 
    sentence_first_lang = models.TextField(blank=True, null=True)  
    word_second_lang = models.CharField(max_length=255)  
    sentence_second_lang = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"{self.word_first_lang} - {self.word_second_lang}"