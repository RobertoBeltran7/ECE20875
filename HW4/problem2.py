
def stencil(data, f, width) :
    """
    perform a stencil using the filter f with width w on list data
    output the resulting list
    note that if len(data) = k, len(output) = k - width + 1
    f will accept as input a list of size width and return a single number
    :param data: list
    :param f: function
    :param width: int
    :return: list
    """
    #Fill in
    l=[]

    for i,j in enumerate(data):
        if len(l) == len(data)-width+1:
            break
        l.append(f(data[i:i+width]))

    return l

def createBox(box) :
    """
    create a box filter from the input list "box"
    this filter should accept a list of length len(box) and return a simple
    convolution of it.
    the meaning of this box filter is as follows:
    for each element the input list l, multiple l[i] by box[i]
    sum the results of all of these multiplications
    return the sum
    So for a box of length 3, filter(l) should return:
      (box[0] * l[0] + box[1] * l[1] + box[2] * l[2])
    The function createBox returns the box filter itself, as well as the length
    of the filter (which can be passed as an argument to conv)

    :param box: list
    :return: function, int
    """
    #Fill in
    def boxFilter(l) :
        # Fill in
        if len(l) != len(box):
            print("Calling box filter with the wrong length list. Expected list of length", len(box))
        sum=0
        for i in range(len(l)):
            sum=sum+box[i]*l[i]

        return sum

    return boxFilter, len(box)
        
if __name__ == '__main__' :    
    def movAvg(l) :
        if (len(l) != 3) :
            print(len(l))
            print("Calling movAvg with the wrong length list")
            exit(1)
        return float(sum(l)) / 3
    
    def sumSq(l) :
        if (len(l) != 5) :
            print("Calling sumSq with the wrong length list")
            exit(1)
        return sum([i ** 2 for i in l])
    
    
    data = [2, 5, -10, -7, -7, -3, -1, 9, 8, -6]
    
    print(stencil(data, movAvg, 3))
    print(stencil(data, sumSq, 5))
    
    #note that this creates a moving average!
    boxF1, width1 = createBox([1.0 / 3, 1.0 / 3, 1.0 /3])
    print(stencil(data, boxF1, width1))
    
    boxF2, width2 = createBox([-0.5, 0, 0, 0.5])
    print(stencil(data, boxF2, width2))
