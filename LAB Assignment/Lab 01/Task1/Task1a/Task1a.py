f =  open('input1a.txt', 'r')
f1= open("output1a.txt", 'w')
first_line = f.readline().strip()


T = int(first_line)

for i in range (T):
  current_number = int(f.readline().strip())
  if current_number%2 == 0:
    f1.write(f'{current_number} is even number\n')
  else:
    f1.write(f'{current_number} is odd number\n')
    
  
f.close()
f1.close()