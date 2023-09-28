# Take qty and price and display amount after 10% discount

price = int(input("Enter price :"))
qty = int(input("Enter qty : "))

amount = price * qty
discount = amount * 10 // 100
net_amount = amount - discount

print('Net Amount =', net_amount)
