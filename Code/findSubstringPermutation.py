def findSubstringPermutations(sub, longer):
    perms = []
    permutate("", sub, perms)

    print(longer + " contains these permutations of " + sub + ":")
    for i in range(len(longer)-len(sub)):
        window = longer[i:i+len(sub)]
        if window in perms:
            print(window)

def permutate(prefix, s, perms):
    for i in range(len(s)):
        perm = prefix + s[i] + s[:i] + s[i+1:]
        if perm not in perms:
            perms.append(perm)
        permutate(prefix+s[i], s[:i]+s[i+1:], perms)
