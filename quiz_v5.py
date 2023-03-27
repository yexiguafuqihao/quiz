def count_words():

    line = input('Input sentence: ')
    words = line.split(' ')
    freqs, records = [],[]
    for s in words:
        s = clean(s)
        if s not in records:
            records.append(s)
            freqs.append([s, 1])
        else:
            n = len(records)
            pos = -1
            for i in range(n):
                if s == records[i]:
                    pos = i
                    break
            freqs[pos][1] += 1
    
    records.sort()
    high = 0
    for freq in freqs:
        if high < freq[1]:
            high = freq[1]

    results = []
    for k in records:
        for freq in freqs:
            if k == freq[0]:
                results.append(freq)
    
    print('Frequency: {}'.format(results))
    for freq in results:
        k, num = freq
        if num >= high:
            print('{:<15}{:>3}'.format(k, num))

def clean(s):

    s = s.lower()
    if len(s) < 1:
        return ''
    n, i = len(s), 0
    while i < n and s[i].isalpha():
        i += 1
    return s[:i]
    
if __name__ =='__main__':

    count_words()