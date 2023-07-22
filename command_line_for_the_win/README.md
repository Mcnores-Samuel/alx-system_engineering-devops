# Project: command_line_for_the_win

This project demostrates the use of sftp (secure file transfer protocol)
Below I demostrate how I used sftp to transfer the images from my local
machine to the sandbox environment.

# USAGE:
Open the terminal on local machine and type the following.
```
sftp my_user_name_on_sandbox@hostname.
```
sftp will request password, (enter the password)

After the connection is successful, change directory to the directory
where to insert the file, in my case (/root/alx-system_engineering-devops/command_line_for_the_win/)

### sending file:
```
sftp> put filename
Uploading filename to /path/directory/filename
```
