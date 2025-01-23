import os
import sys
import django
import requests

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms_project.settings')
django.setup()

from content_manager.models import WordPhrase

def load_data():
    url = "https://pecto-content-f2egcwgbcvbkbye6.z03.azurefd.net/language-data/language-data/russian-finnish/cards/curated_platform_cards/sm1_new_kap1.json"
    response = requests.get(url)
    data = response.json()

    for item in data:
        # Extract data 
        word_first_lang = item.get('wordFirstLang', '')
        sentence_first_lang = item.get('sentenceFirstLang', '')
        word_second_lang = item.get('wordSecondLang', '')
        sentence_second_lang = item.get('sentenceSecondLang', '')
        
        print(f"Loading: {word_first_lang} - {word_second_lang} - {sentence_first_lang}")

        # Create the WordPhrase object
        WordPhrase.objects.create(
            word_first_lang=word_first_lang,
            sentence_first_lang=sentence_first_lang,
            word_second_lang=word_second_lang,
            sentence_second_lang=sentence_second_lang
        )
    print("Data loaded successfully!")

if __name__ == "__main__":
    load_data()