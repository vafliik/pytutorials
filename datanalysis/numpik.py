import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series(np.random.randn(5), index = ['a', 'b', 'c', 'd', 'e'])

print(s.count())
