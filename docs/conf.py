# -*- coding: utf-8 -*-
import sys, os, pkginfo, datetime

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
pkg_info = pkginfo.Develop(os.path.join(os.path.dirname(__file__),'..'))

intersphinx_mapping = {'http://docs.python.org': None}

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx'
    ]

# General
source_suffix = '.rst'
master_doc = 'index'
project = pkg_info.name
copyright = '2015-%s Jump Systems LLC' % datetime.datetime.now().year
version = release = pkg_info.version
exclude_patterns = [
    'description.rst',
    '_build'
]
pygments_style = 'sphinx'

# Options for HTML output
html_theme = 'default' if on_rtd else 'classic'
htmlhelp_basename = project+'doc'

# Options for LaTeX output
latex_documents = [
  ('index',project+'.tex', project+u' Documentation',
   'Jump Systems LLC', 'manual'),
]

