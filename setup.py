from setuptools import setup
setup(
    install_requires=[
        "meerk40t>=0.8.0001",
        "qrcode>=7.0",
        "python-barcode>=0.10",
    ],
  name = 'meerk40t-barcodes',         # How you named your package folder 
  packages = ['meerk40t-barcodes'],   # Chose the same as "name"
  version = '0.2',
  license='MIT',  
  description = 'This plugin for meerk40t provides barcode creation functionality',
  author = 'jpirnay',                   # Type in your name
  author_email = 'your.email@domain.com',     
  url = 'https://github.com/meerk40t/meerk40t-barcodes',
  download_url = 'https://github.com/meerk40t/meerk40t-barcodes/archive/v02.tar.gz',    
  keywords = ['meerk40t', 'barcodes', 'plugin'],
)
