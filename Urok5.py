# # f = open(r'test.txt', 'r', encoding='utf-8')
# # for i in f:
# #     print(i, end= '')
#
# with open(r'test.txt', 'r', encoding='utf-8') as f:
#     f.seek(8)
#     print(f.read())
#     print(f.tell())
#     print(f.name)
#     print(f.mode)
#     print(f.close())
#
# print('end')

import json

'data' = {
'income': {
'salary': 50000,
'bonus': 20000
            }
        }
print(type(data))
