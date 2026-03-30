# pylint: disable=all
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os.path
import platform
import subprocess

import os

from typing import Any
from urllib.parse import urlparse
from sphinx.errors import ConfigError

git_version = subprocess.check_output(
    ['git', 'describe', 'HEAD', '--tags', '--always'])

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "gitWorkInstructions"
copyright = "2024 - present, NewTec GmbH"
author = "NewTec GmbH"
release = git_version.decode()
version = release  # Do not differenciate between release and version
conf_py_path = "/doc/"  # with leading and trailing slashes

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # https://sphinxthemes.com/extensions/sphinxcontrib-mermaid
    "sphinxcontrib.mermaid",   # Mermaid diagrams
    # https://github.com/sphinx-contrib/plantuml
    "sphinxcontrib.plantuml",  # Plantuml diagrams
    # https://sphinxthemes.com/extensions/sphinx-copybutton
    "sphinx_copybutton",       # Copy button
    # https://sphinx-togglebutton.readthedocs.io/en/latest/
    "sphinx_togglebutton",     # Toggle button
    # https://www.sphinx-doc.org/en/master/usage/markdown.html
    'myst_parser',             # MyST markdown parser
    # Extension for the Read the Docs theme, which provides a modern and responsive design for documentation. 
    # https://sphinx-rtd-theme.readthedocs.io/en/stable/
    'sphinx_rtd_theme',        # Read the Docs theme
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store"
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# HTML theme and static files
html_theme = "sphinx_rtd_theme"
html_theme_options = {   
    'style_nav_header_background': '#0C2C40',   # Set the navigation header background color to NewTec black  #0C2C40
}

html_last_updated_fmt = "%b %d, %Y"

# Copy favorite icon to static path.
html_favicon = '../doc/images/favicon.ico'

# Copy logo to static path.
html_logo = '../doc/images/NewTec_Logo.png'

html_static_path = ["_static"]
#html_js_files = ['version_selector.js']
html_css_files = [
    "custom.css"
]

# Mermaid configuration
mermaid_output_format = "svg"
mermaid_cmd = os.path.join("node_modules", ".bin", "mmdc")
mermaid_params = ["--theme", "dark", "--backgroundColor", "transparent"]

if platform.system() == "Windows":
    mermaid_cmd_shell = "true"

# MyST configuration
myst_enable_extensions = ["colon_fence", 'attrs_block']
myst_heading_anchors = 2

# Toggle button configuration
togglebutton_hint = ""
togglebutton_hint_hide = ""
