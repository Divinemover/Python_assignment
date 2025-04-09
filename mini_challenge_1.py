fruits: list = ['apples', 'banana', 'oranges']
fruits.append('grape')
print(f'Total fruits: {len(fruits)}')
fruits.insert(0, 'pineapple')
fruits.remove('banana')
for item in fruits:
    print(item.upper())
x = fruits.count('mango')
if x == 0:
    print('Mango is not in the list')
else:
    print('Mango is in the list')