#!/usr/bin/env python
# coding: utf-8

# In[12]:


a=5
b=6
c=a+b
print("a ={}".format(a))
print("b ={}".format(b))
print("c={}+{}={}".format(a,b,a+b))


# In[14]:


x=int(input("Enter Number 1:"))
y=int(input("Enter Number 2:"))
print("{}+{}={}".format(x,y,x+y))


# In[11]:


n=int(input("enter number:"))
if n%2==0:
    print('%d is even number'%n)
else:
    print('%d odd number'%n)


# In[16]:


n=int(input("enter number:"))
if n%2==0:
    print('%d is even number'%n)
else:
    print('%d odd number'%n)
    
if n>0:
    print('%d is positive number'%n)
elif n==0:
    print('%d Zeror'%n)
else:
    print('%d nagative number'%n)


# In[25]:


print(" log in page")
user= input(" Username: ")
pwd=input(" Pasword: ")

if user=="user" and pwd=="123":
    print(" Welcome Computer Sciences, You have logged in")
else:
    print(" try again")


# In[1]:


i=1
while i <= 10:
    if i<10:
        print(i, end=',')
    else:
        print(i, end='.')
    i= i+1
        


# In[5]:


site = "Programmer"
for n in site:
    print(n)
print(type(n))


# In[8]:


names =['Mateo','john','Eric','Mark','Robert']
for n in names:
    print(n)


# In[2]:


import pandas as pd
print('panda Version', pd.__version__)


# In[7]:


df = pd.read_clipboard()
df


# In[6]:


df1 =pd.read_csv('https://github.com/datasciencedojo/datasets/raw/master/titanic.csv')
df1


# In[9]:


df =pd.read_excel('D:/lerninign for IT4/Learning Part Two/Data Minning/DataDemo.xlsx')
df


# In[9]:


df1.info()


# In[10]:


df1.describe()


# In[49]:


df1.iloc[0,0]


# In[40]:


import pandas as pd
df2= pd.read_excel('D:/lerninign for IT4/Learning Part Two/Data Minning/DataDemo.xlsx')
df2


# In[53]:


def modifys(value):
       if value == True:
           return "yes"
       else:
           return "No"

def modify1(value):
       if value == "no":
           return "0"
       else:
           return "1"
       
df2["Windy"].apply(modifys)
df2["Play"].apply(modify1)

df2


# In[39]:


print("Complate")


# In[58]:


df2.replace(to_replace="no",value="0")
df3=df2
df3.replace(to_replace=="yes",value="1")
df2
df3


# In[ ]:




