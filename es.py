# program that reads in a text file & counts the number of e's it contains.

with open("moby-dick.txt", "r") as reader:
    read_file = reader.read()
    e_count = 0
    for i in read_file:
        if i == "e":
            e_count = e_count + 1
    print(e_count)
        