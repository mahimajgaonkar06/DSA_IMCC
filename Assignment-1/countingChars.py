s=input("enter a sentence: ")
vowels=['a','e','i','o','u','A','E','I','O','U']
conso=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z',
        'B','C','D','J','F','G','H','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
Digits=['0','1','2','3','4','5','6','7','8','9']
countV=0
countC=0
countD=0
countChar=0

for i in s:
        if i in vowels:
                countV+=1
        elif i in conso:
                countC+=1
        elif i in Digits:
                countD+=1
        else:
                countChar+=1

print("vowels: ",countV)
print("consonants: ",countC)
print("digits: ",countD)
print("special Character: ",countChar)

# problems faced in this program: 
# 1. list must be in string as we are excepting input in string other wise digits wont be counted
# if i==vowels cant happen, when we are comparing with list we must use 'in' operator

    