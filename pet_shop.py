#Write a program that calculates the necessary costs for the purchase of food for dogs and other animals.
#One package of dog food costs BGN 2.50, and any other that is not for them costs BGN 4.
number_of_dogs=int(input())
number_of_animals=int(input())
cost_dogs=number_of_dogs*2.5
cost_animals=number_of_animals*4
cost=cost_animals+cost_dogs
print(f'{cost:.2f} lv.')