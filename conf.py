# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'BIAY'
copyright = '2025, Linus Fernandes'
author = 'Linus Fernandes'
release = '1.0'
version = '1.0'
master_doc = 'index'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser","sphinxcontrib.cairosvgconverter"]

templates_path = ['_templates']
exclude_patterns = ["stitch.md","January/*.md","February/*.md", "March/*.md", "April/*.md", "May/*.md", "June/*.md", "July/*.md", "August/*.md", "September/*.md", "October/*.md"\
                    , "November/*.md", "December/*.md", "*Index.md"]
suppress_warnings = ['toc.not_included','myst.xref_missing','image/svg+xml']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

# -- Options for linkcheck
linkcheck_timeout = 5  # seconds
linkcheck_ignore = [
    r'http://localhost:\d+/',  # Ignore local dev servers
    r'https://example\.com/redirect',  # Ignore known redirect
  r'https://www.facebook.com/groups/ascensioncatholic/posts/1354591171863758/',
]
linkcheck_ignore_redirects = True

# -- Options for PDF output
latex_engine = 'lualatex'

latex_elements = { 
        'fontpkg': r'''
        \usepackage{fontspec}
    ''',
    'preamble': r'''
\pdfminorversion=7
\setmainfont{Symbola}
''',
 }
