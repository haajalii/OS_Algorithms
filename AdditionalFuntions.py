def add_idle(idle, gap):
    if gap > 0:
        return [idle + gap, gap]
    return [idle, 0]


def check_done_services(process):
    done = [False, False, False]
    if process['cpu_time1'] == 0:
        done[0] = True
    if process['io_time'] == 0:
        done[1] = True
    if process['cpu_time2'] == 0:
        done[2] = True
    return done
