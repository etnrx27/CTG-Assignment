#S10204829
#This Code Encrypts RC4's Secret Key with
#Elgamal's A-symmetric Cryptosystem &
#Paillier's A-symmetric Cryptosystem
import math
import random


def CalculateInverse(n,lcm,g):
    #Using Eucledean Method
    org_n = n
    l = (g**lcm % (n*n)) - 1 #Formula states that Lfunc = (x-1)//n               
    x = l//n                 #x in this case is equal to (g**lcm % (n*n))
    #gcd(x,n)
    first_digit = x
    if first_digit == 0:
        return False
    second_digit = n
    remainder = 0
    count = 0
    List_of_eqns = []
    addition1 = 0
    addition2 = 0
    #Loops until the remainder of the eqn is 1
    while remainder != 1:
        check = count * x
        while check <= n:
            count += 1
            check = count * x
        remainder = n - ((count -1) * x )
        #print(str(int(n))+" = "+str(count-1) + " * "+str(int(x)) + " + "+str(remainder))
        List_of_eqns +=[str(int(remainder))+"=-" + str(count-1) + "*" + str(int(x)) + "+" +str(int(n)),]
        #print(List_of_eqns)
        #E.g. 221 = 1*139 + 82; 82 = -1*139 + 221
        #n = 221
        #x = 139
        n = x #This makes n become 139
        x = remainder #This makes x become 82
        #It then becomes 139 = 1*82 + 57; 57 = -1*82 + 139
        count = 0
        #Validating to see if modular multiplicative inverse exists
        if n < x:
            return False
            break
        if x == 0:
            return False
            break
        # Loops i number of time for number of eqns in the list
        for i in range(len(List_of_eqns)):
            #Finding indexes of signs in the eqn
            substitutionlist = []
            equals_index = List_of_eqns[i].index("=")
            plus_index = List_of_eqns[i].index("+")
            multiply_index = List_of_eqns[i].index("*")
            #Finding value of values thru slice operator
            #Variable 1 is the number before tbe equal sign [82]
            variable1 = List_of_eqns[i][0:equals_index]
            #Variable 2 is the number between the equal sign and multiply sign [-1]
            variable2 = List_of_eqns[i][equals_index+1:multiply_index]
            #Variable 3 is the number between multiply sign and plus [139]
            variable3 = List_of_eqns[i][multiply_index+1:plus_index]
            #Remainder_val is the number after the plus [221]
            remainder_val = List_of_eqns[i][plus_index+1:]
            if i == 1:
                #To find first value to substitute the eqn in
                org_equal_index = List_of_eqns[i-1].index("=")
                org_plus_index = List_of_eqns[i-1].index("+")
                org_multiply_index = List_of_eqns[i-1].index("*")
                org_rem = List_of_eqns[0][0:org_equal_index]
                org_var2 = List_of_eqns[0][org_equal_index+1:org_multiply_index]
                org_var3 = List_of_eqns[0][org_multiply_index+1:org_plus_index]
                org_var1 = List_of_eqns[0][plus_index+1:]
                multiplier2 = 1
                #Substitution is the string to substitute into the eqn
                substitution = "("+org_var2+"*"+org_var3+"+"+str(multiplier2)+"*"+org_var1+")"
                #print(substitution)
                multiplier1 = int(variable2) * int(org_var2) +1 # (-1 * -1);-1(139);-1(82)
                multiplier2 = int(variable2) * multiplier2
                
                substitution2 = "("+str(multiplier1) +"*"+org_var3+"+"+str(multiplier2)+"*"+org_var1+")"
                substitutionlist += [substitution2,]
                #print(str(variable1)+"="+str(variable2)+substitution+"+"+str(remainder_val))
                #print(str(variable1)+"="+substitution2)
                #print()
            if i > 1:
                #For the rest of the values, must substitute the values with the new eqn
                org_s2 = substitution
                substitution = substitution2
                #print(variable1+"="+variable2+"*"+substitution2+"+"+str(remainder_val))
                
                #Finding index values of signs in new string
                s2_open = substitution2.index("(")
                s2_multiply1 = substitution2.index("*")
                multiplier1 = int(substitution2[s2_open+1:s2_multiply1]) * int(variable2)
                substitution2 = substitution2[s2_multiply1+1:]
                s2_plus = substitution2.index("+")
                s2_multiply2 = substitution2.index("*")
                multiplier2 = int(substitution2[s2_plus+1:s2_multiply2]) * int(variable2)
                substitution2 = "("+str(multiplier1)+"*"+org_var3+"+"+str(multiplier2)+"*"+org_var1+")"
                #print(variable1+"="+substitution2+"+"+org_s2)
                #Adding the substituted eqn together
                s2_open2 = substitution2.index("(")
                s2_multiply3 = substitution2.index("*")
                org_s2_open = org_s2.index("(")
                org_s2_multiply1 = org_s2.index("*")
                addition1 = int(substitution2[s2_open2+1:s2_multiply3]) + int(org_s2[org_s2_open+1:org_s2_multiply1])
                substitution2 = substitution2[s2_multiply3+1:]
                org_s2 = org_s2[org_s2_multiply1+1:]
                s2_plus2 = substitution2.index("+")
                org_s2_plus = org_s2.index("+")
                s2_multiply4 = substitution2.index("*")
                org_s2_multiply2 = org_s2.index("*")
                addition2 = int(substitution2[s2_plus2+1:s2_multiply4]) + int(org_s2[org_s2_plus+1:org_s2_multiply2])
                substitution2 = "("+str(addition1)+"*"+org_var3+"+"+str(addition2)+"*"+org_var1+")"
                #print(variable1+"="+substitution2)
    #print("gcd of "+str(int(first_digit))+" is "+str(addition1) + " mod " +str(org_n) + " = "+str(addition1 % org_n))
    #print("gcd of "+str(int(second_digit))+" is "+str(addition2) + " mod " + str(org_n) +" = "+str(addition2 % org_n))
    return (addition1 % org_n)
    #Returns the modular multiplicative inverse

