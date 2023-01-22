import AdditionalFuntions


def make_ready_queue(process_details):
    # process_format = [arrival_time, cpu_time1or2, process_ID]
    ready_queue = []
    for key in process_details:
        arrival = [process_details[key]['arrival_time'], process_details[key]['cpu_time1'], key]
        ready_queue.append(arrival)
        ready_queue.sort()
    return ready_queue


def remaining_cpu(current_time, cpu_time, next_start_time):
    return cpu_time - (next_start_time - current_time)


def current_index(ready, time):
    lst = []
    temp = 0
    for p in ready:
        if p[0] <= time:
            temp = p[0]
            lst.append(p[1::])
        elif not lst:
            time = p[0]
            temp = p[0]
            lst.append(p[1::])
    lst.sort()
    # find index of chosen element
    for j in ready:
        if j[-1] == lst[0][1]:
            return ready.index(j)


def next_process(ready, process, time):
    lst = []
    temp_ready = ready[::]
    temp_process = process[::]
    selected_process = process[::]
    if not ready:
        return [ready, process]
    for p in ready:
        if (time + process[1]) > p[0] and time >= p[0]:
            lst.append(p)
    if lst:
        for i in lst:
            if i in ready:
                ready.remove(i)
        # process[1] = remaining_cpu(time, process[1], lst[0][0])
        # process[0] = lst[0][0]
        lst.append(process)
        selected_process = lst[current_index(lst, time)]
        selected_process[0] = time
        # if selected_process[2] == process[2]:
        # ready.append(process)
        # else:
        # ready.append(selected_process)
        lst.remove(selected_process)
        # ready.remove(selected_process)
        # lst.remove(process)
        # lst.append([temp_process[0]] + process[1::])
    # print(lst, selected_process[2])
    # print(ready)
    # returns [ready list after comparing, items that failed in that comparison, winner process]
    ready = ready + lst
    ready.sort()
    return [ready, selected_process]


def srtf(process_details):
    current_time = 0
    idle = 0
    ready_queue = make_ready_queue(process_details)
    result = {}
    next_p = []
    for i in ready_queue:
        result[i[2]] = {
            'start': None,
            'end': None
        }
    pop_index = current_index(ready_queue, current_time)
    key = ready_queue.pop(pop_index)[2]
    while len(ready_queue) >= 0 and key:
        # print(ready_queue)
        gap = 0
        current_process_info = process_details[key]
        if current_process_info['cpu_time1'] > 0:
            current_process = [current_process_info['arrival_time'], current_process_info['cpu_time1'], key]
        else:
            current_process = [current_process_info['arrival_time'], current_process_info['cpu_time2'], key]
        [idle, gap] = AdditionalFuntions.add_idle(idle, current_process[0] - current_time)
        current_time += gap
        current_process[0], current_process_info['arrival_time'] = current_time, current_time
        [ready_queue, current_process] = next_process(ready_queue, current_process, current_time)
        key = current_process[2]
        current_process_info = process_details[key]
        current_process[0], current_process_info['arrival_time'] = current_time, current_time
        # current_process_info = process_details[current_process[2]]
        done_service = AdditionalFuntions.check_done_services(current_process_info)

        if done_service == [False, False, False]:
            # print(current_process)
            # print(current_process_info)
            # print('cpu1: _')
            if not result[current_process[2]]['start']:
                result[current_process[2]]['start'] = current_time
            current_process_info['arrival_time'] = current_time
            current_process_info['arrival_time'] += 1
            current_process_info['cpu_time1'] -= 1
            current_time += 1
            if current_process_info['cpu_time1'] == 0:
                done_service[0] = True
        if done_service == [True, False, False]:
            ready_queue.append([
                (current_process_info['arrival_time'] + current_process_info['io_time']),
                current_process_info['cpu_time2'],
                key
            ])
            current_process_info['arrival_time'] += current_process_info['io_time']
            current_process_info['io_time'] = 0
            pop_index = current_index(ready_queue, current_time)
            next_p = ready_queue.pop(pop_index)
            key = next_p[2]
        if done_service == [True, True, False]:
            # print('cpu2: _')
            current_process_info['arrival_time'] = current_time
            current_process_info['arrival_time'] += 1
            current_process_info['cpu_time2'] -= 1
            current_time += 1
            if current_process_info['cpu_time2'] == 0:
                done_service[2] = True
                if len(ready_queue) > 0:
                    pop_index = current_index(ready_queue, current_time)
                    next_p = ready_queue.pop(pop_index)
                    key = next_p[2]
                else:
                    key = None
                result[current_process[2]]['end'] = current_time
        ready_queue.sort()

    result['idle'] = idle
    result['total'] = current_time

    return result
