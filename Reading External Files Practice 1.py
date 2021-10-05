# Finally we will learn how to read data from external files
# Python read command

friends_file = open("friends.txt", "r")

# You must enter the directory location unless in the same folder
# "r" means read, "w" means write, "a" means append (add), "r+" is read and write
# Make sure to store the open function in a variable
# If you open a file, you must close it. Same as C++

#print(friends_file.readable())  # Returns a boolean value if file is a readable
#print(friends_file.read())  # Read the whole file
#print(friends_file.readline())  # Read a single line
#print(friends_file.readlines())  # Reads the file and puts the objects in a list/array
#print(friends_file.readlines()[2])  # Readline at index position

for friend in friends_file.readlines():
    print(friend)

friends_file.close()
