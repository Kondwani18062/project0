name = input("Student name: ").strip().title()
program = input("Program: ").strip().title()
total_fees = float(input("Total fees (K): "))
amount_paid = float(input("Amount paid (K): "))

balance = total_fees - amount_paid
print()
print(f"{'FEE SUMMARY':^30}")
print(f"Student Name: {name}")
print(f"Program: {program}")
print(f"Total Fees: {total_fees} K")
print(f"Amount Paid: {amount_paid} K")
print(f"Balance: {balance} K")