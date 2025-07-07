import json

with open('ast.json') as f:
    ast = json.load(f)

types = set()

def collect_types(node):
    types.add(node['type'])
    if 'children' in node:
        for child in node['children']:
            collect_types(child)

collect_types(ast)

print('Node types found:')
for t in sorted(types):
    print('-', t)
