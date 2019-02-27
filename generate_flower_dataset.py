
import subprocess
from os import listdir
from os.path import isfile, join, isdir
from PIL import Image

FLOWER_DATASET_URL = "http://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz"
FLOWER_LOCAL_DATASET_DIR = "datasets/flowers"
FLOWER_LOCAL_DATASET_IMAGE_DIR = "datasets/flowers/jpg"
FLOWER_LOCAL_DATASET_ZIP = "datasets/flowers/102flowers.tgz"

def resizeToResolution(resolution=512):
    files = [f for f in listdir(FLOWER_LOCAL_DATASET_IMAGE_DIR) if isfile(join(FLOWER_LOCAL_DATASET_IMAGE_DIR, f))]
    for file in files:
        if ".jpg" in file:
            img = Image.open("%s/%s" % (FLOWER_LOCAL_DATASET_IMAGE_DIR,file))
            new_img = img.resize((512,512))
            new_img.save("%s/%s" % (FLOWER_LOCAL_DATASET_DIR,file), "JPEG", optimize=True)

def getData():
    downloadCommand = "wget %s -P %s" %(FLOWER_DATASET_URL, FLOWER_LOCAL_DATASET_DIR)
    subprocess.call(downloadCommand.split())
    unzipCommand = "tar -xvzf %s -C %s" % (FLOWER_LOCAL_DATASET_ZIP, FLOWER_LOCAL_DATASET_DIR)
    subprocess.call(unzipCommand.split())

def preClean():
    if isdir(FLOWER_LOCAL_DATASET_IMAGE_DIR):
        deleteDir = "rm -rf %s" % (FLOWER_LOCAL_DATASET_IMAGE_DIR)
        subprocess.call(deleteDir.split())

def clean():
    deleteOriginalImages = "rm -rf %s" % (FLOWER_LOCAL_DATASET_IMAGE_DIR)
    subprocess.call(deleteOriginalImages.split())
    files = [f for f in listdir(FLOWER_LOCAL_DATASET_DIR) if isfile(join(FLOWER_LOCAL_DATASET_DIR, f))]
    for file in files:
        if ".jpg" not in file:
            deleteFile = "rm -rf %s/%s" % (FLOWER_LOCAL_DATASET_DIR, file)
            subprocess.call(deleteFile.split())

def main():
    preClean()
    getData()
    resizeToResolution()
    clean()

if __name__ == "__main__":
    main()

#----------------------------------------------------------------------------
