
# Proejct Euler 51
def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1
import itertools
primes = list(itertools.islice(gen_primes(), 100000))
print(primes)

def checkFriends(p,q): # Assume p and q have same length and q > p
    diffs = [int(str(q)[i])-int(str(p)[i]) for i in range(len(str(p)))]
    # print(p,q,diffs)
    if len(set(diffs)) == 2 and 0 in diffs:
        # print(p, q, q-p, diffs, [k for k in range(len(str(p))) if diffs[k] != 0])
        return True, [k for k in range(len(str(p))) if diffs[k] != 0]

    else:
        return False, []
    # p_str = str(p)
    # q_str = str(q)
    # diff = [i for i in range(len(str(p))) if str(p)[i] != q_str[i]]
    # p_diff = set([p_str[i] for i in diff])
    # q_diff = set([q_str[i] for i in diff])
    #
    # if len(p_diff) == 1 and len(q_diff) == 1:
    #     return True, diff
    # else:
    #     return False, []

foundIt = False
myBigDict = {}
for i in range(len(primes)):
    p = primes [i]
    # print(f"*** {p} ***")
    p_dict = {}
    for j in range(i+1, len(primes)):
        q = primes[j]
        if len(str(q)) > len(str(p)):
            break
        result, indices = checkFriends(p, q)
        if result == True:
            # indices.sort()
            p_dict[tuple(indices)] = p_dict.get(tuple(indices),[]) + [q]
    # print(p_dict)
    for tup in p_dict:
        if len(p_dict[tup]) >= 5:
            print(len(p_dict[tup]), p, tup, p_dict[tup])
            if len(p_dict[tup]) >= 7:
                foundIt = True
    if foundIt:
        break

