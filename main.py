# Check if List contains a String case-insensitive in Python

my_str = 'bobby'

my_list = ['BOBBY', 'HADZ', 'COM']

if my_str.lower() in (item.lower() for item in my_list):
    # 👇️ this runs
    print('The string is in list')
else:
    print('The string is not in the list')