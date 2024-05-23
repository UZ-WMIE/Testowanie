# hipoteza H0: mi =  mi0

import numpy as np
from scipy.stats import t

n = 10000
mi0 = 12
sigma_kwadrat = 36

X = np.random.normal(mi0, np.sqrt(sigma_kwadrat), n)
mean = np.mean(X)

df = n - 1
s = t.rvs(df, size=n)

Y = (mean-mi0) / (np.sqrt(s ^ 2/n))

alfa = 0.05
yi = np.abs(Y)
