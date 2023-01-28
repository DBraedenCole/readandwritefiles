def main():
    import csv

    # read file and skip header
    sales = open("sales.csv", "r")
    reader = csv.reader(sales, delimiter=",")
    next(reader)

    # create file to write to
    sales_report = open("salesreport.csv", "w")
    writer = csv.writer(sales_report, delimiter=",")

    # initialize variables to use for calculations and lists
    total = 0
    cust_id = ""
    id_list = []
    total_list = []

    # loop through sales to sum total, if cust_id is in the id_list else append to id_list
    for r in reader:
        cust_id = r[0]
        total = float(r[3]) + float(r[4]) + float(r[5])
        if cust_id in id_list:
            total_list[id_list.index(cust_id)] += total
        else:
            id_list.append(cust_id)
            total_list.append(total)

    # write the heder to the new csv
    header = ["Customer |", "Total"]
    writer.writerow(header)

    # loop to write to file based on the lists
    for i in range(len(id_list)):
        row = (id_list[i], format(total_list[i], ",.2f"))
        writer.writerow(row)

    # close the files
    sales.close()
    sales_report.close()


main()
