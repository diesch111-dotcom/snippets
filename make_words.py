''' make_words.py

For instance replace A in Aark with other letters

The idle IDE is usually part of the PYTHON installation!
If need be install the idle3 IDE on the LinuxMint terminal:
sudo apt update
sudo apt install idle3
...once installed shows up under 'Programming' as IDLE

tested with idle IDE and LinuxMint  vegaseat  07aug2026
'''

# make your own words, when Q comes up we want to use Qu
str1 = 'Aark'
print( "Replace A in %s with other letters:" % str1 )
# go from B to Z
for n in range(66, 91):
    ch = chr(n)
    if ch == 'Q':      # special case Q, use Qu
        ch = ch + 'u'
    print(str1.replace('A', ch))

print("using a generator expression...")

print('\n'.join(chr(n)+('ark','uark')[chr(n)=='Q']for n in range(66, 91)))

'''
Replace A in Aark with other letters:
Bark
Cark
Dark
Eark
Fark
Gark
Hark
Iark
Jark
Kark
Lark
Mark
Nark
Oark
Park
Quark
Rark
Sark
Tark
Uark
Vark
Wark
Xark
Yark
Zark
using a generator expression...
Bark
Cark
Dark
Eark
Fark
Gark
Hark
Iark
Jark
Kark
Lark
Mark
Nark
Oark
Park
Quark
Rark
Sark
Tark
Uark
Vark
Wark
Xark
Yark
Zark

'''
