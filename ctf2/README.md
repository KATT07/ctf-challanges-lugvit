a encrypted flag encoded into a image (med)                                                                                                                
encode:                                                                                                                
cat image.png + zip(flag.txt -> encrypted_flag.txt) -> output.png                                                                                                                
modify exif data of output.png and add hashed(sha256) key to decrypt    (make = "SHA HASH" model = hash)                                                                                                            
decode:                                                                                                                                                                                                                    
binwalk -> decrypt hashed key in exif -> extract the flag with key                                                                                                               
SHA-256 key: passwordispassword                                                                                                                


# For Participants:

Description:

my friend sent me this strange image and told there is something hidden inside can u find out what it is?

Hint 1:                                                                                                                                                                     
are u sure the file is just the image?                                                                                                         
Hint 2:                                                                                                                                                                     
i wonder what hash it is                                                                                                        
Hint 3:                                                                                                                                                                    
use a bigger wordlist                                                                                                                                                   
