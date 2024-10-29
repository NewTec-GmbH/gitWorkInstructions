# pylint: disable=all
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os.path
import platform
import subprocess
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
    "sphinxcontrib.mermaid",   # Mermaid diagrams
    "sphinxcontrib.plantuml",  # Plantuml diagrams
    "myst_parser",             # MyST markdown parser
    "sphinx_rtd_dark_mode",    # Dark mode
    "sphinx_copybutton",       # Copy button
    "sphinx_togglebutton"      # Toggle button
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
html_last_updated_fmt = "%b %d, %Y"
html_theme_options = {
    'style_external_links': True
}

html_static_path = ["_static"]
html_css_files = [
    "css/svg.css",
    "css/width.css"
]

# HTML dark theme options
default_dark_mode = True

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
