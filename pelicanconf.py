#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Samdney'
SITENAME = u"Samdney's Blog"
SITEURL = ''

PATH = 'content'

STATIC_PATHS = ['blog', 'pages', 'images']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'

PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

SUMMARY_MAX_LENGTH = 15

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

###
# Plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['render_math', 'pelican_fontawesome', 'summary']

###
# THEME: nest
###
# Theme
THEME = 'themes/nest'

SITESUBTITLE = u'Samdney\'s Blog'

#DISPLAY_PAGES_ON_MENU

# Minified CSS
NEST_CSS_MINIFY = True
# Add items to top menu before pages
#MENUITEMS = [('Home', '/'), ('Contact', 'placeholder'), ('Categories','/categories.html')]
MENUITEMS = [('Categories','/categories.html'), ('Contact', '/contact.html')]
# Add header background image from content/images : 'background.jpg'
NEST_HEADER_IMAGES = 'AfterThe_digital_War_Samdney_lowerQuality.jpg'
#NEST_HEADER_LOGO = '/image/logo.png'
# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [('Archives', '/archives.html'),('Tags','/tags.html'), ('Authors','/authors.html')]
NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_LINKS_COLUMN_TITLE = u'Links'
#NEST_COPYRIGHT = u'&copy; blogname 2015'
# Footer optional
NEST_FOOTER_HTML = ''
# index
NEST_INDEX_HEAD_TITLE = u'0000 0000'
NEST_INDEX_HEADER_TITLE = u'Samdney\'s Blog'
#NEST_INDEX_HEADER_SUBTITLE = u'Smashing The Stack For Fun And Profit'
NEST_INDEX_HEADER_SUBTITLE = u'The acquisition of wealth is no longer the driving force in our lives. ...We work to better ourselves ...and the rest of humanity. - Jean-Luc Picard, Star Trek: First Contact, 1996'
NEST_INDEX_CONTENT_TITLE = u'Last Posts'
# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Archives'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Posts Archives'
NEST_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Archives for all posts'
NEST_ARCHIVES_CONTENT_TITLE = u'Archives'
# article.html
NEST_ARTICLE_HEADER_BY = u'By'
NEST_ARTICLE_HEADER_MODIFIED = u'modified'
NEST_ARTICLE_HEADER_IN = u'in category'
# author.html
NEST_AUTHOR_HEAD_TITLE = u'Posts by'
NEST_AUTHOR_HEAD_DESCRIPTION = u'Posts by'
NEST_AUTHOR_HEADER_SUBTITLE = u'Posts archives'
NEST_AUTHOR_CONTENT_TITLE = u'Posts'
# authors.html
NEST_AUTHORS_HEAD_TITLE = u'Author list'
NEST_AUTHORS_HEAD_DESCRIPTION = u'Author list'
NEST_AUTHORS_HEADER_TITLE = u'Author list'
NEST_AUTHORS_HEADER_SUBTITLE = u'Archives listed by author'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Categories'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Archives listed by category'
NEST_CATEGORIES_HEADER_TITLE = u'Categories'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Archives listed by category'
# category.html
NEST_CATEGORY_HEAD_TITLE = u'Category Archive'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Category Archive'
NEST_CATEGORY_HEADER_TITLE = u'Category'
NEST_CATEGORY_HEADER_SUBTITLE = u'Category Archive'
# pagination.html
DEFAULT_PAGINATION = 3
NEST_PAGINATION_PREVIOUS = u'Previous'
NEST_PAGINATION_NEXT = u'Next'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'
# tag.html
NEST_TAG_HEAD_TITLE = u'Tag archives'
NEST_TAG_HEAD_DESCRIPTION = u'Tag archives'
NEST_TAG_HEADER_TITLE = u'Tag'
NEST_TAG_HEADER_SUBTITLE = u'Tag archives'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Tags List'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'Tags List'
NEST_TAGS_CONTENT_TITLE = u'Tags List'
NEST_TAGS_CONTENT_LIST = u'tagged'
# Static files
#STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg']
#EXTRA_PATH_METADATA = {
#    'extra/robots.txt': {'path': 'robots.txt'},
#    'extra/favicon.ico': {'path': 'favicon.ico'},
#    'extra/logo.svg': {'path': 'logo.svg'}
#}
###

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('http://www.carolin-zoebelein.de/',
    'http://www.carolin-zoebelein.de'),)

# Social widget
SOCIAL = (('<i class="fa fa-twitter" aria-hidden="true"></i> SamdneyTweet', 'https://twitter.com/SamdneyTweet'),
          ('<i class="fa fa-github" aria-hidden="true"></i> Samdney', 'https://github.com/Samdney'),
	  ('<i class="fa fa-file-text-o" aria-hidden="true"></i> arXiv', 'https://arxiv.org/find/math/1/au:+Zobelein_C/0/1/0/all/0/1'), )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True