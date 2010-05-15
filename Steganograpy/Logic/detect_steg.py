'''
Created on Feb 27, 2010

@author: Zachary Varberg
'''
import re
import math

from PIL import Image, ImageOps
from Logic import steganography as Steg
from scipy import stats

TWL = open('../Logic/TWL06.txt')
TWL_words = TWL.read().split()

def dictionary_steg_detect(image):
    my_image = Image.open(image)
    pixels = my_image.load()
    probable_encodings = {'forward':[],'backward':[]}

    for red_bits in xrange(1,5):
        for green_bits in xrange(1,5):
            for blue_bits in xrange(1,5):
                bit_list = [red_bits, green_bits, blue_bits]
                back_char_data = []
                forw_char_data = []
                back_char_byte = []
                forw_char_byte = []
                char_count = 0
                for x in xrange(int(math.ceil((240.0/sum(bit_list))))):
                    pixel = pixels[x,0]
                    for i in xrange(3):
                        binnum = Steg.dec_2_bin(pixel[i])
                        data = binnum[-bit_list[i]:]
                        forw_char_byte.extend(data)
                        data.reverse()
                        back_char_byte.extend(data)
                        if len(back_char_byte)>=8:
                            back_char_data.append(chr(Steg.bin_2_dec(''.join(back_char_byte[:8]))))
                            back_char_byte = back_char_byte[8:]
                        if len(forw_char_byte)>=8:
                            forw_char_data.append(chr(Steg.bin_2_dec(''.join(forw_char_byte[:8]))))
                            forw_char_byte = forw_char_byte[8:]
                for char in back_char_data:
                    if re.match('[a-zA-Z0-9 \n\r=+-]',char):
                        char_count += 1
                if stats.binom_test(char_count, len(back_char_data),67.0/256) < .00001:
                    word_list = ''.join(back_char_data).upper().split()
                    if any(x in TWL_words for x in word_list):
                        probable_encodings['backward'].append(tuple(bit_list))
                char_count = 0
                for char in forw_char_data:
                    if re.match('[a-zA-Z0-9 \n\r=+-]',char):
                        char_count += 1
                if stats.binom_test(char_count, len(forw_char_data),67.0/256) < .00001:
                    word_list = ''.join(forw_char_data).upper().split()
                    if any(x in TWL_words for x in word_list):
                        probable_encodings['forward'].append(tuple(bit_list))
    return probable_encodings

def noise_steg_detect(image):
    orig_image = Image.open(image)
    equal_image = Image.open(image)
    
    equal_image = ImageOps.grayscale(equal_image)
    equal_image = ImageOps.equalize(equal_image)

    orig_image.show()
    equal_image.show()
                    
if __name__ == "__main__":
    print dictionary_steg_detect("C:\Documents And Settings\Zachary Varberg\Projects"+
                           "\Python\Steganogra-py\Steganograpy\Resources\\asdf1.png")