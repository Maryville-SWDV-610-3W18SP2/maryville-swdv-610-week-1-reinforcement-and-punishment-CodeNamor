#F. Derek Roman -- SWDV-610-3W-Data-Structures--Week-1
#I attest that this is my own work

def is_multiple(n, m):
    if n % m == 0:
        print(n, "is a multple of", m)
        return True
    else:
        print(n, "is not a multiple of", m)
        return False
    
def main():
    num = int(input("Please enter a number:  "))
    mult = int(input("Please enter a number to check if it is a multiple of:  "))
    is_multiple(num, mult)
    
main()