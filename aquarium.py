# For his birthday, Lubomir received an aquarium in the shape of a parallelepiped. You have to calculate how much
# liters of water will collect the aquarium if it is known that a certain percentage of its capacity is occupied by sand,
# plants, heater and pump. 
# Its dimensions - length, width and height in centimeters will be entered by the console.
# One liter of water is equal to one cubic decimeter.
# Write a program that calculates the liters of water needed to fill the aquarium.

length_in_cm=int(input())
width_in_cm=int(input())
height_in_cm=int(input())
percentage_occupied_volume=float(input())
volume_aquarium=length_in_cm*width_in_cm*height_in_cm
total_liters=volume_aquarium*0.001
percentage=percentage_occupied_volume*0.01
liters=total_liters*(1-percentage)
print(f'{liters:.3f}')