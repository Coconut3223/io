import pygments
from docutils import frontend, utils
from docutils.parsers.rst import Parser
import re
settings = frontend.get_default_settings(Parser)

def patch_defi(self, inputstring, document):
    print(self)
    import re
    from docutils.parsers.rst import Parser
    tag = 'defi_text'
    pattern = r'\s==(?P<defi_text>\w+)==\s'
    def to_defi(matched):
        value = matched.group(tag)
        return f' :defi:`{value}` '

    return self.parse(re.sub(pattern, to_defi, inputstring), document)

Parser.parse = patch_defi
    
    
with open('temp.rst', encoding='utf-8') as file:
    document = utils.new_document(file.name, settings)
    Parser().parse(file.read(), document)


print(document.pformat())









    