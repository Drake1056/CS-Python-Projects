# Ask usrer for the file's name
filename = input("File name: ")
new_filename = filename.lower()

# gif or jpeg or jpg or png, print "image/type"
if 'gif' | 'jpeg' | 'png' | 'jpg'  in new_filename:
    print("image/type")

# If PDF of Zip, print "application/PDF"


# If txt, print "text/plain"



# otherwise, print "application/octet-stream"