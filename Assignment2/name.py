with open("name.txt", "r") as f:
	content = f.read()

split_content = content.split()
print("First name: {} \nMiddle name: {} \nLast name: {} ".format(split_content[0], split_content[1],split_content[2]))