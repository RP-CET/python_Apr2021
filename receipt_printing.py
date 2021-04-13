company = "ABC Pte Ltd"
print (" " * (18-len(company)//2) + company)
print ()

items = ["apples", "oranges", "Japanese Honeydew"]
prices = [3.55, 7.34, 66.55]

for i in range(3):
    #print (str(items[i]) + str(prices[i]))
    
    line = "%-25s $%10.2f" % (items[i].upper(), prices[i])
    print (line)

print (" " * 27 + "=" * 10)    
print (" " * 26  + "$%10.2f" % (sum(prices)))