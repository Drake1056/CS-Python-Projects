# Ask usrer for the file's name
filename = input("File name: ")
new_filename = filename.lower()

# gif or jpeg or jpg or png, print "image/type"
if '.gif'  in new_filename:
    print("image/type")
if '.jpeg' in new_filename:
    print("image/jpeg")
if '.jpg' in new_filename:
    print("image/jpg")
elif '.png' in  new_filename:
    print("image/png")

# If PDF of Zip, print "application/type"
if '.pdf' in new_filename:
    print("application/pdf")
elif '.Zip' in new_filename:
    print("application/Zip")

# If txt, print "text/plain"
if '.txt' in new_filename:
    print("text/plain)


# otherwise, print "application/octet-stream"
else:
    print("application/octet-stream")