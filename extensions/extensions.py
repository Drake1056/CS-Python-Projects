# Ask usrer for the file's name
filename = input("File name: ")
new_filename = filename.lower()

# gif or jpeg or jpg or png, print "image/type"
if '.gif'  in new_filename:
    print("image/gif")
elif '.jpeg' in new_filename:
    print("image/jpeg")
elif '.jpg' in new_filename:
    print("image/jpg")
elif '.png' in  new_filename:
    print("image/png")

# If PDF of Zip, print "application/type"
elif '.pdf' in new_filename:
    print("application/pdf")
elif '.zip' in new_filename:
    print("application/zip")

# If txt, print "text/plain"
elif '.txt' in new_filename:
    print("text/plain")


# otherwise, print "application/octet-stream"
else:
    print("application/octet-stream")