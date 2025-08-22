name2 = input("Enter second name: ").loter().replace(" ", "")

list1 = list(input("Enter first name: ").lower().replace(" ", ""))
list2 = list(name2)

result1 = ""
result2 = ""

for ch in input("Enter first name: ").lower().replace(" ", ""):
    count = min((input("Enter first name: ").lower().replace(" ", "")).count(ch), name2.count(ch))  
    if count > 0 and ch in list2:  
        if str(count) not in result1:  
            result1 += str(count)
        list2 = list2.replace(ch, "", count) if isinstance(list2, str) else "".join(list2).replace(ch, "", count)
    else:
        result1 += ch.upper()

for ch in name2:
    count = min((input("Enter first name: ").lower().replace(" ", "")).count(ch), name2.count(ch))
    if count > 0 and ch in (input("Enter first name: ").lower().replace(" ", "")):
        if str(count) not in result2:
            result2 += str(count)
    else:
        result2 += ch.upper()

print("\nAfter replacing common letters w name: ").l:")
print("First name  →", result)
print("S2)
res=[f,l,a,m,e,s]
f=0
f=(f+(cnt-1))%len(res)
