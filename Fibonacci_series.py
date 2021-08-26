list=[]
def fibonacci(num):
    for i in range(num):
        if i==0 or i==1:
           list.append(i)
        else:
            i=0
            for j in range(i-2,i):

                i+=list[j]

            list.append(i)
    return list
n=int(input("Enter number of terms:"))
print(fibonacci(n))









