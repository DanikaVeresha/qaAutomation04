
string = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."
# string = "This toool is cool. But that owl is awful. MAGIC TOOOLS Ltd."

print(f'String: {string}')
symbol = "o"
result = ''
for item in string.lower().split('.'):
    for i in item.split():
        if i.count(symbol) == 2:
            result += i.capitalize() + ' '
print(f'Result: {". ".join(result.split())}')





