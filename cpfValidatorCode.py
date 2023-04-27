cpf = input("Enter your CPF (put a space between each number): ")

arrayCpf = cpf.split(" ")

lenCpfNum = len(arrayCpf)
firt9digitsOfCpf = lenCpfNum - 2

i = 11
p = 0
sumMultiplications = 0 # initializing the variable to store the sum of all multiplications

for i in range(firt9digitsOfCpf):
    i -= 1
    cpfItem = int(arrayCpf[p]) # converting the item to an integer before multiplying
    multiplication = cpfItem * i
    p += 1
    sumMultiplications += multiplication # adding the result of each multiplication to the sum

print("Sum of multiplications:", sumMultiplications) 