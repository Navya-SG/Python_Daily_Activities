#import numpy as np

#numpy array
import numpy as np
arr = np.array([1,2,3,4])
print(arr) #[1 2 3 4]
print(type(arr)) #<class 'numpy.ndarray'>

#2D array
import numpy as np
arr = np.array([[1,2],[3,4]])
print(arr) #[[1 2]
 	     [3 4]] the inner list is a row

#list vs array in numpy
import numpy as np
lst =[1,2,3,4]
arr = np.array([1,2,3,4])
print(lst) #[1, 2, 3, 4]
print(arr) #[1 2 3 4]
#print(lst + 5) #error
print(arr + 5) #[6 7 8 9]

#numpy array shape
import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([[1,2],[3,4]])
arr3 = np.array([[1,2],[3,4],[5,6],[7,8]])
arr4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1.shape) #(4, )
print(arr2.shape) #(2, 2)
print(arr3.shape) #(4, 2)
print(arr4.shape) #(3, 3)

#numpy array datatype
import numpy as np
arr1 = np.array([1,2,3,4])
print(arr1.dtype) #int64
arr2 = np.array([1.0,2.3,6.9])
print(arr2.dtype) #float64
arr3 = np.array([True,False])
print(arr3.dtype) #bool

#numpy functions
#np.zeros(x,y)
import numpy as np
arr = np.zeros((3,4))
print(arr) #3X4 matrix filled with 0.
 
#np.ones(x,y)
import numpy as np
arr = np.ones((2,2))
print(arr) #2X2 matrix filled with 1.

#np.arange(start,stop,step)
import numpy as np
arr = np.arange(5,20,2) 
print(arr) #[ 5  7  9 11 13 15 17 19]

#np.arange(start,stop,num) # num= number of samples
import numpy as np
arr1 = np.linspace(0,1,5) 
print(arr1) #[0.   0.25 0.5  0.75 1.  ]
arr2 = np.linspace(0,1,7) 
print(arr2) #[0.         0.16666667 0.33333333 0.5        0.66666667 0.83333333 1.        ]
 
#vectorized operations(Each operation is applied element-wise)
import numpy as np
arr1 = np.array([1,2,3]) 
arr2 = np.array([4,5,6]) 
print(arr1+arr2) #[5 7 9]
print(arr1*2) #[2 4 6]

#.apply with pandas for column wise
import pandas as pd
import numpy as np
df=pd.read_json("data.json")#pandas
df[["mark"]].apply([np.mean,np.std]) #[[]] #pandas+numpy
print(df["mark"])#pandas