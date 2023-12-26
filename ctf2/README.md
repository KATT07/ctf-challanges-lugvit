a encrypted flag encoded into a image (med)                                                                                                                
encode:                                                                                                                
cat image.png + zip(flag.txt -> encrypted_flag.txt) -> output.png                                                                                                                
modify exif data of output.png and add hashed(sha256) key to decrypt    (make = "SHA HASH" model = hash)                                                                                                            
decode:                                                                                                                                                                                                                    
binwalk -> decrypt hashed key in exif -> extract the flag with key                                                                                                               
SHA-256 key: passwordispassword                                                                                                                
