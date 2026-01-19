# PART 1 

#1.1 Printing output using for command 

for i in range(1,5): #i stores one of the numbers 1-5 at a time
    for j in range(i): #this loop runs inside the first loop; how many times output comes on same line
        print(i, end=" ") #print current number and don't go to new line instead add a space
    print()

#1.2 flowchart 
print("start")
i=0
print('i=0')

for i in range(5):
    if i < 5:
        print("*")
    else:
        print('end')

#1.3 Fibonacci sequence

fib_numbers = [0,1] #list created with first 2 numbers 

#generating next numbers 
for i in range(8):
    next_value = fib_numbers[-1] + fib_numbers[-2] #add last 2 numbers in list we created which are 1 and 0
    fib_numbers.append(next_value) #add new number to list 
print(fib_numbers)

#1.4 