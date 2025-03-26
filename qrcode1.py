import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def generate_qr(student_name, student_id, dob, admission_no, filename="student_qr.png"):
    """Generates a QR code with student details and saves it as an image."""
    data = f"Name: {student_name}\nID: {student_id}\nDOB: {dob}\nAdmission No: {admission_no}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR Code saved as {filename}")

def read_qr(filename):
    """Reads and decodes the QR code from an image file."""
    img = Image.open(filename)
    decoded_data = decode(img)
    
    if decoded_data:
        return decoded_data[0].data.decode("utf-8")
    else:
        return "No QR code found."

# Example Usage
generate_qr("John Doe", "12345", "2002-05-15", "A001")
print("Decoded Data:")
print(read_qr("student_qr.png"))
