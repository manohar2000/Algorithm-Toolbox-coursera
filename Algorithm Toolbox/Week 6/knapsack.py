import numpy

def maxGold(W, n, item_list):
    val = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            val[i][j] = val[i][j-1]
            if item_list[j-1]<=i:
                temp = val[i-item_list[j-1]][j-1] + item_list[j-1]
                if temp > val[i][j]:
                    val[i][j] = temp

    return (int(val[W][n]), val)

def printItems(val, item_list, i, j, arr):
    if i == 0 and j == 0:
        arr.reverse()
        return arr
    if val[i][j] == val[i][j-1]:
        arr.append(0)
        return printItems(val, item_list, i, j-1, arr)
    else:
        arr.append(1)
        return printItems(val, item_list, i-item_list[j-1], j-1, arr)
        
if __name__ == '__main__':
    W, n               = [int(i) for i in input().split()]
    item_weights       = [int(i) for i in input().split()]
    max_weight, Matrix = maxGold(W, n, item_weights)
    bool_vector      = printItems(Matrix, item_weights, W, n, [])
    optimal = [str(j) for i, j in enumerate(item_weights) if bool_vector[i]]
    print(f"Weights in knapsack of capacity {W}: {' '.join(optimal)}")
