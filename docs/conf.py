# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Tested on:
#  | sphinx                    3.1.0
#  | groundwork-sphinx-theme   1.1.1
#  | sphinx-autodoc-typehints  1.10.3

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import re

sys.path.insert(0, os.path.abspath("../src"))

# -- Project information -----------------------------------------------------

project = "discordRebot"
copyright = "2020, Naveen S R"
author = "Naveen S R"

version = ""
with open("../src/discordRebot/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.viewcode",
]


napoleon_include_init_with_doc = False
autoclass_content = "both"
autodoc_member_order = "bysource"
autodoc_typehints = "signature"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "groundwork"  # "alabaster" #"sphinx_rtd_theme"

pygments_style = "rrt"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
# html_css_files = ['css/custom.css',]

html_logo = "_static/img/discordRebot.png"

html_theme_options = {
    "sidebar_width": "240px",
    "stickysidebar": True,
    "stickysidebarscrollable": True,
    "contribute": True,
    "github_fork": "nkpro2000sr/discord-rebot",
    "github_user": "nkpro2000sr",
}
