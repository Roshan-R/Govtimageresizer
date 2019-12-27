from PIL import Image
import os.path
import sys

#function to calculate the best width and height for the image

def cal(img,basewidth,max_height):
        width,height = img.size
        while True:
            #to maintain aspect ratio
            wpercent = (basewidth/float(img.size[0]))
            height = int((float(img.size[1])*float(wpercent)))
            if height > max_height:
                basewidth = basewidth - 1
            else:
                break
        return width,height

def save(img,extension):
    dest = input("\nEnter the destinantion file name : ")
    if os.path.exists(dest+'.'+extension):
        print("This file already exists")
        save(img)
    img.show()
    img.save(dest+'.'+extension)

def pdf(img):
    extension = 'pdf'
    pdf = img.convert('RGB')
    save(pdf,extension)

def pixel(img,extension):
    max_width = int(input("\nEnter the max width :"))
    max_height = int(input("Enter the max height : "))
    width,height = img.size
    selection = input("\nDo you want to preserve the aspect ratio? (Y/n) : ")
    #not preserving aspect ratio
    if selection == 'n' or selection == 'N' :
        img = img.resize((max_width,max_height),Image.ANTIALIAS)
        save(img,extension)
    #preserving aspect ratio
    elif selection == 'y' or selection == 'Y':
        reqwidth,reqheight = cal(img,max_width,max_height)
        img = img.resize((reqwidth,reqheight), Image.ANTIALIAS)
        save(img,extension)  
def main():
    img = Image.open(sys.argv[1])
    if not img:
        print("The file does not exist")
        exit()
    print("Welcome to the image resizer tool !")
    print("\n1 - Resize image pixels\n2 - Resize image file size\n3 - Convert to pdf\n")
    selection = int(input("Enter any one of the selection (1-3) : "))
    extension = sys.argv[1].split('.')[1]
    if selection == 1:
        pixel(img,extension)
    if selection == 3:
        pdf(img)
main()

