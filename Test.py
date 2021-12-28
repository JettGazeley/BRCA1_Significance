#sample data
group_names = ["name1", "name2", "name3"]
group_found = ["name1", "2", "4"]
group_missing = ["1", "5", "3"]

#check if data is found in the sample
def data_check():
    for i in range (0, len(group_names)):
        if group_names[i] in group_found:
            print("found a matched data point")
        if group_names[i] not in group_missing:
            print("missing a data point") 
    return 0

def main():
    data_check()

if __name__ == "__main__":
    main()