'''
Copyright (C) 2010 Zachary Varberg
@author: Zachary Varberg

This file is part of Steganogra-py.

Steganogra-py is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Steganogra-py is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Steganogra-py.  If not, see <http://www.gnu.org/licenses/>.
'''
from PIL import Image

class FileTooLargeException(Exception):
    '''
    Custom Exception to throw if the file is too large to fit in 
    the Image file specified
    ''' 
    pass


def dec_2_bin(n):
    '''
    Function to convert an integer to a string of 1s and 0s that is the
    binary equivalent.
    '''
    return list(bin(n)[2:].zfill(8))

def bin_2_dec(n):
    '''
    Function that takes a string of 1s and 0s and converts it back to an
    integer
    '''
    return int(n,2)

def encode(im_file, en_file, red_bits=1, green_bits=1, blue_bits=1):
    ''' 
    im_file is a string that is the file name of the image to 
    encode the data into.  The data comes from en_file.  Currently
    only character data is supported.  The red, green, and blue bits
    variables determine how many bits of each color to encode the data
    into.
    '''
    in_image = Image.open(im_file,'r')
    data_file = open(en_file,'rb')
    data = ""
    for line in data_file:
        for char in line:
            data += "".join(dec_2_bin(ord(char)))
    # Termination characters
    data+= "".join(dec_2_bin(255)) + "".join(dec_2_bin(255))
    
    color_bits = [red_bits, green_bits, blue_bits]
    i = 0;
    curCol = 0;
    out_image = in_image.copy()
    x = -1
    y = -1
    for pixel in in_image.getdata():
        # This will hold the new array of R,G,B colors with the 
        # embedded data
        new_col_arr = []
        
        x = (x + 1)%out_image.size[0]
        if x == 0:
            y += 1
            
        for color in pixel:
            new_col = 0
            # if we still have data to encode
            if(i < len(data)):
                
                # Number of bits to encode for this color
                bits = color_bits[curCol%3]

                # Encode the number of bits requested
                tmp_color = dec_2_bin(color)
                
                tmp = list(data[i:i+bits])
                tmp.reverse()
                tmp_color[-bits:]=tmp
                i+=bits
                
                #Pull out a new int value for the encoded color
                new_col = bin_2_dec("".join(tmp_color))
            else:
                new_col = color
            
            # Append the new color to our new pixel array
            new_col_arr.append(new_col)
            curCol +=1
        
        # Append the new 3 color array to our new image data
        out_image.putpixel((x,y),tuple(new_col_arr))
    
    # If there wasn't enough pixels to encode all the data.
    if i != len(data):
        raise FileTooLargeException("Image to small for current settings.")

    return out_image
    
def decode(im_dec, red_bits=1, green_bits=1, blue_bits=1):
    '''
    Inverse of decode.  im_dec is the image file with the encoded data.
    red_bits, green_bits, and blue_bits are the number of each color bit
    that was encoded in the image.  It is important that these match the 
    values specified when encode was called, otherwise the output will be 
    garbage.  This method will return a string that is the character data
    encoded in the file.
    '''
    in_image = Image.open(im_dec)

    # Number of consecutive ones to track if we've found the termination
    # characters
    num_ones = 0
    
    # The data pulled out
    data = []
    
    tmp_list = []
    color_bits = [red_bits, green_bits, blue_bits]
    try:
        for pixel in in_image.getdata():
            i = 0
            for color in pixel:
                tmp_color = list(dec_2_bin(color))
                
                bits = color_bits[i%3]

                # Pull out the specified number of bits based on the color
                tmp = tmp_color[-bits:]
                tmp.reverse()
                tmp_list.extend(tmp)
                
                # If we have a full bit or more add the bit to the data
                if len(tmp_list)>=8:
                    data.append(tmp_list)
                    tmp_list = tmp_list[8:]
                
                # If we've had 16 ones in a row quit looking
                if len(data)>=2 and sum((int(x) for x in data[-1]))==8:
                    if sum((int(x) for x in data[-2]))==8:
                        raise StopIteration
                i += 1
                
    except StopIteration:
        pass
    
    
    chars = ""
    for char in data[:-1]:
        tmp_color = chr(bin_2_dec("".join(char)))
        if(ord(tmp_color)!=255):
            chars+=tmp_color
        
    return chars

def save_file(data, file_name):
    '''
    This will write all of the information in data (currently only
    character data is tested) and save it to the file file_name
    '''
    out_file = open(file_name,'wb+')
    out_file.write(data)
    out_file.close()

if __name__ == '__main__':
    pass
#    encode('flower.png','Macbeth.txt',0,1,6).save('newOut.png')
#    save_file(decode('newOut.png',0,1,6),'newOut1.txt')

