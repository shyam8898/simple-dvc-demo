import pytest

class NotInRange(Exception):
    def __init__(self, message="value not in range"):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a=5
    # can pass ValeError to test it is not in range
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange