n = int(input("Enter number of training examples: "))

data = []

for i in range(n):
    print(f"\nExample {i+1}")
    a1 = input("Attribute 1: ")
    a2 = input("Attribute 2: ")
    a3 = input("Attribute 3: ")
    c = input("Class (Yes/No): ")
    data.append([a1, a2, a3, c])

h = None

for row in data:
    if row[-1] == "Yes":
        if h is None:
            h = row[:-1]
        else:
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = "?"

print("\nMost Specific Hypothesis:", h)
