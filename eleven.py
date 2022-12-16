wrong_A_P = [2, 5, 8, 11, 15, 17]
wrong_G_P = [3, 9, 27, 81, 244, 729]

A_P_len = len(wrong_A_P)
G_P_len = len(wrong_G_P)

correct_a_p = []
correct_g_p = []

A_progression = 3

for i in range(A_P_len-1):
    if i == A_P_len-1:
        if wrong_A_P[i]-wrong_A_P[i-1] == A_progression:
            correct_a_p.append(wrong_A_P[i])
            break
    else:
        if wrong_A_P[i+1]-wrong_A_P[i] != A_progression:
            tmp = wrong_A_P[i]+A_progression
            correct_a_p.append(wrong_A_P[i])
            wrong_A_P[i+1] = tmp
        else:
            correct_a_p.append(wrong_A_P[i])


print(correct_a_p)

G_progression = 3

for i in range(G_P_len):
    if i == G_P_len-1:
        if wrong_G_P[i]/wrong_G_P[i-1] == G_progression:
            correct_g_p.append(wrong_G_P[i])
            # break
    else:
        if wrong_G_P[i+1]/wrong_G_P[i] != G_progression:
            tmp = wrong_G_P[i]*G_progression
            correct_g_p.append(wrong_G_P[i])
            wrong_G_P[i+1] = tmp
        else:
            correct_g_p.append(wrong_G_P[i])


print(correct_g_p)
