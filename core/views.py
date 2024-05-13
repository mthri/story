from django.shortcuts import render, redirect
from django.urls import reverse

from story.models import Story


def home_page(request, *args, **kwargs):
    pk = kwargs.get('pk')
    try:
        if pk:
            story = Story.objects.get(pk=pk, accept=True)
    except Story.DoesNotExist:
        return redirect(reverse('home-page'))

    return render(request, 'core/index.html', context={'pk': pk})