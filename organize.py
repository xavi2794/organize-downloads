import shutil, os

# Make Video directory
def make_video_directory():
    if not os.path.exists('Videos'):
        os.makedirs('Videos')

# Make Images directory
def make_image_directory():
    if not os.path.exists('Images'):
        os.makedirs('Images')

# Make Music directory
def make_music_directory():
    if not os.path.exists('Music'):
        os.makedirs('Music')

# Make Document directory
def make_document_directory():
    if not os.path.exists('Documents'):
        os.makedirs('Documents')

# Make Program directory
def make_program_directory():
    if not os.path.exists('Programs'):
        os.makedirs('Programs')

#Make Other directory
def make_other_directory():
    if not os.path.exists('Others'):
        os.makedirs('Others')

ext = {
    '.pdf': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.xlsx': 'Documents',
    '.pps': 'Documents',
    '.pptx': 'Documents',
    '.png': 'Images',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.tif': 'Images',
    '.psd': 'Images',
    '.exe': 'Programs',
    '.iso': 'Programs',
    '.msi': 'Programs',
    '.mp3': 'Music',
    '.mp4': 'Videos',
    '.mpeg': 'Videos'
}

archivos = os.listdir()

for archivo in archivos:
    nombre, extension = os.path.splitext(archivo)
    for key, value in ext.items():
        if extension == key:
            destination = value
            if value == 'Images':
                make_image_directory()
                shutil.move(archivo, destination)
            elif value == 'Documents':
                make_document_directory()
                shutil.move(archivo, destination)
            elif value == 'Programs':
                make_program_directory()
                shutil.move(archivo, destination)
            elif value == 'Music':
                make_music_directory()
                shutil.move(archivo, destination)
            elif value == 'Videos':
                make_video_directory()
                shutil.move(archivo, destination)
            else:
                make_other_directory()
                shutil.move(archivo, 'Others')






 