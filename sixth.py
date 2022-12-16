
string = "PQRQRQRQRQRQA" 
substring = "QRQ"


total_str_length=len(string)
total_sub_str_length = len(substring)

cnt = 0
for i in range(0,(total_str_length-1)):
    tmp = string[i:i+total_sub_str_length]
    if tmp == substring:
        cnt+=1
    
print(cnt)