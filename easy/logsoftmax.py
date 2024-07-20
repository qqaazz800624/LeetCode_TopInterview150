#%%

from typing import List
import numpy as np

import numpy as np
from typing import List

def logsoftmax(x: List[float], i: int) -> float:
    exp_x = np.exp(x - np.max(x))  # Stability improvement by subtracting max(x)
    sum_exp_x = np.sum(exp_x)
    log_sum_exp_x = np.log(sum_exp_x)
    logsoftmax_i = x[i] - np.max(x) - log_sum_exp_x  # Direct calculation
    return logsoftmax_i

x = [1, 2, 3]
i=2

# x = [0.5, 0.4, 0.8, 7000]
# i = 0
logsoftmax(x, i)

#%%




#%%





#%%