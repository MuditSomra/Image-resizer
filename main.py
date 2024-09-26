import cv2
print(cv2.__version__)
image = cv2.imread("bhisham.jpg")
# cv2.imshow('Image Window',image)

def resize(width,height):
    return cv2.resize(image,(width,height))

def flip(x):
    return cv2.flip(image,x)

def drawLine(x1,y1,x2,y2,r,g,b,thicknessVal):
    return cv2.line(image,(x1,y1),(x2,y2),(r,g,b),thickness=thicknessVal)

def drawCircle(x,y,radius,r,g,b,thicknessVal):
    return cv2.circle(image, (x,y), radius, (r,g,b), thickness=thicknessVal)

def drawRectangle(x1,x2,y1,y2,r,g,b,thicknessVal):
    return cv2.rectangle(image, (x1,y1), (x2,y2), (r,g,b), thickness=thicknessVal)

# res_img = resize(133,132)
# new_line_img = drawLine(3,5,644,333,333,0,4,2)
new_rect_img = drawRectangle(2,4,133,3333,33,234,33,774)


cv2.waitKey(0)
cv2.destroyAllWindows()
