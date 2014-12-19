from django.shortcuts import render, get_object_or_404
from .models import Tag, Entry
from .forms import EntryForm
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import Group
import registration.backends.simple.views

class Register(registration.backends.simple.views.RegistrationView):
	"""class that overwrite the default get_success_url"""
	def get_success_url(self, request, user):
		return "/"

	def register(self, request, **cleaned_data):
		user = super(Register, self).register(request, **cleaned_data)
		user.groups.add(Group.objects.get(name = "externals"))
		return user
		

@login_required
def entry_list(request):

	entries = Entry.objects.order_by('-created_date')
	return render(request, 'myapp/entry_list.html', {'entries' : entries})


@login_required
def entry_new(request):
	if request.method == 'POST':
		form = EntryForm(request.POST)
		if form.is_valid():
			entry = form.save(commit=False)
			entry.author = request.user
			entry.save()
			form.save_m2m()
			return redirect('myapp.views.entry_list')
	else:
		form = EntryForm()
	return render(request, 'myapp/entry_edit.html', {'form': form})


@login_required
def entry_details(request,pk):
	entry = get_object_or_404(Entry, pk=pk)
	return render(request, 'myapp/entry_details',{'entry' : entry})


@permission_required('myapp.delete_entry', raise_exception=True)
def entry_remove(request,pk):
	entry = get_object_or_404(Entry, pk=pk)
	entry.delete()
	return redirect('myapp.views.entry_list')


@login_required
def entry_edit(request,pk):
	entry = get_object_or_404(Entry, pk=pk)

	if not((request.user.has_perm('myapp.change_entry') and request.user == entry.author) or request.user.is_staff):
		raise PermissionDenied

	if request.method == "POST":
		form = EntryForm(request.POST, instance=entry)
		if form.is_valid():
		    entry = form.save(commit=False)
		    entry.author = request.user
		    entry.save()
		    form.save_m2m()
		    return redirect('myapp.views.entry_details', pk=entry.pk)
	else:
	    form = EntryForm(instance=entry)
	return render(request, 'myapp/entry_edit.html', {'form': form})


@login_required
def tagged_list(request,pk):
	entries = Entry.objects.filter(tags=pk)
	return render(request, 'myapp/entry_list.html',{'entries' : entries})