def ElGamal_GenerateKey():
    q = random.randint(11,50)#Put low as it may crash the program if too big
    g = random.randint(2,q-1)#Original formula is g = random.randint(1,q-1); changed to prevent 1 from occuring
    a = random.randint(2,q-1)#Original formula is a = random.randint(1,q-1); changed to prevent 1 from occuring

    while math.gcd(g,q) != 1: # Check if g is co prime with q since integers can
        g = random.randint(2,q-1) #only be from cyclic group
        math.gcd(g,q)
    while math.gcd(a,q) != 1: #Formula states a & q must  have a gcd of 1
        a = random.randint(2,q-1)
        math.gcd(a,q)
    while a == g: #Cannot be equal
        a = random.randint(2,q-1)
    cyclicgroup = [] #Cyclic group consists of numbers from 1 to q-1; where the numbers are co-prime ; gcd == 1
    for i in range(2,q):
        if math.gcd(i,q) == 1:
            cyclicgroup+=[str(i),]
    h = g ** a
    publickey = [cyclicgroup,q,g,h]
    privatekey = [a]
    #print("Elgamal's Publickey is[cyclicgroup,q,g,h]: "+str(publickey))
    #print("Elgamal's Privatekey is[a]: "+str(privatekey))
    return [cyclicgroup,q,g,h,a]

