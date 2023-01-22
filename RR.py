import AdditionalFuntions


def make_ready_queue(process_details):
    ready_queue = []
    for key in process_details:
        arrival = [process_details[key]['arrival_time'], process_details[key]['cpu_time1'], key]
        ready_queue.append(arrival)
        ready_queue.sort()
    return ready_queue


def ready_processes(ready, time):
    lst = []
    for p in ready:
        if p[0] <= time:
            lst.append(p)
    if lst:
        return lst
    return ready[::]


def next_process(ready):
    return ready[0]


def rr(process_details, tq):
    current_time = 0
    idle = 0
    ready_queue = make_ready_queue(process_details)

    result = {}
    for i in ready_queue:
        result[i[2]] = {
            'first': False,
            'start': 0,
            'end': 0
        }
    while len(ready_queue) > 0:
        gap = 0
        ready_process = ready_processes(ready_queue, current_time)
        current_process = ready_process.pop(0)
        ready_queue.remove(current_process)
        [idle, gap] = AdditionalFuntions.add_idle(idle, current_process[0] - current_time)
        current_time += gap
        current_process_info = process_details[current_process[2]]
        done_service = AdditionalFuntions.check_done_services(current_process_info)

        # check if the cpu_time_1 is done or not
        if done_service == [False, False, False]:
            if not result[current_process[2]]['first']:
                result[current_process[2]]['start'] = current_time
                result[current_process[2]]['first'] = True
            if current_process_info['cpu_time1'] > tq:
                current_time += tq
                current_process[0] = current_time
                current_process[1] -= tq
                current_process_info['cpu_time1'] -= tq
                ready_process.append(current_process)
                ready_queue.append(current_process)
            else:
                current_time += current_process_info['cpu_time1']
                current_process_info['cpu_time1'] = 0
                done_service[0] = True

        # check if the io_time is done or not
        if done_service == [True, False, False]:
            ready_process.append([
                (current_time + current_process_info['io_time']),
                current_process_info['cpu_time2'],
                current_process[2]
            ])
            ready_queue.append([
                (current_time + current_process_info['io_time']),
                current_process_info['cpu_time2'],
                current_process[2]
            ])
            current_process_info['io_time'] = 0

        # check if the cpu_time_2 is done or not
        if done_service == [True, True, False]:
            if current_process_info['cpu_time2'] > tq:
                current_time += tq
                current_process[0] = current_time
                current_process[1] -= tq
                current_process_info['cpu_time2'] -= tq
                ready_process.append(current_process)
                ready_queue.append(current_process)
            else:
                current_time += current_process_info['cpu_time2']
                current_process_info['cpu_time2'] = 0
                result[current_process[2]]['end'] = current_time

        ready_queue.sort()

    result['idle'] = idle
    result['total'] = current_time

    return result
