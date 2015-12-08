#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PUBLISH = False

# Site Information
################################################################################
AUTHOR = 'Joshua Ellis'
SITENAME = "Joshua Ellis's Blog"
SITETITLE = "Joshua Ellis"
SITESUBTITLE = "Masters of Physics Candidate"
SITEDESCRIPTION = "Blog of young physicist Joshua Ellis"
# SITEURL = 'http://192.168.2.184:8000'
SITEURL = 'http://10.9.146.61:8000'
TIMEZONE = 'Australia/Melbourne'
DEFAULT_LANG = 'en_AU'
OG_LOCALE = DEFAULT_LANG
FAVICON = ''
CC_LICENSE = {'name': 'Attribution-ShareAlike', 'slug': "by-sa", 'version': "4.0"}

# Theme
################################################################################
THEME = 'themes/jp-ellis'

# Paths
################################################################################
PATH = 'content'
STATIC_PATHS = ['images', 'files']
ARTICLE_PATHS = ['blog', 'projects']

# Readjust all the paths as I prefer URLs which do not end in .html
########################################
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'

PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'

CATEGORIES_SAVE_AS = 'category/index.html'
CATEGORIES_URL = 'category/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'

TAGS_SAVE_AS = 'tag/index.html'
TAGS_URL = 'tag/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_URL = 'tag/{slug}/'

AUTHORS_SAVE_AS = 'author/index.html'
AUTHORS_URL = 'author/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = ''

# Feeds
################################################################################
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Links
################################################################################

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Github', 'https://github.com/JP-Ellis'),
          ('Email', 'mailto:coujellis@gmail.com'),
          ('LinkedIn', 'https://au.linkedin.com/in/joshuapellis'),
          # ('GooglePlus', 'https://plus.google.com/u/0/+JoshuaEllisP'),
)

# Site Settings
################################################################################
DEFAULT_PAGINATION = 5
DEFAULT_METADATA = {
    'status': 'draft',
}

# Plugins
################################################################################
PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'render_math',
    'sitemap',
]

# Sitemap
########################################
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 1.0,
        'pages': 0.0
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}

# Pygments
################################################################################
PYGMENTS_RST_OPTIONS = {
    'linenos': 'table',
}

# Render Math
################################################################################
MATH_JAX = {
    'auto_insert': False,
    'tex_extensions': ['autoload-all.js'],
}
