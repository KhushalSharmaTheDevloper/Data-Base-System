print('starting in 3 seconds and loading data ...')
import time as t  ##import module
t.sleep(3)  #sleep(STOP)

name = input('Enter Name' + '\n') ##take input
age  = input("Enter Age" + '\n')  ##take age input
print('Updating List Please Wait...')
t.sleep(5)
f = open("data_list.txt" , 'a')##File Name
f.write("name is " + name +' '+ "and age is " + age + '\n') ##Update List
f.close()                      ## CLOSE LIST
f = open("data_list.txt", "r") #open list for faster load time
inp = input('Do You Want To See List??') ##OPTION
if inp == 'yes':  #StateMent True Or False
    print(f.read()) ##if true
else:
    print('ok')## if false.
quit

## ----------------------------------------------END---------------------------------------------##


