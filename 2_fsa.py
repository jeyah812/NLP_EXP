def ends_with_ab(s):
    state = 0
    for ch in s:
        if state == 0:
            state = 1 if ch == 'a' else 0
        elif state == 1:
            state = 2 if ch == 'b' else 1 if ch == 'a' else 0
        elif state == 2:
            state = 1 if ch == 'a' else 0
    return state == 2

print(ends_with_ab("cab"))