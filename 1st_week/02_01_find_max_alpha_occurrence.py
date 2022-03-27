def find_max_occurred_alphabet(string):
    string = string.replace(' ','')
    counter={}
    for s in string:
        if s not in counter:
            counter[s]=0
        counter[s]+=1
        # counter = {'s':2, 'g':4}
    max_num=0
    for s in string:
        if counter[s] > max_num:
            max_num=counter[s]
            max_word=s
    return max_word

        




print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", find_max_occurred_alphabet("best of best sparta"))