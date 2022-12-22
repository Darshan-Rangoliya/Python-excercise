def arithmatic_progression_fun(arthmetic_list,ap):
    A_P_len = len(arthmetic_list)
    for index in range(A_P_len-1):
        if arthmetic_list[index+1] - ap != arthmetic_list[index]:
            arthmetic_list[index+1] = arthmetic_list[index] + ap
    print(arthmetic_list)

def geometric_progression_fun(geometric_list,gp):
    G_P_len = len(geometric_list)
    for index in range(G_P_len-1):
        if geometric_list[index+1] / gp != geometric_list[index]:
            geometric_list[index+1] = geometric_list[index] * gp
    print(geometric_list)

wrong_A_P = [2, 5, 8, 11, 15, 17]
wrong_G_P = [3, 9, 27, 81, 244, 729]

arithmatic_progression_fun(wrong_A_P,3)
geometric_progression_fun(wrong_G_P,3)