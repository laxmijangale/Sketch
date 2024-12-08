import cv2
import os

# Image path
image_path = r"C:\Users\91726\OneDrive\Desktop\Python\Original_img.jpg"

# Read the image
img = cv2.imread(image_path)
if img is None:
    print("Error: Could not read the image. Check the file path.")
else:
    try:
        # Step 1: Convert the image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Step 2: Invert the grayscale image
        inverted_img = cv2.bitwise_not(gray_img)

        # Step 3: Blur the inverted image
        blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), sigmaX=0, sigmaY=0)

        # Step 4: Invert the blurred image
        inverted_blurred_img = cv2.bitwise_not(blurred_img)

        # Step 5: Create the pencil sketch
        sketch_img = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)

        # Display the results
        cv2.imshow("Original Image", img)
        cv2.imshow("Pencil Sketch", sketch_img)

        # Save the sketch
        output_dir = r"C:\Users\91726\OneDrive\Desktop\Python"
        output_path = os.path.join(output_dir, "sketch_results.jpg")

        # Ensure directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save the image
        if cv2.imwrite(output_path, sketch_img):
            print(f"Sketch saved successfully at {output_path}")
        else:
            print("Error: Failed to save the sketch.")

        # Wait and close the windows
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An error occurred: {e}")
