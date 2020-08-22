curr_item = " "
items = []

while curr_item != "":
    curr_item = input("Enter an item that you need to do: ")
    if curr_item != "":
        items.append(curr_item)
print(items)
