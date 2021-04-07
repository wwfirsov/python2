def m_table(a, b):
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            print(x, '*', y, '=', x * y)

m_table(3, 3)