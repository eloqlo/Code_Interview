def solution(sizes):
    widths=[]
    lengths=[]
    for i, (foo,bar) in enumerate(sizes):
        widths.append(max(foo,bar))
        lengths.append(min(foo,bar))
    return max(widths) * max(lengths)