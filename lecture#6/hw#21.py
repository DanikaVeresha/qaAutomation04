"""Task 21."""

import glob
import os


path = "source_directory"
os.chdir(path)

res = glob.glob('**/*.txt', recursive=True)
for items in res:
    print(f'file: {os.path.basename(items)} - size: {os.path.getsize(items)} bytes')

result = [i for i in res if os.path.getsize(i) <= 120]
with open('combined_files.txt', 'w') as x:
    for item in result:
        with open(item, 'r') as f:
            x.write(f'{os.path.basename(item)}\n')
            x.write(f'{f.read()}\n')
            
# path = "source_directory"
# pattern_to_search = os.path.join(path, '**/*.txt')
# res = glob.glob(pattern_to_search, recursive=True)


