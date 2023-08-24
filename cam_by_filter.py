### Homwork #1

## Import Packages

import cv2
import numpy as np
import datetime 

## Webcam

cap = cv2.VideoCapture(0)
name = input("Enter Your Name Please : ")

# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print(width, height)

while True:
	ret, frame = cap.read()

	if ret:

		# Create Filters

		normal_frame = cv2.flip(frame, 1)

		red_filter = normal_frame.copy()
		red_filter[:, :, 2] = 255

		inverse_filter = 255 - normal_frame

		gray = cv2.cvtColor(normal_frame, cv2.COLOR_BGR2GRAY)
		gray_filter = np.expand_dims(gray, axis = 2)
		gray_filter = np.concatenate([gray_filter, gray_filter, gray_filter], 2)

		image1 = np.concatenate([normal_frame, red_filter], 1)
		image2 = np.concatenate([inverse_filter, gray_filter], 1)

		img = np.concatenate([image1, image2], 0)

		# Describe Name And Time In Stream

		font = cv2.FONT_HERSHEY_SIMPLEX
		date_time = str(datetime.datetime.now())
		cv2.putText(img, date_time,(15, 25),
					font, 0.8, (0, 0, 255), 2)

		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, name,(15, 50),
					font, 0.8, (0, 0, 255), 2)

		# Show Camera

		img_resize = cv2.resize(img, None, fx = 0.75, fy = 0.75)
		cv2.imshow("Laptop WebCam", img_resize)
		q = cv2.waitKey(1)

		if q == ord('q') or q == ord('Q'):
			break

cap.release()
cv2.destroyAllWindows()
