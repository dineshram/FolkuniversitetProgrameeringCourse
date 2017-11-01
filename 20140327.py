Python 3.3.4 (v3.3.4:7ff62415e426, Feb 10 2014, 18:12:08) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def a(b, c, d): pass

>>> a()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a()
TypeError: a() missing 3 required positional arguments: 'b', 'c', and 'd'
>>> a(1, 2, 3)
>>> print(a(1,2,3))
None
>>> print(type(1/2))
<class 'float'>
>>> print(5//2)
2
>>> print(5%2)
1
>>> print(5//8)
0
>>> print(5%8)
5
>>> print(5*6-7/2)
26.5
>>> print len([1,2])
SyntaxError: invalid syntax
>>> print len(([1,2]))
SyntaxError: invalid syntax
>>> print(len[1,2])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(len[1,2])
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print((len([1,2])))
2
>>> print((len([1,2])))
KeyboardInterrupt
>>> a= [1, 2, 3, 4, 1, 3]
>>> print(len(a))
6
>>> b = (1, 2, 3, 4, 1, 3)
>>> print(len(b))
6
>>> nums = set([1,1,2,3,3,3,4])
>>> print len(nums)
SyntaxError: invalid syntax
>>> print(len(nums))
4
>>> print(type(nums))
<class 'set'>
>>> a = (1, 2, 3)
>>> print(type(a))
<class 'tuple'>
>>> x = True
y = False
z = False
SyntaxError: multiple statements found while compiling a single statement
>>> x = True
>>> y = False
>>> z = False
>>> if x or y and z:
	print "yes"
	
SyntaxError: invalid syntax
>>> if x or y and z:
	print "yes"
	
SyntaxError: invalid syntax
>>> if (x or y and z):
	print("yes")

	
yes
>>> if (x or y and z):
	print("yes")
	else:
		
SyntaxError: invalid syntax
>>> if (x or y and z):
	print("yes")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if (x or y and z): print("yes")
	else print("no")
	
SyntaxError: unexpected indent
>>> if x or y and z: print("yes")
else: print("no")

yes
>>> if x and y or z: print("yes")
else: print("no")

no
>>> ================================ RESTART ================================
>>> 
Type the Name - leave blank to finishd
Type the Street, Town, Phone. Leave blank to finisha
Type the Name - leave blank to finish
Traceback (most recent call last):
  File "C:\Python33\input_example1.py", line 10, in <module>
    name = raw_input("Which name to display?(blank to finish)")
NameError: name 'raw_input' is not defined
>>> ================================ RESTART ================================
>>> 
Type the Name - leave blank to finisha
Type the Street, Town, Phone. Leave blank to finishd
Type the Name - leave blank to finish
Which name to display?(blank to finish)a
a d
Which name to display?(blank to finish)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a = input()
1
>>> a = input("please give me something to print :")
please give me something to print :2
>>> print ("your input was %s" %a)
your input was 2
>>> print ("your input was %s")
your input was %s
>>> 
>>> 
>>> userName = input("Please choose a user name :")
KeyboardInterrupt
>>> def example():
	userName = input("Please choose a user name :")
	if (userName == "Bob"):
		print("Hi Bob !!!")
	else: print("Bad name !!!!")

	
>>> example()
Please choose a user name :monty python
Bad name !!!!
>>> bob
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    bob
NameError: name 'bob' is not defined
>>> example()
Please choose a user name :bob
Bad name !!!!
>>> example()
Please choose a user name :Bob
Hi Bob !!!
>>> 
>>> def example():
	userName = input("Please choose a user name :")
	if (userName == "Bob"):
		print("Hi %s !!!" %userName)
	else: print("Bad name !!!!")

	
>>> example()
Please choose a user name :Bob
Hi Bob !!!
>>> print("Hi" + userName !!!)
SyntaxError: invalid syntax
>>> print("Hi" + userName+ "!!!")
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print("Hi" + userName+ "!!!")
NameError: name 'userName' is not defined
>>> print("Hi" + %userName+ "!!!")
SyntaxError: invalid syntax
>>> def example():
	userName = input("Please choose a user name :")
	if (userName == "Bob"):
		print("Hi" + userName+ "!!!")
	else: print("Bad name !!!!")

	
>>> example()
Please choose a user name :Bob
HiBob!!!
>>> 
>>> 
>>> 
>>> def example():
	userName = input("Please choose a user name :")
	if (len(userName) == 6):
		print("Hi" + userName + "!!!")
	else: print("Bad name !!!!")

	
>>> example()
Please choose a user name :Bob
Bad name !!!!
>>> example()
Please choose a user name :donald
Hidonald!!!
>>> 
>>> 
>>> def example():
	while(True):
		userName = input("Please choose a user name :")
		if (len(userName) == 6):
			print("Hi " + userName + " !!!")
		else: print("Bad name !!!!")

		
>>> example()
Please choose a user name :bob
Bad name !!!!
Please choose a user name :donald
Hi donald !!!
Please choose a user name :askfgsdk.hsdlg
Bad name !!!!
Please choose a user name :kjgvsdjfg
Bad name !!!!
Please choose a user name :
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    example()
  File "<pyshell#94>", line 3, in example
    userName = input("Please choose a user name :")
  File "C:\Python33\lib\idlelib\PyShell.py", line 1381, in readline
    line = self._line_buffer or self.shell.readline()
KeyboardInterrupt
>>> def example():
	while(True):
		userName = input("Please choose a user name :")
		if (len(userName) >= 6):
			print("Hi " + userName + " !!!")
		else: print("Bad name !!!!")

		
>>> import sys
>>> def example():
	while(True):
		userName = input("Please choose a user name :")
		if (len(userName) >= 6):
			print("Hi " + userName + " !!!")
			sys.exit()
		else: print("Bad name !!!!")

		
>>> example()
Please choose a user name :jkefh
Bad name !!!!
Please choose a user name :bommarley
Hi bommarley !!!
>>> def example():
	while(True):
		userName = input("Please choose a user name :")
		if (len(userName) >= 6):
			print("Hi " + userName + " !!!")
			break()
		else: print("Bad name !!!!")
		
SyntaxError: invalid syntax
>>> def example():
	while(True):
		userName = input("Please choose a user name :")
		if (len(userName) >= 6):
			print("Hi " + userName + " !!!")
			break
		else: print("Bad name !!!!")

		
>>> example()
Please choose a user name :elisabeth
Hi elisabeth !!!
>>> 
>>> 
>>> 
>>> def example():
	while(True):
		userName = input("Please choose a user name :")
		if (len(userName) >= 6):
			print("Hi " + userName + " !!!")
			break
		else: print("Bad name !!!!")

		
>>> def example():
	while(True):
		userName = input("Please choose a user name :")
		if (len(userName) >= 6):
			print("Hi " + userName + " !!!")
			break
		else: print("Bad name !!!!")
	print("hey ! i am outside the while loop now !!!")

	
>>> example()
Please choose a user name :kjhl-upæiåæo
Hi kjhl-upæiåæo !!!
hey ! i am outside the while loop now !!!
>>> def example():
	while(True):
		userName = input("Please choose a user name :")
		if (len(userName) >= 6):
			print("Hi " + userName + " !!!")
			sys.exit()
		else: print("Bad name !!!!")
	print("hey ! i am outside the while loop now !!!")

	
>>> example()
Please choose a user name :hf,kglkj.jø
Hi hf,kglkj.jø !!!
>>> addressBook = {}
>>> print(type(addressBook))
<class 'dict'>
>>> addressBook = {}
>>> 
>>> # read entries till an empty string
>>> name = input("Type the Name - leave blank to finish ")
Type the Name - leave blank to finish 
>>> 
>>> 
>>> 
>>> def myAddressBokk():
	addressBook = {}
	name = input("Type the Name - leave blank to finish ")
	while name != "":
		entry = input("Type the Street, Town, Phone. Leave blank to finish ")
		addressBook[name] = entry
		name = input("Type the Name - leave blank to finish ")

		
>>> def myAddressBokk():
	addressBook = {}
	name = input("Type the Name - leave blank to finish ")
	while name != "":
		entry = input("Type the Street, Town, Phone. Leave blank to finish ")
		addressBook[name] = entry
		name = input("Type the Name - leave blank to finish ")
	name = input("Which name to display?(blank to finish)")
	while name != "":
	   print (name, addressBook[name])
	   name = input("Which name to display?(blank to finish) ")

	   
>>> myAddressBook()
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    myAddressBook()
NameError: name 'myAddressBook' is not defined
>>> myAddressBokk()
Type the Name - leave blank to finish dinesh
Type the Street, Town, Phone. Leave blank to finish bergen
Type the Name - leave blank to finish bob
Type the Street, Town, Phone. Leave blank to finish chicago
Type the Name - leave blank to finish elisabeth
Type the Street, Town, Phone. Leave blank to finish new york
Type the Name - leave blank to finish 
Which name to display?(blank to finish)bob
bob chicago
Which name to display?(blank to finish) dinesh
dinesh bergen
Which name to display?(blank to finish) 
>>> 
>>> 
>>> 
>>> def myAddressBokk():
	addressBook = {}
	name = input("Type the Name - leave blank to finish ")
	while name != "":
		entry = input("Type the Street, Town, Phone. Leave blank to finish ")
		addressBook[name] = entry
		name = input("Type the Name - leave blank to finish ")

		
>>> addressBook = {}
>>> def myAddressBokk():
	global addressBook = {}
	name = input("Type the Name - leave blank to finish ")
	while name != "":
		entry = input("Type the Street, Town, Phone. Leave blank to finish ")
		addressBook[name] = entry
		name = input("Type the Name - leave blank to finish ")
		
SyntaxError: invalid syntax
>>> def myAddressBokk():
	global addressBook
	name = input("Type the Name - leave blank to finish ")
	while name != "":
		entry = input("Type the Street, Town, Phone. Leave blank to finish ")
		addressBook[name] = entry
		name = input("Type the Name - leave blank to finish ")

		
>>> def dispalyMyAddressBook():
	global addressBook
	name = input("Which name to display?(blank to finish)")
	while name != "":
	   print (name, addressBook[name])
	   name = input("Which name to display?(blank to finish) ")

	   
>>> myAddressBook()
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    myAddressBook()
NameError: name 'myAddressBook' is not defined
>>> myAddressBokk()
Type the Name - leave blank to finish dinesh
Type the Street, Town, Phone. Leave blank to finish bergen
Type the Name - leave blank to finish bob
Type the Street, Town, Phone. Leave blank to finish new york
Type the Name - leave blank to finish marley
Type the Street, Town, Phone. Leave blank to finish india
Type the Name - leave blank to finish 
>>> 
>>> 
>>> displayMyAddressBook()
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    displayMyAddressBook()
NameError: name 'displayMyAddressBook' is not defined
>>> dispalyMyAddressBook()
Which name to display?(blank to finish)marley
marley india
Which name to display?(blank to finish) dinesh
dinesh bergen
Which name to display?(blank to finish) 
