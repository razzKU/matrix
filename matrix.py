
limit = int(input("Enter the Dimension: "))
if limit > 3:
    data = limit + 2
    last = limit + 1
    matrix = []

    for i in range(data):
        a = []
        for j in range(data):
            if i == 0 or i == last or j == 0 or j == last:
                a.append(0)
            else:
                a.append(int(input(f"Enter [{i}][{j}]th element: ")))
        matrix.append(a)

    print("\nThe Matrix is: \n")
    for i in range(1, limit + 1):
        for j in range(1, limit + 1):
            print(matrix[i][j], end="\t")
        print()

    k_limit = limit * limit
    # print(k_limit, end="k_limit====================================================================")
    k_matrix = []
    n = 1
    k_r = 1
    j_value = 1
    for k in range(1, k_limit + 1):
        # print(j_value, end="j_value==================")
        sum = 0
        avg = 0
        for i in range(k_r - 1, k_r + 2):
            for j in range(j_value - 1, j_value + 2):
                # print(matrix[i][j], end="\t\t helloo\n")
                sum = sum + matrix[i][j]
                avg = round(sum / 9, 1)
        k_matrix.append(str(avg))
        j_value = j_value + 1
        if k == limit * n:
            n = n + 1
            k_r = k_r + 1
            j_value = 1
            # print(n * limit, end="\t\tn*limit")
    print("\nThe new Matrix is: \n")
    n = 1
    for i in range(k_limit):
        if i == n * limit:
            print("\n")
            n = n + 1
        print(k_matrix[i], end="\t\t")

else:
    print("Please enter the Dimension greater than 3 :)")


