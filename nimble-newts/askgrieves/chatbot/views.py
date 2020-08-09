from django.forms.models import model_to_dict
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.utils.functional import lazy
from .models import WikiArticle

from wikipediaapi import Wikipedia

WIKI_WIKI = Wikipedia('en')


class Message:
    send = True

    def __init__(self, text):
        if Message.send:
            self.action = 'send'
        else:
            self.action = 'receive'
        Message.send = not self.send
        self.text = text


def home(request):
    return render(request, 'home.html')


def chat_page(request, bot_name):
    return render(request, 'home.html', {'bot': bot_name})


def experimental(request):
    return render(request, 'landing_page.html')


def get_wikipedia(request):
    article_name = request.POST.get('article_name')
    wiki_page = WIKI_WIKI.page(article_name)
    if not wiki_page.exists():
        raise Http404('Wiki page does not exist')
    else:
        def get_wiki_details():
            return {
                'summary': WIKI_WIKI.extracts(wiki_page, excsentences=3),
                'full_page': wiki_page.text
            }
        # Lazy evaluation of wiki page, inspired by https://code.djangoproject.com/ticket/29413
        article, created = WikiArticle.objects.get_or_create(name=article_name,
                                                             defaults=lazy(get_wiki_details, dict)())
        # Serialize article without full text
        serialized_article = model_to_dict(article, fields=('name', 'summary'))
    return JsonResponse(serialized_article)
