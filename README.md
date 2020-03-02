# es

**Simple program which takes a file directory of a text file, opens the file, reads the file & outputs the number of e's within the text**

*Week 7 Task*

Program Overview:
- Program takes the name or the file directory of the text file to be read as a command line argument.
```
import sys                                  
file_name = sys.argv[1]
```
- Note that sys.argv[0] the script name.
- Program opens file in read mode & reads file.
- **.read()** reads entire file. 
```
with open(file_name, "r") as reader:       
    read_file = reader.read()
```
- Initiate 'e' counter with e_count = 0.
- **for** loop through every character 'i' in the read file.
- Using a **if** statement & the boolean expression i == "e" adding +1 to e_count when satisified.
```
    e_count = 0                             
    
    for i in read_file:                    
        if i == "e":                       
            e_count = e_count + 1
```
- Program outputs value of e_count.
```
    print(e_count)
```
- Program automatically closes text file after contents of **with** statement is complete & program is finished.

Example of input & output of Program:
```
python es.py moby-dick.txt
116960
```

References:

[Project Gutenbery- Moby Dick Text File](https://www.gutenberg.org/files/2701/old/moby10b.txt)

[Real Python - Reading & Writing Files](https://realpython.com/read-write-files-python/)

[Stack Overflow - Command Line Arguments](https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python/7439162)
