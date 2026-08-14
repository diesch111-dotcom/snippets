#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' ASCII_table.py

Print a 16 column table of ASCII characters from 0 to 127
 
very good info ...
http://www.theasciicode.com.ar/

SyntaxWarning: invalid escape sequence 'backslash'

tested with VSCodium IDE on LinuxMint  VegasEat 19jul2026
'''

# dictionary of non-printable asccii characters
controls_dic = {
0: 'NUL', 1: 'SOH', 2: 'STX', 3: 'ETX', 4: 'EOT', 5: 'ENQ', 6: 'ACK',
7: 'BEL', 8: 'BS', 9: 'HT', 10: 'LF', 11: 'VT', 12: 'FF', 13: 'CR',
14: 'SO', 15: 'SI', 16: 'DLE', 17: 'DC1', 18: 'DC2', 19: 'DC3',
20: 'DC4', 21: 'NAK', 22: 'SYN', 23: 'ETB', 24: 'CAN', 25: 'EM',
26: 'SUB', 27: 'ESC', 28: 'FS', 29: 'GS', 30: 'RS', 31: 'US'
}

n = 1
for k in range(0, 128):
    if k < 32:
        s = controls_dic[k]
    else:
        s = chr(k)
    if n % 16 > 0:
        #print("%4s" % s, end=" ")
        print(f"{s:4s}", end=" ")
        
    else:
        #print("%4s" % s)
        print(f"{s:4s}")
    n += 1

"""
 NUL  SOH  STX  ETX  EOT  ENQ  ACK  BEL   BS   HT   LF   VT   FF   CR   SO   SI
 DLE  DC1  DC2  DC3  DC4  NAK  SYN  ETB  CAN   EM  SUB  ESC   FS   GS   RS   US
        !    "    #    $    %    &    '    (    )    *    +    ,    -    .    /
   0    1    2    3    4    5    6    7    8    9    :    ;    <    =    >    ?
   @    A    B    C    D    E    F    G    H    I    J    K    L    M    N    O
   P    Q    R    S    T    U    V    W    X    Y    Z    [    \    ]    ^    _
   `    a    b    c    d    e    f    g    h    i    j    k    l    m    n    o
   p    q    r    s    t    u    v    w    x    y    z    {    |    }    ~    

"""
