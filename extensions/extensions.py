# Ask usrer for the file's name
filename: input("File name: ")
new_filename = filename.lower().strip()

# gif or jpeg or jpg or png, print "image/type"
if 'gif' | 'jpeg' | 'png' | 'jpg'  in filename:
    print("image/type")

# If PDF of Zip, print "application/PDF"


# If txt, print "text/plain"



# otherwise, print "application/octet-stream"