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
    """Parse `self.input` into a document tree."""
    self.document = document = self.new_document()
    self.input = pre_process(self.input)
    print(self.input)
    self.parser.parse(self.input, document)
    document.current_source = document.current_line = None

Reader.parse = parse