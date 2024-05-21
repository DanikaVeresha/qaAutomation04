"""Task 31. Please look at the wiki_page.txt file because I have changed it."""
import re


def get_links(html_file):
    """Get value of href attribute for tag 'a'. Do it: using string methods"""
    with open(html_file, 'r') as file:
        for line in file:
            value = line.find('<a')
            value_end = line.rfind('</a>')
            line_values = line[value:value_end]
            result = re.findall(r'href="([^"]*)"', line_values)
            for res_line in result:
                yield res_line


for item in get_links('wiki_page.txt'):
    print(item)




