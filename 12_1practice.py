"""
PYTHON ALL-IN-ONE PRACTICE WORKBOOK
===================================
Variables to Sets: real-world examples, questions, answers, and explanations.
Read the comments first, then run the code and change the sample values.
"""

# ============================================================
# 1. VARIABLES: storing a customer's basic information
# ============================================================
# Theory: A variable is a name that stores a value.
# Real world: An app stores a customer's name, age, and city.

customer_name = "Abhi"
customer_age = 21
customer_city = "Pune"
print("1. Customer:", customer_name, customer_age, customer_city)

# Question: Create a variable called customer_status and print it.
# Answer:
customer_status = "active"
print("Customer status:", customer_status)
# Why: The value "active" is stored inside customer_status.


# ============================================================
# 2. DATA TYPES: product information
# ============================================================
# Theory: A data type tells Python what kind of value we have.
# Real world: An online product has an integer ID, price, name, and stock status.

product_id = 101              # int: whole number
product_price = 499.99        # float: decimal number
product_name = "Keyboard"    # str: text
product_available = True      # bool: True or False
product_tags = ["computer", "accessory"]  # list: collection

print("2. Product types:")
print(type(product_id), type(product_price), type(product_name))
print(type(product_available), type(product_tags))

# Question: What is the type of None?
# Answer:
not_delivered = None
print("None type:", type(not_delivered))
# Why: None means that a value is currently missing or not assigned.


# ============================================================
# 3. OPERATORS: shopping bill and comparison
# ============================================================
# Theory: Operators perform calculations or comparisons.
# Real world: Calculate a bill and check whether a customer gets free delivery.

item_price = 800
quantity = 3
total_bill = item_price * quantity
print("3. Total bill:", total_bill)

# Question: Give free delivery when the bill is 2000 or more.
# Answer:
free_delivery = total_bill >= 2000
print("Free delivery:", free_delivery)
# Why: >= compares total_bill with 2000 and returns True or False.

# Question: Apply a 10% discount using an arithmetic operator.
# Answer:
discount = total_bill * 10 / 100
final_bill = total_bill - discount
print("Discount:", discount, "Final bill:", final_bill)
# Why: / calculates the percentage and - subtracts it from the bill.


# ============================================================
# 4. TYPE CASTING: converting form data
# ============================================================
# Theory: Type casting converts a value from one data type to another.
# Real world: Data received from a form is often text, even when it is a number.

age_text = "21"
age_number = int(age_text)
print("4. Next year age:", age_number + 1)
# Why: int("21") changes text into the number 21.

# Question: Convert a price to text for an invoice message.
# Answer:
price = 750
invoice_message = "Price: " + str(price)
print(invoice_message)
# Why: str(price) allows a number to join a string.


# ============================================================
# 5. INPUT: collecting customer data
# ============================================================
# Theory: input() reads information typed by the user, and returns a string.
# Real-world input example (uncomment to try it):
# customer = input("Enter your name: ")
# order_quantity = int(input("Enter quantity: "))
# print(customer, "ordered", order_quantity, "items")

# Question: Without input, calculate an order total from sample values.
# Answer:
ordered_quantity = 4
unit_price = 125
print("5. Order total:", ordered_quantity * unit_price)
# Why: int(input()) should be used when the user types a whole number.


# ============================================================
# 6. STRINGS AND SLICING: order code
# ============================================================
# Theory: A string is text. Indexing starts at 0, and slicing selects part of text.
# Real world: An order code may contain a store prefix and a numeric part.

order_code = "PUNE2026"
print("6. First character:", order_code[0])
print("Store prefix:", order_code[:4])
print("Year part:", order_code[4:])
print("Reversed code:", order_code[::-1])
# Why: [start:stop] selects characters, while [::-1] reverses the string.

# Question: Print the last three characters of the order code.
# Answer:
print("Last three:", order_code[-3:])


# ============================================================
# 7. STRING METHODS: cleaning a customer message
# ============================================================
# Theory: String methods inspect or create changed versions of text.
# Real world: Clean a customer's name before displaying it.

