#Question 1
a, b = 2.1, 2.9
assert round(a) == 2, "test 1.1 failed"
assert round(b) == 3, "test 1.2 failed"
assert round(-a) == -2, "test 1.3 failed"
assert round(-b) == -3, "test 1.4 failed"

#Question 2
assert (int(a), int(b)) == (2, 2), "test 2.1 failed"
assert (int(-a), int(-b)) == (-2, -2), "test 2.2 failed"

#Question 3
assert list(range(12, 16)) == [12,13,14,15], "test 3.1 failed"
assert list(range(0, 10, 2)) == [0,2,4,6,8], "test 3.2 failed"
assert list(range(5, -1, -1)) == [5,4,3,2,1,0], "test 3.3 failed"

#Question 4
import random
assert random.randint(1, 10) in [1,2,3,4,5,6,7,8,9,10], "test 4.1 failed"
assert random.randint(1, 2) in [1,2], "test 4.2 failed"

#Question 5
def what(n):
    if n == 1:
        return 1
    else:
        return n + what(n-1)

assert what(10) == 55, "test 5.1 failed"

#Question 6
def what(n, m):
    if n < 0:
        return -what(-n, m)
    else:
        if n == 1:
            return m
        else:
            return m + what(n-1, m)

assert what(-5,3) == -15, "test 6.1 failed"

#Question 7
def what():
    pass

assert what() == None, "test 7.1 failed"

#Question 8
a = [3,1,5,6,4,2]
assert random.choice(a) in [3,1,5,6,4,2], "test 8.1 failed"

#Question 9
b = sorted(a)
random.shuffle(a)
assert sorted(a) == sorted(b), "test 9.1 failed"

#Question 10
try:
    print(1 + 'a')
except:
    print('1a')
#should print 1a

print("All tests passed")

#Question 11
numberOfStreaks = 0
Sample_space = ['H', 'T']
for experimentNumber in range(10000):
 # Code that creates a list of 100 'heads' or 'tails' values.
    coin_flips = ''
    for _ in range(100):
        coin_flips += random.choice(Sample_space)

 # Code that checks if there is a streak of 6 heads or tails in a row.
    count = 1
    for i in range(1,len(coin_flips),1):
        if coin_flips[i] == coin_flips[i-1]:
            count += 1
            if count == 6:
                numberOfStreaks += 1
                break
        else:
            count = 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))


#Question 12
matrix = {}
matrix[0,0] = 1
matrix[1,0] = -2
matrix[0,1] = 3
matrix[1,1] = 8
print(matrix)

#Question 13
#Escape characters
print('Don\'t touch Mikey\'s hair')
print('Hi guys\nso nice to see you')
#Raw strings
print(r'Don\'t touch Mikey\'s hair')
print(r'Hi guys\nso nice to see you')
#Multiline strings
print('''Dear Annabelle,

The muck and bitter cold of the English frontline would be quite unbearable 
if it weren't for the everlasting impression your beauty has left on the inside of my eyelids.

Regrads,
Jonathan
''')
#Comments
def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')

#Question 14
#isX() methods
print('ello guvna'.isalpha())
print('ello guvna'.isalnum())
print('Ello Guvna'.istitle())
#join() method
print(' '.join(['What', 'great', 'salsa', 'this', 'is']))
#split() method
print('What great salsa this is'.split(' '))

#Question 15
#text justification
print('BINGO'.rjust(10))
print('BINGO'.ljust(10, '*'))
#removing whitespace
print('XXXXXyandzXXXXX'.strip('X'))
print('XXXXXyandzXXXXX'.rstrip('X'))
print('XXXXXyandzXXXXX'.lstrip('X'))
#ord() and chr()
print(ord('B'))
print(chr(66))
print(chr(66) == 'B' and ord('B') == 66)

#Question 16 is on page 144. I am aware of it
