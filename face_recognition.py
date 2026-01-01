import cv2
import os
import numpy as np

DATASET_PATH = r"C:\Users\gaytr\OneDrive\Desktop\OpenCV\archive\Dataset\Faces"


faces = []
labels = []
label_map = {}
label_id = 0

for person_name in os.listdir(DATASET_PATH):
    person_path = os.path.join(DATASET_PATH, person_name)

    if not os.path.isdir(person_path):
        continue

    label_map[label_id] = person_name

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)

        # Skip folders
        if not img_name.lower().endswith(('.jpg', '.png', '.jpeg')):
            continue

        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            continue

        img = cv2.resize(img, (200, 200))

        faces.append(img)
        labels.append(label_id)

    label_id += 1

print("Faces loaded:", len(faces))
print("Classes:", len(label_map))

if len(faces) == 0:
    print("❌ No images loaded. Check dataset structure.")
    exit()

# Train model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))
recognizer.save("face_model.yml")

print("✅ Model trained successfully")

#Test on one image
# Test on one image (NO face detection needed)

test_img = cv2.imread("test.jpg")

if test_img is None:
    print("❌ Test image not found")
    exit()

gray_test = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
gray_test = cv2.resize(gray_test, (200, 200))

label, confidence = recognizer.predict(gray_test)
name = label_map[label]

print(f"Predicted: {name}")
print(f"Confidence: {confidence:.2f}")

cv2.putText(
    test_img,
    f"{name} ({int(confidence)})",
    (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)

cv2.imshow("Result", test_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
