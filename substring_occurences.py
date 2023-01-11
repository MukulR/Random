def count_substring(string, substring):
    j = 0
    count = 0
    for i in range(len(string)):
        if substring[j] == string[i]:
            j += 1
            if j == len(substring):
                count += 1
                j = 0
        else:
            j = 0
    
    print(count)

count_substring("aaaa", "a")