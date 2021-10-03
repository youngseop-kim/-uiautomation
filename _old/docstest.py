import re
with open('docs', 'r') as f1:
    content = f1.read()

    found = re.findall(
        pattern = 'UIA_.*\n\d{5}',
        string = content
        )

with open('docsresult', 'w') as f2:
    for i in found:
        prop, id_ = i.split('\n')
        f2.write(
            f"self['{prop}'] = \\" + f'\n\tUIAutomationClient.{prop}\n'
            )

'''
ffound = []
with open('docs', 'r') as f1:
    readlines = f1.readlines()
    for readline in readlines:
        found = re.findall('.*\t\d*\t\n', readline)
        if len(found) > 0:
            ffound.append(found[0])
    
with open('docsresult', 'w') as f2:
    for found in ffound:
        f2.write(
            found.split("\t")[1] + 
            ' : ' +
            "'" + 
            found.split("\t")[0] +
            "',\n"
            )
'''
'''
readlines = f1.readlines()
for i, readline in enumerate(readlines):
    if readline.startswith('            '):
        readlines[i] = f'            ({readline.strip()}, None,)\n'

with open('docsresult', 'w') as f2:
    f2.write(''.join(readlines))
'''

'''
content = f1.read()

found = re.findall(
    pattern = 'UIA_.*\n\d{5}',
    string = content
    )
    

with open('docsresult', 'w') as f2:
    for i in found:
        prop, id_ = i.split('\n')
        f2.write(
            f"self['{prop}'] = \\" + f'\n\tUIAutomationClient.{prop}\n'
            )
'''