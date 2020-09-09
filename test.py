# dic = {"hi": 3, "bye": 1, "yes": 2}
# number_of_selected_employees = len(dic) + 1
# l = []
# for i in range(1, number_of_selected_employees):
#     for e, pos in dic.items():
#         if i == pos:
#             l.append(e)

# print(l)


abc=['q','a','bg','hj']
num=[1,3,2,4]
doc_dic={}
l=[]
for i in range(0,len(abc)):
    doc_dic[abc[i]] = num[i]
print(doc_dic)
for n in range(0, len(abc)+1):
    for e, pos in doc_dic.items():
        if n == pos:
            l.append(e)

print(l)
