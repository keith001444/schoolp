import sqlite3

def insert_image(db_path, admission_no, image_file):
    if image_file and image_file.filename:
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Read the image file as binary
            image_data = image_file.read()  # Directly read from the file object

            # Update the image where admission_no matches
            cursor.execute("UPDATE students SET profile_pic = ? WHERE admission_no = ?", 
                           (image_data, admission_no))

            conn.commit()
            conn.close()
            print("Image inserted successfully!")
        except Exception as e:
            print("Error inserting image:", e)
    else:
        print("No image file provided!")

def insert_image_t(db_path, username, image_file):
    if image_file and image_file.filename:
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Read the image file as binary
            image_data = image_file.read()  # Directly read from the file object

            # Update the image where admission_no matches
            cursor.execute("UPDATE admin_data SET profile_picture = ? WHERE position = ?", 
                           (image_data, username))

            conn.commit()
            conn.close()
            print("Image inserted successfully!")
        except Exception as e:
            print("Error inserting image:", e)
    else:
        print("No image file provided!")
