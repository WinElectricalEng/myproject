print("Please enter a sequence of natural numbers terminated by -1")
number = input(" ")
# convert string into integer
number = int(number)
count = 0
sum = 0
#assign the first ever entering number is minimum
min = number
# as long as user do not enter -1 while loop is still running
#if the user enter -1, it will come out from while loop
#print min -1 and average -1
while(number != -1): 
    count = count + 1
    #comparing if the number user enter is smaller than current mini number
    # if user input number is smaller than current number 
    #then replace input number into min and store it to print later
    if (number <= min): 
        min = number
    #continue adding those number into sum 
    sum = sum + number
    #repeat the loop till user enter the terminated -1
    number = input("enter next number and hit ENTER ")
    number = int(number)
if (count == 0):
    print ("min = -1 and average = -1")    
else:
    print ("count = " + str(count) + "\n min = " + str(min) + "\n sum = " + str(sum) + "\n Avg = " + str(sum/count))