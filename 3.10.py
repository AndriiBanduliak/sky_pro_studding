'''for num in range(1, 5):

    print('smile for 1 minute')

for num in range(10):
    print(f'{num} * 9 = {num*9}')

action = ['buy it', 'use it', 'break it', 'fix it']

action_index = range(len(action))

for i in action_index:
    print(i + 1)
    print(action[i])'''

price = int(input())

for i in range(1,13):
    monthly_payment = int(price / i)
    print(f'{i} month - {monthly_payment}')