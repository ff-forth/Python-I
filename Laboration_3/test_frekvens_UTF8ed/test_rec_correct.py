import sys
from rekursion import pascal

RESULTS = [[1],
           [1, 1],
           [1, 2, 1],
           [1, 3, 3, 1],
           [1, 4, 6, 4, 1],
           [1, 5, 10, 10, 5, 1],
           [1, 6, 15, 20, 15, 6, 1],
           [1, 7, 21, 35, 35, 21, 7, 1],
           [1, 8, 28, 56, 70, 56, 28, 8, 1],
           [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]
try:
    for i in range(10):
        assert pascal(
            i) == RESULTS[i], f"pascal({i}) gav fel resultat, det borde varit {RESULTS[i]}, men blev {pascal(i)}"
except AssertionError as error:
    print("Fel: ", error)
    sys.exit(1)
else:
    print("Resultat OK - Din funktion räknar rätt!")
