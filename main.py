import GetInput
import timeCalc


process_details = GetInput.get_input('./inputFile.csv')

for keys in process_details:
    print(str(keys) + ' : ' + str(process_details[keys]))