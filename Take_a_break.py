import webbrowser
import time

# I wrote this loop using for in
n=[]
for n in range(0,3):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=4bmUFRxNEIg")
    print(time.ctime())
    n += 1

# Mentor wrote using while loop
total_breaks = 3
break_count = 0

print ("This program started on " + time.ctime())
while break_count<total_breaks:
    time.sleep(5) #5 sec
    webbrowser.open("https://www.youtube.com/watch?v=4bmUFRxNEIg")
    print(time.ctime())
    break_count += 1