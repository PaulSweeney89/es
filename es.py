# program that reads in a text file from a inputted file directory & counts the number of e's it contains.
# sample file directory: /home/paul/Desktop/es/moby-dick.txt

#input text file directory to be read
txt_file = input("please input text file directory ")


# use 'with' statement to open text file & automatically close file after statement is executed.
with open(txt_file, "r") as reader:        # open file in read mode 'r'. 
    read_file = reader.read()              # read file
    
    e_count = 0                            # initiate e counter with e_count = 0.
    
    for i in read_file:                    # 'for' loop through every character 'i' in read file.
        if i == "e":                       # 'if' statement 'i' = 'e' is True
            e_count = e_count + 1          # add 1 to e counter.

    # print final e_count value when for loop has gone through all characters in read text file.
    print(e_count)
