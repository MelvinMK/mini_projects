def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

def Intersection(lst1, lst2):
    return list(set(lst1).intersection(lst2))


lst1_input = input("Enter elements for list 1: ")
lst1 = list(map(int, lst1_input.split()))


lst2_input = input("Enter elements for list 2: ")
lst2 = list(map(int, lst2_input.split()))

print("List 1:", lst1)
print("List 2:", lst2)

print("The Union of list 1 and list 2 is:", Union(lst1, lst2))
print("The Intersection of list 1 and list 2 is:", Intersection(lst1, lst2))

s = set(lst2)
diff1 = [x for x in lst1 if x not in s]
print("The difference between list 2 and list 1 is:", diff1)

s1 = set(lst1)
diff2 = [x1 for x1 in lst2 if x1 not in s1]
print("The difference between list 1 and list 2 is:", diff2)