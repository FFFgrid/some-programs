def quicksort(seq):
    if len(seq) < 2:
        return seq
    else:
        base = seq[0]
        left = [elem for elem in seq[1:] if elem < base]
        right = [elem for elem in seq[1:] if elem > base]
        return quicksort(left) + [base] + quicksort(right)
