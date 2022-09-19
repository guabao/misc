__doc__ = "Photo compression"

import argparse
import os

from io import BytesIO # "import BytesIO" directly in python2
from PIL import Image


def compress_photo(filename, rgb_rate, height_rate, width_rate):
    path, ext = filename.split(".")
    if ext != "jpg":
        raise NotImplementedError("Only support jpg for now!")
    img = Image.open(filename)
    # scaling img
    new_width = int(img.size[0] * width_rate)
    new_height = int(img.size[1] * height_rate)
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    # here, we create an empty string buffer
    buffer = BytesIO()
    img.save(buffer, "JPEG", quality=int(rgb_rate))
    # write the buffer to a file to make sure it worked
    new_path = path + "_compressed." + ext
    with open(new_path, "wb") as handle:
        handle.write(buffer.getbuffer())
    return None

def main(args):
    if args.file:
        compress_photo(args.file, args.rgb_rate)
    elif args.directory:
        l = os.listdir(args.directory)
        for li in l:
            filepath = args.directory + "/" + li
            compress_photo(filepath,
                           args.rgb_rate,
                           float(args.height_rate),
                           float(args.width_rate))
    else:
        raise NotImplementedError("Not support other config yet!")

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="directory of photos")
    parser.add_argument("-f", "--file", help="filename of photo")
    parser.add_argument("-rr", "--rgb_rate", help="RGB compression rate")
    parser.add_argument("-wr", "--width_rate", help="width compression rate")
    parser.add_argument("-hr", "--height_rate", help="height compression rate")
    args = parser.parse_args()
    main(args)
    print("DONE!")
