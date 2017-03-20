#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PUBLISH = False

# Site Information
################################################################################
AUTHOR = 'Joshua Ellis'
SITENAME = "Joshua Ellis"
SITETITLE = "Joshua Ellis"
SITESUBTITLE = "PhD Candidate"
SITEDESCRIPTION = "Blog of young physicist Joshua Ellis"
SITEURL = 'http://localhost:8000'
# SITEURL = 'http://10.9.146.61:8000'
TIMEZONE = 'Australia/Melbourne'
DEFAULT_LANG = 'en_AU'
OG_LOCALE = DEFAULT_LANG
FAVICON = ''
CC_LICENSE = {'name': 'Attribution-ShareAlike', 'slug': "by-sa", 'version': "4.0"}

FRONTMATTER = """
<p>
I'm Joshua Ellis, a PhD candidate at <a href="https://unimelb.edu.au">The University of Melbourne</a>.
</p>

<p>
In addition to physics, I also enjoy coding.  I have done a fair bit of coding
in C, C++, <a href="https://www.rust-lang.org">Rust</a>, Python and TeX/LaTeX.
You can see some of the coding projects I have worked in over in the <a
href="http://www.jpellis.me/projects/">projects section</a>.
</p>

<p>
This website will also contain a few blog posts which I intend to write when I
have some spare time.  At the present stage, I intend to write posts on whatever
I find interesting, whether it be in physics or some other interest of mine.
</p>

<p>
Feel free to share what you like and I'd love to hear from you.
</p>
"""

# Theme
################################################################################
THEME = 'themes/jp-ellis'

# Paths
################################################################################
PATH = 'content'
ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['blog', 'pages', 'static']
EXTRA_PATH_METADATA = {
    'static/CNAME': {'path': 'CNAME'},
    'static/robots.txt': {'path': 'robots.txt'},
    'static/google7e93ca521c7ff343.html': {'path': 'google7e93ca521c7ff343.html'},
    'static/googleca17b845931f3580.html': {'path': 'googleca17b845931f3580.html'}
}

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
          ('Email', 'mailto:josh@jpellis.me'),
          ('LinkedIn', 'https://au.linkedin.com/in/joshuapellis'),
)

# Defaults
################################################################################
DEFAULT_PAGINATION = 5
DEFAULT_METADATA = {
    'status': 'draft',
}

# Jinja Settings
################################################################################
JINJA_ENVIRONMENT = {}

# Plugins
################################################################################
PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'pelican-page-hierarchy',
    'render_math',
    'sitemap',
    'summary',
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

# Markdown
################################################################################
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'linenums': True,
            'css_class': 'highlight',
        },
        'markdown.extensions.extra': {},
        # 'markdown.extensions.fenced_code': {},
    },
    'output_format': 'html5',
}
