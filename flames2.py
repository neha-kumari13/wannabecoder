
name1 = input("Enter first name: ").strip().lower().replace(" ", "")
name2 = input("Enter second name: ").strip().lower().replace(" ", "")

list1 = list(name1)
list2 = list(name2)

for ch in name2:
    if ch in list1:
        list1.remove(ch) 
    else:
        list2.append(ch)  

count = len(list1) + (len(list2) - len(name2)) 

if count == 0:
    count = 1

flames = ["F", "L", "A", "M", "E", "S"]
while len(flames) > 1:
    idx = (count - 1) % len(flames)
    flames.pop(idx)
meanings = {
    "F": "Friends",
    "L": "Love",
    "A": "Affection",
    "M": "Marriage",
    "E": "Enemies",
    "S": "Siblings"
}

print("Result:", meanings[flames[0]])
