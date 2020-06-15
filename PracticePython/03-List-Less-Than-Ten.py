if __name__ == "__main__":
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # Initial exercise
    for x in a:
        if x < 5:
            print(x)
    
    # Extra 1
    b = []
    for x in a:
        if x < 5:
            b.append(x)
    print(b)

    # One-liner (not my work)
    print([b for b in a if b < 5])