str1=input('输入字符串')
str1=str1.lower()
a=[]
def strSort(words):
    tempword = words
    for i in range(2**len(words)):
        int_bin = str(bin(i)).replace("0b","")
        for i in range(len(words)-len(int_bin)):
            int_bin = "".join(("0",int_bin))
        for index, i in enumerate(int_bin):
            if i=='1':
                wordslst = list(words)
                wordslst[index] = wordslst[index].upper()
                words = "".join(wordslst)
        yield words
        words = tempword

for word in strSort(str1):
    a.append(word)
a=set(a)
b='\n'.join(a)
print(b)
