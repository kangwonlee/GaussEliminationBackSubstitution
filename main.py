import pprint
from typing import List, Union

Scalar = Union[int, float]
Row = List[Scalar]
Matrix = List[Row]


def back_substitution(Uc:Matrix) -> Row:
    # number of unknowns
    n = len(Uc)
    result = [None] * n

    # last unknown
    result[n-1] = Uc[n-1][n] / Uc[n-1][n-1]

    # row loop from second last to the first unknowns
    for i in range(n-2, 0-1, -1):
        print("result =", result)
        print("i =", i)
        print(f"row Uc[{i}]:", Uc[i])
        s = Uc[i][n]
        print(f"s =", s)

        # column loop
        for j in range(i+1, n-1+1):
            print("j =", j)
            print(f"s <- {s} - (result[{j}] = {result[j]}) * (Uc[{i}][{j}] = {Uc[i][j]})")
            s += (-1) * result[j] * Uc[i][j]
            print(f"s = {s}")
        print(f"new result = {s}/{Uc[i][i]}")
        result[i] = s / Uc[i][i]

    return result


def main():
  matUc = [
    [2, 1, 2, 1, 6],
    [0.0, -9.0, 0.0, 9.0, 18.0],
    [0.0, 0.0, -1.0, -4.0, -11.0],
    [0.0, 0.0, 0.0, 13.0, 39.0]
  ]

  print('before calling back_substitution()')
  pprint.pprint(matUc)
  result = back_substitution(matUc)
  print('after calling back_substitution()')
  print('result =', result)


if "__main__" == __name__:
  main()
