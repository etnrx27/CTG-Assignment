# Elgamal X Pallier Cryptosystem
This is a combination of two asymetric cryptosystems, elgamal and pallier. 
It first encrypts a text of letters using Pallie Encryption and then encrypted again through El Gamal cryptosystem.

# Keys
Public key (G,q,g,h,n,pg): where G,q,g,h is the public key in ElGamal, and n,g is the public key in Paillier.
Private key (x,lcm,mmi): where x is the private key in ElGamal, lcm and mmi are the private keys in Paillier.
 
# Encryption
1) Enter Plain Text (In alphabelts; hello etc)
2) Copy and Paste the public key; cyclic group can be excluded for convenience; exclude the 1st and last brackets
3) The first set of encrypted values will then be generated [Paillier Encrypted]
4) Enter the Value of K (Any Number in the cyclic group) until the program stops asking for input[based on number of letters in Plain Text]
5) Take notes of the encrypted values. [El Gamal Encrypted]

# Decryption 
1) Enter number of encrypted sets [5 if hello is used]
2) Enter Private key of EXP [Copy and Paste from Key Generation; exclude the 1st and last brackets]
3) Enter Public key of EXP;cyclic group can be excluded for convenience; exclude the 1st and last brackets
4) Enter Encrypted Values One by one
5) Decrypted Values will then be outputted into a string 

# Materials
1) EXP Algorithm.py - code for the generation of keys, encryption and decryption process
2) EXP_Algorithm_Slides.pptx - Slides explaining the flow of the algorithm 



