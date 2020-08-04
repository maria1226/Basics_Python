number_of_transactions=int(input())

transactions_made=0
account_balance=0
while transactions_made < number_of_transactions:
    transaction_value=float(input())
    if transaction_value<0:
        print(f'Invalid operation')
        break
        
    account_balance +=transaction_value
    transactions_made+=1
    print(f'Increase:{transaction_value}')

print(f'Total:{account_balance}')    
