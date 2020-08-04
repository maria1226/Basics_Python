# Bozhidara has several houses on the Black Sea coast and wants to green the yards of some of them, such as
# thus creating a cozy atmosphere and comfort for your guests. 
# She has hired a company for this purpose.
# Write a program that calculates the necessary funds that Bozhidara will have to pay to
# the company executing the project. 
# The price per square meter is BGN 7.61 with VAT. Because her yard is quite
# large, the contractor company offers an 18% discount on the final price.
Sq_meters_that_will_be_landscaped=float(input())

price=Sq_meters_that_will_be_landscaped*7.61

discount=price*0.18

final_price=price-discount

print(f'The final price is: {final_price:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')