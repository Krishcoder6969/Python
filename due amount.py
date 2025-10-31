def calculate_due_amount(total_bill_amount, amount_paid):
  """
  Calculates the remaining due amount after a payment.

  Args:
    total_bill_amount: The total amount of the bill.
    amount_paid: The amount the customer has paid.

  Returns:
    The remaining amount due. If the amount paid exceeds the bill, 
    a negative value indicates overpayment.
  """
  due_amount = total_bill_amount - amount_paid
  return due_amount


try:
  bill = float(input("Enter the total bill amount: "))
  payment = float(input("Enter the amount paid by the customer: "))

  # Calculate the due amount
  remaining_due = calculate_due_amount(bill, payment)

  # Display the result
  if remaining_due > 0:
    print(f"The customer still owes: ${remaining_due:.2f}")
  elif remaining_due < 0:
    print(f"The customer overpaid by: ${abs(remaining_due):.2f}. A refund is due.")
  else:
    print("The bill has been fully paid.")

except ValueError:
  print("Invalid input. Please enter numerical values for amounts.")