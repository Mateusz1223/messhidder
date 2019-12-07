# messhidder

This is simple steganography tool that hiddes messages in JPG and PNG immages.

## usage
`python3 -e(to encode)/-d(to decode) input_file`

hide.py uses `pillow` and `bitarray` modules.
To download pillow type `pip install Pillow`
To download bitarray type `pip install bitarray`

### encryption

`python3 hide.py -e image.jpg`
It asks you for a message to hide and creates `r.png` file which contains hidden message.

### decryption

`python3 hide.py -d r.png`
to encrypt a message from image.

__________________________________________________________________________________________

This is orginal image:

<img src="image.jpg" width="600">

This is the image with hidden message "This is message":

<img src="r.png" width="600">
