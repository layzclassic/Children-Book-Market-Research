from PIL import Image, ImageDraw
import csv



def main(image_path, outfile, text_path):
    #confirm image size

    #open excel sheet according to chapter

    #print text to image and save to directory
    print_text()
    print('done')

def print_text():
    W, H = (300, 200)
    msg = "hello"

    im = Image.new("RGBA", (W, H), "yellow")
    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(msg)
    draw.text(((W - w) / 2, (H - h) / 2), msg, fill="black")

    im.save("hello.png", "PNG")

if __name__ == '__main__':
    chapter = str(1)
    image_path = '/images/Chapter {}/raw'.format(chapter)
    outfile = '/images/Chapter {}/text'.format(chapter)
    text_path = 'dialogue.xlsx'
    main(image_path, outfile, text_path)



