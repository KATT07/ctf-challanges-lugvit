import hashlib
from exif import Image

# using hexdigest()
st = "passwordispassword"
st_hash = hashlib.sha256(st.encode('utf-8')).hexdigest()

with open('/root/output.jpg', 'rb') as image_file:
    my_image = Image(image_file)
image_file.close()
my_image.make = "SHA HASH"
my_image.model = st_hash
print(my_image.make)
print(my_image.model)
with open('/root/output.jpg', 'wb') as image_file:
    image_file.write(my_image.get_file())
image_file.close()
