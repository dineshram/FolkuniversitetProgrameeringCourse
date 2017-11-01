Python 3.3.4 (v3.3.4:7ff62415e426, Feb 10 2014, 18:12:08) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> from turtle import *
>>> setup()
>>> title("Fun with turtles!!!!")
>>> clear()
>>> turtle.shape(turtle)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    turtle.shape(turtle)
NameError: name 'turtle' is not defined
>>> 
>>> 
>>> forward(100)
>>> turn_left()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    turn_left()
NameError: name 'turn_left' is not defined
>>> 
>>> 
>>> left()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    left()
TypeError: left() missing 1 required positional argument: 'angle'
>>> left(90)
>>> forward(100)
>>> left(90)
>>> forward(100)
>>> left(90)
>>> forward(100)
>>> 
>>> 
>>> clear()
>>> reset()
>>> 
>>> 
>>> 
>>> left(1)
>>> forward(1)
>>> 
>>> for count in 360:
	left(1)
	forward(1)

	
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    for count in 360:
TypeError: 'int' object is not iterable
>>> for count < 360:
	
SyntaxError: invalid syntax
>>> for count in range(360):
	left(1)
	forward(1)

	
>>> for count in range(360):
	left(115)
	forward(115)

	
>>> print('Bill Gates')
Bill Gates
>>> for count in range(10):
	print('Bill gates')

	
Bill gates
Bill gates
Bill gates
Bill gates
Bill gates
Bill gates
Bill gates
Bill gates
Bill gates
Bill gates
>>> 
>>> 
>>> 
>>> reset()
>>> 
>>> 
>>> 
>>> 
>>> for count in range(4):
	left(90)
	forward(200)

	
>>> def square():
	
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> for count in range(4):
	forward(100)

	
>>> reset()
>>> for count in range(4):
	forward(100)
	  left(90)
	  
SyntaxError: unexpected indent
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def square():
	for count in range(4):
		left(90)
		forward(100)

		
>>> square()
>>> 
>>> 
>>> reset()
>>> square()
>>> 
>>> 
>>> 
>>> def square(size):
	for count in range(4):
		left(90)
		forward(size)

		
>>> square()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    square()
TypeError: square() missing 1 required positional argument: 'size'
>>> square(500)
>>> square(10)
>>> square(50)
>>> 
>>> 
>>> reset()
>>> 
>>> for count in range(5):
	square(count*50)

	
>>> reset()
>>> 
>>> 
>>> 
>>> 
>>> for count in range(10):
	square(count*10)

	
>>> 
>>> 
>>> reset()
>>> down()
>>> up()
>>> 
>>> 

>>> forward(40)
>>> down()
>>> forward(40)
>>> 
>>> 
>>> 
>>> reset()
>>> 
>>> def square():
	for count in range(4):
		forward(50)
		right(90)

		
>>> for count in range(100):
	up()
	left(90)
	forward(25)
	square()

	
Traceback (most recent call last):
  File "<pyshell#130>", line 5, in <module>
    square()
  File "<pyshell#124>", line 4, in square
    right(90)
  File "<string>", line 1, in right
  File "C:\Python33\lib\turtle.py", line 1670, in right
    self._rotate(-angle)
  File "C:\Python33\lib\turtle.py", line 3268, in _rotate
    self._update()
  File "C:\Python33\lib\turtle.py", line 2655, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python33\lib\turtle.py", line 565, in _delay
    self.cv.after(delay)
  File "C:\Python33\lib\tkinter\__init__.py", line 530, in after
    self.tk.call('after', ms)
KeyboardInterrupt

>>> 
>>> 
>>> 
>>> def square(length):
	down()
	for count in range(4):
		forward(length)
		right(90)

		
>>> for count in range(100):
	up()
	left(90)
	forward(25)
	square(count)

	
>>> reset()
>>> def square(length):
	down()
	for count in range(4):
		forward(length)
		right(90)

		
>>> for count in range(10):
	up()
	left(90)
	forward(25)
	square(count)

	
>>> reset()
>>> 
>>> 
>>> for count in range(10):
	up()
	left(90)
	forward(25)
	square(count)

	
>>> reset()
>>> 
>>> 
>>> 
>>> for count in range(10):
	up()
	left(90)
	forward(25)
	square(count)

	
>>> for count in range(10):
	up()
	left(90)
	forward(25)
	square(count)

	

>>> def draw():
	for count in range(10):
		up()
		left(90)
		forward(25)
		square(count)

		
>>> 
>>> reset()
>>> draw()
>>> 
>>> 
>>> 
>>> draw()
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    draw()
  File "<pyshell#158>", line 6, in draw
    square(count)
  File "<pyshell#140>", line 5, in square
    right(90)
  File "<string>", line 1, in right
  File "C:\Python33\lib\turtle.py", line 1670, in right
    self._rotate(-angle)
  File "C:\Python33\lib\turtle.py", line 3268, in _rotate
    self._update()
  File "C:\Python33\lib\turtle.py", line 2652, in _update
    self._update_data()
  File "C:\Python33\lib\turtle.py", line 2643, in _update_data
    self._pencolor, self._pensize)
  File "C:\Python33\lib\turtle.py", line 544, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Python33\lib\tkinter\__init__.py", line 2310, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".47957264"
