
def pageCount(n, p):
    return 0 if p == 1 else 1 if n % 2 == 0 and (n - p) == 1 else int(min([p/2, n/2-p/2]))

                    

