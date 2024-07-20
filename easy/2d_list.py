#%% 2 (a)

def foo_1(row_num, col_num):
    two_d_list = [[i*col_num + j for j in range(col_num)] for i in range(row_num)]
    return two_d_list


m1 = foo_1(row_num=3, col_num=3)
m2 = foo_1(row_num=3, col_num=4)

print(m1)

#%% 2 (b) transpose of m1 and m2

def foo_2(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

foo_2(m1)


#%% 2 (c)

transposed_m1 = foo_2(m1)
transposed_m2 = foo_2(m2)

print(transposed_m2)



#%% 2 (d)

import numpy as np

def foo_1(row_num, col_num):
    two_d_list = [[i*col_num + j for j in range(col_num)] for i in range(row_num)]
    return two_d_list



#%%




#%%