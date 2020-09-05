Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list and its default functions
>>> lst=[25,47,25,69,25,46]
>>> lst
[25, 47, 25, 69, 25, 46]
>>> len(lst)
6
>>> min(lst)
25
>>> max(lst)
69
>>> sum(lst)
237
>>> lst1=[4,6,8,4]
>>> lst2=[7,5,3,8,1]
>>> c=(lst1,lst2)
>>> c
([4, 6, 8, 4], [7, 5, 3, 8, 1])
>>> 
>>> #dictionary and its default functions
>>> dit={"name":"geetha","age" : 20,"number": 681568381}
>>> len(dit)
3
>>> str(dit)
"{'name': 'geetha', 'age': 20, 'number': 681568381}"
>>> type(dit)
<class 'dict'>
>>> 
>>> #sets and its default values
>>> 
>>> st={"sai","geetha",4,6,8,5,58,5,64,}
>>> st
{64, 4, 5, 'geetha', 6, 8, 'sai', 58}
>>> st.add(9)
>>> st
{64, 4, 5, 'geetha', 6, 8, 9, 'sai', 58}
>>> st.discard(64)
>>> print(st)
{4, 5, 'geetha', 6, 8, 9, 'sai', 58}
>>> a={1,2,5,12}
>>> b={5,6,89,26}
>>> a-b
{1, 2, 12}
>>> print(a|b)
{1, 2, 5, 6, 12, 89, 26}
>>> 
>>> #tuple and its default functions
>>> 
>>> tup("geetha","@","letsupgrade.in")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    tup("geetha","@","letsupgrade.in")
NameError: name 'tup' is not defined
>>> tup=("geetha","@","letsupgrade.in")
>>> tup.count("@")
1
>>> tup2=("sai","@","geetha")
>>> len(tup)
3
>>> max(tup)
'letsupgrade.in'
>>> min(tup)
'@'
>>> max(tup2)
'sai'
>>> len(tup2)
3
>>> min(tup2)
'@'
>>> 
>>> #string and its methods
>>> 
>>> sttr=("ha","hmm","achaa")
>>> str
<class 'str'>
>>> 
>>> 
>>> str=("ha","hmm","achaa")
SyntaxError: invalid syntax
>>> str=("ad","gh","ab")
>>> str
('ad', 'gh', 'ab')
>>> str.count("ab")
1
>>> str.index("ad")
0
>>> 