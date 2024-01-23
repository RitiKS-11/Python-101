from collections import defaultdict
import csv


def parse_content(filepath):
    with open(filepath) as file:
        district, kpi = file.readline().replace('\n', '').replace(' ', '').split('|')
        list1 = []
        list2 = []

        for line in file:
            line = line.replace('\n', '').replace(' ', '')
            data = line.split('|')

            if district.rstrip() in data:
                district, kpi = data[0], data[1]
                continue

            if len(data) == 2 and len(list1) < 3:
                list1.append({district:data[0], kpi:data[1]})

            elif len(data) == 2:
                list2.append({district:data[0], kpi:data[1]})

        return (list1, list2)
    

def merge_list(list1, list2):
    merged_list = []
    new_dict = defaultdict()

    for item in list1 + list2:
        for key, value in item.items():
            new_dict[key] = value

        if len(new_dict) == 3:
            merged_list.append(dict(new_dict))

    return merged_list


def write_csv(result):
    with open('merger.csv', 'a') as file:
        fields = ['District', 'KPI_1', 'KPI_2']
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()

        for item in result:
            writer.writerow(item)


if __name__ == "__main__":
    list1, list2 = parse_content("merger.txt")
    print(list1, list2)
    result = merge_list(list1, list2)
    write_csv(result)

    