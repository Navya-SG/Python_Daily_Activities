# merge dicts
dict1={'x':10,'y':20}
dict2={'y':99,'z':30}
dict1.update(dict2)
print(dict1)

dict1={'x':10,'y':20}
dict2={'y':99,'z':30}
dict1|dict2
print(dict1)

dict1={'x':10,'y':20}
dict2={'y':99,'z':30}
merge={**dict1,**dict2}
print(merge)

# add key:value to dict id its not present
d={'x':10,'y':20}
keys = d.keys()
d["c"]=3
print(len(keys))
print(d)
print(len(d))

#items
print(d.items())
print(type(d['x'])) #type

# pop
d={'x':10,'y':20}
d.pop('z')
print(d)  #->error

d={'x':10,'y':20}
d.pop('y')
print(d) 

# key/value search
d={'x':10,'y':20}
print('x' in d) #key search
print(20 in d) #value search

#nested dict into list
student=[
        {"name":{1:"navya",2:"navi"},
         "roll no":{3:"gokila"}
        }]
print(student)

#access values
student={"amit":{"math":95, "science":89},
          "ravi":{"math":80, "science":92},}
print(student["ravi"]["science"])

#len - takes item(key:value-pair) len
employee={"name":"john", "age":22, "salary":3200}
print(len(employee))

# activity
grades={"anita":92,
        "ravi":85,
        "kiran":76,
        "zoya":88}  #dictionary
#get grades based on input name or print name not found
print(grades.get(input("enter name:"),"name not found")) 

#activity
access_data={(100,209):"Alice",
            (104,210):"Bob",
            (105,211):"Charlie",
            (106,212):"Diana"}
key=tuple(map(int,input("enter key:").split(',')))
print(access_data.get(key) or access_data.get(key[::-1]) or "key not match")

#
d={'x':10}
value_view=d.values()
d['y']=20
print(list(value_view))

#
new_dict={}
dict1={"name":"ravi","age":25}
dict2={"age":"30","city":"chennai"}
new_dict.setdefault(dict1,dict2)
print(new_dict)

#
d={'one':1,'two':2}
x=d.pop('three',1)
print(x)

#
d={'one':1,'two':2}
d['three']=5 #adds if not present already
d['four']+=5 #-> error('four' not present)
d['two']+=5 #only if its already present
print(d)
d.popitem() #last item
print(d)

#
d={'a':100}
d.pop('a')
print(d['a']) #error line

#
x=(1,2)
y=[1,2]
d={}
d[x]=10
d[y[0],y[1]]=20
print(d)

#
d={'x':5}
d2=d
d.clear()
print(len(d2)) #0

#
d={'a':1,'b':2}
v=d.values()
d['c']=3
print(3 in v) #True

#
d={'p':100,'q':200}
print(list(d.items())[0][1]) #100

#
d={'a':1,'b':2}
v=list(d.values())
v.append(3)
print(len(d)) #2

#
data=((10,20),(30,40,50),(60,70))
(a,b),(c, *rest),(d,e)=data
print(a+c+d,len(rest))

#
d={'l1':{'l2':{'l3':'found'}}}
res=d.get('l1',{}).get('missing',{}).get('l3','not found')
print(res) #notfound

#
d=({'count':5},)
r=d*2
r[0]['count'] +=10 #5+10=15
r[1]['total'] = 25 #total:25 is added to d
print(r[0]['count'],r[1]['total']) #15 25

#
base={'user':{'profile':{'name':'john'}}}
update={'user':{'profile':{'age':25},'settings':{'theme':'dark'}}}
base['user'].update(update['user'])
print(base['user']['profile']) #{age:25}

#
s=(10,20,30,40,50,60)
start,*middle,end=s[::2]
print(start,end,len(middle)) #10 50 1