#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Fname_list2.py

writing and reading files using the 'with' context manager
'with' will close the file handle properly

read in a file of female first names where each name is on a sepearate line
display a list via
pprint.pprint(object, stream=None, indent=1, width=80,
    depth=None, *, compact=False)
compact=True will print as many sequence elements as will fit within
the given width (default is 80) on each line

Python module json can be used to dump and load list objects
json --> JavaScript Object Notation
eg.
fname = "mylist.jsn"
with open(fname, "w") as fout:
    json.dump(mylist2, fout)
eg.
with open(fname, "r") as fin:
    mylist3 = json.load(fin)
    

tested with LinuxMint and Spyder IDE  dns(vegaseat)  4jul2026
"""

import pprint
import bisect 
import json  # for optional save and load the resulting list
import os
# change te diredory
# this will find eg. '../data/FNames.txt'
os.chdir('/media/dietrich41/9325-9047/AAtest_py/data')

file_name = "../data/FNames.txt"
# note that readlines() gives a list of the file data lines
# it keeps the newline character at the end
with open(file_name, "r") as fin:
    fem_name_list2 = fin.readlines()
    
#print(fem_name_list2)

fem_name_list = []
# to avoid the trailing newline charatcer use
with open(file_name, "r") as file:
    for line in file:
        fem_name_list.append(line.strip())

# sort in place
fem_name_list.sort()

#print(fem_name_list, len(fem_name_list))
print(len(fem_name_list))

# insert a new name at the correct position in the list
new_name = 'Baerbel'
# uses insort (insert in sorted list)
bisect.insort(fem_name_list, new_name)

# length of list (number of items)
print(len(fem_name_list))

print('='*76)

# testing
# list all the names that start with 'Y'
fem_name_list_Y = [name for name in fem_name_list if name.startswith('Y')]
pprint.pprint(fem_name_list_Y, width=76, compact=True)

'''
['Yahni', 'Yana', 'Yolanda', 'Yoriko', 'Youko', 'Yulia', 'Yvette']
'''

print('='*76)
        
pprint.pprint(fem_name_list, width=76, compact=True)

'''
['Abby', 'Abigail', 'Adela', 'Adele', 'Adelheide', 'Adrian', 'Adrianna',
 'Adrienne', 'Agatha', 'Agnes', 'Akiko', 'Akina', 'Alana', 'Alea', 'Alena',
 'Alessandra', 'Alexa', 'Alexandra', 'Alexia', 'Alexis', 'Alice', 'Alicia',
 'Alison', 'Alissa', 'Alley', 'Allie', 'Allison', 'Allyssa', 'Alva',
 'Amanda', 'Amber', 'Amie', 'Amy', 'Anabel', 'Anastasia', 'Andrea', 'Aneke',
 'Angela', 'Anita', 'Anja', 'Anke', 'Ann', 'Anna', 'Anne', 'Annette',
 'Annette', 'Annie', 'Aphrodite', 'April', 'Arden', 'Aria', 'Arial',
 'Arianna', 'Ariel', 'Arlinda', 'Ashley', 'Astrid', 'Athena', 'Audra',
 'Audrey', 'Auria', 'Autumn', 'Ava', 'Avis', 'Azizi', 'Azuma', 'Babett',
 'Baerbel', 'Barb', 'Barbara', 'Barbie', 'Baylee', 'Bea', 'Beate',
 'Beatrice', 'Becky', 'Belinda', 'Bella', 'Bernadette', 'Beth', 'Betia',
 'Betty', 'Bia', 'Bianca', 'Billiejo', 'Birgit', 'Blair', 'Blake', 'Bobbie',
 'Bonnie', 'Brenda', 'Briana', 'Bridgett', 'Britt', 'Brittany', 'Brittney',
 'Brooke', 'Caitlin', 'Callie', 'Callista', 'Camille', 'Candice', 'Candy',
 'Cara', 'Carissa', 'Carla', 'Carly', 'Carmela', 'Carmen', 'Carmine',
 'Carol', 'Carolina', 'Caroline', 'Carolyn', 'Carra', 'Carrie', 'Carson',
 'Casey', 'Cassandra', 'Cassie', 'Cathy', 'Celeste', 'Celia', 'Celina',
 'Chantelle', 'Charlene', 'Charlotte', 'Chasey', 'Chastity', 'Chelsea',
 'Cher', 'Cherie', 'Cheryl', 'Cheyen', 'Cheyenne', 'Chihiro', 'Chloe',
 'Chrissy', 'Christa', 'Christina', 'Christine', 'Cindy', 'Claire',
 'Clarice', 'Clarissa', 'Claudia', 'Cleo', 'Colleen', 'Collette', 'Connie',
 'Coreen', 'Corinna', 'Corky', 'Corrie', 'Corrine', 'Cory', 'Crystal',
 'Cyndi', 'Cynthia', 'Dagmar', 'Daisy', 'Dale', 'Dallas', 'Dana', 'Daniela',
 'Danielle', 'Daphne', 'Darcy', 'Darla', 'Dawn', 'Debbie', 'Debora',
 'Debra', 'Dee', 'Deena', 'Deidra', 'Deidre', 'Deleen', 'Delila', 'Demi',
 'Demitra', 'Denise', 'Desiree', 'Devine', 'Devon', 'Diana', 'Dianne',
 'Dixie', 'Dolly', 'Donita', 'Donna', 'Doris', 'Dorothy', 'Dotty', 'Drew',
 'Druna', 'Eden', 'Edina', 'Edith', 'Edna', 'Eileen', 'Elaine', 'Elana',
 'Elena', 'Elke', 'Ellen', 'Elli', 'Ellina', 'Eloise', 'Elona', 'Emillia',
 'Emily', 'Emma', 'Erika', 'Erin', 'Esmeralda', 'Ester', 'Euphemia', 'Eva',
 'Eve', 'Evelyn', 'Evgenia', 'Evgina', 'Faith', 'Fawn', 'Faye', 'Febe',
 'Felicia', 'Fila', 'Fran', 'Francesca', 'Frankie', 'Frannie', 'Frieda',
 'Gabriella', 'Gabrielle', 'Gaby', 'Gail', 'Gale', 'Geneve', 'Georgia',
 'Gerda', 'Gilda', 'Gillian', 'Gin', 'Gina', 'Ginger', 'Gisela', 'Gita',
 'Gitte', 'Gloria', 'Grace', 'Gretel', 'Gwen', 'Haley', 'Haley', 'Halle',
 'Hanna', 'Hannah', 'Hattie', 'Hayley', 'Hazel', 'Heather', 'Heidi',
 'Heidrun', 'Heika', 'Heike', 'Helen', 'Helena', 'Helga', 'Hilda', 'Hilde',
 'Hildegard', 'Hisako', 'Holly', 'Ilse', 'Indigo', 'Inga', 'Inge',
 'Ingeborg', 'Ingrid', 'Irena', 'Irene', 'Irmgard', 'Isabel', 'Isolde',
 'Ivana', 'Iveta', 'Ivy', 'Jackie', 'Jacqueline', 'Jade', 'Jamie', 'Jana',
 'Jane', 'Janessa', 'Janet', 'Janice', 'Janie', 'Janine', 'Janis', 'Jannay',
 'Jasmine', 'Jayda', 'Jean', 'Jenna', 'Jennifer', 'Jenny', 'Jerry', 'Jess',
 'Jessica', 'Jessie', 'Jessy', 'Jette', 'Jezebel', 'Jill', 'Jimmiann',
 'Joanne', 'Jocelyn', 'Jodie', 'Jody', 'Joelle', 'Johanna', 'Joli', 'Joni',
 'Jonnie', 'Jordan', 'Josie', 'Joy', 'Joyce', 'Juana', 'Judy', 'Julia',
 'Julie', 'Kalin', 'Kalissa', 'Kanami', 'Kandace', 'Karen', 'Karie',
 'Karin', 'Karina', 'Karita', 'Karla', 'Karni', 'Kassia', 'Kassy', 'Katama',
 'Kate', 'Katelyn', 'Kathrin', 'Kathy', 'Katia', 'Katie', 'Katja', 'Kay',
 'Keiko', 'Kelly', 'Kelsey', 'Kerry', 'Keyla', 'Kia', 'Kim', 'Kimberly',
 'Kintra', 'Kira', 'Kirsten', 'Kitty', 'Krista', 'Kristen', 'Kristina',
 'Ksenia', 'Kyndal', 'Lace', 'Laika', 'Lana', 'Lara', 'Laura', 'Laverne',
 'Layla', 'Lea', 'Leah', 'Lee', 'Leigh', 'Lena', 'Lenka', 'Lenna',
 'Lenoshka', 'Lesa', 'Leslie', 'Libby', 'Liddy', 'Liese', 'Liesel', 'Lila',
 'Lillian', 'Lilly', 'Lina', 'Linda', 'Lindsey', 'Linet', 'Lisa', 'Lissie',
 'Liv', 'Liz', 'Liza', 'Lola', 'Lolita', 'Lonnie', 'Lora', 'Lorain', 'Lore',
 'Loretta', 'Lorey', 'Lori', 'Lorna', 'Louise', 'Lucie', 'Lucinda', 'Lucy',
 'Ludmila', 'Lulu', 'Lydia', 'Lyndell', 'Lyndsey', 'Lynette', 'Lynn',
 'Mable', 'Macie', 'Maddie', 'Madeleine', 'Madeline', 'Madge', 'Madlyn',
 'Mae', 'Maggy', 'Maia', 'Malka', 'Malory', 'Mandy', 'Manu', 'Mara',
 'Marcee', 'Marcella', 'Marcia', 'Marcy', 'Mareik', 'Margot', 'Margret',
 'Maria', 'Marian', 'Mariane', 'Marianne', 'Marie', 'Marijam', 'Marika',
 'Marika', 'Mariko', 'Marilyn', 'Marina', 'Maris', 'Mariska', 'Marissa',
 'Marla', 'Marlena', 'Marlene', 'Marlise', 'Marly', 'Marsha', 'Marta',
 'Martha', 'Martina', 'Mary', 'Maryann', 'Masha', 'Mason', 'Matilda',
 'Mattie', 'Maui', 'Maura', 'Megan', 'Melanie', 'Melanie', 'Melany',
 'Melilla', 'Melinda', 'Melissa', 'Melody', 'Mena', 'Mercedes', 'Meredith',
 'Meris', 'Mesina', 'Mette', 'Miana', 'Micah', 'Michelle', 'Mickey',
 'Mickie', 'Mila', 'Millie', 'Mindy', 'Mira', 'Miranda', 'Mirja', 'Mirka',
 'Misha', 'Mishka', 'Missy', 'Misty', 'Mita', 'Molly', 'Monica', 'Monika',
 'Monique', 'Morgan', 'Myra', 'Myril', 'Nadia', 'Nadya', 'Nancy',
 'Nantasha', 'Naomi', 'Natalia', 'Nataly', 'Natanya', 'Neriah', 'Nicki',
 'Nicole', 'Nikkita', 'Nina', 'Nisha', 'Nishi', 'Noleen', 'Nora', 'Odell',
 'Olga', 'Olive', 'Olivia', 'Opal', 'Paige', 'Paisley', 'Paloma', 'Pam',
 'Pamela', 'Paola', 'Parsy', 'Patricia', 'Patt', 'Pattie', 'Paula',
 'Pauline', 'Peggy', 'Pennie', 'Persia', 'Petra', 'Petrinka', 'Phoebe',
 'Phyllis', 'Pia', 'Poppy', 'Priscilla', 'Rachel', 'Raine', 'Ramona',
 'Rana', 'Randy', 'Raquel', 'Rayna', 'Reba', 'Rebecca', 'Regan', 'Regina',
 'Rena', 'Renate', 'Renee', 'Rennie', 'Rhonda', 'Rhonda', 'Ricki', 'Ricky',
 'Rina', 'Rita', 'Robby', 'Roberta', 'Robin', 'Rochelle', 'Romina', 'Rory',
 'Rosalie', 'Rose', 'Rosie', 'Roxie', 'Ruby', 'Ruth', 'Sabine', 'Sabrina',
 'Sadie', 'Sage', 'Sahar', 'Sally', 'Samantha', 'Sameerah', 'Sandra',
 'Sandy', 'Sarah', 'Sasha', 'Savanna', 'Sayaka', 'Scarlett', 'Sedta',
 'Selia', 'Selina', 'Selma', 'Seneca', 'Serena', 'Serina', 'Shalini',
 'Shana', 'Shane', 'Shannon', 'Shareen', 'Sharia', 'Sharon', 'Sharry',
 'Shay', 'Sheila', 'Shelby', 'Shelly', 'Sheralee', 'Shereen', 'Sherrie',
 'Sherry', 'Sheryl', 'Shirley', 'Shizuka', 'Shoshonna', 'Sidney', 'Sierra',
 'Silke', 'Silvia', 'Silvie', 'Simone', 'Sina', 'Sittia', 'Skyler', 'Sofia',
 'Sonja', 'Sophia', 'Sophie', 'Stacey', 'Stacy', 'Star', 'Stella',
 'Stephanie', 'Stephie', 'Stevie', 'Sue', 'Summer', 'Sunny', 'Surrey',
 'Susan', 'Susanna', 'Susie', 'Suzette', 'Svenja', 'Svetlana', 'Sybille',
 'Sydney', 'Sylvia', 'Sylvie', 'Tabatha', 'Tabby', 'Tabitha', 'Tamara',
 'Tammy', 'Tanya', 'Tara', 'Tatum', 'Tatyana', 'Taylor', 'Teresa', 'Teri',
 'Terry', 'Tess', 'Tessa', 'Tessie', 'Thelma', 'Theresa', 'Tiffany', 'Tina',
 'Tineke', 'Toni', 'Tonie', 'Tonya', 'Tori', 'Tracy', 'Trina', 'Trine',
 'Trish', 'Trisha', 'Trissa', 'Trixie', 'Tyler', 'Ulla', 'Ulrike', 'Unne',
 'Ursel', 'Ursula', 'Uschi', 'Ute', 'Val', 'Valerie', 'Vanessa', 'Velvet',
 'Venice', 'Venus', 'Vera', 'Verena', 'Verginia', 'Veronica', 'Veruschka',
 'Vicki', 'Vicky', 'Victoria', 'Viola', 'Violet', 'Vivian', 'Vlada',
 'Wanda', 'Wendy', 'Whitney', 'Wilda', 'Wilma', 'Xena', 'Xenia', 'Xuan',
 'Yahni', 'Yana', 'Yolanda', 'Yoriko', 'Youko', 'Yulia', 'Yvette', 'Zaila',
 'Zara', 'Zelda', 'Zena', 'Zia', 'Zina', 'Zoe', 'Zoey']
'''

"""
print('='*76)

# safe result to a new file
file_name2 = "../data/FNames2.jsn"
# 'with' will close the file handle properly
# "w" will create a new file if it does not exist
# otherwise it will overwrite the existing file
# "wa" will append to an existing file
with open(file_name2, "w") as fout:
    json.dump(fem_name_list, fout)

print("{} has been written".format(file_name2))

# test ...
with open(file_name2, "r") as fin:
    fem_name_list3 = json.load(fin)

print('='*76)
        
pprint.pprint(fem_name_list3, width=76, compact=True)

"""
