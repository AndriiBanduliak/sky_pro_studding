shopping_list = ['apple','milk']
destination = input('Where ar u doing to do?\n')
if destination == 'picnic':
    shopping_list.append('shashlic')
    shopping_list.append('alcogol')
elif destination == 'guest':
    shopping_list.append('wine')
    shopping_list.append('cake')
elif destination == 'staying home':
    shopping_list.append('ice cream')
    shopping_list.append('popcorn')
else: print('Error')
print(f'Your shopping list {len(shopping_list)} of goods, {shopping_list}')

