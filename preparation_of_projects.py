#Write a program that calculates how many hours an architect will need to draw projects of several construction sites. 
#The preparation of a project takes approximately three hours.
name=input()
number_of_projects=int(input())
required_hours=number_of_projects*3
print(f'The architect {name} will need {required_hours} hours to complete {number_of_projects} project/s.')