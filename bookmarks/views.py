# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import feedparser
from bookmarks.models import *
from bookmarks.forms import *

def bulletin_board(request):
		bookmark_array = BookmarkList.objects.all()
		bookmarks = bookmark_array.order_by('-date')
		variables = RequestContext(request, {
			'bookmarks': bookmarks,
		})
		#
		# In case of POST
		#
		if request.method == 'POST':
			form = BookmarkSaveForm(request.POST)
			if form.is_valid():
				bookmark = _bookmark_save(request, form)
				#
				# Check to see if AJAX is working
				#
				ajax = 'ajax' in request.GET
				if ajax:
					variables = RequestContext(request, {
						'bookmarks': [bookmark],
					})
					return render_to_response(
						'bb.html', variables
					)
				# Otherwise... not sure what this does
				else:
					return HttpResponseRedirect(
						"/"
					)
			else:	
				return HttpResponse(u'Form not valid')
		elif 'url' in request.GET:
			url = request.GET['url']
			title = ''
			tags = ''
			try:
				link = Link.objects.get(url=url)
				bookmark = BookmarkList.objects.get(
					link=link,
				)
				title = bookmark.title
			except (Link.DoesNotExist, BookmarkList.DoesNotExist):
				pass
			form = BookmarkSaveForm({
				'url': url,
				'title': title,
				
			})
		else:
			return render_to_response(
				'bb.html',
				variables
			)	
		return render_to_response(
			'bb.html', variables
		)	
		return render_to_response('news.html', variables)
		
def bookmark_save_page(request):
	ajax = 'ajax' in request.GET
	if request.method == 'POST':
		form = BookmarkSaveForm(request.POST)
		if form.is_valid():
			bookmark = _bookmark_save(request, form)
			if ajax:
				variables = RequestContext(request, {
					'bookmarks': [bookmark],
				})
				return render_to_response(
					'bb.html', variables
				)
			else:
				return HttpResponseRedirect(
					"/"
				)
		else:
			if ajax:
				return HttpResponse(u'failure')
	elif 'url' in request.GET:
		url = request.GET['url']
		title = ''
		try:
			link = Link.objects.get(url=url)
			bookmark = BookmarkList.objects.get(
				link=link,
			)
			title = bookmark.title
		except (Link.DoesNotExist, BookmarkList.DoesNotExist):
			pass
		form = BookmarkSaveForm({
			'url': url,
			'title': title,
			
		})
	else:
		form = BookmarkSaveForm()
	variables = RequestContext(request, {
		'form': form
	})
	if ajax:
		return render_to_response(
			'bb.html',
			variables
		)
	else:
		return render_to_response(
			'bookmark_save.html',
			variables
		)
		
from datetime import date		
def _bookmark_save(request, form):
	# Create or get link
	link, dummy = Link.objects.get_or_create(
		url=form.cleaned_data['url']
	)
	bookmark, created = BookmarkList.objects.get_or_create(
		link=link,
	)
	if not created:
		return bookmark
	else:
		# Update bookmark title.
		bookmark.title = form.cleaned_data['title']
		# Update bookmark subtitle.
		bookmark.subtitle = form.cleaned_data['subtitle']
		# Update bookmark type.
		bookmark.type = form.cleaned_data['type']
		# Create new tag list.
		# Share on the main page if requested.
		# Save bookmark to database.
		bookmark.save()
		return bookmark

def news_feed(request):
	a = feedparser.parse('http://news.ycombinator.com/rss')
	a.iconpic = "hn.png"
	a.number = "1"
	b = feedparser.parse('http://feeds.feedburner.com/TechCrunch/')
	b.iconpic = "tc.png"
	b.number = "2"
	c = feedparser.parse('http://feeds.mashable.com/Mashable')
	c.iconpic = "ma.png"
	c.number = "3"
	d = feedparser.parse('http://feeds.fastcompany.com/fastcompany/headlines')
	d.iconpic = "fco.jpg"
	d.number = "4"
	e = feedparser.parse('http://feeds.feedburner.com/tedblog')
	e.iconpic = "ted.jpg"
	e.number = "5"
	f = feedparser.parse('http://rss1.smashingmagazine.com/feed/')
	f.iconpic = "smashing-logo.png"
	f.number = "6"
	# Create array
	letters = [a, b, c, d, e, f]
	all_feeds = []
	for i in range(3):
		for letter in letters:
			letter.entries[i].iconpic = letter.iconpic
			letter.entries[i].number = letter.number
			all_feeds.append(letter.entries[i])
	variables = RequestContext(request, {
		'all_feeds': all_feeds
	})
	if request.method == 'POST':
		form = BookmarkSaveForm(request.POST)
		if form.is_valid():
			bookmark = _bookmark_save(request, form)
			post_variables = RequestContext(request, {
				'bookmarks': [bookmark],
				'show_edit': True,
				'show_tags': True
				})
			return render_to_response(
				'bb.html', post_variables
				)
		else:
			return render_to_response('news.html', variables)
	else:
		return render_to_response('news.html', variables)

def newsbookmark_save_page(request):
	bookmarks = BookmarkList.objects.order_by('-date')
	variables = RequestContext(request, {
		'bookmarks': bookmarks,
	})
	if request.method == 'POST':
		form = BookmarkSaveForm(request.POST)
		if form.is_valid():
			bookmark = _bookmark_save(request, form)
			variables = RequestContext(request, {
					'bookmarks': [bookmark],
				})
			return render_to_response(
				'bb.html', variables
			)
		else:
			return HttpResponse(u'failure')
	elif 'url' in request.GET:
		url = request.GET['url']
		title = ''
		try:
			link = Link.objects.get(url=url)
			bookmark = BookmarkList.objects.get(
				link=link,
			)
			title = bookmark.title
		except (Link.DoesNotExist, BookmarkList.DoesNotExist):
			pass
		form = BookmarkSaveForm({
			'url': url,
			'title': title,
		})
	else:
		return render_to_response(
			'bb.html',
			variables
			)	