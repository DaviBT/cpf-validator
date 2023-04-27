cpf = input("Enter your CPF (put a space between each number): ") 

arrayCpf = cpf.split(" ")

lenCpfNum = len(arrayCpf)
firt9digitsOfCpf = lenCpfNum - 2

i = 11
position = 0
sumMultiplications = 0 # initializing the variable to store the sum of all multiplications

for i in range(firt9digitsOfCpf):
    i -= 1
    cpfItem = int(arrayCpf[position]) # converting the item to an integer before multiplying
    multiplication = cpfItem * i
    position += 1
    sumMultiplications += multiplication # adding the result of each multiplication to the sum

restOf = sumMultiplications % 11
if restOf < 2:
    verifyingDigit = 0
else:
    verifyingDigit = 11 - restOf

secondVerificationCpfArray = arrayCpf

k = 10
b = 0
while b < 2:
    secondVerificationCpfArray.pop(k)
    b += 1
    k -= 1

factor = 11
sumMultiplications2 = 0
position2 = 0
secondVerificationCpfArray.append(verifyingDigit)
for i in range(10):
    cpfItem2 = secondVerificationCpfArray[position2] 
    cpfItem2 = int(cpfItem2) # converting the item to an integer before multiplying
    multiplication2 = cpfItem2 * factor
    sumMultiplications2 += multiplication2 # adding the result of each multiplication to the sum
    position2 += 1
    factor -= 1

restOf2 = sumMultiplications2 % 11

if restOf2 < 2:
    verifyingDigit2 = 0
else:
    verifyingDigit2 = 11 - restOf2

CpfArray = secondVerificationCpfArray
CpfArray.append(verifyingDigit2)

# Divide array in groups of three
groupsOfThree = [CpfArray[i:i+3] for i in range(0, len(CpfArray)-2, 3)]

# array containing group of three separated by a float
groupsWithFloat = [''.join(map(str, group)) for group in groupsOfThree]

# Joining every groups in a unique string separated by a float 
stringNum = '.'.join(groupsWithFloat)

# putting a hyphen in the last two and joinning the last two itens
LastTwo = ''.join(map(str, CpfArray[-2:]))
stringNum += '-' + LastTwo

print(stringNum)