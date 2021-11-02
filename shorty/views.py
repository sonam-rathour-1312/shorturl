from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import Url
from .forms import ShortenerForm

# Create your views here.
def home(request):
    templates='shorty/home.html'

    context={}

    # Empty form
    context['form']=ShortenerForm()

    if request.method=='GET':
        return render(request, templates, context)
    elif request.method=='POST':
        used_form=ShortenerForm(request.POST)

        if used_form.is_valid():

            shortened_object=used_form.save()
            new_url=request.build_absolute_uri('/') + shortened_object.short_url
            long_url=shortened_object.long_url

            context['new_url']=new_url
            context['long_url']=long_url

            return render(request, templates, context)

        context['errors']=used_form.errors

        return render(request, templates, context)

def redirect_url_view(request, shortened_part):

    try:
        shortener=Url.objects.get(short_url=shortened_part)

        shortener.click+=1
        shortener.save()

        return HttpResponseRedirect(shortener.long_url)
    except:
        raise Http404('Sorry this link is broken :(')
