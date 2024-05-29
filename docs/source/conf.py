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




"""
hex(ord('#')) == '0x23'
True
"""


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
        
def replace_title(text):
    import re
    pattern = r'(?P<title>\#+\s[^\n]+\n)'
    tag = 'title'
    def add_title(matched):
        level_symbal = {
            1:'=',  2:'-',  3:'~',
            4:'^',  5:'+',  6:'\''
            }
        value = matched.group(tag)
        split_ = value.split('#')
        level, size = len(split_)-1, len(split_[-1])-1
        return f'{split_[-1][1:]}{level_symbal[level]*size*2}\n'
    return re.sub(pattern, add_title, text)

def pre_process(text):
    text = replace_double_equalsymbol(text)
    text = replace_title(text)
    print(f'dewdwaaaaaaaaaaaaaaaaaaaaa\n{text}')
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

from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from docutils.parsers.rst.roles import set_classes
from docutils import nodes
from docutils.parsers.rst.directives.admonitions import BaseAdmonition



def BaseAdmonition_run(self):
    set_classes(self.options)
    if self.content:
        text = '\n'.join(self.content)
        admonition_node = self.node_class(text, **self.options)
        print(self.node_class)
        self.add_name(admonition_node)
        admonition_node.source, admonition_node.line = \
            self.state_machine.get_source_and_line(self.lineno)
        if self.node_class is nodes.admonition:
            title_text = self.arguments[0]
            textnodes, messages = self.state.inline_text(title_text,
                                                        self.lineno)
            title = nodes.title(title_text, '', *textnodes)
            title.source, title.line = (
                    self.state_machine.get_source_and_line(self.lineno))
            admonition_node += title
            admonition_node += messages
            if 'classes' not in self.options:
                admonition_node['classes'] += ['admonition-'
                                            + nodes.make_id(title_text)]
        self.state.nested_parse(self.content, self.content_offset,
                                admonition_node)
    else:
        admonition_node = self.node_class(None, **self.options)
        self.add_name(admonition_node)
        admonition_node.source, admonition_node.line = \
            self.state_machine.get_source_and_line(self.lineno)
        if self.node_class is nodes.admonition:
            title_text = self.arguments[0]
            textnodes, messages = self.state.inline_text(title_text,
                                                        self.lineno)
            title = nodes.title(title_text, '', *textnodes)
            title.source, title.line = (
                    self.state_machine.get_source_and_line(self.lineno))
            admonition_node += title
            admonition_node += messages
            if 'classes' not in self.options:
                admonition_node['classes'] += ['admonition-'
                                            + nodes.make_id(title_text)]
        self.state.nested_parse(self.content, self.content_offset,
                                admonition_node)
        
    return [admonition_node]

BaseAdmonition.run = BaseAdmonition_run




project = 'cocobook'
copyright = '2024, coconut'
author = 'coconut'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions =['sphinxemoji.sphinxemoji',]
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