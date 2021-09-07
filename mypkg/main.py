import numpy as np
from mypkg.module3.mod3 import func_from_mod3

def test_numpy():
    a = np.arange(15).reshape(3, 5)
    print(a)
    print(a.shape)
    print(a.dtype.name)
    
def run():
    func_from_mod3()
    test_numpy()

if __name__ == "__main__":
    run()