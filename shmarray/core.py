import posix_ipc
import os
import numpy as np


def remove(addr):
    """ Remove shared memory bucket """
    try:
        posix_ipc.unlink_shared_memory(addr)
    except posix_ipc.ExistentialError:
        pass

def put(addr, x):
    """ Put numpy array bytes into shared memory bucket """
    f = posix_ipc.SharedMemory(addr, flags=posix_ipc.O_CREAT, read_only=False)
    ff = os.fdopen(f.fd, mode='ab')
    ff.write(x.data)
    ff.close()

def get(addr, dtype):
    """ Get numpy array from shared memory bucket and dtype """
    f = posix_ipc.SharedMemory(addr, read_only=True)
    ff = os.fdopen(f.fd, mode='rb')
    dt = np.dtype(dtype)
    x = np.memmap(ff, shape=f.size / dt.itemsize, dtype=dt, mode='r')
    return x
