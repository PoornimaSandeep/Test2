print("Given two integers dividend and divisor, divide two integers without using multiplication")
n1=90
n2=40

count=0
if n1>n2:
   dividend=n1
   divisor=n2
   for i in range(dividend):
       dividend=dividend-divisor
       if(dividend==0):
             count += 1
             break;
       elif (dividend<0):
             break;
       count += 1
print("quotient",count)






