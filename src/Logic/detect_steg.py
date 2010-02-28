'''
Created on Feb 27, 2010

@author: Zachary Varberg
'''

from PIL import Image
from Logic import Steganography as Steg
import re
import math

TWL = open('TWL06.txt')
TWL_words = TWL.read().split()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

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
                        binnum = Steg.Dec2Bin(pixel[i])
                        data = binnum[-bit_list[i]:]
                        forw_char_byte.extend(data)
                        data.reverse()
                        back_char_byte.extend(data)
                        if len(back_char_byte)>=8:
                            back_char_data.append(chr(Steg.Bin2Dec(''.join(back_char_byte[:8]))))
                            back_char_byte = back_char_byte[8:]
                        if len(forw_char_byte)>=8:
                            forw_char_data.append(chr(Steg.Bin2Dec(''.join(forw_char_byte[:8]))))
                            forw_char_byte = forw_char_byte[8:]
                for char in back_char_data:
                    if re.match('[a-zA-Z0-9 \n\r=+-]',char):
                        char_count += 1
                if binomial_probability(len(back_char_data),char_count) < .00001:
                    word_list = ''.join(back_char_data).upper().split()
                    if True in [x in TWL_words for x in word_list]:
                        probable_encodings['backward'].append(tuple(bit_list))
                char_count = 0
                for char in forw_char_data:
                    if re.match('[a-zA-Z0-9 \n\r=+-]',char):
                        char_count += 1
                if binomial_probability(len(forw_char_data),char_count) < .00001:
                    word_list = ''.join(forw_char_data).upper().split()
                    if True in [x in TWL_words for x in word_list]:
                        probable_encodings['forward'].append(tuple(bit_list))
    return probable_encodings
                    
                
def binomial_probability(n,k):    
    bin_coeff = (factorial(n)*1.0)/(factorial(k)*factorial(n-k))
    prob = bin_coeff * pow((67.0/256),k) * pow((1 - (67.0/256)),(n-k))
    return prob
                    
if __name__ == "__main__":
    print dictionary_steg_detect("C:\Documents And Settings\Zachary Varberg\Projects"+
                           "\Python\Steganogra-py\src\Resources\\asdf1.png")