# List practice!
friends = ["Luis", "Chris", "Jason", "Ben", "Jeourdin"]
lucky_numbers = [1, 3, 5, 7, 9]
# Remember, list index starts at 0. Luis is in the 0 position

print(friends)

print(friends[1:])  # Prints only items after index 1

#friends.extend(lucky_numbers)  # Adds another list to the main list
#print(friends)

friends.append("Sebas")  # Add an item to the end of the list
print(friends)

friends.insert(1, "Graham")
print(friends)

friends.remove("Graham")
print(friends)

#friends.clear()  # Clears the whole list
#print(friends)

friends.pop()  # Removes last item in list
print(friends)

print(friends.index("Jason"))  # Prints the index position of the item

friends.sort()  # Sorts the list alphabetically/numerically
print(friends)

lucky_numbers.reverse()  # Reverse order of list
print(lucky_numbers)

friends_copy = friends.copy()  # Copy the list, assign to new variable
print(friends_copy)
