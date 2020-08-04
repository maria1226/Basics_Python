# 1. Read student name
name=input()
# 2. Read marks until grades < 12
grades_counter=1
grades_sum=0
while  grades_counter<=12:
    current_grade_final_mark=float(input())
    # 2.1 Compare if mark>=4
    if current_grade_final_mark>=4:
        # 2.2 Complete grade
        # 2.3 Sum marks to total sum of marks
        print(f'completed grade №: {grades_counter} ')
        grades_counter+=1
        grades_sum+=current_grade_final_mark
        

# 3 Calculate average grade
average_grade=grades_sum/12
# 4. Print text +average grade
print(f'{name} graduated. Average grade: {average_grade:.2f}')