col_1='AFKIU'
col_2='BGLQV'
col_3='CHMRWZ'
col_4='DINSX'
col_5='EJOTY'



count =int(input("Enter the length of the word."))
letter_place_number_list = []
next_letter_order= []
next_letter_place_number_list = []
next_next_letter_order = []
next_alphabel_table = []
for i in range(count):
    letters_place_number = input(f"Enter the {str(i+1)} letter in which coloumn: ")
    letter_place_number_list.append(letters_place_number)

for letter_place_number in letter_place_number_list:
    letter_place_number = int(letter_place_number)
    if letter_place_number == 1:
        next_letter_order.append(col_1)
    elif letter_place_number == 2:
        next_letter_order.append(col_2)
    elif letter_place_number == 3:
        next_letter_order.append(col_3)
    elif letter_place_number == 4:
        next_letter_order.append(col_4)
    elif letter_place_number == 5:
        next_letter_order.append(col_5)
for row in next_letter_order:
    #print(row)
    next_alphabel_table.append(row)
print(next_alphabel_table)
for i in range(count):
    next_letters_place_number = input(f"Enter the {str(i+1)} letter in which coloumn: ")
    next_letter_place_number_list.append(next_letters_place_number)
#print(letter_place_number_list)
#print(next_letter_order)


for i in range(count):
    for j in next_letter_place_number_list:
        j=int(j)
        print(next_alphabel_table[i][j-1])
        next_letter_place_number_list.remove(str(j))
        break

