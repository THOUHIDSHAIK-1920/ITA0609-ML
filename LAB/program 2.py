import pandas as pd

data = pd.read_csv("training.csv")

S = list(data.iloc[0, :-1])
G = ["?"] * len(S)

for _, row in data.iterrows():
    if row[-1] == "Yes":
        for i in range(len(S)):
            if S[i] != row[i]:
                S[i] = "?"
    else:
        for i in range(len(G)):
            if row[i] != S[i]:
                G[i] = S[i]

print("Specific Hypothesis:", S)
print("General Hypothesis:", G)
