# meerk40t-barcodes-extension
MeerK40t Barcode extension.


# Barcode-Extensions.

* Registers the console command: `qrcode` which will generate a qrcode
     Usage:    `qrcode x_pos y_pos dim code`
     Arguments:
     x_pos          X-position of qr-code
     y_pos          Y-position of qr-code
     dim            Width/length of qr-code
     code           Text to create qr-code from

     Options:
     --boxsize  (-x)      Boxsize (default 10)
     --border   (-b)      Border around qr-code (default 4)
     --version  (-v)      size (1..40)
     --errcorr  (-e)      error correction, one of L (7%), M (15%), Q (25%), H (30%)

* Registers the console command: `barcode` which will generate a barcode
     Usage:    `barcode x_pos y_pos dimx dimy btype code`
     Arguments:
     x_pos     X-Position of barcode
     y_pos     Y-Position of barcode
     dim       Width of barcode, may be 'auto' to keep native width
     dimy      Height of barcode, may be 'auto' to keep native height
     btype     Barcode type
     code      The code to process

     Options:
     --notext  (-n)      suppress text display
     --asgroup (-a)      create a group of rects instead of a path

# Installing

* Download into a directory:
* `$ pip install .`

# Development

* If you are developing your own extension for meerk40t you will want to use:
* `$ pip install -e .` this installs the python module in edit mode which allows you to easily see and experience your changes. Without reinstalling your module.
