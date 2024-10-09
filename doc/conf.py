# pylint: disable=all
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os.path
import platform

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "gitWorkInstructions"
copyright = "2024 - present, NewTec GmbH"
author = "NewTec GmbH"
release = "1.0.0"
conf_py_path = "/doc/"  # with leading and trailing slashes

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxcontrib.mermaid",  # Mermaid diagrams
    "myst_parser",  # MyST markdown parser
    "sphinx_rtd_dark_mode",  # Dark mode
    "sphinx_copybutton",  # Copy button
    "sphinx_togglebutton"  # Toggle button
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
myst_enable_extensions = ["colon_fence"]
myst_heading_anchors = 2

# Toggle button configuration
togglebutton_hint = ""
togglebutton_hint_hide = ""
