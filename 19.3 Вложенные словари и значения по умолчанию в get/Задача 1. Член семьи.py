# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }
family = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}
print(family)
childrens_dict = {}
for child in family['children']:
    childrens_dict[child['name']] = child['age']
print(childrens_dict)

if childrens_dict.get('Bob', None):
    print("Bob найден")
else:
    print("Bob-а нету!")

if childrens_dict.get('surname', None):
    print(childrens_dict.get('surname', None))
else:
    print("Nosurname")