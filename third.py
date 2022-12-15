sentences = ["My name is Ram", "He is a good person", "You should be careful while coding", "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen."]

word_tree = []

for i in sentences:
    tmp = i.split(' ')
    word_tree.append(tmp)


final_res = {}

temp = ''
for i in sentences:
    temp=temp+i+' '

print(temp.count('The'))

for i in word_tree:
    for j in i:
        if j in final_res.keys():
            final_res[j]= temp.count(j+' ')
        else:
            final_res[j]= temp.count(j+' ')

print(final_res)