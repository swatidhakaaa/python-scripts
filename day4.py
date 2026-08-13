#info={"Key":"Value","Name":"ApnaCollege","Learning":"Coding","Age":35,"is_adult":True,"Marks":94.4}
#print(info)

#info={"Name":"ApnaCollege","Subject":["Python","C","Java"],"Topics":("Dict","Set"),"Age":35,"is_adult":True,"Marks":94.4}
#print(type(info))
#print(info["Name"])
#print(info["Topics"])
#print(info["Subject"])

#info["Name"]="Swati"
#info["Surname"]="Dhaka"
#print(info)

#null_dict={}
#null_dict["Name"]="ApnaCollege"
#print(null_dict)

#student={"name":"rahul kumar","subjects":{"phy":97,"chem":98,"maths":95}}
#print(student)
#print(student["subjects"])
#print(student["subjects"]["chem"])

#print(student.keys())
#print(list(student.keys()))
#print(len(list(student.keys())))

#print(student.values())
#print(list(student.values()))
#print(len(list(student.values())))

#print(student.items())

#pairs=list(student.items())
#print(pairs[0])

#print(student["name2"])
#print(student.get("name2"))

#student.update({"city":"delhi"})
#print(student)

#student.update({"city":"delhi","age":19})
#print(student)

#student.update({"name":"neha kumari","city":"delhi","age":19})
#print(student)

#collection={1,2,3,4}
#print(type(collection))


#collection={1,2,2,2,"hello","world","world",4}
#print(collection)
#print(type(collection))

#collection={}
#print(type(collection))

#collection=set()
#print(type(collection))

#collection=set()
#collection.add(1)
#collection.add(2)
#collection.add(2)
#collection.add("HELLO")
#collection.add((1,2,3))
#collection.remove(1)
#collection.clear()
#print(len(collection))

#set1={1,2,3}
#set2={2,3,4}
#print(set1.union(set2))
#print(set1)
#print(set2)

#set1={1,2,3}
#set2={2,3,4}
#print(set1.intersection(set2))


#dict={"CAT":"A small anima","TABLE":["A piece of furniture","List of facts & figures"]}
#print(dict)

#Subjects={"python","java","C++","python","javascript","java","python","java","C++","C"}
#print(Subjects)
#print(len(Subjects))

#marks={}

#x=int(input("enter phy:"))
#marks.update({"phy":x})
#x=int(input("enter maths:"))
#marks.update({"maths":x})
#x=int(input("enter chem:"))
#marks.update({"chem":x})

#print(marks)

#values={9,"9.0"}
#print(values)

#values={9,9.0}
#print(values)

#values={"9",9.0}
#print(values)

values={("float",9.0),("int",9)}
print(values)