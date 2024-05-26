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


import sphinx, sphinx-autobuild