def is_isomorphic(s, t):
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

print(is_isomorphic("egg", "add"))
print(is_isomorphic("foo", "bar"))
