from email import header
from django.shortcuts import render

import random
import json
import urllib.request
import urllib.parse
import urllib
# Create your views here.


def index(request):
    link = "https://poetrydb.org/title"
    f = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    titles = urllib.request.urlopen(f).read()
    readable = titles.decode('utf-8')
    data = json.loads(readable)
    poemUrl = "http://poetrydb.org/title/" + \
        urllib.parse.quote(
            (data['titles'][random.randint(0, 2971)]), safe='-\"\\,.:;[]/!’()É_`?*=\'')
    f = urllib.request.Request(poemUrl, headers={'User-Agent': 'Mozilla/5.0'})
    contents = urllib.request.urlopen(f).read()
    readable = contents.decode('utf-8')
    data = json.loads(readable)
    title = data[0]['title']
    author = data[0]['author']
    lines = data[0]['lines'][:min(len(data[0]['lines']), 20)]
    return render(template_name='poems/index.html', request=request, context={
        'author': author,
        'title': title,
        'poem': lines})
