import json

with open('classes.json') as f:
    classes = json.load(f)

for cls in classes:
    name = None
    fields = []
    for child in cls['children']:
        if child['type'] == 'type_identifier':
            name = child['text']
        if child['type'] == 'field_declaration_list':
            for fd in child['children']:
                type_name = ''
                field_name = ''
                for fd_child in fd['children']:
                    if 'text' in fd_child:
                        if 'type' in fd_child and 'type_identifier' in fd_child['type']:
                            type_name = fd_child['text']
                        elif fd_child['type'] == 'primitive_type':
                            type_name = fd_child['text']
                        elif fd_child['type'] == 'field_identifier':
                            field_name = fd_child['text']
                if type_name and field_name:
                    fields.append({"type": type_name, "name": field_name})

    print("## Instruction:")
    print("このC++のstructの内容を簡単に説明し、PlantUMLのクラス図を生成してください。")
    print("## Input:")
    print(json.dumps({"type": "struct_specifier", "name": name, "fields": fields}, indent=2))
    print("\n---------------------------------\n")
