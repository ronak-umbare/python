import qrcode

upi_id = input("Enter ur UPI ID = ")

# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE'
#Defining the payment URLs based on payment method

phonepay = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
gpay = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#creating qr's
phonepayQr = qrcode.make(phonepay)
paytmQR = qrcode.make(paytm)
gpayQR = qrcode.make(gpay)

#saving
# phonepayQr.show("phpe.png")
# paytmQR.show("payt.png")
gpay.show("gpay.png")
