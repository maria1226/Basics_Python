# 1. Read size of new space
width= int(input())
length = int(input())
height = int (input())

space_volume=width*length*height
volume_taken=0
# 2. Read input command 
while volume_taken<space_volume:
    input_text=input()
    # 2.2 if input is "Done" -> break
    if input_text=='Done':
        # 2.2.1 print cubic meters left
        print (f'{space_volume - volume_taken} Cubic meters left.')
        break
        # 2.1 if input is a number -> move boxes
    boxes_count=int(input_text)
    needed_volume = boxes_count
    volume_taken+=needed_volume
# 2.1.1 if free space is not enough -> print cubic meters needed
if volume_taken > space_volume:
    print (f'No more free space! You need {volume_taken-space_volume} Cubic meters more')
