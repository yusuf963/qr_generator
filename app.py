import qrcode
import qrcode.image.svg
# Link for website
url = "https://www.instagram.com/nunoalecrim/"
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('nuno_qr.gif')
#Generate svg format file
factory = qrcode.image.svg.SvgImage
svg_image = qrcode.make(url, image_factory = factory)
img.save('nuno_qr.svg')