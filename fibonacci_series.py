a=int(input())
first_num=0
second_num=1
print(first_num,end="")
print(second_num,end="")
for i in range(a):
    next_num=first_num+second_num
    print(next_num,end="")
    first_num=second_num
    second_num=next_num

#input:5
#output:0112358
