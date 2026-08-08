''' number_trick_all_the_same.py

The "all the same" number trick ...

Ask a person for their favorite number from 1 to 9
let's say the person picks 7
then you take the number below 7 which is 6
then the difference between this number and 9
which is 3, combine 6 and 3 to give a multiplier of 63
now 12345679 * 63 = 77777777

Some folks think numbers are magic, here are some examples...

tested with SublimeText IDE on LinuxMint  vegaseat 15jun2026
'''

n = 12345679  # that's 1 to 9 with the 8 is left out!

print('-'*9)
# k goes from 9 to <82 in steps of 9
for k in range(9, 82, 9):
    print( n * k )

""" result...
---------
111111111
222222222
333333333
444444444
555555555
666666666
777777777
888888888
999999999
"""

print('-'*40)

# same on steroids
steroid = 1000000001
n = 12345679  # that's 1 to 9 with the 8 is left out!

for k in range(9, 82, 9):
    print( steroid* n * k )

""" result...
111111111111111111
222222222222222222
333333333333333333
444444444444444444
555555555555555555
666666666666666666
777777777777777777
888888888888888888
999999999999999999
"""

print('-'*40)

# magic prime 37
n = 37

for k in range(3, 28, 3):
    print( n * k )

""" result...
111
222
333
444
555
666
777
888
999
"""

print('-'*40)

# the up and down number trick ...
# result is a number that goes from 1 to 9 and down again

n = 111111111   # that's nine ones

print("{:d} * {:d} = {:d}".format(n, n, n * n))

""" result...
111111111 * 111111111 = 12345678987654321
"""

print('-'*40)

sum10 = sum(range(10 + 1))
print(sum10)   # 55

sum100 = sum(range(100 + 1))
print(sum100)   # 5050

sum1000 = sum(range(1000 + 1))
print(sum1000)   # 500500

