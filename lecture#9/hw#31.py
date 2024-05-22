"""Task 31. Please look at the wiki_page.txt file because I have changed it."""
import re


def get_links_re(html_file):
    """Get value of href attribute for tag 'a'. Do it: using regular expressions"""
    with open(html_file, 'r') as file:
        for line in file:
            if 'href' in line:
                yield from re.findall(r'<a.*?href="(.+?)"', line)


for i in get_links_re('wiki_page.txt'):
    print(i)

print('------------------------------------------------')


def get_links_str(html_file):
    """Get value of href attribute for tag 'a'. Do it: using string methods"""
    with open(html_file, 'r') as file:
        for line in file:
            start_of_range = line.find("<a", 0, len(line))
            end_of_rnage = line.find("</a>", 0, len(line))
            while start_of_range != -1:
                yield line[line.find('href="', start_of_range, end_of_rnage) + len('href="'):
                           line.find('"', line.find('href="', start_of_range,  end_of_rnage) + len('href="'), end_of_rnage)]
                start_of_range = line.find("<a", start_of_range + 1, len(line))
                end_of_rnage = line.find("</a>", end_of_rnage + 1, len(line))


for item in get_links_str('wiki_page.txt'):
    print(item)

