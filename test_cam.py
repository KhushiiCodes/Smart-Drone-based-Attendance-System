import cv2

# Try multiple camera indexes
for i in range(5):
    print(f"Checking camera index {i}...")

    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)

    if cap.isOpened():
        print(f"✅ Camera found at index {i}")

        while True:
            ret, frame = cap.read()

            if not ret:
                print("❌ Failed to grab frame")
                break

            cv2.imshow(f"Camera Index {i}", frame)

            # Press ESC to exit
            if cv2.waitKey(1) == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
        break
    else:
        print(f"❌ No camera at index {i}")