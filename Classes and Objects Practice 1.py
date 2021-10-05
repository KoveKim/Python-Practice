# Classes and Objects Practice! Finally!
# A class is basically its own datatype.
# A class defines the object, the object is the iteration.
# Think of it like a blueprint and a build.
# Functions within classes are called methods
# Classes are useful because you can model real world objects and create datatypes

import math  # Btw, this is called a module. It's just a set of functions in a library
import random  # You can also import your own functions from your own code
# And remember, you can download external modules by using "pip" in cmd prompt

class Student:
    def __init__(self, name, major, gpa, is_failing):  # This is the "initialize" function
    # Anything after "self" are the attributes you want to define
    # Must assign the values of the attributes
        self.name = name  # The name of the "Student" object is the name that you pass in
        self.major = major
        self.gpa = gpa
        self.is_failing = is_failing


# Below are the objects of the class "Student"
# Every time you call to the "Student" object, it's calling the "init" function
# Then you pass in the attributes
student1 = Student("Khristian", "CompSci", 3.0, True)
student2 = Student("Luis", "Business", 3.5, False)
student3 = Student("Jason", "Hospitality", 4.0, False)

