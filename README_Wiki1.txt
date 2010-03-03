=README=

This is a readme for Steganogra-py a free steganography tool written inpython and created by Zachary Varberg, 2010.

==EXECUTION==

===RUN===

Simply run Steganogra-py.exe to start the program.
There are two tabs, encode and decode.  These are used for their obviouspurposes.

===ENCODING===

On the encode page you will find options for which file you wouldlike to encode (currently only .txt files are supported), what image you wouldlike to encode it in (currently only .png files are supported), and where youwould like to save the newly encoded image (also .png only).  You are given theoption to choose how many of each colors bits you would like to use for encodeddata with the remainder of the 8 to be used for the original images color data.These start with the least significant bit and move towards more significant bits.Once everything is set press the encode button, and it will do the rest.

===DECODING===

The decoding precess is very similar to encoding.  You choose image file with theencoded data, and the file where you would like to save the output.  You choose thenumber of bits of each color that were encoded (NOTE: it is important that you choosethe same number for each color that was chosen when encoding, otherwise the outputwill be garbage), and press decode.

==NEW TO 1.1==
* *Threading*:  Steganogra-py is now a multi-threaded app with logic running on aseperate thread than the GUI, this allows the UI to remain responsive.

* *Progress Dialog*:  Previously, once the encode button was pressed there was noindication to the user that anything was happening.  With 1.1 there is now aprogress dialog.  The progress dialog does NOT actually display 0-100 percentcompletion of the task.  It DOES however provide some feedback showing that theapplication is working.

* *Optimizations*:  There were a variety of optimizations that went into this versionof Steganogra-py.  Without boring you with the low-level details the encodingportion was sped up by nearly 20% in tests.  This may or may not be the norm, butthe application was certainly sped up.

* *Documentation*:  With v1.1 I have considerably expanded the documentation for theproject.  Hopefully this will include updating of the wiki page found at http://code.google.com/p/steganogra-py/wiki/Home


And thats it!  This is hopefully a very simple to use steganography app.  While a numberof improvements were made for v1.1 they were mostly cosmetic and performance issues.  Thefeature set was not significantly expanded.  BUT, development continues and future featuresinclude, suggested encoding styles, random encoding, steganography detection (this one israther difficult so it may or may not happen), as well as support for other file-types. Ifyou have any requests for future features, please don't hesitate to let me know atZach.Varberg (at) Gmail (dot) com!

The source code is available at http://code.google.com/p/steganogra-py/downloads/list