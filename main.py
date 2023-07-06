from pprint import pprint
import os


def pars_str(line):
    line = line.strip().split('|')
    lst = []
    for j in line:
        a = j.strip()
        if a.isnumeric():
            lst.append(int(a))
        else:
            lst.append(a)
    return {'ingredient_name': lst[0], 'quantity': lst[1], 'measure': lst[2]}


def creat_dict():
    with open('D:\\recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        dish = ''
        for line in file:
            line = line.strip()
            if line == '':
                continue
            if line.isnumeric():
                ingr_count = int(line.strip())
                cook_book[dish] = []
                for ingredients in range(ingr_count):
                    cook_book[dish].append(pars_str(file.readline()))
            else:
                dish = line.strip()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        lst_ingredients = creat_dict().get(dish)
        for dict_ingredients in lst_ingredients:
            name_ingredient = dict_ingredients.get('ingredient_name')
            quantity_ingredients = dict_ingredients.get('quantity')
            measure_ingredients = dict_ingredients.get('measure')
            if name_ingredient in shop_list:
                quantity = dict_ingredients.get('quantity')
                quantity_ingredients += quantity
            shop_list[name_ingredient] = {'measure': measure_ingredients,
                                          'quantity': quantity_ingredients * person_count}
    return shop_list


def creat_file(lst_file):
    lst = []
    for index, i in enumerate(lst_file):
        name_path = os.path.basename(i)
        with open(i, encoding='utf-8') as f:
            lst_file = f.readlines()
            lst.append([len(lst_file), name_path, lst_file])
    lst.sort()
    with open('..\\res.txt', 'w', encoding='utf-8') as file:
        for l in lst:
            file.write(f'{l[1]}\n')
            file.write(f'{l[0]}\n')
            file.write(f'{" ".join(l[2]).strip()}\n')


pprint(creat_dict())
print('-'*90)
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print('-'*90)
pprint(creat_file(['..\\1.txt', '..\\2.txt', '..\\3.txt']))