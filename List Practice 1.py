# Problem: There are 10 rules that need to be displayed.
# Instructions: Type the rules out, and print them all in the most efficient way possible.
# Challenge: Utilize a list and a for loop

print("Program starting...")

rule1 = "No running"
rule2 = "No eating"
rule3 = "No sitting"
rule4 = "No smiling"
rule5 = "No pooping"
rule6 = "No laughing"
rule7 = "No drinking"
rule8 = "No breathing"
rule9 = "No blinking"
rule10 = "No moving"
rules_list = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10]

# Using the for loop, we can list each rule along with its number sequentially
#for i in range(len(rules_list)):
#    print("Rule #", i, ": ", rules_list[i], end="\n")

for count, value in enumerate(rules_list):
    print("Rule #", count, ": ", rules_list[count], end="\n")

print("Program complete!")
