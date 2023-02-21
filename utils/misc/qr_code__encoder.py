import cv2


# read the QRCODE image


def qr_decode(filename: str):
    print(filename)
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    # if there is a QR code
    # print the data
    if vertices_array is not None:
        print("QRCode data:")
        return data
    else:
        return "QR kod aniqlanmadi!"