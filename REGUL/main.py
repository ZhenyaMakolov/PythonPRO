import re
from pprint import pprint
import csv
from collections import OrderedDict


## Читаем адресную книгу в формате CSV в список contacts_list:
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# Выполнение пуктов 1-3 задания.
contacts_list1 = []
for i in contacts_list:
    join_list = ','.join(i)
    pattern1 = re.compile(r"([А-Я][A=А-Яа-я]+[,\s]*)[,\s*]([А-Я][A=А-Яа-я]+[,\s]*)[,\s*]([А-Я][A=А-Яа-я]+)*(\,*)")
    pattern2 = re.compile(r"(8|\+7)?[- (]*(\d{3})[- )]*(\d{3})[- ]*(\d{2})[- ]*(\d{2})[ (]*((\w+\.)[ \S)]*(\d{4})([ )]*))*")
    subst1 = r"\1,\2,\3,"
    subst2 = r"+7(\2)\3-\4-\5 \7\8"
    result1 = pattern1.sub(subst1, join_list)
    result2 = pattern2.sub(subst2, result1)
    split_tuple = result2.split(',')
    contacts_list1.append(split_tuple)
    contacts_list1 = sorted(contacts_list1)

    def remove_duplicates(list_: list) -> list:
        k = 0
        while k < len(list_) - 1:
            for list1, list2 in zip(list_[k], list_[k + 1]):
                if list1 == list2:
                    new_list = list(OrderedDict.fromkeys(list_[k] + list_[k + 1]))
                    list_.remove(list_[k + 1])
                    list_.remove(list_[k])
                    list_.append(new_list)
                break
            k += 1
        return list_

remove_duplicates(contacts_list1)


# Запись в новый файл изменных данных.
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list1)