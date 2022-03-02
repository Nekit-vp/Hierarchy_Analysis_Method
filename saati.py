from re import T
import numpy as np

def vector(matrix):
    newMatrix = np.zeros(len(matrix))
    matSum = np.zeros(len(matrix))
    for i in range(0, len(matrix)):
        vect = matrix[:, i]
        w = vect / vect.sum()
        for j in range(0, len(matrix)):
            matSum[j] += w[j] 
    matSum = matSum / len(matrix)
    return matSum

def matrix(number):
    """Function for creating a pairwise matrix"""
    A = np.ones([number, number])
    importance = [i for i in range(1, 10)] # list of allowed importance values
    importance2 = [i/10 for i in range(1, 10)]
    value = importance + importance2
    for i in range(0, number):
        for j in range(0, number):
            if i < j:
                a = str(input(f'How much more important {i+1} than {j+1}? Type an integer from 0.1 to 9: '))
                if float(a) in value: # error handling
                    A[i,j] = float(a)
                    A[j, i] = 1 / float(a)
                else:
                    print("It is an incorrect value. Let's start again \n")
                    main()
    return A

def main():

    numberCrit = str(input("How many criteria do you want to enter? Type an integer: "))
    if numberCrit.isdigit(): # error handling
        A = matrix(int(numberCrit))
        print(A)
        weights = vector(A)
        for i in range(len(weights)):
            print(f'Criterion {i} = {np.round(weights[i], 2)}')
    else:
        print("Something went wrong. Let's try again \n")
        main()

    numberAlt = str(input("How many alternativ do you want to enter? Type an integer: "))
    if numberAlt.isdigit(): # error handling
        leftTable = np.zeros([int(numberAlt),int(numberCrit)])
        print(leftTable)
        for i in range(0, int(numberCrit)):
            print(f'table  {i+1}' )
            A = matrix(int(numberAlt))
            print(A)
            leftTable[:, i] = vector(A)
        print()
        print("Table of indicators of selected alternatives:")
        print(leftTable)
    else:
        print("Something went wrong. Let's try again \n")
        main()
    
    result = np.matmul(leftTable, weights)
    print()
    print(result)
    print()
    for i in range(len(result)):
            print(f'Alternative {i} = {np.round(result[i], 2)}')


if __name__ == "__main__":
    main()