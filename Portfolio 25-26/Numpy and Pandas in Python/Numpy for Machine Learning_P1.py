Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import numpy
ModuleNotFoundError: No module named 'numpy'
pip install numpy
SyntaxError: invalid syntax
import numpy
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import numpy
ModuleNotFoundError: No module named 'numpy'
import numpy as np
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
import numpy as np
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
import sys
print(sys.executable)
C:\Users\Administrator\AppData\Local\Programs\Python\Python311\pythonw.exe
import numpy
import numpy as np
a = [24.2, 45.2, 24.5, 64.3]
b = np.array(a)
print b
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print (b)
[24.2 45.2 24.5 64.3]
print b * 9/5 + 32
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print (b * 9/5 + 32)
[ 75.56 113.36  76.1  147.74]
c = [x * 9/5 + 32 for x in a]
print (c)
[75.56, 113.36, 76.1, 147.73999999999998]
d = np.arrange(1,10)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d = np.arrange(1,10)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\numpy\__init__.py", line 805, in __getattr__
    raise AttributeError(f"module {__name__!r} has no attribute {attr!r}")
AttributeError: module 'numpy' has no attribute 'arrange'. Did you mean: 'arange'?
d = np.arange(1,10)
print (d)
[1 2 3 4 5 6 7 8 9]
elephant = range(1,10)
print (elephant)
range(1, 10)
e = range(1,10)
print (e)
range(1, 10)
e = np.arange(0.5, 10.3, 0.6)
print (e)
[ 0.5  1.1  1.7  2.3  2.9  3.5  4.1  4.7  5.3  5.9  6.5  7.1  7.7  8.3
  8.9  9.5 10.1]
to print 50 values b/w 1 and 10
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# to print 50 values b/w 1 and 10
print (np.linspace(1,10))
[ 1.          1.18367347  1.36734694  1.55102041  1.73469388  1.91836735
  2.10204082  2.28571429  2.46938776  2.65306122  2.83673469  3.02040816
  3.20408163  3.3877551   3.57142857  3.75510204  3.93877551  4.12244898
  4.30612245  4.48979592  4.67346939  4.85714286  5.04081633  5.2244898
  5.40816327  5.59183673  5.7755102   5.95918367  6.14285714  6.32653061
  6.51020408  6.69387755  6.87755102  7.06122449  7.24489796  7.42857143
  7.6122449   7.79591837  7.97959184  8.16326531  8.34693878  8.53061224
  8.71428571  8.89795918  9.08163265  9.26530612  9.44897959  9.63265306
  9.81632653 10.        ]
# to define the number of items
print (np.linspace(1,10,20))
[ 1.          1.47368421  1.94736842  2.42105263  2.89473684  3.36842105
  3.84210526  4.31578947  4.78947368  5.26315789  5.73684211  6.21052632
  6.68421053  7.15789474  7.63157895  8.10526316  8.57894737  9.05263158
  9.52631579 10.        ]
print(1, 10, 9, True)
1 10 9 True
print (np.linspace(1, 10, 9, True))
[ 1.     2.125  3.25   4.375  5.5    6.625  7.75   8.875 10.   ]
print (np.linspace(1, 10, 9, False))
[1. 2. 3. 4. 5. 6. 7. 8. 9.]
print (np.linspace(1, 10, 50, False, True))
(array([1.  , 1.18, 1.36, 1.54, 1.72, 1.9 , 2.08, 2.26, 2.44, 2.62, 2.8 ,
       2.98, 3.16, 3.34, 3.52, 3.7 , 3.88, 4.06, 4.24, 4.42, 4.6 , 4.78,
       4.96, 5.14, 5.32, 5.5 , 5.68, 5.86, 6.04, 6.22, 6.4 , 6.58, 6.76,
       6.94, 7.12, 7.3 , 7.48, 7.66, 7.84, 8.02, 8.2 , 8.38, 8.56, 8.74,
       8.92, 9.1 , 9.28, 9.46, 9.64, 9.82]), np.float64(0.18))
python intro.py
SyntaxError: invalid syntax
python Intro.py
SyntaxError: invalid syntax

===================== RESTART: D:/Portfolio '25-'26/Numpy and Pandas in Python/Intro.py =====================
[0 1 2 3 4 5 6 7 8 9]

===================== RESTART: D:/Portfolio '25-'26/Numpy and Pandas in Python/Intro.py =====================
[0 1 2 3 4 5 6 7 8 9]
(10,)

===================== RESTART: D:/Portfolio '25-'26/Numpy and Pandas in Python/Intro.py =====================
[0 1 2 3 4 5 6 7 8 9]
(10,)
[0 1 2 3 4 5 6 7 8 9]

===================== RESTART: D:/Portfolio '25-'26/Numpy and Pandas in Python/Intro.py =====================
[0 1 2 3 4 5 6 7 8 9]
(10,)
[0 1 2 3 4 5 6 7 8 9]
[0 2 4 6 8]

===================== RESTART: D:/Portfolio '25-'26/Numpy and Pandas in Python/Intro.py =====================
[0 1 2 3 4 5 6 7 8 9]
(10,)
[0 1 2 3 4 5 6 7 8 9]
[0 2 4 6 8]
Traceback (most recent call last):
  File "D:/Portfolio '25-'26/Numpy and Pandas in Python/Intro.py", line 21, in <module>
    np4 = np.zeros()
TypeError: zeros() missing required argument 'shape' (pos 0)

===================== RESTART: D:/Portfolio '25-'26/Numpy and Pandas in Python/Intro.py =====================
[0 1 2 3 4 5 6 7 8 9]
(10,)
[0 1 2 3 4 5 6 7 8 9]
[0 2 4 6 8]
Traceback (most recent call last):
  File "D:/Portfolio '25-'26/Numpy and Pandas in Python/Intro.py", line 21, in <module>
    np4 = np.zeros()
TypeError: zeros() missing required argument 'shape' (pos 0)

===================== RESTART: D:/Portfolio '25-'26/Numpy and Pandas in Python/Intro.py =====================
[0 1 2 3 4 5 6 7 8 9]
(10,)
[0 1 2 3 4 5 6 7 8 9]
[0 2 4 6 8]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
>>> 
===================== RESTART: D:/Portfolio '25-'26/Numpy and Pandas in Python/Intro.py =====================
[0 1 2 3 4 5 6 7 8 9]
(10,)
[0 1 2 3 4 5 6 7 8 9]
[0 2 4 6 8]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
>>> 
===================== RESTART: D:/Portfolio '25-'26/Numpy and Pandas in Python/Intro.py =====================
[0 1 2 3 4 5 6 7 8 9]
(10,)
[0 1 2 3 4 5 6 7 8 9]
[0 2 4 6 8]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
[1 2 3 4 5]
>>> 
===================== RESTART: D:/Portfolio '25-'26/Numpy and Pandas in Python/Intro.py =====================
[0 1 2 3 4 5 6 7 8 9]
(10,)
[0 1 2 3 4 5 6 7 8 9]
[0 2 4 6 8]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
[1 2 3 4 5]
Traceback (most recent call last):
  File "D:/Portfolio '25-'26/Numpy and Pandas in Python/Intro.py", line 36, in <module>
    np6 = np.array(list2)
ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (4,) + inhomogeneous part.
