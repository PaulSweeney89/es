# program that reads in a text file & counts the number of e's it contains.

for n in range(0, 256):
    print(f"{n:3} {n:08b} {chr(n)}")

with open("moby-dick.txt", "r") as reader:
    for i in reader:
        value_count = 0
        if f"{chr(i)}" == "e":
            value_count = value_count + 1 

        print(value_count)