# program that reads in a text file from a inputted file directory & counts the number of e's it contains.
# sample file directory: /home/paul/Desktop/es/moby-dick.txt

import sys                                     # import sys module
file_name = sys.argv[1]                        # input text file name assigned as a command line argument

try:                                           # try function to incorporate error message when input file is not found.
    with open(file_name, "r") as reader:       # use 'with' statement to open text file & automatically close file after statement is executed.
        read_file = reader.read()              # open file in read mode 'r'. 
            
        print(read_file.count('e'))            # updated to use count function, feedback from Andrew 11.03.2020. 
                                                
except FileNotFoundError:                      # file not found error, when input command line file is not found.
    print("File " + sys.argv[1] + " Not Found!")
    
