def getInteger(prompt):
    result = int(raw_input(prompt))
    return result

def Main():
    print "Started"
    output = getInteger("Please enter a number: ")
    print output

if __name__ == "__main__":
    Main()
