print("Hey! Let's check your English :) ")
name = input('What is your name? ')
print(f"Hello, {name}.", '\n', f"So, {name}, let's start!")

print("First question: ", '\n', 'My name ****** Vova')
c = input()

if c == "is":
    print('Correct')
    suma1 = 10
else:
    c = 'is'
    print('Wrong answer!', f'Correct answer is "{c}"')
    suma1 = 0
print()

print("Second question: ", '\n', "I ****** coder")
c2 = input()

if c2 == 'am':
    print('Correct')
    suma2 = 10
else:
    c2 = 'am'
    print('Wrong answer!', f'Correct answer is"{c2}"')
    suma2 = 0

print()
print("Third question: ", '\n', "I live ***** Moscow")
c3 = input()

if c3 == 'in':
    print('Correct')
    suma3 = 10
else:
    c3 = 'in'
    print('Wrong answer!', f'Correct answer is "{c3}"')
    suma3 = 0

suma = suma1 + suma2 + suma3
points = int(suma / 10)
print()
print()

if points == 1:
    print(f"That's all, {name}. Test is complete.", '\n',
          "You have answered correct on: ", points, 'question')
    print()
    print('NOT BAD, You have 33% of correct answers')
elif points == 2:
    print(f"That's all, {name}. Test is complete.", '\n',
          "You have answered correct on: ", points, 'questions')
    print()
    print('GOOD WORK, You have 66% of correct answers')
elif points == 3:
    print(f"That's all, {name}. Test is complete.", '\n',
          "You havea answered correct on: ", points, 'questions')
    print()
    print('AWESOME!!! You have 100% of correct answers')
else: print('LOOOSEEER!!!','\n','You do not answered on any question correct!!!!WTF')
