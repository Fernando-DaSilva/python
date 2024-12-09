#!/usr/bin/env python
# coding: utf-8

# In[2]:


first_name = 'Esperanza'
last_name = 'Pérez Íñiguez'

print(first_name + ' ' + last_name)


# In[3]:


print(type(first_name))


# In[4]:


print(first_name[0])
print(first_name[1])
print(first_name[2])
print(first_name[3])
print(first_name[4])
print(first_name[5])
print(first_name[6])
print(first_name[7])






# In[4]:


for letter in first_name:
    print(first_name[letter])


# In[8]:


age = 53
print(type(age))


# In[12]:


age_str = '53a' 


# In[10]:


print(type(age_str))


# In[13]:


print(int(age_str))


# In[18]:


payment = 3.4524


# In[20]:


print(type(payment))


# In[21]:


a = 10
b = 15
c = 20

x = a + b 
print(x) 


# In[22]:


y = c - a
print(y)


# In[23]:


z = a * b 
print(z) 


# In[24]:


d = a / b 
print(d) 


# In[29]:


e = c // 3
print(e) 


# In[30]:


x = c ** 2


# In[31]:


print(x)


# In[34]:


x = (( 3 * 2 ) - ( 4 + 1 )) * 3
print(x) 


# In[37]:


x = 221321 % 221
print(x) 


# In[38]:


def my_function():
  print("Hello from a function")

my_function()


# In[39]:


def my_function(name):
  print(f"Hello {name}")

my_function('John')


# In[46]:


def my_function(first_name, last_name, age):
    name_of_the_person = first_name + ' ' + last_name
    born_in_the_year_of = 2024 - age 
    return f"Hello {name_of_the_person}",born_in_the_year_of

name_of_the_person, born_in_the_year_of = my_function('John','Doe', 53)

print(name_of_the_person)
print(born_in_the_year_of)


# In[53]:


cup3 = 'water' 
def blender(fruit_01, fruit_02, liquid):
    first_juice = fruit_01 + fruit_02 + liquid
    second_juice = fruit_01 + liquid
    third_juice = liquid 
    return third_juice, second_juice

cup1, cup2 = blender(' orange ',' banana',' grapes juice ')
print(cup1)
print(cup2)
print(cup3)


                        
    


# In[58]:


def filter_water(water, liters):
    return f"{liters} of {water} is filtered"

cup = filter_water('H2O', 10)
print(cup) 


# In[57]:


print(cup)


# In[60]:


water = 'H2O'
liters = 10
print(f"{water} + {liters}")


# In[5]:


def baskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    sqr_delta = delta ** -2
    x1 = (-b + sqr_delta) / ( 2 * a )
    x2 = (-b - sqr_delta) / ( 2 * a )
    return x1, x2

r1, r2 = baskara(10,11,12)
print(r1)
print(r2)


# In[ ]:




