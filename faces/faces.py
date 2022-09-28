def main():
        #Get input from user
        user = input()
      # Call convert function
        result = convert(user)

        # print output
        print(result)

def convert(user)
    #Replace :) for happy emoji
    user1 = user.replace(":)", '🙂')

    # Replace :( for sad emoji
    user2 =user1.replace(":(", '🙁')
    # Return string

main()