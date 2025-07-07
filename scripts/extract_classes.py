import json

with open('ast.json') as f:
    ast = json.load(f)

def find_structs_and_classes(node):
    results = []
    if node['type'] in ('class_specifier', 'struct_specifier'):
        results.append(node)
    if 'children' in node:
        for child in node['children']:
            results.extend(find_structs_and_classes(child))
    return results

classes = find_structs_and_classes(ast)

with open('classes.json', 'w') as f:
    json.dump(classes, f, indent=2)

print(f'Found {len(classes)} classes/structs and saved to classes.json')
