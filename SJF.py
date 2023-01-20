import AdditionalFuntions


def make_ready_queue(process_details):
    ready_queue = []
    for key in process_details:
        arrival = [process_details[key]['arrival_time'], process_details[key]['cpu_time1'], key]
        ready_queue.append(arrival)
        ready_queue.sort()
    return ready_queue


# finding the best process index in ready queue
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


def sjf(process_details):
    current_time = 0
    idle = 0
    ready_queue = make_ready_queue(process_details)
    result = {}
    for i in ready_queue:
        result[i[2]] = {
            'start': 0,
            'end': 0
        }
    while len(ready_queue) > 0:
        gap = 0
        pop_index = current_index(ready_queue, current_time)
        current_process = ready_queue.pop(pop_index)
        [idle, gap] = AdditionalFuntions.add_idle(idle, current_process[0] - current_time)
        current_time += gap
        current_process_info = process_details[current_process[2]]
        done_service = AdditionalFuntions.check_done_services(current_process_info)

        # check if the cpu_time_1 is done or not
        if not done_service[0]:
            result[current_process[2]]['start'] = current_time
            current_time += current_process_info['cpu_time1']
            current_process_info['cpu_time1'] = 0

        # check if the io_time is done or not
        if not done_service[1]:
            ready_queue.append([
                (current_time + current_process_info['io_time']),
                current_process_info['cpu_time2'],
                current_process[2]
            ])
            current_process_info['io_time'] = 0

        # check if the cpu_time_2 is done or not
        if done_service == [True, True, False]:
            current_time += current_process_info['cpu_time2']
            result[current_process[2]]['end'] = current_time
            current_process_info['cpu_time2'] = 0
        ready_queue.sort()

    result['idle'] = idle
    result['total'] = current_time

    print(result)


