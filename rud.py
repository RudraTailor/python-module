#####################################################
##  module by <<RUDRA>>                            ##
## to import this module simply type "import rud"  ##
## while using write 'rud.fx_name()'               ##
##                                                 ##
## help(rud) to get a summary of the module        ##
#####################################################

def mul():
    a = int(input("Enter number:"))
    b = int(input("Enter number:"))
    print("Multiplication:",end = " ")
    print(a*b)

def div():
    a = int(input("Enter number:"))
    b = int(input("Enter number:"))
    print("Division:",end = " ")
    print(a/b)

def add():
    a = int(input("Enter number:"))
    b = int(input("Enter number:"))
    print("Addition:",end = " ")
    print(a+b)

def sub():
    a = int(input("Enter number:"))
    b = int(input("Enter number:"))
    print("Subtraction:",end = " ")
    print(a-b)

def rem():
    a = int(input("Enter number:"))
    b = int(input("Enter number:"))
    print("Your remainder is",end = " ")
    print(a%b)

def exp():
    a = int(input("Enter number:"))
    b = int(input("Enter number:"))
    print(a,"raised to",b,"=",end=" ")
    print(a**b)

def repw(a,b):
    #a = input("Enter the word to be displayed:")
    #b = int(input("Enter the repitition:"))
    for i in range(b):
        print(a)

# menu-driven calculator f(x)

def calc():

    print("--------------------------")
    print("Mathematical operations")
    print("--------------------------")
    print("1. Perform Addition")
    print("2. Perfrom Subtraction")
    print("3. Perfrom Multiplication")
    print("4. Perfrom Division")
    print("5. Remainder")
    print("6. Power of one number raised to another")
    print("####################################################")
    n = int(input("Select operation to be done: "))
    
    if n == 1:
        add()
    elif n == 2:
        sub()
    elif n ==3:
        mul()
    elif n == 4:
        div()
    elif n == 5:
        rem()
    elif n == 6:
        exp()
    else:
        print("Invalid option try again!")
        calc()


#search for  a word in '.txt' file and get the count of the word
#note: write the path address in fname eg: c:\desktop\abc.txt
def swf(fname,word):

    f = open(fname,"r")
    t = f.read().split()

    cnt = 0 
    for i in t:
        if i == word:
            cnt = cnt + 1
            print(i)
            
    
    print("Total count of word",word,":",cnt)

           
        
    f.close()

#Read a '.txt' file and print the numnber of lines as input by the user.

def distf(fname,numl):
    f = open(fname,'r')
    for i in range(numl):
        t = f.readlines(numl)
        print(t,'\n')
    f.close()


#AREA OF DIFFERENT SHAPES


def ar_tri(base,height):

    area = (1/2)*base*height

    print("Area of triangle with base",base,"cm and height",height,"cm = ", area)

def ar_rec(l,b):

    area = l * b

    print("Area os rectangle with length",l," cm and breath/width",b,"cm = ", area)

def ar_sq(a):

    area = a*a

    print("Area of square with side",a,"cm = ", area)


def ul(string):
    if string.isupper():
       
        print(string.lower())

def lu(string):
    if string.islower():

        print(string.upper())

#check upper and lower case charc in a string

def check_ul(string):

    count_upper = 0
    count_lower = 0

    for i in string:
        if i.isupper():
            count_upper = count_upper + 1
        elif i.islower():
            count_lower = count_lower + 1
        else:
            continue
    
    print("Total number of UPPERCASE charc = ",count_upper)
    print("Total number of LOWERCASE charc = ",count_lower)

#Check for palindrome string

def palindrome(string):

    if string == string[::-1]:
        print("String entered IS palindrome")
    else:
        print("String entered is NOT palindrome")



#add bold,italic,underline text using ANSI ESCAPE code

def bold_txt(string):
    return("\033[1m" + string + "\033[0m")

def italic_txt(string):
    return("\x1B[3m" + string + "\x1B[0m")

def uline_txt(string):
    return("\033[4m" + string + "\033[0m")

#decorator
 
def dec_hash(n):
    print("# " * n , end = " ")
    print("\n")
    
def dec_dln(n):
    print("- " * n, end = " ")
    print("\n")

def dec_uln(n):
    print("_" * n, end = "")
    print("\n")


#convert list to tuple and viz.

def clt(list):
    t = tuple(list)
    print("Conversion result: ",t)

def ctl(tuple):
    l = list(tuple)
    print("Conversionn result: ", l)

#INT <-> $currency converter

def c_inr(inr,curr):
    if curr == "usd" or curr == "USD":
        amt =  inr / 83.24 
        print("Converted value of USD $",amt)
    elif curr == "cad" or curr == "CAD":
        amt =  inr / 60.62 
        print("Converted value of CAD $",amt)
    elif curr == "BTC" or curr == "btc":
        amt = inr * 4.0e-7
        print("Converted value of $BTC",amt)
    else:
        print("Conversion unavailable;" + "\x1b[3m" + "TRY AGAIN!" + "\x1b[0m")


























    






