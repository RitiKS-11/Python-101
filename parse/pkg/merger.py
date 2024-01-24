from collections import defaultdict
import csv
from nltk.metrics import edit_distance

def parse_content(filepath):
    with open(filepath) as file:
        district, kpi = file.readline().replace('\n', '').replace(' ', '').split('|')
        list1, list2 = [], []

        for line in file:
            data = line.replace('\n', '').split('|')

            if district in [d.strip() for d in data]:
                district, kpi = data[0].strip(), data[1].strip()
                continue
            
            if len(data) == 2:
                val1, val2 = data[0].strip(), data[1].strip()

                if  len(list1) < 3:
                    list1.append({district:val1, kpi:val2})
                else:
                    list2.append({district:val1, kpi:val2})

        return (list1, list2)
    

def merge_list(combined_list):
    new_dict = defaultdict(dict)
    # combined_list = list1 + list2

    for item in combined_list:
            district = item['District']
            new_dict[district] =  new_dict[district] | item 


    for key, value in new_dict.items():
        value.setdefault('KPI_1', None)
        value.setdefault('KPI_2', None)
            
        new_dict[key] = new_dict[key] | value

    return new_dict


def write_csv(result):
    with open('merger.csv', 'a') as file:
        fields = ['District', 'KPI_1', 'KPI_2']
        writer = csv.DictWriter(file, fieldnames=fields) 

        writer.writeheader()

        for _, value in result.items():
            writer.writerow(value)


def fix_word(key, key2):
    distance = edit_distance(key, key2)
    combined_word = ''

    if distance <= 1:

        for i in range(len(key2) + 1):
            candidate_word = key[:i] + key2[i:]
            distance = edit_distance(key2, candidate_word)

            if distance == 1:
                combined_word = candidate_word


        return combined_word
    

def update_combine_list(list1, list2):
    combined_list = sorted(list1 + list2, key=lambda x: x['District'])
    new_list = []
    for index, d in enumerate(combined_list):
        if (index+1) < len(combined_list):
            ne_w = fix_word(combined_list[index+1]['District'], d['District'])

        if ne_w:
            d['District'] = ne_w

        new_list.append(d)

    return new_list

if __name__ == "__main__":
    list1, list2 = parse_content("merger.txt")
    combined_list = update_combine_list(list1, list2)
    result = merge_list(combined_list)
    write_csv(result)
    # print(result)
