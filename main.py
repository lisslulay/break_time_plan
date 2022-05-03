from log import *
from const import *
from helpMethod import *



""" Get all the records in file
"""
def readRecords() -> list:
    f = open(RECORD_FILE, 'r')
    records = f.readlines()
    f.close()
    return records


""" Get the least record
    ["05-02: 120\n", "05-03: 120\n"] -> ["05-03", 120]
"""
def readLeastRecords(records: list) -> list[str, int]:
    record = records[-1].split(SEPARATOR)
    record[1] = int(record[1].strip())
    return record


""" Print all break rules
"""
def printRules():
    print("Rules: ")
    for i, rule in enumerate(RULES):
        print("\t", i, rule)
    
    
""" Get user input
    [15, 1]
    return list, the first is increase break time, the second is the log
"""
def getUserUpdate() -> int:
    time = -1
    desc = -1
    confirm = False

    while not confirm:
        
        time = int(input("Earn break (min): "))

        rightNumber = 0;
        while rightNumber == 0:
            try:
                desc = RULES[int(input("Choose one rules: "))]
                rightNumber = 1
            except IndexError as e:
                print("please input again {0}".format(str(e)))

        
        answer = int(input("Are you confirm (0:again / 1:yes)? "))
        if answer == 1:
            confirm = True

    addLineInLog(time, desc)
    
    return time


""" Update time in records
    If original file have current time, update
    else add current time entry
"""
def updateRecordsInFile(records: list, addTime: int):
    record = readLeastRecords(records)
    if record[0] == currentData():
        ## update
        newTime = record[1] + addTime
        records[-1] = record[0] + ": " + str(newTime) + "\n"
        addChangeInLog(currentData(), record[1], newTime)
        
    else:
        ## add new entry
        entry = currentData() + ": " + str(addTime) + "\n"
        addChangeInLog(currentData(), None, addTime)
        records.append(entry)

    f = open(RECORD_FILE, 'w')
    f.writelines(records)
    f.close()
        

        
def main():
    exit = 0
    records = readRecords()
    if len(records) >= 2:
        print(records[-2] + records[-1])
    else:
        print(records)
    printRules()
    
    while exit == 0:
        print("========================================")
        time = getUserUpdate()
        records = readRecords()
        updateRecordsInFile(records, time)
        exit = int(input("Click to exit (0:again / 1:exit)"))
    

if __name__ == "__main__":
    main()
