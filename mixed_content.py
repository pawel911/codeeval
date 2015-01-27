import sys

test_cases = open(sys.argv[1], 'r')

for line in test_cases:
    
    line = line.rstrip("\n").split(',')
    
    numbers = []
    strings = []
    
    for i in range(len(line)):
        if line[i][0].isdigit: numbers.append(line[i])
        else: strings.append(line[i])
           
    if len(strings) > 0 and len(numbers) > 0:
        output = ",".join(strings) + "|" + ",".join(numbers)
    elif len(strings) == 0: output = ",".join(numbers)
    elif len(numbers) == 0: output = ",".join(strings)
    else: output = ""  
          
    print output

test_cases.close()
