

def find_prime_list_under_number_1(number):
    lst=[]
    for i in range(2,number+1):
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            lst.append(i)
    return lst

def find_prime_list_under_number_2(number):
    lst=[]
    for i in range(2,number+1):
        for j in range(2,i):
            if i%j == 0 and j*j <= i:
                break
        else:
            lst.append(i)
    return lst

print(find_prime_list_under_number_1(20))
print(find_prime_list_under_number_2(20))
