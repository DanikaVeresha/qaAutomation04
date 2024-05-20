"""Task 31. Obtaining attribute value"""
import re
from bs4 import BeautifulSoup


print('-----------------Version 1 of the solution-----------------------')


def get_links_v1(html):
    """Version 1 of the solution with using regular expressions"""
    with open(html, 'r') as file:
        for link in re.findall('a href="(.+?)"', file.read()):
            yield link


# res_v1 = get_links_v1('wiki_page.txt')
# print(f'{res_v1.__sizeof__()} bytes')
for item_v1 in get_links_v1('wiki_page.txt'):
    print(item_v1)


print('-----------------Version 2 of the solution-----------------------')


def get_links_v2(html):
    """Version 2 of the solution"""
    with open(html, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        return links


# res_v2 = get_links_v2('wiki_page.txt')
# print(f'{res_v2.__sizeof__()} bytes')
for item_v2 in get_links_v2('wiki_page.txt'):
    print(item_v2)


print('-----------------Version 3 of the solution-----------------------')


def get_links_v3(doc):
    """Version 3 of the solution"""
    with (open(doc, 'r') as file):
        for line in file:
            if 'a href=' in line:
                first_enter = (line.find('a href="') + 8,
                               line.find('"', line.find('a href="') + 8))
                second_enter = (line.rfind('a href="') + 8,
                                line.find('"', line.rfind('a href="') + 8))
                if first_enter[0] != second_enter[0] and first_enter[1] != second_enter[1]:
                    yield line[first_enter[0]:first_enter[1]]
                yield line[second_enter[0]:second_enter[1]]


# res_v3 = get_links_v3('wiki_page.txt')
# print(f'{res_v3.__sizeof__()} bytes')
for item_v3 in get_links_v3('wiki_page.txt'):
    print(item_v3)

