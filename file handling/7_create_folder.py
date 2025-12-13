import os
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'watermelon']

os.chdir('fruit')
print(os.getcwd())

for item in fruits:
    os.mkdir(item)
    print(f"{item}folder created")