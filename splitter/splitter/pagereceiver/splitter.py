#!/usr/bin/python3
# 2018.01.16 01:11:49 CST
# 2018.01.16 01:55:01 CST
import cv2
import numpy as np




# def hor_norm(upper,lower,tlr):
# 	telorance = tlr
# 	t=[]
# 	ret1=[]
# 	ret2=[]

# 	for i in range(0, len(upper)-1):
# 		if( abs(upper[i] - upper[i+1]) < telorance ):
# 			t.append(upper[i])
# 		if( abs(upper[i] - upper[i+1]) < telorance ):
# 			t.append(lower[i])

# 	for x in upper:
# 		if (x not in t):
# 			ret1.append(x)

# 	for i in range(0, len(lower)-1):
# 		if( abs(lower[i] - lower[i+1]) < telorance ):
# 			t.append(lower[i+1])

# 	for x in lower:
# 		if (x not in t):
# 			ret2.append(x)

# 	return ret1,ret2

def hor_norm(upper,lower,tlr):
	telorance = tlr
	t=[]
	ret1=[]
	ret2=[]

	for i in range(0, len(lower)-1):
		if( abs(lower[i] - upper[i+1]) < telorance ):
			t.append(lower[i])
			t.append(upper[i+1])

	for x in upper:
		if (x not in t):
			ret1.append(x)

	for x in lower:
		if (x not in t):
			ret2.append(x)

	return ret1,ret2


def ver_norm(upper,lower,tlr):
	telorance = tlr
	t=[]
	ret1=[]
	ret2=[]

	for i in range(0, len(lower)-1):
		if( abs(lower[i] - upper[i+1]) < telorance ):
			t.append(lower[i])
			t.append(upper[i+1])

	for x in upper:
		if (x not in t):
			ret1.append(x)


	for x in lower:
		if (x not in t):
			ret2.append(x)

	return ret1,ret2


telorance = 15


## (1) read
img = cv2.imread("t.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## (2) threshold
th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

## (3) minAreaRect on the nozeros
pts = cv2.findNonZero(threshed)
ret = cv2.minAreaRect(pts)

(cx,cy), (w,h), ang = ret
if w>h:
	w,h = h,w
	ang += 90

## (4) Find rotated matrix, do rotation
M = cv2.getRotationMatrix2D((cx,cy), ang, 1.0)
rotated = cv2.warpAffine(threshed, M, (img.shape[1], img.shape[0]))



cv2.imwrite("rotated1.png", rotated)

## (5) find and draw the upper and lower boundary of each lines
hist = cv2.reduce(rotated,1, cv2.REDUCE_MAX).reshape(-1)

th = 2
H,W = img.shape[:2]
puppers = [y for y in range(H-1) if hist[y]<=th and hist[y+1]>th]
# uppers = upper_norm(puppers)
plowers = [y for y in range(H-1) if hist[y]>th and hist[y+1]<=th]
# lowers = lower_norm(plowers)

uppers,lowers = hor_norm(puppers,plowers,7)

print("after edit")

cropped = rotated[uppers[4]:lowers[4] , 0:W]

cropped = cv2.flip(cropped, 1 )

hist2 = cv2.reduce(cropped,0, cv2.REDUCE_AVG).reshape(-1)

# print("afterx")

xH,xW = cropped.shape[:2]
pxuppers = [x for x in range(xW-1) if hist2[x]<=th and hist2[x+1]>th]
pxlowers = [x for x in range(xW-1) if hist2[x]>th and hist2[x+1]<=th]

xuppers,xlowers = ver_norm(pxuppers,pxlowers,10)

cropped2 = cropped[0:xH, xuppers[4]:xlowers[4]]
cv2.imwrite("cropped2.jpg", cropped2)

rotated = cv2.cvtColor(rotated, cv2.COLOR_GRAY2BGR)

print("puppers")
print(puppers)
print(plowers)
print("uppers")
print(uppers)
print(lowers)
# print("xuppers")
# print(xuppers)
# print(xlowers)

# print("HW")
# print(H)
# print(W)
# print("xHW")
# print(xH)
# print(xW)

print("hist")
print(len(hist))
print(hist)
print("hist2")
print(len(hist2))
print(hist2)



cropped = cv2.cvtColor(cropped, cv2.COLOR_GRAY2BGR)


#horizental lines 
for y in uppers: #upper(blue)
	cv2.line(rotated, (0,y), (W, y), (255,0,0), 1)

for y in lowers:
	cv2.line(rotated, (0,y), (W, y), (0,255,0), 1)


#vertical lines
for y in xuppers:
	cv2.line(cropped, (y,0), (y, xH), (255,0,0), 1)

for y in xlowers:
	cv2.line(cropped, (y,0), (y, xH), (0,255,0), 1)


cv2.imwrite("result1.png", rotated)
cv2.imwrite("cropped1.png", cropped)
# cv2.imwrite("rotated90.jpg", rotated90)


