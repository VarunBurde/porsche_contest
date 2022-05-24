# Import modules
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


# Initialize camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# Let camera warm up
time.sleep(0.3)
print("Press q to quit")

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    
    height = image.shape[0]
    width = image.shape[1]

    region_of_interest_vertices = [
    (0, height),
    (width/2, height/2),
    (width, height)
]
    
    cropped_image = region_of_interest(image,
                np.array([region_of_interest_vertices], np.int32),)
    
    cv2.imshow("Preview", image)
    
        
    
    rawCapture.truncate(0)

    key = cv2.waitKey(1)
    if key == ord("q"):
        print("Quitting")
        break

cv2.destroyAllWindows()
camera.close()


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    channel_count = img.shape[2]
    match_mask_color = (255,) * channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image



