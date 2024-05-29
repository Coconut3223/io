# import pygments
# from docutils import frontend, utils
# from docutils.parsers.rst import Parser
# import re
# settings = frontend.get_default_settings(Parser)

# def patch_defi(inputstring, document):
#     tag = 'defi_text'
#     pattern = r'\s==(?P<defi_text>\w+)==\s'
#     def to_defi(matched):
#         value = matched.group(tag)
#         return f' :defi:`{value}` '

#     return parse(re.sub(pattern, to_defi, inputstring), document)

# Parser.parse = patch_defi
    
    
# with open('temp.rst', encoding='utf-8') as file:
#     document = utils.new_document(file.name, settings)
#     Parser().parse(file.read(), document)


# print(document.pformat())

"""
from docutils.readers import Reader

def replace_double_equalsymbol(text):
    import re
    pattern = r'\s*==(?P<defi_text>\w+)==\s'
    tag = 'defi_text'
    def to_defi(matched):
        value = matched.group(tag)
        return f' :defi:`{value}` '
    return re.sub(pattern, to_defi, text)
        

def pre_process(text):
    text = replace_double_equalsymbol(text)
    return text
    
    
def parse(self):
    \"""Parse `self.input` into a document tree.\"""
    self.document = document = self.new_document()
    self.input = pre_process(self.input)
    print(self.input)
    self.parser.parse(self.input, document)
    document.current_source = document.current_line = None

Reader.parse = parse

"""

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



