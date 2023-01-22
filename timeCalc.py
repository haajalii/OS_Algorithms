def waiting_time(arrival, end, service, io):
    return end - (arrival + service + io)


def turn_around_time(arrival, end):
    return end - arrival


def response_time(start, arrival):
    return start - arrival


def avg_time(count, times_list):
    sum = 0
    for time in times_list:
        sum += time
    return sum / count


def utilization(total, idle):
    return round((total - idle) / total, 2)


def throughput(total, n):
    return round(n * 1000 / total, 2)
