import codecs

encoded_string = 'Pbatenghyngvbaf ba ohvyqvat n pbqr-rqvgvat ntrag!'
decoded_string = codecs.decode(encoded_string, 'rot_13')
print(decoded_string)