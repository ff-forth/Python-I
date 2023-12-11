from rekursion import pascal
from bdb import Bdb
import sys


class RecursionDetected(Exception):
    pass


class RecursionDetector(Bdb):
    def __init__(self, *args):
        Bdb.__init__(self, *args)
        self.stack = set()

    def user_call(self, frame, argument_list):
        code = frame.f_code
        if code in self.stack:
            raise RecursionDetected
        self.stack.add(code)

    def user_return(self, frame, return_value):
        self.stack.remove(frame.f_code)


def test_recursion(func):
    detector = RecursionDetector()
    detector.set_trace()
    try:
        func()
    except RecursionDetected:
        return True
    else:
        return False
    finally:
        sys.settrace(None)


assert test_recursion(lambda: pascal(4)), "Din funktion är inte rekursiv"
try:
    pascal(4)
except RecursionError:
    print("Din rekursion är oändlig")
    sys.exit(1)

print("Rekursionstest OK- din funktion är rekursiv")
