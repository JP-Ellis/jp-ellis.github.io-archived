#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

PUBLISH = True

SITEURL = '//jpellis.me'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [
    ".git",
    ".gitignore",
    "CNAME",
    "google7e93ca521c7ff343.html",
    "googleca17b845931f3580.html",
    "googleca17b845931f3580.html",
]

# Services
################################################################################
# GOOGLE_ANALYTICS = 'UA-62514224-3'
GOOGLE_TAG_MANAGER = 'GTM-M7H67J'
DISQUS_SITENAME = "jpellisgithubio"
