import FCFS
import GetInput
import SJF
import timeCalc


process_details = GetInput.get_input('./inputFile.csv')

# for keys in process_details:
#     print(str(keys) + ' : ' + str(process_details[keys]))

# FCFS.fcfs(process_details)
SJF.sjf(process_details)