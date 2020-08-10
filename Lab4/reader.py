import csv

AMPLITUDE = [64, 128, 256, 512]
WIDTH = [8, 16, 32]


def read_file():
    data = {}
    with open('experiment_fitts_log.txt', newline='') as csvfile:
        experiment_reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in experiment_reader:
            name, amp, width, s_id, time = row
            key = (amp, width)
            value = time
            if key in data:
                data[key].append(value)
            else:
                if int(s_id) > 2:
                    data[key] = [value]
    return data


def summarise_data(data):
    """Data is a dictionary in the from of Key:(amp, width) value: [time] indexed by selection ID"""
    average_results = []
    counter = 0;

    for key, values in data.items():
        width = key[0]
        amp = key[1]
        time = round(float(values)/1000, 4)

    return average_results


def main():
    data_set = read_file()
    data_summary = summarise_data(data_set)
    print(data_summary)


if __name__ == '__main__':
    main()