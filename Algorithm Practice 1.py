'''
PROBLEM: Alice has some cards with numbers written on them.
She arranges the cards in decreasing order,
and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a
given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
'''
# I made all these algorithms from scatch, with no prior experience in
# algorithms or data structures. This is just to get my brain started


import math
import random


# Version 1. Short and simple; count up until we get it.
def checking_algorithm1(cards1, correct_card1):
    selected_card1 = 0
    flipped_cards1 = 0
    is_matching1 = False

    while is_matching1 == False:
        for i in range(0, cards1):
            if selected_card1 != correct_card1:
                selected_card1 += 1
                flipped_cards1 += 1
            elif selected_card1 == correct_card1:
                print("Correct! The correct card was", correct_card1, "and you flipped", flipped_cards1, "cards!")
                return True
            else:
                print("***Error in program***")
# ISSUE: Does not stop counting at cards1 value. Resolve later.


# Version 2. Split sequence in half, check 1 half, then the other until we get it.
def checking_algorithm2(cards2, correct_card2):
    selected_card2 = 0
    flipped_cards2 = 0
    is_matching2 = False

    while is_matching2 == False:
        selected_card2 = round(cards2/2)
        if selected_card2 == correct_card2:
            print("Oh! You guessed correctly first try.")
            return True
        else:
            for x in range(0, selected_card2):  # Check the first half
                selected_card2 -= 1
                flipped_cards2 += 1
                if selected_card2 == correct_card2:
                    print("Correct! The correct card was", correct_card2, "and you flipped", flipped_cards2, "cards!")
                    return True
                elif selected_card2 == 0:  # Check the other half if not in first half
                    selected_card2 = round(cards2/2)
                    for y in range(selected_card2, cards2):
                        selected_card2 += 1
                        flipped_cards2 += 1
                        if selected_card2 == correct_card2:
                            print("Correct! The correct card was", correct_card2, "and you flipped", flipped_cards2, "cards!")
                            return True
# ISSUE: Very long and clunky, too confusing to read. Simplify later.


# Version 3. We simply choose a random value until we get it.
def checking_algorithm3(cards3, correct_card3):
    selected_card3 = 0
    flipped_cards3 = 0
    is_matching3 = False

    while is_matching3 == False:
        for i in range(0, cards3):
            selected_card3 = random.randint(0, cards3)
            flipped_cards3 += 1
            if selected_card3 == correct_card3:
                print("Correct! The correct card was", correct_card3, "and you flipped", flipped_cards3, "cards!")
                return True
# ISSUE: The computer doesn't remember what cards it's already flipped.
# Will flip the same card multiple times, leading to "Flipped 10+ times". Fix later.


checking_algorithm1(7, 5)
checking_algorithm2(7, 2)
checking_algorithm3(7, 4)
