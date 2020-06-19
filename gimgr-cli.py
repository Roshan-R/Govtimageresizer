import argparse
from PIL import Image


def cal(img,max_width,max_height):
        width,height = img.size
        ratio = width/height
        if width > height:
            width = max_width
            height = int(width/ratio) 
        else:
            height = max_height
            width = int(height*ratio)
        return width, height

def save(img, image, output):
    if '.' in output:
        if output.split('.')[1] != image.split('.')[1]:
            print("Not the same extension !")
            exit()
    else:
        output += '.' + image.split('.')[1]
    img.show()
    print(output)
    img.save(output)

def pdf(image):
    img = Image.open(image)
    if not img:
        print("The file does not exist")
        exit()
    extension = 'pdf'
    pdf = img.convert('RGB')
    save(pdf, image, extension)
    print("\nCreated .pdf file sucessfully !")

def pixel(image, max_width, max_height, aspect_ratio, output):
    img = Image.open(image)
    if not img:
        print("The file does not exist")
        exit()
    width,height = img.size
    print(img)
    extension = image.split('.')[1]
    #preserving aspect ratio
    if aspect_ratio:
        reqwidth,reqheight = cal(img,max_width,max_height)
        img = img.resize((reqwidth,reqheight), Image.ANTIALIAS)
        save(img, image, output)  
    #not preserving aspect ratio
    else:
        img = img.resize((max_width,max_height),Image.ANTIALIAS)
        save(img, image, output)

def main():

    parser = argparse.ArgumentParser(prog="gimgr",description="an image manipulation tool")

    main_group = parser.add_mutually_exclusive_group()
    group = parser.add_mutually_exclusive_group()
    main_group.add_argument('-p', '--pixel', action='store_true', help="to specify pixel argument")
    main_group.add_argument('-f', '--file', action = 'store_true', help="to specify file argument")
    group.add_argument('-d', '--dimension',metavar='',  help="specify dimensions")

    parser.add_argument('-a', '--preserve', action='store_true', help="whether to preserve aspect ratio of not")
    parser.add_argument('-c', '--convert', action='store_true', help="converts given file to pdf")
    parser.add_argument('-i', '--input', metavar='', help="Name of input file")
    parser.add_argument('-o', '--output', metavar='', help="Output filename", required='True')
    
    args = parser.parse_args()

    if args.pixel:
        if args.file:
            print("Invalid input format")
            print("Use -h or --help for help")
            exit()
        if not args.dimension:
            print('You need to specify the dimension for pixel ')
        else:
            print("you've chosen p")
            dimension = args.dimension
            pixel(args.input,int(dimension.split('x')[0]), int(dimension.split('x')[1]), args.preserve, args.output)
    elif args.convert:
        pdf(args.input)
    else:
        print("Nothin here :(")
    
if __name__ == "__main__":
    main()
