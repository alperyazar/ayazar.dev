# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Alper Yazar'
copyright = '2011-2024, Alper Yazar. Licensed under CC BY-SA 4.0'
html_title = "Alper Yazar"
author = 'Alper Yazar'

# The full version, including alpha/beta/rc tags
release = ''
version = 'ayazar.dev'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser',
'sphinx.ext.todo',
'sphinx_last_updated_by_git',
'sphinxcontrib.youtube',
'sphinx_sitemap',
'sphinx_copybutton',
'sphinxext.opengraph',
'sphinxcontrib.asciinema'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# https://pypi.org/project/sphinx-sitemap/
sitemap_url_scheme = "{link}"


# -- Options for HTML output -------------------------------------------------

# sphinx-sitemap için gerekli
# https://pypi.org/project/sphinx-sitemap/
html_baseurl = 'https://ayazar.dev/'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# https://stackoverflow.com/a/64106835
html_css_files = ["custom.css"]

# https://stackoverflow.com/a/54665517/1766391
html_favicon = 'favicon.ico'

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo
# https://pradyunsg.me/furo/customisation/logo/#same-logo-for-light-and-dark-mode
html_logo = 'logo.png'

# https://stackoverflow.com/a/53288958/1766391
html_extra_path = ['ads.txt', 'CNAME', 'robots.txt', 'extra', 'favicon.ico']

html_show_sourcelink = False
html_copy_source = False

# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
#    'announcement': 'Web sitemi tekrar düzenliyorum. Eksik içerikler, çalışmayan bağlantılar olabilir. 😇',
    'source_repository': 'https://github.com/alperyazar/ayazar.dev/',
    'source_branch': 'master',
    'source_directory': 'docs/source/',
    "light_css_variables": {
      "font-stack": "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji",
      "font-stack--monospace": "\"Reddit Mono\", \"SFMono-Regular\", Menlo, Consolas, Monaco, Liberation Mono, Lucida Console, monospace",
      "color-brand-primary": "#111",
      "color-brand-content": "#111",
      "color-brand-visited": "#111",
      "ayazardev-bold": "#fabfc8",
      "ayazardev-em": "#c0eeff",
      "ayazardev-article-color": "#111",
      "ayazardev-aftera": "url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAQElEQVR42qXKwQkAIAxDUUdxtO6/RBQkQZvSi8I/pL4BoGw/XPkh4XigPmsUgh0626AjRsgxHTkUThsG2T/sIlzdTsp52kSS1wAAAABJRU5ErkJggg==);"
    },
    "dark_css_variables": {
      "color-brand-primary": "#d0d0d0",
      "color-brand-content": "#d0d0d0",
      "color-brand-visited": "#d0d0d0",
      "ayazardev-bold": "#995d6d",
      "ayazardev-em": "#266173",
      "ayazardev-article-color": "#d0d0d0",
      "ayazardev-aftera": "url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAP0lEQVQY042PSQoAMAgDO+L/v2xPhVITbG7RkIVlUFV1c9oBUOJ8n84xpthjEj8igJhEtovjLVoNs2MUUsUpbMPMLAXUjJjTAAAAAElFTkSuQmCC);"
    }
}

language = 'tr'

todo_include_todos = True

# https://github.com/wpilibsuite/sphinxext-opengraph
ogp_site_url = "https://ayazar.dev"

# Should be disabled to override description per page basis
ogp_enable_meta_description = False

ogp_social_cards = {
    "image_mini": "logo.png",
    "enable": False #disabled. can be enabled after https://github.com/wpilibsuite/sphinxext-opengraph/pull/110 due to emoji
}

