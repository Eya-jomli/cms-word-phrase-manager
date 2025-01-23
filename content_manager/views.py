from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import WordPhrase
from .forms import WordPhraseForm

def word_list(request):
    query = request.GET.get('q')
    # Filter 
    if query:
        words = WordPhrase.objects.filter(
            word_first_lang__icontains=query
        ) | WordPhrase.objects.filter(
            word_second_lang__icontains=query
        )
    else:
        words = WordPhrase.objects.all()

    # 10 items per page
    paginator = Paginator(words, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'content_manager/word_list.html', {'page_obj': page_obj, 'query': query})

def edit_word(request, pk):
    word = get_object_or_404(WordPhrase, pk=pk)
    if request.method == "POST":
        form = WordPhraseForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return redirect('word_list')
    else:
        form = WordPhraseForm(instance=word)
    return render(request, 'content_manager/edit_word.html', {'form': form})

def add_word(request):
    if request.method == "POST":
        form = WordPhraseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('word_list')
    else:
        form = WordPhraseForm()
    return render(request, 'content_manager/add_word.html', {'form': form})