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

def encode(im_file, en_file, color_bits=[1,1,1], forward=True):
    ''' 
    im_file is a string that is the file name of the image to 
    encode the data into.  The data comes from en_file.  Currently
    only character data is supported.  The bits list is how many bits 
    of each color to encode the data into.  In the form 
    [red_bits, green_bits, blue_bits]
    '''
    in_image = Image.open(im_file,'r')
    data_file = open(en_file,'rb')
    data = ""
    for line in data_file:
        for char in line:
            data += "".join(dec_2_bin(ord(char)))
    # Termination characters
    data+= "".join(dec_2_bin(255)) + "".join(dec_2_bin(255))
    
    check_size(len(data), in_image, sum(color_bits))
    
    curCol = i = 0;
    out_image = in_image.copy()
    x = y = -1
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
                
                # get the next bits (number) bits from data, reverse (may change) them and
                # assign them to the last bits (number) bits of the current color.
                if i+bits > len(data):
                    diff = i+bits - len(data)
                    data += ('1'*diff)
                
                if forward:
                    tmp_color[-bits:] = data[i:i+bits]
                else:
                    tmp_color[-bits:] = reversed(data[i:i+bits])
                
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
    
def decode(im_dec, color_bits=[1,1,1], forward=True):
    '''
    Inverse of decode.  im_dec is the image file with the encoded data.
    The bits list are the number of each color bit hat was encoded in the 
    image in the form [red_bits, green_bits, blue_bits].  It is important 
    that these match the values specified when encode was called, otherwise
    the output will be garbage.  This method will return a string that is 
    the character data encoded in the file.
    '''
    in_image = Image.open(im_dec)

    # The data pulled out
    data = []
    
    # A list to build the individual bits in
    tmp_list = []
    try:
        for pixel in in_image.getdata():
            i = 0
            for color in pixel:
                tmp_color = list(dec_2_bin(color))
                
                bits = color_bits[i%3]

                # Pull out the specified number of bits based on the color
                if forward:
                    tmp_list.extend(tmp_color[-bits:])
                else:
                    tmp_list.extend(reversed(tmp_color[-bits:]))

                # If we have a full bit or more add the bit to the data
                if len(tmp_list)>=8:
                    data.append(chr(bin_2_dec(''.join(tmp_list[:8]))))
                    tmp_list = tmp_list[8:]
                
                # If we've had 16 ones in a row quit looking
                if len(data) >= 2 and ord(data[-1]) == 255:
                    if ord(data[-2]) == 255:
                        raise StopIteration
                i += 1
                
    except StopIteration:
        pass
    
    return ''.join(data[:-2])

def save_file(data, file_name):
    '''
    This will write all of the information in data (currently only
    character data is tested) and save it to the file file_name
    '''
    out_file = open(file_name,'wb+')
    out_file.write(data)
    out_file.close()
    
def check_size (bit_num, image, bits_per_pix):
    max_bits = reduce(lambda x,y: x*y, image.size)*bits_per_pix
    if max_bits < bit_num:
        raise FileTooLargeException("Image to small for current settings.")

    

if __name__ == '__main__':
    print "TESING ENCODE FORWARD"
    encode('..\Resources\\flower.png', '..\Resources\Macbeth.txt',[2,2,3]).save('..\Resources\\asdf1.png')
    import hashlib
    m = hashlib.md5()
    m.update(''.join(open('..\Resources\\asdf1.png','rb').readlines()))
    assert(m.digest() == '\xc6E\xfd\x98\x0012\r\x8a\xf2\x98\xd1\x93\xd2\x16\xed')
    print "PASSED ENCODE FORWARD TEST"
    
    print "TESTING DECODE FORWARD"
    save_file(decode('..\Resources\\asdf1.png',[2,2,3]),'..\Resources\\asdf1.txt')
    m = hashlib.md5()
    m.update(''.join((open('..\Resources\\asdf1.txt','r').readlines())))
    decoded = m.digest()
    m = hashlib.md5()
    m.update(''.join((open('..\Resources\Macbeth.txt','r').readlines())))
    from_text = m.digest()
    assert(decoded == from_text)
    print "PASSED DECODE FORWARD TEST"
    
    print "TESTING ENCODE BACKWARD"
    encode('..\Resources\\flower.png', '..\Resources\Macbeth.txt',[2,2,3],False).save('..\Resources\\asdf1.png')
    m = hashlib.md5()
    m.update(''.join(open('..\Resources\\asdf1.png','rb').readlines()))
    assert(m.digest() == 'K\x7f\xe2\x90\xa5\xee\x8a\x00\xa6\xb5z\xe0\xf9}\xe0\x84')
    print "PASSED ENCODE BACKWARD TEST"
    
    print "TESTING DECODE BACKWARD"
    save_file(decode('..\Resources\\asdf1.png',[2,2,3],False),'..\Resources\\asdf1.txt')
    m = hashlib.md5()
    m.update(''.join((open('..\Resources\\asdf1.txt','r').readlines())))
    decoded = m.digest()
    m = hashlib.md5()
    m.update(''.join((open('..\Resources\Macbeth.txt','r').readlines())))
    from_text = m.digest()
    assert(decoded == from_text)
    print "PASSED DECODE BACKWARD TEST"


