import glob
import os


res = glob.glob('**/*.txt', recursive=True)
for items in res:
    print(f'file: {os.path.basename(items)} - size: {os.path.getsize(items)} bytes')


result = [i for i in res if os.path.getsize(i) <= 120]
with open('combined_files.txt', 'w') as x:
    output = [os.path.basename(i) for i in result]
    x.write(str(output))








