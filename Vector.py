# Following lessons of Khan Academy and apply it in python


# Check Real Coordinate space
def dimension(vector):
    return len(vector)


def add_vector(vector1, vector2):
    if not (len(vector1) == len(vector2)):
        print("Cannot add this vectors")
        return -1

    result = []
    for i in range(0, len(vector1)):
        result.append(vector1[i] + vector2[i])

    return result


def multiply_by_scalar(vector1, scalar=1):
    for i in range(0, len(vector1)):
        vector1[i] = vector1[i] * scalar


def represent_by_basis_2d(vector1):
    print(vector1[0] + "i + " + vector1[1] + "j")


# basis vector
i_basis = [1, 0]
j_basis = [0, 1]

v1 = [0, 2]
v2 = [1, 3]

print(dimension(v1))
print(add_vector(v1, v2))
print(v1)
multiply_by_scalar(v1, 2)
print(v1)
