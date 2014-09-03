from django.shortcuts import render
from .models import Tag, Entry
from .forms import EntryForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def entry_list(request):

	entries = Entry.objects.order_by('created_date')
	return render(request, 'myapp/entry_list.html', {'entries' : entries})

@login_required
def entry_new(request):
	if request.method == 'POST':
		form = EntryForm(request.POST)
		if form.is_valid():
			entry = form.save(commit=False)
			entry.author = request.user
			entry.save()

			for tag_name in form.cleaned_data['tags']:
				tag, created = Tag.objects.get_or_create(name = tag_name)
				entry.tags.add(tag)

			entry.save()
			return redirect('myapp.views.entry_list')
	else:
		form = EntryForm()
	return render(request, 'myapp/entry_edit.html', {'form' : form})
