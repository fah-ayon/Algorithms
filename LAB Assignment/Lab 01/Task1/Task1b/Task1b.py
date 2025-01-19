a = open('input1b.txt', 'r')
b = open ('output1b.txt', 'w')

fst_line = a.readline().strip()
T =  int(fst_line)

for fst_line in a:
    operand1 , operand2, operator =  fst_line.split()[1], fst_line.split()[3],fst_line.split()[2]
    result = None

    if operator == '+':
        result = int(operand1) + int(operand2)
        b.write(f'The result of {operand1}{operator}{operand2} is {result}\n')
    elif operator == '-':
        result = int(operand1) - int(operand2)
        b.write(f'The result of {operand1}{operator}{operand2} is {result}\n')
    elif operator == '*':
        result = int(operand1) * int(operand2)
        b.write(f'The result of {operand1}{operator}{operand2} is {result}\n')
    elif operator == '/':
        result = int(operand1) / int(operand2)
        b.write(f'The result of {operand1}{operator}{operand2} is {result}\n')

a.close()
b.close()