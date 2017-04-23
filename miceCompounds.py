weight_kg = 0.019 # average kilograms, should really be an user input
dose_mg_kg = 60

# variables for iterations, consider a for loop instead
n = 0
a = 0


################Section 1: calculation of the volume per animal#################

# makes a new empty list
mw_list = []

# opens the file and allows the selection of lines
mw_file = open("C:\DIRECTORY\mw_compounds.txt", "r")
lines = mw_file.readlines()

# takes the new line character from the left and right of the words of the list
# and appends each of the 16 elements from the file to the empty list
while len(mw_list) != 16:
    clean_line = lines[n].strip("\n")
    mw_list.append(clean_line)
    n += 1

# closes opened file
mw_file.close()

ul_per_animal_list = []

while a != 16:
    mw = float((mw_list[a]))
    ul_per_animal = (((weight_kg * dose_mg_kg) / mw) / 0.08) * 1000
    ul_per_animal_list.append(ul_per_animal)
    ul_per_animal = round(ul_per_animal , 2)
    print "Use %r uL of compound number %r, with M.w. = %r" % (ul_per_animal, a, mw)
    a += 1


###Section 2: calculation of the volumes of the solvent for each compound to make a 8*10E-2 solution###

concentration = 0.08 # Molar
animals = 1

m = 0
a = 0
b = 0
c = 0
d = 0
loop = 0

amount_list = []

amount_file = open("C:\DIRECTORY\mg_compounds.txt", "r")
lines = amount_file.readlines()

while len(amount_list) != 16:
    clean_line = lines[m].strip("\n")
    amount_list.append(clean_line)
    m += 1


ul_per_compound_list = []


while b != 16:
    amount = float((amount_list[b]))
    mw = float((mw_list[a]))
    ul_per_compound = ((amount / mw) / concentration) * 1000
    ul_per_compound_list.append(ul_per_compound)
    ul_per_compound = round(ul_per_compound , 2)
    print "Use %r uL of DMSO to compound %r, with M.w. = %r" % (ul_per_compound, a, mw)
    a += 1
    b += 1


while loop != 16:

    while (ul_per_animal_list[c] * animals) < ul_per_compound_list[c]:
        animals += 1

    else:
        animals_corrected = animals - 1
        print "You can only use %d animals for compound number %d" % (animals_corrected, d)
        animals = 0
        c += 1
        d += 1
        loop += 1
