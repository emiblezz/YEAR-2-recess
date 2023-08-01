import tkinter as tk


class Receipt:

  def __init__(self, customer_name, items, total_amount):
    self.customer_name = customer_name
    self.items = items
    self.total_amount = total_amount

  def print_receipt(self):
    print("Printing Receipt:")
    print(f"Customer: {self.customer_name}")
    print("Items:")
    for item in self.items:
      print(f"- {item}")
    print(f"Total Amount: {self.total_amount} Ugx")
    print()


def create_receipt():
  customer_name = entry_customer.get()
  items = entry_items.get("1.0", tk.END).splitlines()
  total_amount = float(entry_amount.get())
  return Receipt(customer_name, items, total_amount)


def print_receipt_details():
  receipt = create_receipt()
  receipt.print_receipt()


# GUI Interface
root = tk.Tk()
root.title("Receipt Book")

# Customer Name
label_customer = tk.Label(root, text="Customer Name:")
label_customer.pack()

entry_customer = tk.Entry(root)
entry_customer.pack()

# Items
label_items = tk.Label(root, text="Items:")
label_items.pack()

entry_items = tk.Text(root, height=5, width=30)
entry_items.pack()

# Total Amount
label_amount = tk.Label(root, text="Total Amount:")
label_amount.pack()

entry_amount = tk.Entry(root)
entry_amount.pack()

# Print Button
button_print = tk.Button(root,
                         text="Print Receipt",
                         command=print_receipt_details)
button_print.pack()

root.mainloop()
