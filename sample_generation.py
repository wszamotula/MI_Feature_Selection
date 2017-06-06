import random
import numpy

def main():
    N = 10000
    data = open('synthdata.txt', 'w')
    labels = open('synthdata_labels.txt', 'w')

    data.truncate()
    labels.truncate()

    #data_array = []
    #label_array = []

    for i in range(N):
        y = numpy.random.binomial(1, 0.5)
        x1 = numpy.random.normal(y, 1.0)
        x2 = numpy.random.normal((x1 + y) / 2, 1.0)
        x3 = numpy.random.normal((x2 + y) / 2, 1.0)
        x4 = numpy.random.normal((x3 + y) / 2, 1.0)
        x5 = numpy.random.normal((x4 + y) / 2, 1.0)
        x6 = numpy.random.normal((x5 + y) / 2, 1.0)
        x7 = numpy.random.normal((x6 + y) / 2, 1.0)
        x8 = numpy.random.normal((x7 + y) / 2, 1.0)
        x9 = numpy.random.normal((x8 + y) / 2, 1.0)
        #data_array.append([x1, x2, x3, x4, x5, x6, x7, x8, x9])
        #label_array.append(y)

        data.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(x1, x2, x3, x4, x5, x6, x7, x8, x9))
        labels.write("{}\n".format(y))

    #mutual_information(data_array, label_array)

    return


def mutual_information(data, labels):
    return


if __name__ == "__main__":
    main()