#check given number is armstrong or not
n=int(input('Enter a number'))
dummy=n
s=0
while dummy>0:
    reminder=dummy%10
    s+=reminder**len(str(n))
    dummy//=10
if n==s:
    print('armstrong number')
else:
    print('not an armstrong number')    


#check given number is armstrong or not without using length function
n=int(input('Enter a number'))
dummy1=n
dummy2=n
s=0
c=0
while dummy1>0:
    dummy1=dummy1//10
    c+=1
while dummy2>0:
    reminder=dummy2%10
    s+=reminder**c
    dummy2//=10
if n==s:
    print('armstrong number')
else:
    print('not an armstrong number')   


#--------------------- using function----------------------------
#check given number is armstrong or not using function
def checkArmstrong(n):
    dummy=n
    s=0
    while dummy>0:
        reminder=dummy%10
        s+=reminder**len(str(n))
        dummy//=10
    if n==s:
        print('armstrong number')
    else:
        print('not an armstrong number')
checkArmstrong(n=int(input('Enter a number')))


#using fuction check given number is armstrong or not without using length function
def checkArmstrong(n):
    dummy1=n
    dummy2=n
    s=0
    c=0
    while dummy1>0:
        dummy1=dummy1//10
        c+=1
    while dummy2>0:
        reminder=dummy2%10
        s+=reminder**c
        dummy2//=10
    if n==s:
        print('armstrong number')
    else:
        print('not an armstrong number') 
checkArmstrong(n=int(input('Enter a number')))