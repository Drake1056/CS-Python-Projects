# Ask usrer for the file's name
filename = input("File name: ")
new_filename = filename.lower()

# gif or jpeg or jpg or png, print "image/type"
if '.gif'  in new_filename:
    print("image/type")
if 'jpeg' in new_filename:
    print("image/jpeg")
if 'jpg' in new_filename:
    print("image/jpg")
if 'png' in  new_filename:
    print("image/png")

# If PDF of Zip, print "application/PDF"


# If txt, print "text/plain"



# otherwise, print "application/octet-stream"