# ths is to open the file which contains random 1's and 0's (you can get random data from here https://qrng.anu.edu.au)
f = open("idk.txt")


# starts a while which continues until it has processed all the data
while True:
    content = f.read(4)   #it reads 4 bits per scan because to implement 12 moves of a rubik's cube you nit 4 bits of binary
    file = open("resultidk.txt", 'a')   # opens another file in which we will store our result
    if (content == '1111'):     # checks if the taken 4 bits are a particular sequence to assign it a particular move
        reusult = "F' "    # stores the move in a var
        print(result)   # prints it 
        file.write(result)  # and then stores the result in the output file 
    if (content == '0000'):
        result = 'F '
        print(result)
        file.write(result)
    if (content == '1000'):
        result = "L' "
        print(result)
        file.write(result)
    if (content == '0100'):
        result = 'L '
        print(result)
        file.write(result)
    if (content == '0010'):
        result = 'R '
        print(result)
        file.write(result)
    if (content == '0001'):
        result = 'B '
        print(result)
        file.write(result)
    if (content == '1100'):
        result = 'D '
        print(result)
        file.write(result)
    if (content == '1010'):
        result = "R' "
        print(result)
        file.write(result)
    if (content == '1001'):
        result = 'U '
        print(result)
        file.write(result)
    if (content == '0110'):
        result = "U' "
        print(result)
        file.write(result)
    if (content == '0101'):
        result = "D' "
        print(result)
        file.write(result)
    if (content == '0011'):
        result = "B' "
        print(result)
        file.write(result)
    if (content == '1110'):
        result = "F' "
        print(result)
        file.write(result)
    if (content == '0111'):
        result = 'U '
        print(result)
        file.write(result) 
    file.close()  # in the end its a good habit to close a file 
    

f.close()

