def rem_dup(dup):
    res = []
    [res.append(n) for n in dup if n not in res]
    return res