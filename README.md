# messhidder

This is simple steganography tool that hiddes messages in JPG and PNG immages.

## usage
`python3 hide.py -e(to encode)/-d(to decode) input_file`

hide.py uses `pillow` and `bitarray` modules.

To download pillow type `pip3 install Pillow`.

To download bitarray type `pip3 install bitarray`.

### encryption

`python3 hide.py -e image.jpg`

It asks you for a message to hide and creates `r.png` file which contains hidden message.

### decryption

`python3 hide.py -d r.png`

to encrypt a message from image.

__________________________________________________________________________________________

This is original image:

<img src="image.jpg" width="400">

This is the image with hidden message "This is a secret message":

<img src="r.png" width="400">
