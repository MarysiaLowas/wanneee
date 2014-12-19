from django import forms
from .models import Entry, Tag
from django.forms import TextInput

class TagsField(forms.Field):

    def to_python(self, value):
        "Normalize data to a list of strings."
        tagsList = []

        # Return an empty list if no input was given.
        if not value:
            return []
        else:
            namesList = value.split(',')
            for name in namesList:
                tag, created = Tag.objects.get_or_create(name = name)
                tagsList.append(tag)
            return tagsList

    def validate(self, value):
        "Check if value consists only of tags."

        # Use the parent's handling of required fields, etc.
        super(TagsField, self).validate(value)


class EntryForm(forms.ModelForm):
	"""a form for adding new entries"""
	tags = TagsField()

	class Meta:
		model = Entry
		fields = ('summary', 'text', 'tags')
        widgets = {
            'tags': TextInput(),
        }

