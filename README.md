FANSI CONVERT
=============

This Python script enables you to convert .ANS or .TXT files to .FAN for the first time in 30 years! You can also do reverse conversions, or export PNG preview images.

* [Why would someone need this?](#why-would-someone-need-this)
* [How do I use this?](#how-do-i-use-this)
* [Important notes](#important-notes)
* [FAN file format](#fan-file-format)


Why would someone need this?
----------------------------

This script is for Atari ST users who want to convert .ANS files to .FAN format for use with "FANSI," an Atari ST ANSI art editor released in 1994 by Eric March.

While FANSI can save artwork as cross-platform .ANS files, it cannot _read_ .ANS files. FANSI will only read its native format (.FAN). 

Since FANSI was just about the only 16-color ANSI art editor available for the Atari ST, this was a major limitation.


How do I use this?
------------------

This script requires Python >= 3.9, and has one dependency: [Pillow](https://pillow.readthedocs.io/en/stable/index.html).

### Installation
```
git clone https://github.com/Kirkman/fansi-convert.git
cd fansi-convert
pip install Pillow
```

### Usage
```
python convert.py [-h] [-P] [-s] input_file
or
python convert.py [--help] [--png] [--scale] input_file
```

### Examples

_Convert an .ANS file to .FAN, generate a PNG image, and set the PNG's scale to 4_
```
python convert.py MYANSI.ANS --png --scale 4
```

_Convert a .TXT file to .FAN_
```
python convert.py MYTEXT.TXT
```

_Convert a .FAN file to .ANS_
```
python convert.py MYFANSI.FAN
```


Important notes
---------------

1. Because FANSI's canvas is limited to a single 80x24 screen, this converter will keep only the initial 80x24 when converting oversized .ANS or .TXT files to .FAN format.

2. The ANSI parser and exporter in this script are extremely simple/naive. You will not get good results if you try to convert ANSImation or files with cursor movement.

3. This script can optionally produce a PNG image as part of the workflow using the `-P` or `--png` flag. This PNG will use FANSI's 4x8 font and color palette. You can adjust the scale of the PNG with the `-s` or `--scale` switch.

4. This script is mainly intended for use with ANSI art files, but it also can be used to convert plain text files to .FAN format. Text files must have the extension .TXT, and conversion is only works in one direction (TXT -> FAN).


![Old advertisement for the Atari ST program "FANSI"](https://raw.githubusercontent.com/Kirkman/fansi-convert/master/FANSI.PNG)


FAN file format
---------------

File is always 36,638 bytes. 

File begins with a six-byte header: `0x00` `0x04` `0x46` `0x4E` `0x43` `0x21` (or `  FNC!`)

After this header, the file contains character data, followed by bitmap/screen data.

### Character data

Character data takes up next 5,904 bytes, encoding one screen of text data (80 cols x 24 rows).

* There are 246 bytes per row. Each row contains 3 sub-rows of 82 bytes.
* Each sub-row begins with the sequence `0x00` `0x50`, followed by 80 bytes; one byte for each character.
	+ Sub-row 1: Encodes the ASCII character code
	+ Sub-row 2: Encodes the background color attribute
	+ Sub-row 3: Encodes the foreground color attribute
	+ Color attributes (08-0F only used for foreground):
		- `0x00`: black
		- `0x01`: red
		- `0x02`: green
		- `0x03`: yellow
		- `0x04`: blue
		- `0x05`: magenta
		- `0x06`: cyan
		- `0x07`: white
		- `0x08`: black high
		- `0x09`: red high
		- `0x0A`: green high
		- `0x0B`: yellow high
		- `0x0C`: blue high
		- `0x0D`: magenta high
		- `0x0E`: cyan high
		- `0x0F`: white high

### Bitmap data

Bitmap data takes up final 30,728 bytes

+ Bitmap data begins with eight-byte header: `0x78` `0x06` `0x01` `0x3F` `0x00` `0xBF` `0x00` `0x04`
+ Remaining 30,720 bytes encode an Atari ST low-resolution screen dump of 320x192 pixels (all of the screen except the final 8 rows of pixels). 
+ On the ST, 4 bitplanes are interleaved per 16-pixel group on each scanline.
