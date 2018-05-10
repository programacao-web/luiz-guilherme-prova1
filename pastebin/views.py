
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from pastebin.forms import PasteForm
from pastebin.models import Paste


def index(request):
    if request.method == "POST":
        form = PasteForm(request.POST)
        if form.is_valid():
            paste = form.save(commit=False)
            paste.save()
            return HttpResponseRedirect('/pastes/{paste.id}'.format(paste=paste))
    else:
        form = PasteForm()

    return render(request, 'pastebin/index.jinja2', {'form': form})


def paste(request, id):
    paste = Paste.objects.get(id=id)
    return render(request, 'pastebin/paste-detail.jinja2', {'paste': paste})


def language_list(request, language):
    pastes = Paste.objects.filter(language=language)
    return render(request, 'pastebin/paste-language.jinja2', {'pastes': pastes})