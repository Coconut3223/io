
 
import re
 
# # 将匹配的数字乘以 2
# def double(matched):
#     value = matched.group('defi_text')
#     return f' :defi:`{value}` '
 
# s = '==23==4HFD ==56== 7'
# print(re.sub(r'\s==(?P<defi_text>\w+)==\s', double, s))

# def patch_defi(self, inputstring, document):
#     import re
    
#     tag = 'defi_text'
#     pattern = r'\s==(?P<defi_text>\w+)==\s'
#     def to_defi(matched):
#         value = matched.group(tag)
#         return f' :defi:`{value}` '
    
#     return 
# re.sub(pattern, to_defi, inputstring)

# file_string = '==23==4HFD ==56== 7'

# print(patch_defi(file_string))


import docutils.parsers
import docutils.parsers.rst

parser = rst.Parser()
document = docutils.utils.new_document(source, settings)
parser.parse(input, document)