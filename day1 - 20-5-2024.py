#1.ANAGRAM(leetcode)
"""
class Solution:
    #def isAnagram(self,s:str, t:str)->bool:
        #s="dog"
        #t="god"
        s1=set(s)
        t1=set(t)
        s2=list(s1)
        t2=list(t1)
        if len(s)!=len(t):
            return False
        if sorted(s2)!=sorted(t2):
            return False
        for i in s2:
            if s.count(i)!=t.count(i):
                return False
            else:
                return True
   """


#anagram(py)
"""
class Sol:
    s="dog"
    t="god"
    s1=set(s)
    t1=set(t)
    s2=list(s1)
    t2=list(t1)
    print(s1)
    print(t1)
    print(sorted(s2))
    print(sorted(t2))
    if len(s)!=len(t):
        print("False")
    if sorted(s2)!=sorted(t2):
        print("False")
    for i in s2:
        if s.count(i)!=t.count(i):
            print("False")
        else:
            print("True")
            break
"""



#2.ISOMORPHIC(leetcode)
"""
class Solution:
    def isIsomorphic(self, s:str, t:str)->bool:
        d={}
        if len(set(s))!=len(set(t)):
            return False
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=t[i]
            else:
                if t[i]!=d[s[i]]:
                    return False
        return True
"""


#isomorphic(py)
"""
class Solution:
    s="egg"
    t="add"
    d={}
    if len(set(s))!=len(set(t)):
        print("False")
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]]=t[i]
        else:
            if t[i]!=d[s[i]]:
                print("False")
    print("True")
"""



#3.DETERMINE COLOR OF A CHESS BOARD
"""
class Solution:
    def squareIsWhite(self, coordinates: str)->bool:
        alp1="aceg"
        alp2="bdfh"
        if coordinates[0] in alp1:
            if int(coordinates[1])%2==0:
                return True
            else:
                return False
        if coordinates[0] in alp2:
            if int(coordinates[1])%2==0:
                return False
            else:
                return True

"""



"""
#determine color of chess board
a1=input()
b1=int(input())
alp1="aceg"
alp2="bdfh"
if a1 in alp1:
    if b1%2==0:
        print("white")
    else:
        print("black")
if a1 in alp2:
    if b1%2==0:
        print("black")
    else:
        print("white")
"""

"""
#list operations
l=[]
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.pop()
print(l)
print(type(l))
print(l[-1])
"""


"""
#stack
class Stack:
    def __init__(self):
        self.l=[]
        self.size=5
    def push(self,data):
        if len(self.l)!=self.size:
            self.l.append(data)
        else:
            print("Stack is full")
    def pop(self):
        if self.size==0:
            print("Stack is empty")
        else:
            self.l.pop()
    def peek(self):
        if self.size==0:
            print("Stack is empty")
        else:
            print(self.l[-1])
a=Stack()
a.push(10)
a.push(20)
a.push(30)
a.pop()
a.peek()
"""


#if negative number.................................
"""
#evaluate reverse polish number(postfix expression)
s="54367+-*+"
stack=[]
for i in s:
    if i.isdigit():
        stack.append(int(i))
    else:
        a=stack.pop()
        b=stack.pop()
        if i=='+':
            stack.append(a+b)
        elif i=='-':
            stack.append(a-b)
        elif i=='*':
            stack.append(a*b)
print(stack)
"""


#print the last entered element
"""
s=[1,2,3,4,5,6,7,8,9,10,11,12]
n=3
#a=s[::-1]
flag=0
while len(s)>1:
    if flag==0:
        for i in range(n):
            if len(s)>1:
                s.pop(0)
            else:
                break
            flag=1
    else: 
        for i in range(n):
            if len(s)>1:
                s.pop()
            else:
                break
            flag=0
print(s[0])
"""


#VALID PARANTHESES-
"""
s=input()
l=[]
flag=0
for i in s:
    if i=='(' or i=='{' or i=='[':
        l.append(i)
    else:
        if len(l)>0:
            if i==')' and l.pop()!='(':
                print("False")
            elif i=='{' and l.pop()!='}':
                print("False")
            elif i=='[' and l.pop()!=']':
                print("False")
        else:
            l.append(i)
print(l)
if len(l)==0:
    print("True")
else:
    print("False")
"""



#IMPLEMENTING QUEUE USING STACK
"""
l=[1,2,3,4]
s=[]
while(l!=0):
    for i in range(len(l)):
        s.append(l.pop())
    print(s)
    if len(s)>0:
        s.pop()
    else:
        break
    for i in range(len(s)):
        l.append(s.pop())
print(l)

"""

class MyQueue:
    def __init__(self):
        self.l=[]
        self.s=[]
    def push(self,x:int)->None:
        self.append(x)
    def pop(self)->int:
        for i in range(len(self.l)):
            self.s.append(self.l.pop())
        a=self.s.pop()
        for i in range(len(self.l)):
    






        





