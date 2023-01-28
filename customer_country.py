def main():
    import csv

    customer_country = open("customer_country.csv", "w", newline="")
    customers = open("customers.csv", "r")
    writer = csv.writer(customer_country, delimiter=",")
    reader = csv.reader(customers, delimiter=",")

    next(reader)
    count = 0
    header = ["Name", "Country"]
    writer.writerow(header)

    for r in reader:
        count += 1
        row = [r[1] + " " + r[2], r[4]]
        writer.writerow(row)

    total = ["TOTAL CUSTOMERS", str(count)]
    writer.writerow("")
    writer.writerow(total)

    customers.close()
    customer_country.close()


main()
