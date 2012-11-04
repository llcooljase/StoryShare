import re
from django.contrib.auth.models import User
from django import forms
			
class BookmarkSaveForm(forms.Form):
	url = forms.URLField(
		label=u'URL',
		required=False,
		widget=forms.TextInput(attrs={'size': 64})
	)
	title = forms.CharField(
		label=u'Title',
		widget=forms.TextInput(attrs={'size': 64})
	)
	subtitle = forms.CharField(
		label=u'Subtitle',
		widget=forms.TextInput(attrs={'size': 64})
	)
	tags = forms.CharField(
		label=u'Tags',
		required=False,
		widget=forms.TextInput(attrs={'size': 64})
	)
	type = forms.IntegerField(
		label=u'Type',
	)
	picture = forms.FileField(
		label=u'Picture',
		required=False,
	)
	school = forms.CharField(
		label=u'School',
		required=False,
		widget=forms.TextInput(attrs={'size': 64})
	)
	hackathon = forms.CharField(
		label=u'Hackathon',
		required=False,
		widget=forms.TextInput(attrs={'size': 64})
	)