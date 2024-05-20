"""Task 31. Obtaining attribute value"""
import re


print('-----------------Version 1 of the solution-----------------------')


def get_links_v1(doc):
    """Version 1 of the solution with using regular expressions"""
    with open(doc, 'r') as file:
        for line in file:
            if '<a' in line:
                for link in re.findall(r'href="(.+?)"', line):
                    yield link


# res_v1 = get_links_v1('wiki_page.txt')
# print(f'{res_v1.__sizeof__()} bytes')
for item_v1 in get_links_v1('wiki_page.txt'):
    print(item_v1)


print('-----------------Version 2 of the solution-----------------------')


def get_links_v3(doc):
    """Version 2 of the solution"""
    with (open(doc, 'r') as file):
        for line in file:
            if '<a' in line:
                first_enter = (line.find('href="') + 6,
                               line.find('"', line.find('href="') + 6))
                second_enter = (line.rfind('href="') + 6,
                                line.find('"', line.rfind('href="') + 6))
                if first_enter[0] != second_enter[0] and first_enter[1] != second_enter[1]:
                    yield line[first_enter[0]:first_enter[1]]
                yield line[second_enter[0]:second_enter[1]]


# res_v3 = get_links_v3('wiki_page.txt')
# print(f'{res_v3.__sizeof__()} bytes')
for item_v3 in get_links_v3('wiki_page.txt'):
    print(item_v3)

