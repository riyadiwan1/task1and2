
def most_frequent():
    s = str(input("enter the word ")).lower()
    fq = {}
    for i in s:
        if i in fq:
            fq[i] += 1
        else:
            fq[i] = 1
    for w in sorted(fq, key=fq.get, reverse=True):
        print(w,'=',fq[w])

most_frequent()