import copy

import FCFS
import GetInput
import RR
import SALT
import SJF
import SRT
import timeCalc


process_details = GetInput.get_input('./inputFile.csv')
process_details_copy = copy.deepcopy(process_details)
wt = []
tat = []
resp = []
avg_wt = 0
avg_tat = 0
avg_resp = 0
utilization = 0
throughput = 0
idle = 0
total = 0
n = len(process_details.keys())
# for keys in process_details:
#     print(str(keys) + ' : ' + str(process_details[keys]))

# FCFS.fcfs(process_details)
# SJF.sjf(process_details)

# SRT.srt(process_details)

# awt tat claculation


# current_time = 5
# process = [5, 4, 'p3']
# ready_queue = [[6, 4, 'p1'], [12, 3, 'p2'], [6, 2, 'p4'], [13, 5, 'p5']]
# print(SALT.next_process(ready_queue, process, current_time))

# SALT.srtf(process_details)
# RR.rr(process_details, 3)

# 66char
def print_result(result, algorithm):

    avg_wt = timeCalc.avg_time(n, wt)
    avg_tat = timeCalc.avg_time(n, tat)
    avg_resp = timeCalc.avg_time(n, resp)
    utilization = timeCalc.utilization(total, idle)
    throughput = timeCalc.throughput(total, n)
    print("+============+===========+==================+===============+==============+")
    print("|" + ' '*((74-len(algorithm))//2) + algorithm + ' '*((74-len(algorithm))//2) + "|")
    print("+============+===========+==================+===============+==============+")
    print("| Process ID | Start-End | Turn Around Time | Response Time | Waiting Time |")
    print("+------------+-----------+------------------+---------------+--------------+")
    for key in list(result.keys())[:-2:]:
        index = list(result.keys()).index(key)
        print('| ' + key + ' '*9, end='')
        print('| ' + str(result[key]['start']) + '-' + str(result[key]['end']) + ' ' * (9 - len(str(result[key]['end']) + str(result[key]['start']))), end='')
        print('| ' + str(tat[index]) + ' ' * (17 - len(str(tat[index]))), end='')
        print('| ' + str(resp[index]) + ' ' * (14 - len(str(resp[index]))), end='')
        print('| ' + str(wt[index]) + ' ' * (13 - len(str(wt[index]))), end='')
        print('|', end='\n')
    print("+------------+-----------+------------------+---------------+--------------+")
    print('| Average' + ' '*16 + '| ' + str(avg_tat) + ' '*(17 - len(str(avg_tat))), end='')
    print('| ' + str(avg_resp) + ' ' * (14 - len(str(avg_resp))), end='')
    print('| ' + str(avg_wt) + ' ' * (12 - len(str(avg_wt))), end='')
    print('|', end='\n')
    print("+------------+-----------+------------------+---------------+--------------+")
    print('\n')
    print('Total Time: ' + str(total))
    print('Idle Time: ' + str(idle))
    print('CPU Utilization: ', utilization)
    print('Throughput: ', throughput)


def create_time_lists(res, process_detail):
    for key in list(res.keys())[:-2:]:
        cpu_time1 = process_detail[key]['cpu_time1']
        cpu_time2 = process_detail[key]['cpu_time2']
        end = res[key]['end']
        start = res[key]['start']
        arrival = process_detail[key]['arrival_time']
        io = process_detail[key]['io_time']
        wt.append(timeCalc.waiting_time(arrival, end, (cpu_time1 + cpu_time2), io))
        tat.append(timeCalc.turn_around_time(arrival, end))
        resp.append(timeCalc.response_time(start, arrival))




algorithm = int(input())
result = {}

if algorithm == 1:
    result = FCFS.fcfs(process_details)
    create_time_lists(result, process_details_copy)
    total = result['total']
    idle = result['idle']
    print_result(result, 'FCFS')
elif algorithm == 2:
    result = SJF.sjf(process_details)
    create_time_lists(result, process_details_copy)
    total = result['total']
    idle = result['idle']
    print_result(result, 'SJF')
elif algorithm == 3:
    tq = int(input())
    result = RR.rr(process_details, tq)
    create_time_lists(result, process_details_copy)
    total = result['total']
    idle = result['idle']
    print_result(result, 'RoundRobin')
elif algorithm == 4:
    SRT.srt(process_details)


