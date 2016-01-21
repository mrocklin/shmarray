import posix_ipc
import os
import numpy as np
from threading import Lock


locks = {}

def get_lock(addr):
    try:
        return locks[addr]
    except KeyError:
        locks[addr] = Lock()
        return locks[addr]


def remove(addr):
    """ Remove shared memory bucket """
    try:
        with get_lock(addr):
            posix_ipc.unlink_shared_memory(addr)
    except posix_ipc.ExistentialError:
        pass

def put(addr, x):
    """ Put numpy array bytes into shared memory bucket """
    with get_lock(addr):
        f = posix_ipc.SharedMemory(addr, flags=posix_ipc.O_CREAT, read_only=False)
        ff = os.fdopen(f.fd, 'ab')
        ff.write(x.data)
        ff.close()

def get(addr, dtype):
    """ Get numpy array from shared memory bucket and dtype """
    f = posix_ipc.SharedMemory(addr, read_only=True)
    ff = os.fdopen(f.fd, 'rb')
    dt = np.dtype(dtype)
    x = np.memmap(ff, shape=f.size / dt.itemsize, dtype=dt, mode='r')
    return x
