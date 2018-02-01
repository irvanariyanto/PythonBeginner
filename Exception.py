def Main():
    try:
        f = open("blah1.txt","r")
        for line in f:
            print line.strip("\n")

        f.close()
    except:
        print "The file was either not found or unable to be read."
    
    finally:
        print "Exiting."

if __name__ == "__main__":
    Main()
