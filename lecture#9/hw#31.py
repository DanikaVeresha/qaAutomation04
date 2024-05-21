"""Task 31. Please look at the wiki_page.txt file because I have changed it."""
# import re


def get_links(html_file):
    """Get value of href attribute for tag 'a'. Do it: using string methods"""
    with open(html_file, 'r') as file:
        for line in file:
            value = line.find('<a')
            value_end = line.find('</a>')
            value_ends = line.rfind('<a')
            value_end_ends = line.rfind('</a>')
            line_values = line[value:value_end]
            # print(line_values)
            line_values_end = line[value_ends:value_end_ends]
            # print(line_values_end)
            if line_values == line_values_end:
                if 'href="' in line_values:
                    start = line_values.find('href="') + len('href="')
                    end = line_values.find('"', start)
                    yield line_values[start:end]
            else:
                if 'href="' in line_values and 'href="' in line_values_end:
                    start = line_values.find('href="') + len('href="') and line_values_end.find('href="') + len('href="')
                    end = line_values.find('"', start) and line_values_end.find('"', start)
                    yield line_values[start:end], line_values_end[start:end]


for item in get_links('wiki_page.txt'):
    if type(item) is tuple:
        for i in item:
            print(i)
    else:
        print(item)
# get_links('wiki_page.txt')



