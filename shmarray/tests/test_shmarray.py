from shmarray import put, get, remove
import numpy as np
from threading import Thread


def test_shmarray():
    remove('foo')
    x = np.arange(5)
    put('foo', x)
    put('foo', x)

    y = get('foo', x.dtype)
    assert isinstance(y, np.ndarray)
    assert (y == np.concatenate([x, x])).all()


def test_threaded():
    remove('foo')
    x = np.arange(5)

    threads = [Thread(target=put, args=('foo', x)) for t in range(100)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    y = get('foo', x.dtype)
    assert (y == np.concatenate([x] * 100)).all()

