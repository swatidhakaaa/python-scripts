#def calc_sum(a,b):
#    sum=a+b
#    print(sum)
#    return sum
#calc_sum(5,10)
#calc_sum(2,10)
#calc_sum(12,17)


#def calc_sum(a,b):
#    return a+b

#sum=calc_sum(1,2)
#print(sum)


#def print_hello():
#    print("Hello")

#print_hello()    
#print_hello()
#print_hello()
#print_hello()
#print_hello()  


#def print_hello():
#    print("hello")
#output=print_hello()
#print(output)


#def calc_avg(a,b,c):
#    sum=a+b+c
#    avg=sum/3
#    print(avg)
#    return avg
#calc_avg(1,2,3)


#def calc_avg(a,b,c):
#    sum=a+b+c
#    avg=sum/3
#    print(avg)
#    return avg
#calc_avg(98,97,95)



#print("ApnaCollege","SwatiDhaka")
#print("SwatiDhaka")
#print("ApnaCollege",end=" ")
#print("SwatiDhaka")



#def cal_prod(a=4,b=2):
#    print(a*b)
#    return a*b
#cal_prod()


#def cal_prod(a,b=2):
#    print(a*b)
#    return a*b
#cal_prod(4)


#cities=["Delhi","Gurgaon","Noida","Pue","Mumbai","Chennai"]
#heroes=["Thor","Ironman","Captain america","Shaktiman"]

#def print_len(list):
#    print(len(list))

#print_len(cities)
#print_len(heroes)


#heroes=["Thor","Ironman","Captain america","Shaktiman"]

#def print_len(list):
#    print(len(list))

#def print_list(list):
#    for item in list:
#        print(item,end=" ")

#print_list(heroes)


#n=5
#fact=1

#for i in range(1,n+1):
#    fact*=i
#print(fact)



#def cal_fact(n):
#    fact=1
#    for i in range(1,n+1):
#        fact*=i
#        print(fact)

#cal_fact(5)



#def converter(usd_val):
#    inr_val=usd_val*96
#    print(usd_val,"USD=",inr_val,"INR")

#converter(10)    



#def check_odd_even(number):
#    if number % 2 == 0:
#        return "EVEN"
#    else:
#        return "ODD"

#print(check_odd_even(4))
#print(check_odd_even(7))



#def show(n):
#    print(n)

#show(5)    


#def show(n):
#    if(n == 0):
#        return
#    print(n)
#    show(n-1)

#show(5)    



#def show(n):
#    if(n == 0):
#        return
#    print(n)
#    show(n-1)
#    print("END")

#show(5)    


#def fact(n):
#    if(n == 1 or n == 0):
#        return 1
#    return fact(n-1)*n
#print(fact(6))



#def calc_sum(n):
#    if(n==0):
#        return
#    print(n)
#    calc_sum(n-1)

#calc_sum(5)
#print(sum)    


#def calc_sum(n):
#    if(n==0):
#        return 0
#    return calc_sum(n-1)+n

#sum=calc_sum(10)
#print(sum)

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits=["mango","apple","litchi","banana"]

print_list(fruits)