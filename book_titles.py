def main():
    file = open("books.txt") #books.txt can be any txt file
    #file = open("books.txt", "r") same thing
    lines = file.read().splitlines() #this line removes all the '/n' at the end of each line so not to be counted in the l
    for line in lines:
        f = line[0] #the first letter of the the title
        l = len(line) #the number of letters in the title
        print(f + str(l)) #the coded name

    file.close()
    return
