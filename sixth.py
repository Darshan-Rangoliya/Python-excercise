string = "PQRQRQRQRQRQA"
substring = "QRQ"

str_length = len(string)
sub_str_length = len(substring)

cnt = 0
for index in range(0, (str_length-1)):
    tmp = string[index : index + sub_str_length]
    if tmp == substring:
        cnt += 1

print(cnt)
