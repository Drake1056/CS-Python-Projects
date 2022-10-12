# Ask user for Input
expression =input("Expression: ")
# Convert user's input into variable
x, y, z = expression.split(" ")

# change x & y into float
x_new = float(x)
z_new = float(z)

# Calculate results
if y == "+":
    result = x_new + z_new
if y == "-":
    result = x_new - z_new
if y == "*":
    result = x_new * z_new
if y == "/":
    result = x_new / z_new
print(round(result, 1))

