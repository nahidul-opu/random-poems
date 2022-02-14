from django.shortcuts import render
from matplotlib.pyplot import title
from scipy import rand
from . import models
import random
import json
import urllib.request
import urllib.parse
import urllib

import poems
# Create your views here.


def get_poem(choice):
    if choice == 'english':
        link = "https://poetrydb.org/title"
        f = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        titles = urllib.request.urlopen(f).read()
        readable = titles.decode('utf-8')
        data = json.loads(readable)
        poemUrl = "http://poetrydb.org/title/" + \
            urllib.parse.quote(
                (data['titles'][random.randint(0, 2971)]), safe='-\"\\,.:;[]/!’()É_`?*=\'')
        f = urllib.request.Request(
            poemUrl, headers={'User-Agent': 'Mozilla/5.0'})
        contents = urllib.request.urlopen(f).read()
        readable = contents.decode('utf-8')
        data = json.loads(readable)
        title = data[0]['title']
        author = data[0]['author']
        lines = data[0]['lines']
        return title, author, lines
    elif choice == "bangla":
        cnt = models.bengaliPoems.objects.count()
        poem = models.bengaliPoems.objects.get(pk=random.randrange(0, cnt))
        poem.poem = (poem.poem).split('\n')
        return poem.title, poem.poet, poem.poem


def index(request):
    choices = ['bangla', 'english']
    title, author, poem = get_poem(random.choice(choices))
    return render(template_name='poems/index.html', request=request, context={
        'author': author,
        'title': title,
        'poem': poem})
