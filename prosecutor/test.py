import torch 
data =[1, 2, 3]
data = torch.tensor(data)
print(data)

import numpy as np 
data = np.array([1, 2, 3])
data = torch.from_numpy(data)
print(data)

import torch 

# create a 3x3 tensor with 
# random values between 0 and 1 
data = torch.rand(3, 3)
print(data)