__doc__ = "Photo compression"

import argparse
import os

from io import BytesIO # "import BytesIO" directly in python2
from PIL import Image


def compress_photo(filename, rate):
    path, ext = filename.split(".")
    if ext != "jpg":
        raise NotImplementedError("Only support jpg for now!")
    img = Image.open(filename)
    # here, we create an empty string buffer
    buffer = BytesIO()
    img.save(buffer, "JPEG", quality=int(rate))
    # write the buffer to a file to make sure it worked
    new_path = path + "_compressed." + ext
    with open(new_path, "wb") as handle:
        handle.write(buffer.getbuffer())
    return None

def main(args):
    if args.file:
        compress_photo(args.file, args.rate)
    elif args.directory:
        l = os.listdir(args.directory)
        for li in l:
            filepath = args.directory + "/" + li
            compress_photo(filepath, args.rate)
    else:
        raise NotImplementedError("Not support other config yet!")

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="directory of photos")
    parser.add_argument("-f", "--file", help="filename of photo")
    parser.add_argument("-r", "--rate", help="photo compression rate")
    args = parser.parse_args()
    main(args)
    print("DONE!")
