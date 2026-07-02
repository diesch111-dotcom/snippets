''' elements_dict2.py
create a dictionary of elements from a csv string/file
the key is the element symbol the value is a tuple
(name, atomic_number, atomic_weight)


works with LinuxMint and Spyder IDE  dns(vegaseat)  17jun2026
'''

import pprint

# a csv string of atomic_num,symbol,name,atomic_weight in each line
# pulled this out of chemical data from past 30+ years of lab work
# csv --> comma separated values
elements_csv = '''\
1,H,Hydrogen,1.008
2,He,Helium,4.002602
3,Li,Lithium,6.94
4,Be,Beryllium,9.0121831
5,B,Boron,10.81
6,C,Carbon,12.011
7,N,Nitrogen,14.007
8,O,Oxygen,15.999
9,F,Fluorine,18.998403163
10,Ne,Neon,20.1797
11,Na,Sodium,22.98976928
12,Mg,Magnesium,24.305
13,Al,Aluminium,26.9815385
14,Si,Silicon,28.085
15,P,Phosphorus,30.973761998
16,S,Sulfur,32.06
17,Cl,Chlorine,35.45
18,Ar,Argon,39.948
19,K,Potassium,39.0983
20,Ca,Calcium,40.078
21,Sc,Scandium,44.955908
22,Ti,Titanium,47.867
23,V,Vanadium,50.9415
24,Cr,Chromium,51.9961
25,Mn,Manganese,54.938044
26,Fe,Iron,55.845
27,Co,Cobalt,58.933194
28,Ni,Nickel,58.6934
29,Cu,Copper,63.546
30,Zn,Zinc,65.38
31,Ga,Gallium,69.723
32,Ge,Germanium,72.63
33,As,Arsenic,74.921595
34,Se,Selenium,78.971
35,Br,Bromine,79.904
36,Kr,Krypton,83.798
37,Rb,Rubidium,85.4678
38,Sr,Strontium,87.62
39,Y,Yttrium,88.90584
40,Zr,Zirconium,91.224
41,Nb,Niobium,92.90637
42,Mo,Molybdenum,95.95
43,Tc,Technetium,97.0
44,Ru,Ruthenium,101.07
45,Rh,Rhodium,102.9055
46,Pd,Palladium,106.42
47,Ag,Silver,107.8682
48,Cd,Cadmium,112.414
49,In,Indium,114.818
50,Sn,Tin,118.71
51,Sb,Antimony,121.76
52,Te,Tellurium,127.6
53,I,Iodine,126.90447
54,Xe,Xenon,131.293
55,Cs,Caesium,132.90545196
56,Ba,Barium,137.327
57,La,Lanthanum,138.90547
58,Ce,Cerium,140.116
59,Pr,Praseodymium,140.90766
60,Nd,Neodymium,144.242
61,Pm,Promethium,145.0
62,Sm,Samarium,150.36
63,Eu,Europium,151.964
64,Gd,Gadolinium,157.25
65,Tb,Terbium,158.92535
66,Dy,Dysprosium,162.5
67,Ho,Holmium,164.93033
68,Er,Erbium,167.259
69,Tm,Thulium,168.93422
70,Yb,Ytterbium,173.054
71,Lu,Lutetium,174.9668
72,Hf,Hafnium,178.49
73,Ta,Tantalum,180.94788
74,W,Tungsten,183.84
75,Re,Rhenium,186.207
76,Os,Osmium,190.23
77,Ir,Iridium,192.217
78,Pt,Platinum,195.084
79,Au,Gold,196.966569
80,Hg,Mercury,200.592
81,Tl,Thallium,204.38
82,Pb,Lead,207.2
83,Bi,Bismuth,208.9804
84,Po,Polonium,209.0
85,At,Astatine,210.0
86,Rn,Radon,222.0
87,Fr,Francium,223.0
88,Ra,Radium,226.0
89,Ac,Actinium,227.0
90,Th,Thorium,232.0377
91,Pa,Protactinium,231.03588
92,U,Uranium,238.02891
93,Np,Neptunium,237.0
94,Pu,Plutonium,244.0
95,Am,Americium,243.0
96,Cm,Curium,247.0
97,Bk,Berkelium,247.0
98,Cf,Californium,251.0
99,Es,Einsteinium,252.0
100,Fm,Fermium,257.0
101,Md,Mendelevium,258.0
102,No,Nobelium,259.0
103,Lr,Lawrencium,262.0
104,Rf,Rutherfordium,267.0
105,Db,Dubnium,270.0
106,Sg,Seaborgium,271.0
107,Bh,Bohrium,270.0
108,Hs,Hassium,277.0
109,Mt,Meitnerium,276.0
110,Ds,Darmstadtium,281.0
111,Rg,Roentgenium,282.0
112,Cn,Copernicium,285.0
113,Uut,Ununtrium,285.0
114,Fl,Flerovium,289.0
115,Uup,Ununpentium,289.0
116,Lv,Livermorium,293.0
117,Uus,Ununseptium,294.0
118,Uuo,Ununoctium,294.0'''

