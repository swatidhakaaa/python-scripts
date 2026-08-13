#f=open("demo.txt","r")

#data=f.read()
#print(data)

#line1=f.readline()
#print(line1)

#line2=f.readline()
#print(line2)

#f.close()

#f=open("demo.txt","w")

#f.write("I want to learn JavaScript tomorrow.123")
#f.close()

#f=open("demo.txt","a")

#f.write("Then I'll move to ReactJS")
#f.close()

#f=open("demo.txt","a")

#f.write("\n After that node")
#f.close()

#f=open("sample.txt","w")
#f.close()

#f=open("demo.txt","r+")
#f.write("abc")
#f.close()


#f=open("demo.txt","r+")
#f.write("abc")
#print(f.read())
#f.close()


#f=open("demo.txt","w+")
#print(f.read())
#f.close()

#f=open("demo.txt","w+")
#print(f.read())
#f.write("abc")
#f.close()

#f=open("demo.txt","a+")
#print(f.read())
#f.write("abc")
#f.close()

#with open("demo.txt","r") as f:
#    data=f.read()
#    print(data)

#with open("demo.txt","w") as f:
#    f.write("new data")

#import os

#os.remove("sample.txt")

#with open("practice.txt","w") as f:
#    f.write("Hi everyone\nwe are learning file I/O\n")
#    f.write("using Java.\nI like programming in Java.")

#with open("practice.txt","r") as f:
#    data=f.read()

#    new_data=data.replace("Java","Python")
#    print(new_data)

#with open("practice.txt","w") as f:
#    f.write(new_data)    

#def check_for_word():
#    word="learning"
#    with open("practice.txt","r") as f:
#        data=f.read()
#        if(data.find(word) != -1):
#            print("Found")
#        else:
#           print("Not Found")

#check_for_word()

#def check_for_line():
#    word="learning"
#    data=True
#    line_no=1
#    with open("practice.txt","r") as f:
#        while data:
#            data=f.readline()
#            if(word in data):
#                print(line_no)
#                return
#            line_no +=1
#        
#    return -1
#check_for_line()


#with open("practice.txt","r") as f:
#    data=f.read()
#    print(data)

#    num=""
#    for i in range(len(data)):
#        if(data[i] == ","):
#            print(int(num))
#            num=""
#        else:
#            num += data[i]

#with open("practice.txt","r") as f:
#    data=f.read()
#    print(data)

#    nums=data.split(",")
#    print(nums)

count=0
with open("practice.txt","r") as f:
    data=f.read()

    nums=data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count +=1

print(count)       