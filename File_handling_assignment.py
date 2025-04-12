#Create a program that reads a file and writes a modified version to a new file.
def file_handling(filename):
    with open(filename,"r") as file:
        data = file.read()
        word_count = len(data.strip())
        data_uppercase = data.upper()
    with open("modified_file.txt", "w") as new_file:
        new_file.write(data_uppercase)
        new_file.write('\n')
        new_file.write(f'Word Count is: {word_count}')

#Ask the user for a filename
filename = input("Enter a filename: ")

#handle errors if it doesn’t exist or can’t be read.
try:
    file_handling(filename)
except FileNotFoundError:
    print('File not found!')
except IOError:
    print("An error occurred while reading the file.")