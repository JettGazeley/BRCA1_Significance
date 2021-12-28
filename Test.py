group_names = ["name1", "name2", "name3"]
group_found = []
group_missing = []


def data ():
    for i in range (0, len(group_names)):
        if group_names[i] in group_found:
            print("found a matched data point")

    return 0






def main():
    print("Hello World!")

if __name__ == "__main__":
    main()