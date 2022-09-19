# bill is array of item prices
# k is anything anna declines
# b is amount bill charged anna for 1/2 of bill
bill = [3, 10, 2, 9]

def bonAppetit(bill, k, b):
    del bill[k]
    what_anna_pays = sum(bill) / 2
    if b != what_anna_pays:
        return int(b - what_anna_pays)
    return 'Bon Appetit'
    
print(bonAppetit(bill, 1, 7))