def Paillier_GenerateKey(): 
    p = random.randint(100,500) #Can be bigger, but was limited as the program may
    q = random.randint(100,500) #take some time to calculate, or may crash
    
    #P & Q must be prime
    while CheckPrime(p) == False:
        p = random.randint(100,500)
        CheckPrime(p)
    while CheckPrime(q) == False:
        q = random.randint(100,500)
        CheckPrime(q)
    n = p * q
    
    # Checks if both primes are of equal length
    while math.gcd(n,(p-1)*(q-1)) != 1:
        p = random.randint(100,500)
        q = random.randint(100,500)
        n = p * q
        math.gcd(n,(p-1)*(q-1))
        
    #g must be co-prime of n**2   
    g = random.randint(1,n**2)
    while math.gcd(g,n**2) != 1:
        g = random.randint(1, n**2)
        math.gcd(g,n**2)
        
    lcm = int((p-1)*(q-1) / (math.gcd(p-1,q-1))) #based on formula of lcm
    inverse = CalculateInverse(n,lcm,g)
    while inverse == False:
        #If inverse is False; Must restart again
        p = random.randint(100,500)
        if CheckPrime(p) == True:
            continue
        q = random.randint(100,500)
        if CheckPrime(q) == True:
            continue
        n = p * q
        if math.gcd(n,(p-1)*(q-1)) == 1:
            lcm = int((p-1)*(q-1) / (math.gcd(p-1,q-1)))
            g = random.randint(1, n**2)
            if math.gcd(g,n**2) == 1:
                inverse = CalculateInverse(n,lcm,g)
    publickey = [n,g]
    privatekey = [lcm,inverse]
    #print("Paillier Public Key is[n,g]: "+str(publickey))
    #print("Paillier Private Key is[lcm,inverse]: "+str(privatekey))
    return [n,g,lcm,inverse]

def ElGamal_Encryption(q,g,h,m):
    k = int(input("Enter value of K: "))
    while math.gcd(k,q) != 1:
        print("The value chosen is not part of the cyclic group.Please choose another value: ")
        k = int(input("Enter k: "))
        math.gcd(k,q)
    p = g**k
    s = h**k
    value = int(m)*s
        
    encryptedmessage = [p, int(m)*s]
    #print("Elgamal Encrypted value is "+str(encryptedmessage))
    return encryptedmessage

def CheckPrime(val):
    for i in range(2,val):
        if val % i == 0:
            return False
            break
    return True
def StringToNum(msg,alphabelts):
    numconv = ""
    for i in range(len(msg)): #For each letter in messaage
        for x in range(len(alphabelts)):#Check with alphabelts list
            if msg[i] == alphabelts[x]:#To get the index value
                numconv += str(x+10) # To make single value into double digit
    return numconv
def NumToString(msg,alphabelts):
    numtoString = ""
    numtoString+=alphabelts[msg-10]#To get back original digit 
    return numtoString
def Paillier_Encryption(n,g,m):
    r = random.randint(1,n)
    while math.gcd(r,n)!=1:
        r = random.randint(1,n)
        math.gcd(r,n)
    encrypted_m = g**m * r**n %(n*n)
    #print("Paillier Encrypted value of m is "+str(encrypted_m))
    return encrypted_m

def Paillier_Decryption(encryptedval,lcm,n,inverse):
    decryptedval = ((encryptedval**lcm % (n*n))-1)//n * inverse % n
    return decryptedval

def ElGamal_Decryption(a,b,Elgamal_priv):
    orgmsg = str(int(b/(a**Elgamal_priv)))
    return orgmsg

def DisplayMenu():
    print("[1] Generate Key")
    print("[2] Encrypt")
    print("[3] Decrypt")
    print("[0] Exit")
