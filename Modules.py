import math

def Main():
    try:
        radius = float(raw_input("Please enter a radius: "))
        area = math.pi * radius**2
        print area
    
    except:
        print "You did not enter a number"

if __name__ == "__main__":
    Main()
