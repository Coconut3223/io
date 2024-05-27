# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import logging
import os
dirname = os.path.abspath(os.path.dirname(__file__))
logging.basicConfig(filename=os.path.join(dirname, 'sphinx.log'))

"""" !!!! modifed by coco"""

from docutils.readers import Reader

def replace_double_equalsymbol(text):
    import re
    pattern = r'(?P<defi_text>\x20?==[^=]+==\s)'
    tag = 'defi_text'
    def to_defi(matched):
        value = matched.group(tag)
        if value.startswith('\x20'):
            return f'\x20:defi:`{value[3:-3]}` '
        else: 
            return f':defi:`{value[2:-3]}` '
    return re.sub(pattern, to_defi, text)
        

def pre_process(text):
    text = replace_double_equalsymbol(text)
    #print(f'dewdwaaaaaaaaaaaaaaaaaaaaa\n{text}')
    return text
    
    
def parse(self):
    """Parse `self.input` into a document tree."""
    print('HHHHHHHHHHHHHHHHHHHHHHHHHere')
    self.document = document = self.new_document()
    #print(self.input)
    self.input = pre_process(self.input)
    #print(self.input)
    self.parser.parse(self.input, document)
    document.current_source = document.current_line = None

Reader.parse = parse


project = 'cocobook'
copyright = '2024, coconut'
author = 'coconut'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions =[]
# extensions = ["myst_parser"]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_material'
html_static_path = ['_static']

html_css_files = ['css/def.css']


keep_warnings = True

rst_prolog = """
.. role:: defi
"""


suppress_warnings = ["config.cache"]  # https://github.com/sphinx-doc/sphinx/issues/12300
# pickling environment... WARNING: cannot cache unpickable configuration value: 'html_context' (because it contains a function, class, or module object)