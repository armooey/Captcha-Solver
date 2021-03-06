from pytesseract import image_to_string
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
from PIL import ImageEnhance

#This function returns the result of Tesseract
def ocr(im):
    return image_to_string(im, lang="Captcha", config="--psm 10 -c tessedit_char_whitelist=ABCDEFGHJKLMNOPRSTUVWXZ")

#Removing Background Color From Left to Right
def rem_back(trg):
    cnt = ImageEnhance.Contrast(trg)
    trg = trg.filter(ImageFilter.MedianFilter(3))
    trg = cnt.enhance(1)
    mat = trg.load()
    tol = 10
    cn = 0
    for r in range(0, trg.height):
        temp = mat[0, r][0]
        for c in range(0, trg.width):
            if (mat[c, r][0] <= temp + tol and mat[c, r][0] >= temp - tol):
                mat[c, r] = (255, 255)
    return trg

#Removing Background Color From Right to Left
def rem_back_rev(trg):
    cnt = ImageEnhance.Contrast(trg)
    trg = trg.filter(ImageFilter.MedianFilter(3))
    trg = cnt.enhance(1)
    mat = trg.load()
    tol = 10
    cn = 0
    for r in range(trg.height - 1, -1, -1):
        temp = mat[trg.width - 1, r][0]
        for c in range(trg.width - 1, -1, -1):
            if (mat[c, r][0] <= temp + tol and mat[c, r][0] >= temp - tol):
                mat[c, r] = (255, 255)
    return trg


#Making Characters ready for OCR
def char_op(trg):
    trg = rem_back(trg)
    trg = rem_back_rev(trg)
    cnt = ImageEnhance.Contrast(trg)
    trg = cnt.enhance(2)
    trg = trg.filter(ImageFilter.MedianFilter(9))
    trg = trg.filter(ImageFilter.RankFilter(5,3))
    br = ImageEnhance.Brightness(trg)
    trg = br.enhance(1)
    trg = trg.convert("RGB")
    trg = ImageOps.expand(trg, 30, 'white')
    return trg

#################################################
#################################################
################Driver Code######################
#################################################
#################################################
im = Image.open("Address to image").convert("LA")
im = im.crop((1, 5, 149, 35))
im = im.resize((5 * im.width, 5 * im.height), Image.ANTIALIAS)
im = im.filter(ImageFilter.MedianFilter(3))
im = im.filter(ImageFilter.GaussianBlur(3))
im = im.filter(ImageFilter.MedianFilter(5))
im = im.filter(ImageFilter.SMOOTH_MORE)
cnt = ImageEnhance.Contrast(im)
im = cnt.enhance(1)
a = im.crop((0, 0, 148, 150))
b = im.crop((148, 0, 296, 150))
c = im.crop((296, 0, 444, 150))
d = im.crop((444, 0, 592, 150))
e = im.crop((592, 0, 740, 150))
#For not displaying the result of Image processing juct comment .show() lines
a = char_op(a)
a.show()
b = char_op(b)
b.show()
c = char_op(c)
c.show()
d = char_op(d)
d.show()
e = char_op(e)
e.show()
print(ocr(a) + ocr(b) + ocr(c) + ocr(d) + ocr(e))
