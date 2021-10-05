# Inheritance / class methods practice

class Chef:

    def make_chicken(self):
        print("Made chicken")


    def make_salad(self):
        print("Made salad")


    def make_special(self):
        print("Made special dish (ribs)")


# ------------------------------------------------

# Very similar class, but with an additional method. This takes too much work and
# adds too many lines of code. Instead, we can use inheritance to cut down code
class ChineseChef:

    def make_chicken(self):
        print("Made chicken")


    def make_salad(self):
        print("Made salad")


    def make_special(self):
        print("Made special dish (orange chicken)")


    def make_friedrice(self):
        print("Made fried rice")


# ---------------------------------------------------

# You can inherit methods and attributes from a different class
# by adding inheritance into the parantheses in the Class name
class ChineseChef2(Chef):

    def make_friedrice(self):
        print("Made fried rice")


    # From inheritance, you can override methods. Look below and compare to "Chef"
    def make_special(self):
        print("Made special dish (orange chicken)")
