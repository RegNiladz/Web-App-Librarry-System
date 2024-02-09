import subprocess
import qrcode
from PIL import Image,ImageDraw, ImageFont
import sys
class qr_generate:
    
    def __init__(self, file_name, file_path) -> None:
        self.file_name = file_name
        self.file_path = file_path
    
    def make_qr(self):
        qrfile_path = f'{self.file_path}/{self.file_name}.png'
        qr = qrcode.make(self.file_name)
        qr.save(qrfile_path)
        edit_qr = Image.open(qrfile_path)
        img_width, img_height = edit_qr.size
        generate_newqr = ImageDraw.Draw(edit_qr)
        font_style = ImageFont.load_default()
        generate_newqr.text((35,img_height - 35),self.file_name, font=font_style)
        edit_qr.save(qrfile_path)
        json_obj = {
            'filepath' : self.file_path,
            'filename' : self.file_name
        }
        print(json_obj)
if __name__ == '__main__':
    args = sys.argv
    qr_obj = qr_generate(args[1], args[2])
    #qr_obj = qr_generate("xd", "qrcode_pictures")
    qr_obj.make_qr()


 