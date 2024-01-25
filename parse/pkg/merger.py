from collections import defaultdict
import csv
from nltk.metrics import edit_distance

def parse_content(filepath):
    with open(filepath) as file:
        district, kpi = file.readline().replace('\n', '').replace(' ', '').split('|')
        kpi1, kpi2 = [], []

        for line in file:
            data = line.replace('\n', '').split('|')
            
            if len(data) == 2:
                value1, value2 = data[0].strip(), data[1].strip()

                if district == value1:
                    district, kpi = value1, value2
                    continue
                
                if  len(kpi1) < 3:
                    kpi1.append({district:value1, kpi:value2})
                else:
                    kpi2.append({district:value1, kpi:value2})

        return (kpi1, kpi2)
    

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

        for _, result in result.items():
            writer.writerow(result)


def fix_word(key, key2):
    distance = edit_distance(key, key2)
    combined_word = ''
    fixed_words = []

    if distance <= 1:
        for i in range(len(key2) + 1):
            candidate_word = key[:i] + key2[i:]
            distance = edit_distance(key2, candidate_word)

            if distance <= 1:
                fixed_words.append(candidate_word)
        
        fixed_words = set(fixed_words)

        if key in fixed_words:
            combined_word =  key
        elif key2 in fixed_words:
            combined_word = key2

    return combined_word

    

def update_combine_list(list1, list2):
    combined_list = sorted(list1 + list2, key=lambda x: x['District'], reverse=True)
    updated_combine_list = list()

    for index, data in enumerate(combined_list):
        if (index+1) < len(combined_list):
            ne_w = fix_word(combined_list[index+1]['District'], data['District'])

            if ne_w:
                data['District'] = ne_w
                combined_list[index+1]['District'] = ne_w
                
        updated_combine_list.append(data)

    return updated_combine_list

if __name__ == "__main__":
    list1, list2 = parse_content("merger.txt")
    combined_list = update_combine_list(list1, list2)
    result = merge_list(combined_list)
    write_csv(result)
