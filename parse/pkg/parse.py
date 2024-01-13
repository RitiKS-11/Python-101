
def parse_content(filepath):
    with open(filepath) as file:
        lines = file.readlines()
        words = [clean_line(line) for line in lines]
    
    for word in words:
        if len(word) < 3:
            continue

        state1, state2 = (word[:3], word[3:]) if len(word) == 6 \
            else (word[:3], '')

        if state1:
            state1.sort(reverse=True)
            write_content(state1)
        if state2:
            state2.sort(reverse=True)
            write_content(state2)     


def clean_line(line):
    old_line = line.split('  ')
    return [word.replace('\n','') for word in old_line if word]


def write_content(state):
    print(state)
    with open('pared_contect.txt', 'a') as file:
        file.write(' '.join(state))
        file.write('\n')
        

if __name__ == "__main__":
    parse_content('unparsed.txt')