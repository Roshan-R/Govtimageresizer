from PIL import Image

def resize():
    basewidth = 200
    img = Image.open('image.png')
    img.show()


def pixel():
    img = Image.open('image.png')
    max_width = int(input("\nEnter the max width :"))
    max_height = int(input("Enter the max height : "))
    width,height = img.size
    selection = input("\nDo you want to preserve the aspect ratio? (Y/n) : ")
    if selection == 'n' or selection == 'N' :
        img = img.resize((max_width,max_height),Image.ANTIALIAS)
        img.show()
    elif selection == 'y' or selection == 'Y':
        basewidth = max_width
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.show()

    
def main():
    print("Welcome to the image resizer tool !")
    print("\n1 - Resize image pixels\n2 - Resize image file size\n3 - Change the extension\n")
    selection = int(input("Enter any one of the selection (1-3) : "))
    if selection == 1:
        pixel()
main()

