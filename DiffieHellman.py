counter=0
n=int(input("Please enter the common prime number "))
for i in range(2,((n//2)+1)):
               if((n%i)==0):
                   counter=counter+1
if counter==0:               
    g=int(input("Enter the generator "))
    x=int(input("Enter A's secret key "))
    y=int(input("Enter B's secret key "))
    print("Implementing Diffie Hellman Key Exchange Algorithm")
    M=(g**x)% n
    print("A's public key is ",M)
    S=(g**y)% n
    print("B's public key is ",S)
    key1=(S**x)%n
    key2=(M**y)%n
    symmetrickey=key1=key2
    print("The Symmetric Key is",key1)
else:
    print("You have entered an invalid prime number")