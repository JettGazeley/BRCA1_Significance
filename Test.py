#Name: Jett Gazeley
#Last Edited: 2021-12-27 (yyyy-mm-dd)


#sample data
input_data = []
group_names = ["name1", "name2", "name3"]
group_found = ["name1", "2", "4"]
group_missing = ["1", 5, "3"]

#check if data is found in the sample
def data_check():
    for i in range (0, len(group_names)):
        if group_names[i] in group_found:
            print("found a matched data point")
            print(group_names[i])
        if group_names[i] not in group_missing:
            print("missing a data point") 
    return 0

def input_check():
    sample = int(input("Enter your data: "))
    if sample in group_missing:
        print("hey - we found it")
        #found_important_data()
    return 0




#main function
def main():
    data_check()
    input_check()

if __name__ == "__main__":
    main()