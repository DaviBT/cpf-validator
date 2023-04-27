cpf = input("Enter your CPF (put a space between each number): ")

arrayCpf = cpf.split(" ")
print(arrayCpf)

lenCpfNum = len(arrayCpf)
firt9digitsOfCpf = lenCpfNum - 2

i = 10

for i in range(firt9digitsOfCpf):
    i -= 1
    cpfItem = arrayCpf[i]
    