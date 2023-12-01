lines = []
with open("./input.txt", "r") as file:
    for line in file.read().strip().split('\n'):
        lines.append(line)

WORD_LIST = [('one','1'), ('two','2'), ('three','3'), ('four','4'), ('five','5'), ('six','6'), ('seven','7'), ('eight','8'), ('nine','9'),
             ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('8','8'), ('9','9')]
total_value = 0

for line in lines:
    line_value = ''
    
    lowest_match = ()
    for word in WORD_LIST:
        pos = line.find(word[0])
        if pos >= 0 and (not lowest_match or pos < lowest_match[0]):
            lowest_match = (pos, word[1])
    line_value += lowest_match[1]
    
    highest_match = ()
    for word in WORD_LIST:
        pos = line.rfind(word[0])
        if pos >= 0 and (not highest_match or pos > highest_match[0]):
            highest_match = (pos, word[1])
    line_value += highest_match[1]
        
    total_value += int(line_value)
     
print(total_value)
input()