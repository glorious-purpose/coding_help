"""Print letters that intersect.
    Original code:
        if len(left) >= len(right):
            for i in range(len(right)):
                if left[i] in right[i]:
                    print(left[i])
        elif len(left) < len(right):
            for i in range(len(left)):
                if right[i] in left[i]:
                    print(right[i])
"""
left = "This is a test."
right = "Tarsnips wheeee"

for i in range(min(len(left), len(right))):
    if left[i] == right[i]:
        print((left[i]))
