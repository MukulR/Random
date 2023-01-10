def permute(chars):
    permutations = []
    if len(chars) == 1:
        return [chars.copy()]
    
    for i in range(len(chars)):
        cur = chars.pop(0)
        branches = permute(chars)

        for branch in branches:
            branch.append(cur)
        
        permutations.extend(branches)
        chars.append(cur)
    return permutations

print(permute(['a','b','c', 'd']))