age=int(input())
washing_machine_price=float(input())
toys_price=float(input())

toys_count = 0
money_amount = 0


for years in range(1,age+1):
    if years % 2 == 0:
        #price
       money_amount += years / 2 * 10
       money_amount-=1
        
    else:
        #toy
        toys_count+=1

toys_price=toys_count*toys_price   
total_amount = toys_price+money_amount

if total_amount>=washing_machine_price:
    print(f'Yes! {total_amount - washing_machine_price:.2f}')
else:
    print(f'No! {washing_machine_price- total_amount:.2f}')
          