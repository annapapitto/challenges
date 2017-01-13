"""
Solution to first challenge, Upvotes, at www.quora.com/challenges.
Please run with python3.
"""

def get_inputs():
    try:
        n, k = list(map(int, input().split()))
        assert n > 0 and k > 0
        upvotes = list(map(int, input().split()))
        assert len(upvotes) == n
        return n, k, upvotes
    except:
        print("Bad inputs.")
        exit()

def run():
    n, k, upvotes = get_inputs()
    totals_non_dec, totals_non_inc = get_totals(n, k, upvotes)

    num_totals = n - k + 1
    use_totals = list(zip(totals_non_dec, totals_non_inc))[:num_totals]

    [ print(nd - ni) for (nd, ni) in use_totals ]
    exit()

def get_totals(n, k, upvotes):
    non_inc, non_dec = 0, 0
    totals_non_inc = [ 0 ] * n
    totals_non_dec = [ 0 ] * n

    for day in range(len(upvotes) - 1):
        cur = upvotes[day]
        nxt = upvotes[day+1]
        non_dec += 1
        non_inc += 1

        if cur < nxt:
            non_inc = 0
        elif cur > nxt:
            non_dec = 0

        for size in range(1, k):
            begin = day + 1 - size
            if begin >= 0:
                totals_non_dec[begin] += min(size, non_dec)
                totals_non_inc[begin] += min(size, non_inc)

    return totals_non_dec, totals_non_inc

run()
