n=int(input())
temp=n
sum=0
while n>0:
  digit=n%10
  sum=sum+digit*digit*digit
  n=n//10
if temp==sum:
    print("armstrong")
else:
    print("not a armstrong")

#input:153
#output:armstrong
