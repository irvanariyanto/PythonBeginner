def Main():
    f = open("myfile.txt", "w")

    for i in range(4):
        f.write(raw_input("Please enter a word: ") + '\n')

    f.close()

if __name__ == "__main__":
    Main()
