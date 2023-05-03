# Make a QR code in Python

import qrcode

# Make a QR code
qr = qrcode.make('https://www.youtube.com/watch?v=9bZkp7q19f0')

# Save the QR code
qr.save('qr.png')
