# TASK 4.1

## Part 1


1. How many states could has a process in Linux?

#### There are five Linux process states: 
#### - created
#### - ready
#### - running
#### - waiting
#### - terminated

2. Examine the pstree command. Make output (highlight) the chain (ancestors) of the current process.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/2.png)

3. What is a proc file system?



4. Print information about the processor (its type, supported technologies, etc.).

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/4.png)

5. Use the ps command to get information about the process. The information should be as follows: the owner of the process, the arguments with which the process was launched for execution, the group owner of this process, etc.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/5.png)

6. How to define kernel processes and user processes?

#### Kernel processes with square brackets. Normal processes is without square brackets.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/6.png)


7. Print the list of processes to the terminal. Briefly describe the statuses of the processes. What condition are they in, or can they be arriving in?

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/7.1.png)

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/7.2.png)

8. Display only the processes of a specific user.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/8.png)

9. What utilities can be used to analyze existing running tasks (by analyzing the help for the ps command)?

#### top

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/9.1.png)

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/9.2.png)


10. What information does top command display?

#### The top command can display system summary information. There are  PID, users , CPU and memory usage ,priority and other information.

11. Display the processes of the specific user using the top command.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/11.png)

12. What interactive commands can be used to control the top command? Give a couple of examples.

#### Sort by %MEM - M 
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/12.1.png)

#### Sort by %CPU - P 
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/12.2.png)

#### Change display units - E - in top values; e - in process list
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/12.3.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/12.4.png)

#### - Change Text Color - Z
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/12.5.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/12.6.png)

#### - Limit Process Number - n [value]. For example - n 5
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/12.7.png)


13. Sort the contents of the processes window using various parameters (for example, the amount of processor time taken up, etc.)
#### Sort by %MEM - M, sort by %CPU - P(see p.12)
#### Sort by TIME+ - T 
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/13.1.png)

#### Sort by PID - N 
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/13.2.png)

14. Concept of priority, what commands are used to set priority?

#### Priority means what task runing early.
#### To change prioryty use comand renaice and nice to start program with special priority.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/14.1.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/14.2.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/14.3.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/14.4.png)

15. Can I change the priority of a process using the top command? If so, how?

#### Change priority: r > [proces value] > [value to change]

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/15.1.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/15.2.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/15.3.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/15.4.png)


16. Examine the kill command. How to send with the kill command process control signal? Give an example of commonly used signals.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/16.1.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/16.2.png)

17. Commands jobs, fg, bg, nohup. What are they for? Use the sleep, yes command to demonstrate the process control mechanism with fg, bg.


![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/17.2.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task3/17.1.png)



## Part 2

1. Check the implementability of the most frequently used OPENSSH commands in the MS
Windows operating system. (Description of the expected result of the commands +screenshots:
command – result should be presented)


2. Implement basic SSH settings to increase the security of the client-server connection (at least)



3. List the options for choosing keys for encryption in SSH. Implement 3 of them.



4. Implement port forwarding for the SSH client from the host machine to the guest Linux virtual machine behind NAT.



5*. Intercept (capture) traffic (tcpdump, wireshark) while authorizing the remote client on the server using ssh, telnet, rlogin. Analyze the result.








