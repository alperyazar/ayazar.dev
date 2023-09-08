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

project = 'Notes'
copyright = '2023, Alper Yazar. CC BY-SA 4.0'
author = 'Alper Yazar'

# The full version, including alpha/beta/rc tags
release = ''
version = 'Alper Yazar'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser',
'sphinx_rtd_theme',
'sphinx.ext.todo',
'sphinx_last_updated_by_git',
'sphinxcontrib.youtube',
'sphinx_sitemap'
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
html_baseurl = 'https://notes.alperyazar.com/'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# https://stackoverflow.com/a/64106835
html_css_files = ["colors.css","table.css","font.css","width.css"]

# https://stackoverflow.com/a/54665517/1766391
html_favicon = 'favicon.ico'

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo
html_logo = 'logo.png'

# https://stackoverflow.com/a/53288958/1766391
html_extra_path = ['robots.txt']

html_show_sourcelink = False
html_copy_source = False

# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    'analytics_id': 'G-VFPBRE75P1',
    'display_version': True,
    'style_external_links': True,
    'prev_next_buttons_location': 'both',
    'navigation_depth': 4,
    'collapse_navigation': False
}

html_context = {
    "display_github" : True,
    "github_user": "alperyazar",
    "github_repo": "notes",
    "github_version": "master",
    "conf_py_path": "/docs/source/"
}

language = 'en'

todo_include_todos = True
