from cache import *

def test_cache():
    # cache = Cache()
    assert slow_function(1) == 1
    assert slow_function(2) == 2
    assert len(cache.data) == 2