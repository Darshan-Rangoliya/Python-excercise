sentences = ["My name is Ram", "He is a good person", "You should be careful while coding", "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen."]

word_tree = [sentence.split(' ') for sentence in sentences]

final_res = {}

temp = ''
for string in sentences:
    temp=temp+string+' '

for word_list in word_tree:
    for word in word_list:
        if word in final_res.keys():
            final_res[word]= temp.count(word+' ')
        else:
            final_res[word]= temp.count(word+' ')

print(final_res)