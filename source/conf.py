# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Welrok'
copyright = '2025, Welrok'
author = 'Welrok'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
# НАСТРОЙКИ БОКОВОЙ ПАНЕЛИ
html_theme_options = {
    'logo_name': 'Welrok API',
    'description': 'Local API Documentation v1.0',
}
templates_path = ['_templates']
html_sidebars = {
    '**': [
        'sidebar.html',  # ТОЛЬКО наш кастомный шаблон
    ]
}