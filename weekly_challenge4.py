with open("input.txt", "r") as file:
    data = file.read()
    length = len(data.strip())
    data_uppercase = data.upper()

with open("output.txt", "w") as file:
    file.write(data_uppercase)
    file.write("\n")
    file.write(f"WORD COUNT: {length}")