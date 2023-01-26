def main():
    import csv

    customer_country = open("customer_country.csv", "w", newline="")
    customers = open("customers.csv", "r")
    cc_file = csv.writer(customer_country, delimiter=",")
    cust_file = csv.reader(customers, delimiter=",")

    next(cust_file)
    count = 0
    header = ["Name", "Country"]
    cc_file.writerow(header)

    for r in cust_file:
        count += 1
        row = [r[1] + " " + r[2], r[4]]
        cc_file.writerow(row)

    total = ["TOTAL CUSTOMERS", str(count)]
    cc_file.writerow("")
    cc_file.writerow(total)

    customers.close()
    customer_country.close()


main()
