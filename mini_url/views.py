from django.shortcuts import render, redirect, get_object_or_404

from .forms import MiniURLForm
from .models import MiniURL


def shorten(request):
	form = MiniURLForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect(list_all)
	
	return render(request, 'mini_url/shorten.html', locals())

def list_all(request):
	mini_urls = MiniURL.objects.order_by('-n_access')

	return render(request, 'mini_url/list_all.html', locals())

def redirection(request, code):
	mini_url = get_object_or_404(MiniURL, code=code)
	mini_url.n_access += 1
	mini_url.save()
	mini_url = MiniURL.objects.get(code=code)

	return redirect(mini_url.url, permanent=True)
