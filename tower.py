li = []
total=0
def prod_prices():
    for i in range(8) :
     a = int(input())
     li.append(a)

def total_prices(total):
    for i in range(8):
     total = total + li[i]
    
prod_prices()
print(li)
total_prices(total)
print(total)


