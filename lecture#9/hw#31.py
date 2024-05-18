"""Task 31. Obtaining attribute value"""
import re
from bs4 import BeautifulSoup


# def get_links(html):
#     """Version 1 of the solution with using regular expressions"""
#     with open(html, 'r') as file:
#         for link in re.findall('a href="(.+?)"', file.read()):
#             yield link
#
#
# # res = get_links('wiki_page.txt')
# # print(res.__sizeof__()) # 224 bytes
# # print(get_links('wiki_page.txt'))
# for item_ in get_links('wiki_page.txt'):
#     print(item_)
#
#
# print('-----------------Version 2 of the solution-----------------------')
#
#
# def get_links(html):
#     """Version 2 of the solution"""
#     with open(html, 'r') as file:
#         soup = BeautifulSoup(file, 'html.parser')
#         links = []
#         for link in soup.find_all('a'):
#             links.append(link.get('href'))
#         return links
#
#
# # res = get_links('wiki_page.txt')
# # print(res.__sizeof__()) # 104 bytes
# # print(get_links('wiki_page.txt'))
# for item in get_links('wiki_page.txt'):
#     print(item)


print('-----------------Version 3 of the solution-----------------------')


def get_link(html):
    """with using string`s method and regular expressions"""
    with open(html, 'r') as file:
        return re.findall('a href="(.+?)"', file.read())


for item_ in get_link('wiki_page.txt'):
    print(item_)
print('-----------------Version 4 of the solution-----------------------')


def get_links(html):
    with open(html, 'r') as file:
        for link in file:
            if '<a href="' in link:
                yield link.split('href="')[1].split('"')[0]


for item_ in get_links('wiki_page.txt'):
    print(item_)