>>> draw()
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    draw()
  File "<pyshell#158>", line 6, in draw
    square(count)
  File "<pyshell#140>", line 5, in square
    right(90)
  File "<string>", line 1, in right
  File "C:\Python33\lib\turtle.py", line 1670, in right
    self._rotate(-angle)
  File "C:\Python33\lib\turtle.py", line 3268, in _rotate
    self._update()
  File "C:\Python33\lib\turtle.py", line 2652, in _update
    self._update_data()
  File "C:\Python33\lib\turtle.py", line 2643, in _update_data
    self._pencolor, self._pensize)
  File "C:\Python33\lib\turtle.py", line 544, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Python33\lib\tkinter\__init__.py", line 2310, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".48483312"
>>> draw()
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> list_of
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    list_of
NameError: name 'list_of' is not defined
>>> list_of_num = [20, 10, 5, -10, 9]
>>> print(max(list_of_numners))
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    print(max(list_of_numners))
NameError: name 'list_of_numners' is not defined
>>> print(max(list_of_num))
20
>>> 
>>> 
>>> 
>>> maximum = 0
>>> for iterator in len(list_of_num):
	if (list_of_num[iterator] > maximum):
		maximum = list_of_num[iterator]

		
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    for iterator in len(list_of_num):
TypeError: 'int' object is not iterable
>>> for iterator in range(len(list_of_num)):
	if (list_of_num[iterator] > maximum):
		maximum = list_of_num[iterator]

		
>>> print(maximum)
20
>>> def max(list_of_num):
	for iterator in range(len(list_of_num)):
		if (list_of_num[iterator] > maximum):
			maximum = list_of_num[iterator]

			
>>> max(lis)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    max(lis)
NameError: name 'lis' is not defined
>>> max(list_of_num)
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    max(list_of_num)
  File "<pyshell#200>", line 3, in max
    if (list_of_num[iterator] > maximum):
UnboundLocalError: local variable 'maximum' referenced before assignment
>>> 
>>> 
>>> 

>>> maximum = 0
>>> def max(list_of_num):
	global maximum
	for iterator in range(len(list_of_num)):
		if (list_of_num[iterator] > maximum):
			maximum = list_of_num[iterator]

			
>>> max(list_of_num)
>>> print(maximum)
20
>>> 
>>> 
>>> 
>>> def max(list_of_num):
	maximum = 0
	for iterator in range(len(list_of_num)):
		if (list_of_num[iterator] > maximum):
			maximum = list_of_num[iterator]
	return maximum

>>> 
>>> max(list_of_num)
20
>>> print(maximum)
20
>>> 
>>> 
>>> 
>>> 
>>> def max(list_of_num):
	test = 0
	for iterator in range(len(list_of_num)):
		if (list_of_num[iterator] > test):
			test = list_of_num[iterator]
	return test

>>> print(test)
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    print(test)
NameError: name 'test' is not defined
>>> def max(list_of_num):
	test = 0
	for iterator in range(len(list_of_num)):
		if (list_of_num[iterator] > test):
			test = list_of_num[iterator]
			print test
	return test
SyntaxError: invalid syntax
>>> def max(list_of_num):
	test = 0
	for iterator in range(len(list_of_num)):
		if (list_of_num[iterator] > test):
			test = list_of_num[iterator]
			print(test)

			
>>> print(max(list_of_num))
20
None
>>> def max(list_of_num):
	test = 0
	for iterator in range(len(list_of_num)):
		if (list_of_num[iterator] > test):
			test = list_of_num[iterator]
			print(test)
	return test

>>> print(max(list_of_num))
20
20
>>> list_of_num = [-1, -10, -50, -3]
>>> print(max(list_of_num))
0
>>> def max(list_of_num):
	test = list_of_num[0]
	for iterator in range(len(list_of_num)):
		if (list_of_num[iterator] > test):
			test = list_of_num[iterator]
			print(test)
	return test

>>> print(max(list_of_num))
-1
>>> def min(list_of_num):
	test = list_of_num[0]
	for iterator in range(len(list_of_num)):
		if (list_of_num[iterator] < test):
			test = list_of_num[iterator]
			print(test)
	return test

>>> print(min(lis_of_num))
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    print(min(lis_of_num))
NameError: name 'lis_of_num' is not defined
>>> print(min(list_of_num))
-10
-50
-50
>>> def min(list_of_num):
	test = list_of_num[0]
	for iterator in range(len(list_of_num)):
		if (list_of_num[iterator] < test):
			test = list_of_num[iterator]
		print(test)
	return test

>>> print(min(list_of_num))
-1
-10
-50
-50
-50
>>> def min(list_of_num):
	test = list_of_num[0]
	for iterator in range(len(list_of_num)):
		if (list_of_num[iterator] < test):
			test = list_of_num[iterator]
	print(test)
	return test

>>> print(min(list_of_num))
-50
-50
>>> 
