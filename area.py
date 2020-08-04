figure_type=input()

if figure_type=='square':
    side_a=int(input())
    area=side_a*side_a
elif figure_type=='rectangle':
    side_a=float(input())
    side_b=float(input())
    area=side_a*side_b

elif figure_type=='circle':
    r=float(input())
    area=3.14*r**2

elif figure_type=='triangle':
    side_a=float(input())
    h=float(input())
    area=(side_a*h)/2

print(f'{area:.3f}')