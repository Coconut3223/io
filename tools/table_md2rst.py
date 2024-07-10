
 
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


# import docutils.parsers
# import docutils.parsers.rst

# parser = rst.Parser()
# document = docutils.utils.new_document(source, settings)
# parser.parse(input, document)


input_ = r"""
||str|int|float|
|0|a|1|0.1|
|1|b|2|0.2|
|2|c|3|0.3|
|3|d|4|0.4|
|4|e|5|0.5|
|5|f|6|0.6|
|6|g|7|0.7|
|7|h|8|0.8|
|8|i|9|0.9|
|9|j|10|1.0|
"""


raise file

data_list = input_.split('\n')[1:-1]
col_num = list(map(lambda x: len(x.split('|')), data_list))
assert len(set(col_num))
data = list(map(lambda x: x.split('|'), data_list))
col_width = [0] * (col_num[0])
chinese_pattern = re.compile("[\u4e00-\u9fff]+")
emoji_pattern = re.compile("[^\u0000-\u00FF\u4e00-\u9fff]")


print(len('✔️'))
for line in data:
    # print(line)
    for i in range(len(line)):
        chinese_matches = re.findall(chinese_pattern, line[i])
        emoji_matches = re.findall(emoji_pattern, line[i]) 
        print(line[i],len(line[i]))
        print(line[i],chinese_matches,emoji_matches)
        a = 1 * sum(map(len, chinese_matches)) + len(line[i]) + 1 * sum(map(len, emoji_matches)) 
        col_width[i] = max(col_width[i], a)
        
print(col_width)

line_sep = '+'.join(map(lambda x: '-'*x, col_width))
header_sep = '+'.join(map(lambda x: '='*x, col_width))
res = [line_sep]

for idx, line in enumerate(data):
    def pad(i, str_):
        chinese_matches = re.findall(chinese_pattern, str_)
        emoji_matches = re.findall(emoji_pattern, str_)
        have = 1 * sum(map(len, chinese_matches)) + len(str_) + 1 * sum(map(len, emoji_matches))  
        return f'{str_}{"".join(["\x20"]* (i-have))}'
        
    res.append('|'.join(list(map(lambda i, str_: pad(i, str_), col_width, line))))
    res.append(line_sep)
res[2] = header_sep
print('\n'.join(res))

    



import re

text = "This is 一些 非 英文 text with 中文 and 日本語 characters.❌"
chinese_matches = re.findall(chinese_pattern, text)
emoji_matches = re.findall(emoji_pattern, text) 

print("Non-English matches:")
for match in emoji_matches:
    print(match)
# with open('./temp.rst','r', encoding='utf-8') as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line.startswith('+'):
#             line_lst = line.split('+')
#         elif line.startswith('|'):
#             line_lst = line.split('|')
#         else: 
#             line_lst=line
#         print(line_lst)
#         if type(line_lst) == list:
#             print(list(map(len, line_lst)))

"""

.. table::

+--------+-----+-----+----+---+---+-----+-----+------+
|        | 1   | 2   | 3  | 4 | 5 | 6   | 7   | 8    |
+========+=====+=====+====+===+===+=====+=====+======+
| State1 | ❌ 1 | ❌ 1 | ✔️ |   |   | ❌ 1 | ❌ 1 | ❌ 2  |
| State2 | ❌ 1 | ❌ 1 | ✔️ |   |   |     |     | ❌ 2  |
+--------+-----+-----+----+---+---+-----+-----+------+
"""