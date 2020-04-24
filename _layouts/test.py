#%%
import numpy as np 
import pandas as pd
x = [[1,1,1,1,1,1,1],[-3,-2,-1,0,1,2,3],[0,0,0,1,1,1,1]]
x = np.array(x)
#%%

x[:,1]

# %%
x

# %%
x[1]

# %%
np.linalg.inv(x[0].dot(x[0].T)).dot(x[0])

# %%
x = x.T
x0 = x[:,0].reshape(-1,1)
x0.shape

# %%
np.linalg.inv(x0.T.dot(x0))


# %%
x1 = x[:,1]
x1 = x1.reshape(-1,1)
x0.T.dot(x1)

# %%
