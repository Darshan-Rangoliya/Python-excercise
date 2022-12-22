wrong_A_P = [2, 5, 8, 11, 15, 17]
wrong_G_P = [3, 9, 27, 81, 244, 729]

A_P_len = len(wrong_A_P)
G_P_len = len(wrong_G_P)

A_progression = 3
G_progression = 3

for index in range(A_P_len-1):
    if wrong_A_P[index+1] - A_progression != wrong_A_P[index]:
        wrong_A_P[index+1] = wrong_A_P[index] + A_progression

print(wrong_A_P)

for index in range(G_P_len-1):
    if wrong_G_P[index+1] / G_progression != wrong_G_P[index]:
        wrong_G_P[index+1] = wrong_G_P[index] * G_progression

print(wrong_G_P)