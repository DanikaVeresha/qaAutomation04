
string = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."
symbol = "o"
result = ''
for item in string.split('.'):
    for i in item.split():
        if (i.count(symbol, 0, len(i)) > 1
                or i.count(symbol.upper(), 0, len(i)) > 1):
            result += i.capitalize() + ' '
print(f'Result: {". ".join(result.split())}')






