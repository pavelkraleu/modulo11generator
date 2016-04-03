def ismodulo11(number):
    if len(str(number)) != 8:
        return "number is too long"
    else:
        presum =[]
        position = len(number) -1
        """There is a problem wiht banc account lenght,
        position 7 starts at 4 and goes further to 8, but if
        the bacn account is 9, we should start with 2 """
        weight = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
        list_number = map(int, str(number))
        #map runs function on every piece of sting, whe
        for n in list_number:
          presum.append(n * weight[position])
          position -= 1
        if sum(presum) % 11 == 0:
            return True
        else:
            return False
            
seed = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]
pairs = []
accounts = []

for n in seed:
    #at this level we have choosen 00
    for m in seed:
        #at this level we are choosing another pair to 11
        pair = []
        pair.append(n)
        pair.append(m)
        if n != m:
            pairs.append(pair)

#assuem you have bank account ["11","22"], LOOK at permutation

for n in pairs:
#at this point i have choosen bank pair
    for first in n:
        for second in n:
            for third in n:
                for fourth in n:
                    num = first + second + third + fourth
                    if ismodulo11(num) and num[0] != "0":
                        accounts.append(num)
                    '''for fifth in n: 
                        num2 = first + second + third + fourth + fifth
                        if ismodulo11(num2) and num2[0] != "0" and not num2 in accounts:
                            accounts.append(num2)'''
print accounts