# TASK 4.2



1) Analyze the structure of the /etc/passwd and /etc/group file, what fields are present in it, what users exist on the system? Specify several pseudo-users, how to define them?

#### passwd structure - username: pswd : uid : gid: uid comments: directory: shell
#### group structure - group_name:password:group_id:list
#### /etc/passwd present users and info about it.
#### /etc/group  precent groups , info about it and users in groups.


![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/1.png)

2) What are the uid ranges? What is UID? How to define it?

#### UID is a number assigned by Linux to each user on the system. 
#### UID ranges:
#### 0 (zero) is reserved for the root;
#### 1–99 are reserved for other predefined accounts;
#### 100–999 are reserved by system for administrative and system accounts/groups;
#### 1000–10000 are occupied by applications account;
#### 10000+ are used for user accounts.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/2.png)

3) What is GID? How to define it?

#### GID is a unique identifier of the group within the system to which the user belongs.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/3.png)

4) How to determine belonging of user to the specific group?

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/4.png)

5) What are the commands for adding a user to the system? What are the basic parameters required to create a user?

#### Name of new user is basic parametr.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/5.png)

6) How do I change the name (account name) of an existing user?

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/6.png)

7) What is skell_dir? What is its structure?

#### The /etc/skel directory contains files and directories that are automatically copied over to a new user’s home directory when such a user is created.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/7.png)

8) How to remove a user from the system (including his mailbox)?

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/8.png)

9) What commands and keys should be used to lock and unlock a user account?

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/9.png)

10) How to remove a user's password and provide him with a password-free login for subsequent password change?

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/10.png)

11) Display the extended format of information about the directory, tell about the information columns displayed on the terminal.

#### drwx------ 14 artur a_group 4096 Apr 27 13:53 .config
#### drwxr-xr-x  2 artur a_group 4096 Apr 12 21:18 Desktop
#### drwxr-xr-x : d - file type(in this case d-directory); rwx- owner permissions; r-x- group permissions; r-x- others permissions  
#### 2 - number of links
#### artur - name owner
#### a_group - group owner
#### 4096 - file size in bytes
#### Apr 12 21:18 - date of last modification
#### Desktop - file name

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/11.png)

12) What access rights exist and for whom (i. e., describe the main roles)? Briefly describe the acronym for access rights.

#### rwxr-xr-- : rwx - owner permissions; r-x - group permissions; r-- - others permissions
####  - - no access; r- access to read file(open directory);
#### w- write or change file; x- execute acces  
#### s - SUID bit ; t or T - sticky bit

13) What is the sequence of defining the relationship between the file and the user?

#### 1- check owner permissions, if user not owner
#### 2- check group permissions, if user not consist in this group
#### 3- check others permissions.
#### 4- check spesial permissions.

14) What commands are used to change the owner of a file (directory), as well as the mode of access to the file? Give examples, demonstrate on the terminal.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/14.png)

15) What is an example of octal representation of access rights? Describe the umask command.



| Octal Value   | File Permissions Set | Permissions Description |
| :------------: |:---------------:| :-----:|
| 0   | 	--- | No permissions  |
| 1   | --x        |   Execute permission only  |
| 2   | -w-        |    Write permission only |
| 3   | -wx | Write and execute permissions |
| 4   | r--        |  Read permission only   |
| 5   | r-x       |    Read and execute permissions  |
| 6   | rw- | Read and write permissions  |
| 7   | rwx       |   Read, write, and execute permissions  |

#### Umask, or the user file-creation mode, is a Linux command that is used to assign the default file permission sets for newly created folders and files.
#### The only umask parameter is an octal number that specifies the attributes that should not be set on a new file (666) or directory (777).

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/15.png)

16) Give definitions of sticky bits and mechanism of identifier substitution. Give an example of files and directories with these attributes.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/16.png)

17) What file attributes should be present in the command script?

File must have x(execute) permision.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m4/task2/17.png)

