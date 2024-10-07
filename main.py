inventory = [
    "SN123456789",
    "SN987654321"
]

def check_item(order_number):
   if len(order_number) == 9 and order_number.startswith("SN"):
        if order_number in valid_orders:
            return "Order number is valid."
        else:
            return "Order number not found. Please try again."
    else:
        return "Invalid order number format. It should be 9 characters long and start with 'SN'."

orderNumber = input("Please enter the order number starting with an SN")

output = check_item(orderNumber)
print(output)
