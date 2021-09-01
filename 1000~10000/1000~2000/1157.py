w = input().upper()
uw = list(set(w))  

cnt_list = []
for x in uw:
    cnt = w.count(x)
    cnt_list.append(cnt) 

if cnt_list.count(max(cnt_list)) > 1:   
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list)) 
    print(uw[max_index])