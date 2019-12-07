# messhidder

This is simple steganography tool that hiddes messages in JPG and PNG immages.

### usage
`python3 -e(to encode)/-d(to decode) input_file`

## encryption

`python3 hide.py -e image.jpg`
It asks you for a message to hide and creates `r.png` file which contains hidden message.

## decryption

`python3 hide.py -d r.png`
to encrypt a message from image.

__________________________________________________________________________________________

This is orginal image:

![original image](image.jpg)

This is the image with hidden message "Message!":

![Image with message](r.png)
