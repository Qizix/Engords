def read_base(base_way):
    base = open(base_way, 'r', encoding='utf-8')
    pair = []
    word = base.read().split()
    i = 0
    t = 0
    while i < len(word):
        pair.append([word[i], word[i+1]])
        i += 2
        t += 1
    return pair