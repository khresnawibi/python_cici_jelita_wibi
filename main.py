import numpy as np


def matrix(judul, data):
    result = np.array(data)

    print(str(judul))
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(matrix('Hasil Keaktifan',
                 [[0, 1, 0.5, 0, 1, 0.5],
                  [1, 0, 0.5, 1, 0, 0.5],
                  [0.5, 0.5, 0, 0.5, 0.5, 0],
                  [0, 1, 0.5, 0, 1, 0.5],
                  [1, 0, 0.5, 1, 0, 0.5],
                  [0.5, 0.5, 0, 0.5, 0.5, 0]]))

    print(matrix('Hasil Nilai UAS',
                 [[0, 30, 10, 5, 2, 15],
                  [30, 0, 40, 25, 32, 5],
                  [10, 40, 0, 15, 8, 25],
                  [5, 25, 15, 0, 7, 10],
                  [2, 32, 8, 7, 0, 17],
                  [15, 5, 25, 10, 17, 0]]))

    print(matrix('Hasil Indeks',
                 [[0, 1, 1, 0, 0, 1],
                  [1, 0, 1, 1, 1, 1],
                  [1, 1, 0, 1, 1, 1],
                  [0, 1, 1, 0, 0, 1],
                  [0, 1, 1, 0, 0, 1],
                  [1, 1, 1, 0, 1, 0]]))

    print(matrix('Hitung similarity semua object'
                 'dimana d(f)ij=1',
                 [[0, 10.66, 3.83, 1.66, 1, 5.5],
                  [10.66, 0, 13.83, 9, 11, 2.16],
                  [3.83, 13.83, 0, 5.5, 3.16, 8.66],
                  [1.66, 9, 5.5, 0, 2.66, 3.5],
                  [1, 11, 3.16, 2.66, 0, 6.16],
                  [5.5, 2.16, 8.66, 3.5, 6.16, 0]]))
