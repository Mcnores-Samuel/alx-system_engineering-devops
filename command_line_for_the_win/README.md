# Project: command_line_for_the_win

This project demonstrates the use of sftp (secure file transfer protocol).
Below I demonstrate how I used sftp to transfer the images from my local
machine to the sandbox environment.

# USAGE:
Open the terminal on the local machine and type the following.
```
sftp my_user_name_on_sandbox@hostname.
```
sftp will request the password, (enter the password)

After the connection is successful, change the directory to the directory
where to insert the file, in my case (/root/alx-system_engineering-devops/command_line_for_the_win/)

### sending file:
```
sftp> put filename
Uploading filename to /path/directory/filename
```
