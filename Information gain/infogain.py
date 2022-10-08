import pandas as pd
import numpy as np
from numpy.core.fromnumeric import nonzero

df = pd.read_csv('InfoGain.csv')

def is_pure(s):
    return len(set(s)) == 1

def most_common(a):
    (values,counts) = np.unique(a,return_counts=True)
    ind=np.argmax(counts)
    return values[ind]

def print_tree(d, depth = 0):
    for key, value in d.items():
        for i in range(depth):
                print(' ', end='')
        if type(value) is dict:
            print(key, end=':\n')
            print_tree(value, depth + 1)
        else:
            print(key, end=': ')
            print(value)

def partition(s):
  return {i: (s==i).nonzero()[0]  for i in np.unique(s)}


def entropy(s):
  unique_,counts_ = np.unique(s,return_counts= True)
  freq_ = counts_.astype(float)/len(s)
  res = 0
  for i in freq_:
    res -= i * np.log2(i)
  return res

def mutual_information(x,y):
  entropy_set = entropy(y)
  unique,counts = np.unique(x ,return_counts= True)
  freq = counts.astype(float)/len(x)

  entropy_subset = 0
  for i,j in zip(freq,unique):
   entropy_subset += i * entropy(y[x == j ])

  return entropy_set - entropy_subset

def recursive_split(x, y):

  if is_pure(y) or len(y) == 0:
    return most_common(y)
  
  gain = np.array([mutual_information(feature,y) for feature in x.T ])
  
  print('features : ',features)
  print('Information Gain : ',gain)
  print('Best split is : ',features[np.argmax(gain)])
 
  x_ = np.argmax(gain)

  if np.all(gain < 1e-6):
    return most_common(y)

  sets = partition(x[:,x_])
  print(sets)

  tree = {} 

  for k,v in sets.items():
    y_subset = y.take(v,axis = 0)
    x_subset = x.take(v,axis = 0)
    print(x_subset,y_subset)
    tree["x_%d = %s" % (x_, k)] = recursive_split(x_subset, y_subset)

  return tree

df_ = df.copy()
df_ = df.drop('profitable',axis = 1)
x = np.array(df_).T

for i in range(len(x[2])):
  if x[2][i] == 2:
    x[2][i] = 'two'
  elif x[2][i] == 4:
    x[2][i] = 'four'
  elif x[2][i] == 5:
    x[2][i] = 'five'

x = x.T
y = np.array(df['profitable'])
features = list(df_)
d = recursive_split(x,y)
Tree = print_tree(d)
print(Tree)