raw_name = "  abhi thombare  "
clean_name = raw_name.strip().title()
print("7. Clean name:", clean_name)
print("Name length:", len(clean_name))
print("Has Abhi:", "Abhi" in clean_name)
# Why: strip() removes outer spaces and title() capitalizes words.

# Question: Replace an old domain in an email address.
# Answer:
old_email = "user@oldsite.com"
new_email = old_email.replace("oldsite.com", "newsite.com")
print("New email:", new_email)
# Why: replace() returns a new string with the selected text changed.


# ============================================================
# 8. MIXED PRACTICE: simple result checker
# ============================================================
# Theory: Real programs combine variables, input, operators, and conditions.
# Real world: Check whether a student passed.

student = "Abhi"
marks = 72
passing_marks = 40
passed = marks >= passing_marks
print("8. Result:", student, "passed:", passed)

# Question: Show a message based on the result.
# Answer:
if passed:
    print("Congratulations! You passed.")
else:
    print("Please try again.")
# Why: if runs one block when the condition is True; else runs otherwise.


# ============================================================
# 9. LISTS: managing an order's items
# ============================================================
# Theory: A list stores multiple values in order and can be changed.
# Real world: A shopping cart contains products.

cart = ["mouse", "keyboard", "USB cable"]
cart.append("headphones")
cart.remove("USB cable")
print("9. Cart:", cart)
print("First item:", cart[0])
# Why: append() adds one item and remove() removes a matching item.

# Question: Sort delivery times and find the fastest time.
# Answer:
delivery_times = [5, 2, 7, 3]
delivery_times.sort()
print("Sorted times:", delivery_times)
print("Fastest time:", delivery_times[0])
# Why: sort() arranges numbers in ascending order.


# ============================================================
# 10. TUPLES: fixed location coordinates
# ============================================================
# Theory: A tuple is ordered like a list, but it cannot be changed.
# Real world: GPS coordinates should remain fixed while being used.

shop_location = (18.5204, 73.8567)
print("10. Latitude:", shop_location[0])
print("Longitude:", shop_location[1])
# Question: Count zeroes in a fixed result tuple.
# Answer:
result_codes = (0, 200, 0, 404, 0)
print("Zero count:", result_codes.count(0))
# Why: count() tells how many times a value appears.
# shop_location[0] = 20  # Error: tuples are immutable.


# ============================================================
# 11. DICTIONARIES: one user's complete profile
# ============================================================
# Theory: A dictionary stores key-value pairs for named information.
# Real world: APIs commonly send user data in dictionary/JSON form.

user = {
    "id": 101,
    "name": "Abhi",
    "email": "abhi@example.com",
    "is_active": True
}

print("11. User name:", user["name"])
user["city"] = "Pune"       # add a new key-value pair
user["is_active"] = False   # change an existing value
print("Updated user:", user)

# Question: Safely read a phone number that may not exist.
# Answer:
print("Phone:", user.get("phone", "Phone not available"))
# Why: get() avoids KeyError and returns the default message if missing.

# Question: Print every field in the user profile.
# Answer:
for key, value in user.items():
    print(key, "=", value)
# Why: items() gives the key and value together in every loop.


# ============================================================
# 12. SETS: unique visitors and common courses
# ============================================================
# Theory: A set stores unique values and is useful for membership and comparison.
# Real world: Remove duplicate visitor IDs from a website report.

visitor_ids = [101, 102, 101, 103, 102, 104]
unique_visitors = set(visitor_ids)
print("12. Unique visitors:", unique_visitors)
# Why: converting a list to a set automatically removes duplicates.

# Question: Find students enrolled in both courses.
# Answer:
python_students = {"Ali", "Sara", "Abhi"}
java_students = {"Sara", "John", "Abhi"}
print("Both courses:", python_students & java_students)
print("All students:", python_students | java_students)
# Why: & gives intersection/common values; | gives union/all values.

# Question: Add a visitor and check membership.
# Answer:
unique_visitors.add(105)
print("Visitor 105 exists:", 105 in unique_visitors)
# Why: add() inserts a value and in checks whether it exists.


# QUICK REVISION
# Variable  -> one named value
# List      -> ordered, changeable collection
# Tuple     -> ordered, fixed collection
# Dictionary-> key-value information
# Set       -> unique values, no fixed index
