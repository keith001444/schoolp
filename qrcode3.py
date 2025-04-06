import sqlite3
import qrcode
import io
import cv2
from PIL import Image
from pyzbar.pyzbar import decode


def generate_qr_st(fname, lname, dob, admission_no, grade):
    """Generates a QR code with student details and saves it to the SQLite database."""
    data =f"School: Chuka University\nFirst Name: {fname}\nLast Name: {lname}\nAdmission Date: {dob}\nAdmission No: {admission_no}\nClass: {grade}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')

    # Convert the image to binary data
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_data = img_byte_arr.getvalue()

    # Store in SQLite database
    conn = sqlite3.connect("student.db")  # Update with your database file
    cursor = conn.cursor()
    
    cursor.execute("UPDATE students SET qrcode_st = ? WHERE admission_no = ?", (img_data, admission_no))
    conn.commit()
    conn.close()

    print("QR Code saved to the database.")

def scan_qr_with_camera():
    """Scans a QR code using the device camera and ensures it reopens properly."""
    while True:  # Ensure the camera can restart each time
        cap = cv2.VideoCapture(0)  # Open camera every time function is called
        print("Scanning for QR code... Press 'q' to exit.")
        
        while cap.isOpened():  # Make sure the camera is active
            ret, frame = cap.read()
            if not ret:
                break

            decoded_objects = decode(frame)
            for obj in decoded_objects:
                qr_data = obj.data.decode("utf-8")
                cap.release()  # Release camera
                cv2.destroyAllWindows()  # Close the scanning window
                False
                return qr_data  # Return detected QR code
            
            cv2.imshow("QR Code Scanner", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()  # Ensure camera is released if loop exits
        cv2.destroyAllWindows()
        print("Restarting scanner...")


def qr_gate_access(data):
    try:
        new_data = data.split()
        if " ".join(new_data[1:3]) == "Chuka University":
            return "access granted"
        else:
            return "Please see the Admin"
    except IndexError:
        return "Please consult with admin"


def qr_class_access(data,the_class):
    try:
        if new_data[16] == the_class:
            return "access granted"
        else:
            return "please contact the admin"
    except IndexError:
        return "please consult with admin"
