# code for python tests

# types of variables / strings, integers and boolean
x = 'fuck u'
y = 1
z = True

# basic variable/string work
print('there was a man and he said ' + x + '.')

# basic string works
phrase = 'learn is hard!'
print(phrase.upper())
print(len(phrase))
print(phrase[0:5])
print(phrase[3:7])
print(phrase.index('is'))

# types of numbers and how to work with then
# real basic shit

# input works
# basic input and receive a message
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# print('Hello ' + name + '! Youre ' + age + ' years old.' )

# very basic adition calculator
# input 2 inputs in 2 variables and transform the str in int or float
# num1 = input('type a number: ')
# num2 = input('type a number: ')
# result = float(num1) + float(num2)
# print(result)

# mad libs game
# color = input('Type a color: ')
# plural_noum = input('Type a plural noum: ')
# character = input('Type a character: ')

# print('Roses are ' + color)
# print(plural_noum +' are blue')
# print('I love ' + character)

# lists

numbers = [3, 5, 6, 7]
games = ["COD", "GOW", "WOW", "LOL", "DOTA"]
games.extend(numbers)
print(games)

# if basic work

x = 5
if x == 5:
     print('Correct')
elif x > 5:
    print('To much')
elif x < 5:
    print('To little')
else:
    print('wtf bro')

# short handle if
# example if a > b: print("a is greater than b")

b = 'sup'
a = b
if a == b: print('a is greater than b')

j = 7
if j == 7:print('Correct')

# short handled elif
#a = 2 b = 330 print("A") if a > b else print("B")

b = 10
c = 30
print('KK') if b > c else print('KKK')

#tryting to setup git repository i hope that works
print('i miss her')


z = True
w = False
if z == True:
    print('It worked')
else:
    print('didnt worked')

