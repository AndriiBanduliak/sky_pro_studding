debt = 12350

while debt > 0:
    print(f'your debt is {debt}')
    payment = int(input('enter the sum: \n'))
    debt -= payment
print('you don"t have any debts')