import io
import socket
import struct
import cv2
import ImageProcessing
import emailer


def process_image(image):
    faces = ImageProcessing.detect_faces(image)
    print("Processed image.")
    if len(faces) > 0:
        print("Sending email.")
        _, encoded_img = cv2.imencode(".png", image)
        emailer.sendMail(["brian.semrau@gmail.com"], "Test Server Msg", "This is the content", [encoded_img])


soc = socket.socket()
soc.bind(('0.0.0.0', 42069))
soc.listen(0)

connection = soc.accept()[0].makefile('rb')
try:
    while True:
        length = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not length:
            break

        stream = io.BytesIO()
        stream.write(connection.read(length))
        stream.seek(0)
        image = cv2.imdecode(stream, 1)

        process_image(image)
finally:
    connection.close()
    soc.close()
