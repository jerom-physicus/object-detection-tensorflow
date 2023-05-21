import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

video = cv2.VideoCapture(0)
labels = []
while True:
    ret, frame = video.read()

    bbox, label, conf = cv.detect_common_objects(frame)

    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Detection", output_image)

    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

print(f"I found a {label},")




