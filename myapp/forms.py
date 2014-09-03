from django import forms
from .models import Entry
from django.forms import TextInput

class TagsField(forms.Field):

    def to_python(self, value):
        "Normalize data to a list of strings."

        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(',')

    def validate(self, value):
        "Check if value consists only of valid emails."

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

