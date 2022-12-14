num = 4
is_solved = False

while not is_solved:
    ans = input("Угадай число: \n")
    if int(ans) == num:
        print("You get the number")
        is_solved = True
    else:
        print('You do not get the number')
