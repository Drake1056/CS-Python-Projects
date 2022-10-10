# Get user input
answer = input("Greeting:  ")

new_answer = answer.lower().strip()

# Check if the answer has "hello"
if 'hello' in new_answer:
    print("$0")

# Check if answer starts with "h"
elif 'h' == new_answer[0]:
    print("$20")

#Otherwise
else:
    print("$100")