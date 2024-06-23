
<body>
    <h1>Python Code Summary</h1>
    <p>This script performs the following actions:</p>
    <ol>
        <li>Prints a message indicating the start of the process and a delay of 3 seconds.</li>
        <li>Imports the <code>time</code> module to handle the delay.</li>
        <li>Pauses the execution for 3 seconds using <code>time.sleep(3)</code>.</li>
        <li>Prompts the user to input their name and age.</li>
        <li>Prints a message indicating that the list is being updated and pauses for 5 seconds.</li>
        <li>Opens a file named <code>data_list.txt</code> in append mode and writes the user's name and age to it.</li>
        <li>Closes the file to save the changes.</li>
        <li>Reopens the file in read mode for faster access.</li>
        <li>Asks the user if they want to see the list of entries.</li>
        <li>If the user responds with 'yes', the contents of the file are printed. If the response is anything other than 'yes', it prints 'ok'.</li>
        <li>The script ends.</li>
    </ol>
    <h2>Code:</h2>
    <pre>
<code>
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
</code>
    </pre>
</body>
</html>
