a encrypted flag encoded into a image (med)                                                                                                                
encode:                                                                                                                
cat image.png + zip(flag.txt -> encrypted_flag.txt) -> output.png                                                                                                                
modify exif data of output.png and add hashed key to decrypt                                                                                                                
decode:                                                                                                                                                                                                                                
binwalk -> decrypt hashed key in exif -> flag                                                                                                                 
SHA-256 key: passwordispassword                                                                                                                
