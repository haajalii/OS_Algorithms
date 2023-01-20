def make_list_process(process_details):
    process_timings = {}
    for key in process_details:
        process_timings[key] = []


def make_ready_queue(process_details):
    ready_queue = []
    for key in process_details:
        arrival = [process_details[key]['arrival_time'], key]
        ready_queue.append(arrival)
        ready_queue.sort()
    return ready_queue


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


def fcfs(process_details):
    current_time = 0
    idle = 0
    ready_queue = make_ready_queue(process_details)
    result = {}
    for i in ready_queue:
        result[i[1]] = {
            'start': 0,
            'end': 0
        }
    while len(ready_queue) > 0:
        gap = 0
        current_process = ready_queue.pop(0)
        [idle, gap] = add_idle(idle, current_process[0] - current_time)
        current_time += gap
        current_process_info = process_details[current_process[1]]
        done_service = check_done_services(current_process_info)

        # check if the cpu_time_1 is done or not
        if not done_service[0]:
            result[current_process[1]]['start'] = current_time
            current_time += current_process_info['cpu_time1']
            current_process_info['cpu_time1'] = 0

        # check if the io_time is done or not
        if not done_service[1]:
            ready_queue.append([
                (current_time + current_process_info['io_time']),
                current_process[1]
            ])
            current_process_info['io_time'] = 0

        # check if the cpu_time_2 is done or not
        if done_service == [True, True, False]:
            current_time += current_process_info['cpu_time2']
            result[current_process[1]]['end'] = current_time
            current_process_info['cpu_time2'] = 0
        ready_queue.sort()

    result['idle'] = idle
    result['total'] = current_time

    print(result)


