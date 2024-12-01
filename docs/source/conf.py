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

project = 'Alper Yazar - ayazar.dev'
copyright = '2011-2024, Alper Yazar. Licensed under CC BY-SA 4.0'
html_title = "Alper Yazar - ayazar.dev"
author = 'Alper Yazar'

# The full version, including alpha/beta/rc tags
release = ''
version = 'ayazar.dev'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser',
'sphinx_rtd_theme',
'sphinx.ext.todo',
'sphinx_last_updated_by_git',
'sphinxcontrib.youtube',
'sphinx_sitemap',
'sphinx_copybutton',
'sphinxext.opengraph',
'sphinxcontrib.asciinema',
'sphinxcontrib.googleanalytics'
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
html_extra_path = ['ads.txt', 'CNAME', 'robots.txt', 'extra', 'favicon.ico']

html_show_sourcelink = False
html_copy_source = False

# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    # 'analytics_id': 'G-FHLWHCPSG0', Not valid in rtd-theme 3.0.2 anymore
    # 'display_version': True, Not valid in rtd-theme 3.0.2 anymore
    'style_external_links': True,
    'prev_next_buttons_location': 'both',
    'navigation_depth': 4,
    'collapse_navigation': False
}

# sphinxcontrib.googleanalytics
googleanalytics_id = 'G-FHLWHCPSG0'
googleanalytics_enabled = True

html_context = {
    "display_github" : True,
    "github_user": "alperyazar",
    "github_repo": "ayazar.dev",
    "github_version": "master",
    "conf_py_path": "/docs/source/"
}

language = 'en'

todo_include_todos = True

# https://github.com/wpilibsuite/sphinxext-opengraph
ogp_site_url = "https://ayazar.dev"

# Should be disabled to override description per page basis
ogp_enable_meta_description = False

ogp_social_cards = {
    "image_mini": "logo.png",
    "enable": False #disabled. can be enabled after https://github.com/wpilibsuite/sphinxext-opengraph/pull/110 due to emoji
}

# https://pypi.org/project/sphinx-disqus/
# disqus_shortname = "ayazardev"


# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_last_updated_fmt
html_last_updated_fmt = "%Y-%m-%d UTC"
html_last_updated_use_utc = True
