def main():
    import csv

    emp_pay = open("EmployeePay.csv", "r")
    reader = csv.reader(emp_pay, delimiter=",")
    next(reader)

    for r in reader:
        tot_pay = float(r[3]) + (float(r[3]) * float(r[4]))
        details = (
            "\nID:\t   "
            + r[0]
            + "\nName:\t   "
            + r[1]
            + " "
            + r[2]
            + "\nTotal Pay: "
            # + "{:,.2f}".format(tot_pay)
            + format(tot_pay, ",.2f")
            + "\n"
        )
        print(details)
        ans = input("Press 'Enter/Return' to Continue or 99 to exit: ")
        if ans == "99":
            exit()
        else:
            continue

    emp_pay.close()


main()