filename = "elements2.csv"
# write to a file, just for kicks
with open(filename, "w") as fout:
    fout.write(elements_csv)

# read the file back in as a csv string
with open(filename, "r") as fin:
    elements_csv2 = fin.read()


# convert csv string to dictionary of
# symbol:(name, int(atomic_number), float(atomic_weight)) pairs
# create an empty dictionary
e_dict2 = {}
for line in elements_csv2.split("\n"):
    e_list = line.split(",")
    #print(e_list)
    e_dict = {e_list[1]: (e_list[2], int(e_list[0]), float(e_list[3]))}
    e_dict2.update(e_dict)

pprint.pprint(e_dict2)

print('-'*30)

# using dictionary comprehension:
# note: split() gives a list
e_dict3 = {line.split(",")[1]: (line.split(",")[2], int(line.split(",")[0]),\
float(line.split(",")[3])) for line in elements_csv2.split("\n")}

pprint.pprint(e_dict3)  # same as e_dict2

''' # dictionary of symbol: (name, atomic_number, atomic_weight)

{'Ac': ('Actinium', 89, 227.0),
 'Ag': ('Silver', 47, 107.8682),
 'Al': ('Aluminium', 13, 26.9815385),
 'Am': ('Americium', 95, 243.0),
 'Ar': ('Argon', 18, 39.948),
 'As': ('Arsenic', 33, 74.921595),
 'At': ('Astatine', 85, 210.0),
 'Au': ('Gold', 79, 196.966569),
 'B': ('Boron', 5, 10.81),
 'Ba': ('Barium', 56, 137.327),
 'Be': ('Beryllium', 4, 9.0121831),
 'Bh': ('Bohrium', 107, 270.0),
 'Bi': ('Bismuth', 83, 208.9804),
 'Bk': ('Berkelium', 97, 247.0),
 'Br': ('Bromine', 35, 79.904),
 'C': ('Carbon', 6, 12.011),
 'Ca': ('Calcium', 20, 40.078),
 'Cd': ('Cadmium', 48, 112.414),
 'Ce': ('Cerium', 58, 140.116),
 'Cf': ('Californium', 98, 251.0),
 'Cl': ('Chlorine', 17, 35.45),
 'Cm': ('Curium', 96, 247.0),
 'Cn': ('Copernicium', 112, 285.0),
 'Co': ('Cobalt', 27, 58.933194),
 'Cr': ('Chromium', 24, 51.9961),
 'Cs': ('Caesium', 55, 132.90545196),
 'Cu': ('Copper', 29, 63.546),
 'Db': ('Dubnium', 105, 270.0),
 'Ds': ('Darmstadtium', 110, 281.0),
 'Dy': ('Dysprosium', 66, 162.5),
 'Er': ('Erbium', 68, 167.259),
 'Es': ('Einsteinium', 99, 252.0),
 'Eu': ('Europium', 63, 151.964),
 'F': ('Fluorine', 9, 18.998403163),
 'Fe': ('Iron', 26, 55.845),
 'Fl': ('Flerovium', 114, 289.0),
 'Fm': ('Fermium', 100, 257.0),
 'Fr': ('Francium', 87, 223.0),
 'Ga': ('Gallium', 31, 69.723),
 'Gd': ('Gadolinium', 64, 157.25),
 'Ge': ('Germanium', 32, 72.63),
 'H': ('Hydrogen', 1, 1.008),
 'He': ('Helium', 2, 4.002602),
 'Hf': ('Hafnium', 72, 178.49),
 'Hg': ('Mercury', 80, 200.592),
 'Ho': ('Holmium', 67, 164.93033),
 'Hs': ('Hassium', 108, 277.0),
 'I': ('Iodine', 53, 126.90447),
 'In': ('Indium', 49, 114.818),
 'Ir': ('Iridium', 77, 192.217),
 'K': ('Potassium', 19, 39.0983),
 'Kr': ('Krypton', 36, 83.798),
 'La': ('Lanthanum', 57, 138.90547),
 'Li': ('Lithium', 3, 6.94),
 'Lr': ('Lawrencium', 103, 262.0),
 'Lu': ('Lutetium', 71, 174.9668),
 'Lv': ('Livermorium', 116, 293.0),
 'Md': ('Mendelevium', 101, 258.0),
 'Mg': ('Magnesium', 12, 24.305),
 'Mn': ('Manganese', 25, 54.938044),
 'Mo': ('Molybdenum', 42, 95.95),
 'Mt': ('Meitnerium', 109, 276.0),
 'N': ('Nitrogen', 7, 14.007),
 'Na': ('Sodium', 11, 22.98976928),
 'Nb': ('Niobium', 41, 92.90637),
 'Nd': ('Neodymium', 60, 144.242),
 'Ne': ('Neon', 10, 20.1797),
 'Ni': ('Nickel', 28, 58.6934),
 'No': ('Nobelium', 102, 259.0),
 'Np': ('Neptunium', 93, 237.0),
 'O': ('Oxygen', 8, 15.999),
 'Os': ('Osmium', 76, 190.23),
 'P': ('Phosphorus', 15, 30.973761998),
 'Pa': ('Protactinium', 91, 231.03588),
 'Pb': ('Lead', 82, 207.2),
 'Pd': ('Palladium', 46, 106.42),
 'Pm': ('Promethium', 61, 145.0),
 'Po': ('Polonium', 84, 209.0),
 'Pr': ('Praseodymium', 59, 140.90766),
 'Pt': ('Platinum', 78, 195.084),
 'Pu': ('Plutonium', 94, 244.0),
 'Ra': ('Radium', 88, 226.0),
 'Rb': ('Rubidium', 37, 85.4678),
 'Re': ('Rhenium', 75, 186.207),
 'Rf': ('Rutherfordium', 104, 267.0),
 'Rg': ('Roentgenium', 111, 282.0),
 'Rh': ('Rhodium', 45, 102.9055),
 'Rn': ('Radon', 86, 222.0),
 'Ru': ('Ruthenium', 44, 101.07),
 'S': ('Sulfur', 16, 32.06),
 'Sb': ('Antimony', 51, 121.76),
 'Sc': ('Scandium', 21, 44.955908),
 'Se': ('Selenium', 34, 78.971),
 'Sg': ('Seaborgium', 106, 271.0),
 'Si': ('Silicon', 14, 28.085),
 'Sm': ('Samarium', 62, 150.36),
 'Sn': ('Tin', 50, 118.71),
 'Sr': ('Strontium', 38, 87.62),
 'Ta': ('Tantalum', 73, 180.94788),
 'Tb': ('Terbium', 65, 158.92535),
 'Tc': ('Technetium', 43, 97.0),
 'Te': ('Tellurium', 52, 127.6),
 'Th': ('Thorium', 90, 232.0377),
 'Ti': ('Titanium', 22, 47.867),
 'Tl': ('Thallium', 81, 204.38),
 'Tm': ('Thulium', 69, 168.93422),
 'U': ('Uranium', 92, 238.02891),
 'Uuo': ('Ununoctium', 118, 294.0),
 'Uup': ('Ununpentium', 115, 289.0),
 'Uus': ('Ununseptium', 117, 294.0),
 'Uut': ('Ununtrium', 113, 285.0),
 'V': ('Vanadium', 23, 50.9415),
 'W': ('Tungsten', 74, 183.84),
 'Xe': ('Xenon', 54, 131.293),
 'Y': ('Yttrium', 39, 88.90584),
 'Yb': ('Ytterbium', 70, 173.054),
 'Zn': ('Zinc', 30, 65.38),
 'Zr': ('Zirconium', 40, 91.224)}
'''

print('-'*40)

# testing the element dictionary e_dict2
# look up the dictionary via the key
print(e_dict2['H'])     # ('Hydrogen', 1, 1.008)
print(e_dict2['Fe'][0]) # Iron

sf = "Atomic weight of {} is {}"
print(sf.format(e_dict2['Au'][0], e_dict2['Au'][2]))

'''
Atomic weight of Gold is 196.966569
'''

print('-'*40)
max_val = 0
# find the element with the highest atomic weight
for value in e_dict2.values():
    #print(value[2])
    val = value[2]
    if val > max_val:
        max_val = val
        max_value = value

print(max_value)  # ('Ununseptium', 117, 294.0)
