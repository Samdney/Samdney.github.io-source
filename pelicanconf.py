#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Carolin Zöbelein'
SITENAME = u"Carolin's Blog"
SITEURL = ''

PATH = 'content'

DATE_FORMATS = {
    'en': ('en_US','%a, %d %b %Y'),
}

#DIRECT_TEMPLATES = ['index']
#PAGINATED_TEMPLATES = {'index': 10}

STATIC_PATHS = ['blog', 'pages', 'images']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'

PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

SUMMARY_MAX_LENGTH = 15

TIMEZONE = 'Europe/Paris'

#DEFAULT_LANG = u'en'
DEFAULT_LANG = u'en_US'
#DEFAULT_LANG = u'de'


### TODO
# Plugins
PLUGIN_PATHS = ['plugins', '../pelican-plugins']
PLUGINS = ['render_math', 'pelican_fontawesome', 'summary']

import markdown

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            #'css_class': 'codehilite',
            'linenums': False,
            'guess_lang': False,
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
        
        'markdown_link_attr_modifier': {
            'new_tab': 'on',
            'no_referrer': 'external_only',
            'auto_title': 'on',
        },
        
        'markdown.extensions.mathjax' : {},
    },
    'output_format': 'html5',
}



###
# THEME: nest
###
# Theme
THEME = 'themes/nest'

SITESUBTITLE = u'Carolin\'s Blog'

SITEURL_SOCIAL = 'https://blog.carolin-zoebelein.de'

#DISPLAY_PAGES_ON_MENU

# Minified CSS
NEST_CSS_MINIFY = True
# Add items to top menu before pages
#MENUITEMS = [('Home', '/'), ('Contact', 'placeholder'), ('Categories','/categories.html')]
MENUITEMS = [('Archives', '/archives.html'), ('Categories','/categories.html'), ('Contact', '/contact.html')]
# Add header background image from content/images : 'background.jpg'
#NEST_HEADER_IMAGES = 'AfterThe_digital_War_Samdney_lowerQuality.jpg'
NEST_HEADER_IMAGES = 'computer-2930704_1280.jpg'

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
NEST_INDEX_HEAD_TITLE = u'Carolin\'s Blog'

NEST_INDEX_HEADER_TITLE_HEAD = True
#NEST_INDEX_HEADER_TITLE = u'Carolin\'s Blog'
NEST_INDEX_HEADER_TITLE = u'Math, CS and Random Stuff :)'
#NEST_INDEX_HEADER_SUBTITLE = u'Smashing The Stack For Fun And Profit'
#NEST_INDEX_HEADER_SUBTITLE = u'The acquisition of wealth is no longer the driving force in our lives. ...We work to better ourselves ...and the rest of humanity.<br /> - Jean-Luc Picard, Star Trek: First Contact, 1996 - '
NEST_INDEX_FOOTER_SUBTITLE = u'The acquisition of wealth is no longer the driving force in our lives. ...We work to better ourselves ...and the rest of humanity.<br /> - Jean-Luc Picard, Star Trek: First Contact, 1996 - '

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
DEFAULT_PAGINATION = 5
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
LINKS = (('https://www.carolin-zoebelein.de/','https://www.carolin-zoebelein.de'),
         ('https://research.carolin-zoebelein.de/', 'https://research.carolin-zoebelein.de'),
         ('Raw Blog content at GitHub','https://github.com/Samdney/Samdney.github.io-source'),)

# Social widget
SOCIAL = (
        ('<i class="fa fa-twitter" aria-hidden="true"></i> SamdneyTweet', 'https://twitter.com/SamdneyTweet'),
        ('<i class="fa fa-github" aria-hidden="true"></i> Samdney', 'https://github.com/Samdney'),
	#('<i class="fa fa-file-text-o" aria-hidden="true"></i> arXiv', 'https://arxiv.org/find/math/1/au:+Zobelein_C/0/1/0/all/0/1'),
        ('<i class="ai ai-arxiv" aria-hidden="true" style="color:white;"></i> arXiv', 'https://arxiv.org/find/math/1/au:+Zobelein_C/0/1/0/all/0/1'),
        )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
