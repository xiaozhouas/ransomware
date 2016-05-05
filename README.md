# ransomware
simple ransomware with fake GUI for security lab project
group member: xiaokang xiang

Python: 3.5.1 is used for this project. Library tkinter is used for GUI interface.

This ransomware have a fake GUI interface while exectued, while in the meantime another thread start to traversal the user disk and encrypt files match the extensions that defined such as doc, txt, pdf. For testing purpose, the program is only set to traversal the directory start from current directory. Comment line 41 and uncomment line 40 in ransomware.py to traversal and encrypt the whole disk. After the traverl is done, all original files are deleted and new files are end with .enc extension and a text file with message called Help.txt is created for victim. Also, there is decryption function in the script for testing purpose as well as I am using the AES as the sysmetric encrption algorithm.  
The ransomware.zip contains the transformed exectuable program could be running in linux system, which is the real 
program that victim would actually interact with. 
