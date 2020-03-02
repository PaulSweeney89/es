# program that reads in a text file from a inputted file directory & counts the number of e's it contains.
# sample file directory: /home/paul/Desktop/es/moby-dick.txt

import sys                                  # import sys module

# use 'with' statement to open text file & automatically close file after statement is executed.
file_name = sys.argv[1]                     # input text file name assigned as a command line argument
with open(file_name, "r") as reader:        # open file in read mode 'r'. 
    read_file = reader.read()              # read file
    
    e_count = 0                            # initiate e counter with e_count = 0.
    
    for i in read_file:                    # 'for' loop through every character 'i' in read file.
        if i == "e":                       # 'if' statement 'i' = 'e' is True (lowecase)
            e_count = e_count + 1          # add 1 to e counter.

    # print final e_count value when for loop has gone through all characters in read text file.
    print(e_count)
