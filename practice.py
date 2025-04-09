empty_list = []
my_lists: list = ['Lists', 1, 3.5, True]

# Number of items in a list
length = len(my_lists)
print(length) 

#Accesing list items
first_item_my_lists = my_lists[0]
last_item_my_lists = my_lists[-1]
print(f'my_lists: first iteme is {first_item_my_lists} and last item is {last_item_my_lists}')

#slicing list
number = [0,1,2,3,4,5,6,7,8,9]
print(f'number[1:5] is {number[1:5]}') #[1, 2, 3, 4]
print(f'number[:7] is {number[:7]}') #[0, 1, 2, 3, 4, 5, 6]
print(f'number[4:] is {number[4:]}') #[4, 5, 6, 7, 8, 9]
print(f'number[::5] is {number[::5]}') #[0, 5]

# Adding list items
my_lists.append('Faith') #adds an item to the end of list
print(my_lists)
my_lists.insert(2, 'Fate') #adds an item to index 2
print(my_lists)

#Reverse order of the list
my_lists.reverse()
print(my_lists)

#create a copy of my_lists
copy_my_lists = my_lists.copy()
print('copy of my_lists:', my_lists)

#count how many times an item appears
x = my_lists.count('Faith')
print(f'Faith appears {x} times in the list')

# modifying the list items
my_lists[0]= 'Banana'
print(my_lists)

#sorting my list

print(f'Reverse sorted list: {my_lists.sort(reverse=True)}')
print(f'case insensitive sorted list: {my_lists.sort(key=str.lower)}')
# Removing item or list
my_lists.remove('Fate') # deletes first occurrence of Fate
print(my_lists) 
my_lists.pop() #deletes the last item
print(my_lists)
del my_lists[0] # del deletes a specific index item
print(my_lists)
my_lists.clear() #deletes the whole list
