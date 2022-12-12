# You are given a set A and  other sets.
# Your job is to find whether set A is a strict superset of each of the  sets.

# Print True, if  is a strict superset of each of the n sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.


seta = set([int(i) for i in input().split()])
n = int(input())
setn = set()
list1 = []
for i in range(n):
    setn = set(int(i) for i in input().split())
    if len(seta) > len(setn):
        for j in setn:
            if j not in seta:
                list1.append("False")
                break
        else:
            list1.append("True")
    else:
        list1.append("False")        
if "False" in list1:
    print("False")
else:
    print("True")