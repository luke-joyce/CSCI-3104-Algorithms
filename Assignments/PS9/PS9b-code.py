
##Code for Q2 part b

def choose_assignments(array):

    ##initiate array to store values bottom up
    Assignments = []
    for i in range(len(array)):
        if i == 0:
            Assignments.append(array[i])
        elif i == 1:
            Assignments.append(max(array[i], array[i - 1]))
        else:
            Assignments.append(max(Assignments[i - 2] + array[i], Assignments[i - 1]))
    return Assignments[-1]


array_1 = [9, 11, 12, 9, 11, 10]
print(choose_assignments(array_1))



##Code for Q2 part c
def choose_assignments_2(array):
    ##Initiate 3 variables for P - 1, P - 2 and the current val
    P2 = 0
    P1 = 0
    P0 = 0
    for i in range(len(array)):
        if i == 0:
            P2 = array[i]
            P1 = array[i]
            P0 = array[i]
        elif i == 1:
            P0 = max(P1, array[i])
            P1 = P0
        else:
            P0 = max(P2 + array[i], P1)
            P2 = P1
            P1 = P0
    return P0


array_2 = [9, 11, 12, 9, 11, 10]
print(choose_assignments_2(array_2))


