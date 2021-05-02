def main():
    arr, li = [], []
    file = open("/usercode/files/books.txt", "r")
    lines = file.read().splitlines()
    for line in lines:
        f = line[0]
        l = len(line)
        print(f + str(l))

    file.close()
    return
