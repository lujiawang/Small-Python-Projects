# squares = []
# for i in range(11):
#     squares.append(i**2)
# print("squares", squares)
#
# x = squares[2:5]
# print("x", x)
#
# y = [x**2 for x in range(11) if x % 2 == 0 ]
# print("y", y)
#
# z = [0]*10
# print("z", z)
#
# x = [[0] * 5 for i in range(5)]
# print("x", x)
# x[0][0] = 42
# print("x", x)

#prints the matrix m. For example, the matrix:
#[[1, 0, 1], [2, 1, 0], [2, 3, 0]]
#would be printed as

#  1 0 1
#  2 1 0
#  2 3 0

def pretty_print_matrix(m):
    for row in m:
        for entry in row:
            print(entry, end = " ")
        print("")


pretty_print_matrix([[1, 0, 1], [2, 1, 0], [2, 3, 0]])
        
# Returns a matrix of all 0s with dimensions rows by columns.
# You should do this in one line, using a list comprehension
def create_0_matrix(rows, cols):
       print([[0]*cols]*rows)
    

create_0_matrix(5,4)

# m and n are lists of the same length representing vectors.
# Returns the dot product of m and n.
def dot_product(m, n):
    i = 0
    sum = 0
    while i < len(m):
        sum += m[i] * n [i]
        i+=1
    print(sum)


dot_product([2]*2,[3]*2)


# Returns the transpose of the matrix m.
def transpose(m):
    for i in range(0,len(m)):
        for j in range(0,i):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    print(m)


transpose([[1, 0, 1], [2, 1, 0], [2, 3, 0]])


#precondtion: m and n are matrices of the same size.
#returns a matrix that is m + n
def add_matrices(m, n):
    for i in range(0,len(n)):
        for j in range(0,len(n[i])):
            m[i][j] += n[i][j]
    print(m)


add_matrices([[1, 0, 1], [2, 1, 0]],[[1, 0, 1], [2, 3, 0]])


# precondition: the number of columns in m is equal to the
# number of rows in n
#returns a matrix that is m x n   
def mult_matrices(m, n):
    i = len(m)
    j = len(m[0])
    k = len(n[0])
    result = []
    for iindex in range(0,i):
        temp = []
        for kindex in range(0,k):
            sum = 0
            for jindex in range(0,j):
                sum += m[iindex][jindex]*n[jindex][kindex]
            temp.append(sum)
            print("temp",temp)
        result.append(temp)
    print("multi",result)
    return result


mult_matrices([[0,1,2,3],[4,5,6,7]],[[8,0],[9,0],[10,0],[11,0]],)


# returns a copy of matrix m
def copy_matrix(m):
    result = []
    for i in range(0,len(m)):
        temp = []
        for j in range(0,len(m[i])):
            print("i",i,"j",j)
            temp.append(m[i][j])
        result.append(temp)
        print("r",result)
    return result


copy_matrix([[0,1,2,3],[4,5,6,7]])


# returns a matrix of size m * m, with 1s on the main diagonal and 0s elsewhere
def identity_matrix(size):
    result = []
    for i in range(0,size):
        temp = []
        for j in range(0,size):
            if(i==j):
                temp.append(1)
            else:
                temp.append(0)
        result.append(temp)
    print(result)


identity_matrix(5)

# returns a matrix that is m^power. Note that m^0 is the identity matrix and
#m^1 = m
def power_matrix(m, power):
    if power == 0:
        identity_matrix(len(m))
    elif power == 1:
        print(m)
    else:
        result = copy_matrix(m)
        for i in range(0,power-1):
            print(result,"m",m)
            temp = mult_matrices(result,m)
            result = copy_matrix(temp)
        print(result)


power_matrix([[0,1],[4,5]],3)
        
    


            
                       
        
    