#MAIN
print("Hello This Service Allows You To Generate Public And Private Keys for Paillier & ElGamal Needed for Encryption & Decryption.")
loop = True
while loop == True:
    DisplayMenu()
    userInput = int(input("Enter Option: "))
    if userInput == 1:
        EL_keys = ElGamal_GenerateKey()
        EL_cyclicgroup = EL_keys[0]
        EL_q = EL_keys[1]
        EL_g = EL_keys[2]
        EL_h = EL_keys[3]
        EL_a = EL_keys[-1]
        P_keys = Paillier_GenerateKey()
        P_n = P_keys[0]
        P_g = P_keys[1]
        P_lcm = P_keys[2]
        P_inverse = P_keys[3]
        EXP_Publickey = [EL_cyclicgroup,EL_q,EL_g,EL_h,P_n,P_g]
        EXP_Privatekey = [EL_a, P_lcm, P_inverse]
        print("EXP's Public key is "+str(EXP_Publickey))
        print("EXP's Private key is "+str(EXP_Privatekey))
    if userInput == 2:
        alphabelts = "abcdefghijklmnopqrstuvwxyz"
        message = input("Enter msg To Encrypt: ")
        EXP_Publickey = input("Enter Public Key for EXP(Exclude cyclic group): ")
        EXP_Publickey = EXP_Publickey.split(",")
        P_n = int(EXP_Publickey[-2])#Extracted from backwards in the event users include cyclic group
        P_g = int(EXP_Publickey[-1])#The code will still work
        encryptedlist = []
        while message.isdigit() == True:
            print("Sorry,this program only acceps text messages")
            message = input("Enter msg To Encrypt: ")
        nummessage = StringToNum(message,alphabelts)#Converts text into numbers
        for i in range(len(message)):
            msgtoencrypt = int(nummessage[0:2])#Take 2digits for each letter
            nummessage = nummessage[2:]#to remove the letter currently being used
            encryptedlist+= [Paillier_Encryption(P_n,P_g,msgtoencrypt),]#Encrypts the message with Paillier
        print("First set of Encryption is: "+ str(encryptedlist))
        E_q = int(EXP_Publickey[-5])#Extracted from backwards in the event users include cyclic group
        E_g = int(EXP_Publickey[-4])#The code will still work
        E_h = int(EXP_Publickey[-3])
        newencryptedlist = []
        for x in range(len(encryptedlist)):
            newencryptedlist += [ElGamal_Encryption(E_q,E_g,E_h,encryptedlist[x]),]
        for z in range(len(newencryptedlist)):
            print("Final Set of Encryption is: ["+str(z+1)+"] "+str(newencryptedlist[z])+"\n")
      
    if userInput == 3:
        alphabelts = "abcdefghijklmnopqrstuvwxyz"
        user_Choice = int(input("Enter number of values to decrypt: "))#Based on number of letters/ how many sets of encryption
        EXP_Privatekey = input("Enter Private key of EXP: ")#EXP's Private Key
        EXP_Publickey = input("Enter Public key of EXP(Exclude cyclic group): ")#EXP's Public Key
        EXP_Privatekey = EXP_Privatekey.split(",")
        EXP_Publickey = EXP_Publickey.split(",")
        EL_a = int(EXP_Privatekey[0])
        P_lcm = int(EXP_Privatekey[1])
        P_inverse = int(EXP_Privatekey[2])
        P_n = int(EXP_Publickey[-2])
        encryptedList = []
        for i in range(user_Choice):
            encryptedvalues = input("Enter Encrypted Values: ")#User enter encrypted values one at a time
            encryptedvalues = encryptedvalues.split(",")
            encryptedList += [encryptedvalues,]
        decryptedletters = ""
        decryptednum = ""
        PaillierEncrypted = []
        for i in range(len(encryptedList)):
            elGamalDecrypted = ElGamal_Decryption(int(encryptedList[i][0]),int(encryptedList[i][1]),EL_a)#Decrypts ElGamal Encryption First
            PaillierEncrypted += [elGamalDecrypted,]
        print("First Decryption Results: "+str(PaillierEncrypted))
        for x in range(len(PaillierEncrypted)):
            PaillierDecrypted = Paillier_Decryption(int(PaillierEncrypted[x]),P_lcm,P_n,P_inverse)
            decryptedletters += NumToString(PaillierDecrypted,alphabelts)
            if (PaillierDecrypted-10) <= 0:
                decryptednum += str(PaillierDecrypted)
            else:
                decryptednum += str(PaillierDecrypted-10)
        print("Final Decrypted Results: "+decryptedletters+"[text]")
        print("Final Decrypted Results: "+decryptednum+"[num]")

    if userInput == 0:
        print("Thank you for using this service. Good bye!")
        loop = False
    
    
