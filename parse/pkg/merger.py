from collections import defaultdict
import csv


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
    

def merge_list(list1, list2):
    new_dict = defaultdict(dict)

    for item in list1 + list2:
        new_dict[item['District']] =  new_dict[item['District']] | item 

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



if __name__ == "__main__":
    list1, list2 = parse_content("merger.txt")
    result = merge_list(list1, list2)
    write_csv(result)

    