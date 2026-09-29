name = input("Student name: ").strip().title()
program = input("Program: ").strip().title()
total_fees = float(input("Total fees (K): "))
amount_paid = float(input("Amount paid (K): "))

balance = total_fees - amount_paid
print()
print(f"{'FEE SUMMARY':^30}")
print(f"Student Name: {name}")
print(f"Program: {program}")
print(f"Total Fees: K{total_fees} ")
print(f"Amount Paid: K{amount_paid} ")
print(f"Balance: K{balance} ")
