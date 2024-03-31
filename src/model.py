# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 11:01:49 2024

@author: https://github.com/AraeneaCLI/
"""

"""
Data Collection
Data Pre Processing
Training Model 
Model Evaluation
"""

from sklearn.datasets import load_boston

boston = load_boston()

X = boston.data
y = boston.target

print(X.shape)
print(y.shape)
