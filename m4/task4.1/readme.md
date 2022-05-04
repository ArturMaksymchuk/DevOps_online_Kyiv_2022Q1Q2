# TASK 4.1

## Part 1

1) Log in to the system as root (or sudo-er).
2) Use the passwd command to change the password. Examine the basic parameters of the command. What system file does it change *?

passwd change /etc/shadow file
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/1-1-2.png)
 
3) Determine the users registered in the system, as well as what commands they execute. What additional information can be gleaned from the command execution?

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/1-3.png)

For example

#### artur: x :1000:1000:Artur,15,555-22-33,555-33-55:/home/artur:/bin/bash  =
#### username: pswd : uid : gid: uid comments: directory: shell
  
#### 1- username
#### 2- password (x-password exist) 
#### 3- uid - unique identifier of the user within the system
#### 4- gid unique identifier of the group within the system to which the user belongs
#### 5- uid comments (Name,office number and phone,home phone)
#### 6- user's home directory
#### 7- program name the user's command interpreter


4) Change personal information about yourself.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/1-4.png)

5) Become familiar with the Linux help system and the man and info commands. Get help on the previously discussed commands, define and describe any two keys for these commands. Give examples.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/1-5.png)

6) Explore the more and less commands using the help system. View the contents of files .bash* using commands.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/1-6.1.png)

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/1-6.2.png)

7) Determine the last logon time for all users. Tip: You should read the documentation for the finger command.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/1-7.png)

8) List the contents of the home directory using the ls command, define its files and directories. Hint: Use the help system to familiarize yourself with the ls command.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/1-8.png)



## Part 2


1) Examine the tree command. Master the technique of applying a template, for example, display all files that contain a character c, or files that contain a specific sequence of characters. List subdirectories of the root directory up to and including the second nesting level.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-1.1.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-1.2.png)


2) What command can be used to determine the type of file (for example, text or binary)? Give an example.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-2.png)


3) Master the skills of navigating the file system using relative and absolute paths. How can you go back to your home directory from anywhere in the filesystem?

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-3.png)

4) Become familiar with the various options for the ls command. Give examples of listing directories using different keys. Explain the information displayed on the terminal using the -l and -a switches.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-4.1.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-4.2.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-4.3.png)

#### drwx------ 14 artur a_group 4096 Apr 27 13:53 .config
#### drwxr-xr-x  2 artur a_group 4096 Apr 12 21:18 Desktop
#### drwxr-xr-x : d - file type(in this case d-directory); rwx- owner permissions; r-x- group permissions; r-x- others permissions  
#### 2 - number of links
#### artur - name owner
#### a_group - group owner
#### 4096 - file size in bytes
#### Apr 12 21:18 - date of last modification
#### Desktop - file name


5) Perform the following sequence of operations:
- create a subdirectory in the home directory;
- in this subdirectory create a file containing information about directories located in the root directory (using I/O redirection operations);
- view the created file;
- copy the created file to your home directory using relative and absolute addressing.
- delete the previously created subdirectory with the file requesting removal;
- delete the file copied to the home directory.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-5.1.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-5.2.png)

6) Perform the following sequence of operations:
- create a subdirectory test in the home directory;
- copy the .bash_history file to this directory while changing its name to labwork2;
- create a hard and soft link to the labwork2 file in the test subdirectory;
- how to define soft and hard link, what do these concepts;
- change the data by opening a symbolic link. What changes will happen and why
- rename the hard link file to hard_lnk_labwork2;
- rename the soft link file to symb_lnk_labwork2 file;
- then delete the labwork2. What changes have occurred and why?

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-6.1.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-6.2.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-6.3.png)


7) Using the locate utility, find all files that contain the squid and traceroute sequence.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-7.png)

8) Determine which partitions are mounted in the system, as well as the types of these partitions.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-8.png)

9) Count the number of lines containing a given sequence of characters in a given file.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-9.png)

10) Using the find command, find all files in the /etc directory containing the host character sequence.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-10.png)

11) List all objects in /etc that contain the ss character sequence. How can I duplicate a similar command using a bunch of grep?


12) Organize a screen-by-screen print of the contents of the /etc directory. Hint: You must use stream redirection operations.


13) What are the types of devices and how to determine the type of device? Give examples.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-13.png)

14) How to determine the type of file in the system, what types of files are there?

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task1/2-14.png)

15) * List the first 5 directory files that were recently accessed in the /etc directory.



