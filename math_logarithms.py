''' math_logarithms.py
working with the math log module

If need be install the idle3 IDE on the LinuxMint terminal:
sudo apt update
sudo apt install idle3
...once installed shows up under 'Programming' under IDLE

tested with IDLE IDE and LinuxMint  vegaseat  07aug2026
'''

import math

# make sure N stays above zero
N = 2.0

print(math.log(math.e))    # 1.0
print(math.log10(math.e))  # 0.4342944819032518

print(math.log10(N)/math.log(N))  # 0.4342944819032518
print(math.log10(math.e)/math.log(math.e))  # 0.4342944819032518

# math.log(N)/math.log10(N) = math.log(math.e)/math.log10(math.e)
# math.log(N)/math.log10(N) = 1.0/math.log10(math.e)
# math.log(N) = math.log10(N)/math.log10(math.e)
# math.log(N)/math.log10(N) = math.log(math.e)/math.log10(math.e)
# math.log(N)/math.log10(N) = math.log(math.e)/math.log10(math.e)
# math.log10(N) = math.log(N)/math.log(math.e)/math.log10(math.e)
# math.log10(N) = math.log(N)/1.0/math.log10(math.e)
# math.log10(N) = math.log(N) * math.log10(math.e)

print()
print(math.log10(N))  # 0.3010299956639812
print(math.log(N) * math.log10(math.e))
# math.log10(math.e)) = 0.4342944819032518
print(math.log(N) * 0.4342944819032518)  # 0.3010299956639812

print()

# stay above zero
print(math.log10(0.01))  # -2.0
print(math.log10(0.01)/math.log(0.01))     # 0.4342944819032518
# calculate math.log10(N) using natural math.log(N)
print(math.log(0.01) * 0.4342944819032518) # -1.9999999999999998

'''
notice that the 2 ratios
math.log10(0.01)/math.log(0.01)
math.log10(math.e)/math.log(math.e)
stay the same, now you can solve for log10() in terms of natural log()

'''

