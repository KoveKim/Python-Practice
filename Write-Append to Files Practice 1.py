# Writing new files / appending to files practice
# If you were to use "w" instead of "a", whatever you write will OVERWRITE the file

numbers_file = open("numbers.txt", "a")  # Appending means adding to the end of the file

#numbers_file.write("00000")  # Check the txt file after running this
numbers_file.write("\n00000")  # If you're appending, use \n to add new line

numbers_file.close()

# Every time this function is ran, it will keep appending 00000

#---------------------------------------------------------------
# You can create files as well. Look below

created_file = open("createdfile.txt", "w")
created_file.write("Hello world!")
created_file.close()

# Check your folder now. Look for the file "createdfile.txt"
# Once the program creates the file once, it will not create a duplicate
# So you can run the program as many times as you want and it won't create a new file
# Unless you specify the new file
# But beware, it will continue to overwrite that file as long as you have "w"
# In the function. Have a failsafe once the file is created
