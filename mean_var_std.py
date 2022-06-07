import numpy as np
def calculate(arr):
    A = {}
    M = np.array(arr)
    try:
        M=M.reshape(3,3)
        A['mean'] = [M.mean(axis=0).tolist(),M.mean(axis=1).tolist(),M.mean()]
        A['variance'] = [M.var(axis=0).tolist(),M.var(axis=1).tolist(),M.var()]
        A['standard deviation'] = [M.std(axis=0).tolist(),M.std(axis=1).tolist(),M.std()]
        A['max'] = [M.max(axis = 0).tolist(),M.max(axis=1).tolist(), M.max()]
        A['min'] = [M.max(axis = 0).tolist(),M.max(axis=1).tolist(), M.max()]
        A['sum'] = [M.sum(axis = 0).tolist(),M.sum(axis=1).tolist(), M.sum()]
        return A
    except ValueError:
        print("List must contain nine numbers.")