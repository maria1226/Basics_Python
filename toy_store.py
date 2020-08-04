trip_cost=float(input())

puzzle_count=int(input())
dolls_count=int(input())
bears_count=int(input())
minions_count=int(input())
trucks_count=int(input())

one_puzzle_price=2.60
one_doll_price=3
one_bear_price=4.10
one_minion_price=8.20
one_truck_price=2

puzzle_total_price=puzzle_count*one_puzzle_price
doll_total_price=dolls_count*one_doll_price
bears_total_price=bears_count*one_bear_price
minions_total_price=minions_count*one_minion_price
trucks_total_price=trucks_count*one_truck_price

total_price=puzzle_total_price+doll_total_price+bears_total_price+minions_total_price+trucks_total_price

total_count=puzzle_count+dolls_count+bears_count+minions_count+trucks_count
if total_count>=50:
    total_price=total_price*(1-0.25)

total_price=total_price*(1-0.1)    

money=abs(total_price-trip_cost)
if total_price>=trip_cost:
    print(f'Yes! {money:.2f} lv left.')
else :
    print(f'Not enough money! {money:.2f} lv needed.')   
