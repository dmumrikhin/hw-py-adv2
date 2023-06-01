import re
import csv
from pprint import pprint

# ## Читаем адресную книгу в формате CSV в список contacts_list:
# with open("phonebook_raw.csv") as f:
#   rows = csv.reader(f, delimiter=",")
#   contacts_list = list(rows)
# # pprint(contacts_list)

with open("phonebook_raw.csv") as f:
    lines = f.readlines()
## 1. Выполните пункты 1-3 задания.
    result_contacts_list = []
    result_contacts_list.append(['lastname', 'firstname', 'surname', 
        'organization', 'position', 'phone', 'email'])
    
    pattern = (r'^([А-ЯЁа-яё]+)\s*,?([А-ЯЁа-яё]*)\s*,?([А-ЯЁа-яё]*),?,?,?'
        r'([А-ЯЁа-яё]*)\s*,?([А-ЯЁа-яёa-zA-Z\s\–]*),(\+*\d?)[\s\(]*'
        r'(\d{0,3})[\s\)-]*(\d{0,3})-?(\d{0,2})-?(\d{0,2})[\s\(]*'
        r'([.доб]*)\s*(\d{0,4})[\s\),]*([a-zA-Z\s\–\@\.\d]*)')
    for line in lines:
        raw_result = re.match(pattern, line)
        if raw_result is not None:
            if raw_result.group(11):
                new_pattern = r'\1,\2,\3,\4,\5,+7(\7)\8-\9-\10 \11\12,\13'
            elif raw_result.group(7) == '':
                new_pattern = r'\1,\2,\3,\4,\5,,\13'
            else:
                new_pattern = r'\1,\2,\3,\4,\5,+7(\7)\8-\9-\10\11\12,\13'
            string = re.sub(pattern, new_pattern, line)
            result = re.split(',|\n', string)
                        
            for item in result_contacts_list:
                if item[0] == result[0]:
                    joint_item = []
                    for i, k in zip(item, result):
                        if i != k:
                            joint_item.append(i + k)
                        else:
                            joint_item.append(i)
                    result_contacts_list.remove(item)
                    item = joint_item
                else:
                    item = result
            result_contacts_list.append(item)

# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
# Вместо contacts_list подставьте свой список:
  datawriter.writerows(result_contacts_list)