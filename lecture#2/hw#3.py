"""Task 3."""

country = ['Ukraine', 'Spain', 'Italy']
capital = ['Kyiv', 'Madrid', 'Rome']
info = dict(zip(country, capital))
for k, v in info.items():
    print(f'{k} : {v}')
