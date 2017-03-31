from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Character
from .forms.forms import FateForm


# Create your views here.
def list_characters(request):
    all_characters = Character.objects.all()
    all_characters_context = {
        'characters': all_characters
    }

    return render(request, 'character/characters.html', all_characters_context)


def character_detail(request, pk=None):
    character = get_object_or_404(Character, id=pk)

    character_context = {
        'character': character
    }

    return render(request, 'character/detail.html', character_context)


def choose_fate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FateForm()

    return render(request, 'character/detail.html', {'form': form})
