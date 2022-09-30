def time_required_to_buy_brute(tickets, k):
    counter = 0
    target = tickets[k]
    while target > 0:
        for i in range(len(tickets)):
            if tickets[i] != 0:
                tickets[i] -= 1
                counter += 1
            if tickets[k] == 0:
                break
        target -= 1
    return counter


def time_required_to_buy_one_pass(tickets, k):
    n = len(tickets)
    result = tickets[k]

    for i in range(n):
        if i < k:
            result += min(tickets[i], tickets[k])
        elif i > k:
            result += min(tickets[i], tickets[k] - 1)
    return result
