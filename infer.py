import cv2

path_to_img = "/home/reza/projects/mine_teeth/YOLO_DATA/test/0277_jpg.rf.5ce1f22a0e596c40a1e0f0d901a42f73.jpg"
path_to_gt = "/home/reza/projects/mine_teeth/YOLO_DATA/test/0277_jpg.rf.5ce1f22a0e596c40a1e0f0d901a42f73.txt"

img = cv2.imread(path_to_img)

with open(path_to_gt) as h:
    gt = [l.strip() for l in h.readlines()]

for bbox in gt:
    bbox = [float(b) for b in bbox.split(" ")]

    x = bbox[1] * img.shape[1]
    y = bbox[2] * img.shape[0]
    w = bbox[3] * img.shape[1]
    h = bbox[4] * img.shape[0]

    top_left_x = int(x - w / 2)
    top_left_y = int(y - h / 2)
    bot_right_x = int(x + w / 2)
    bot_right_y = int(y + h / 2)

    cv2.rectangle(img, (top_left_x, top_left_y), (bot_right_x, bot_right_y), (255,0,0), 1)

cv2.imwrite("SSS.jpg", img)






