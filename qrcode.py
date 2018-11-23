import pyqrcode


def qrcode():
     q=pyqrcode.create('QR Code Generated:')
     q.png('QR_Code.jpg',scale=10)
     print('QR Code Generated...')

if __name__=='__main__':
    qrcode()
