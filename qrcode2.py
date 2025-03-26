import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import cv2

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

def read_qr_from_image(filename):
    """Reads and decodes the QR code from an image file."""
    img = Image.open(filename)
    decoded_data = decode(img)
    
    if decoded_data:
        return decoded_data[0].data.decode("utf-8")
    else:
        return "No QR code found."

def scan_qr_with_camera():
    """Scans a QR code using the device camera."""
    cap = cv2.VideoCapture(0)
    print("Scanning for QR code... Press 'q' to exit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_data = obj.data.decode("utf-8")
            print("QR Code Data:", qr_data)
            cap.release()
            cv2.destroyAllWindows()
            return qr_data
        
        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return "No QR code detected."

# Example Usage
generate_qr("John Doe", "12345", "2002-05-15", "A001")
print("Decoded Data from Image:")
print(read_qr_from_image("student_qr.png"))

print("Scanning QR Code from Camera:")
print(scan_qr_with_camera())
