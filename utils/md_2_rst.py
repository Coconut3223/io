import os
import re

cur_dir = os.path.dirname(__file__)

mds_dir = os.path.join(cur_dir, 'mds')


mds = [os.path.join(mds_dir, md) for md in os.listdir(mds_dir) if md.endswith('md')]
print(mds)
def parse_math(text):
    
    pattern = r'(?P<formula>\$.*?\$)'
    tag = 'formula'
    def to_defi(matched):
        value = matched.group(tag)
        print(value)
        return f' :math:`{value[1:-1]}` '
    return re.sub(pattern, to_defi, text)

def parse_inline_code(text):
    
    pattern = r'(?P<formula>`.*?`)'
    tag = 'formula'
    def to_defi(matched):
        value = matched.group(tag)
        print(value)
        return f' ``{value[1:-1]}`` '
    return re.sub(pattern, to_defi, text)


for md in mds:
    with open(md, 'r', encoding='utf-8') as f, \
        open(f'{md[:-3]}.rst', 'w', encoding='utf-8') as w:
            for line in f.readlines():
                print(line)
                line = parse_inline_code(line)
                line = parse_math(line)
                print(line)
                w.write(line)

        
