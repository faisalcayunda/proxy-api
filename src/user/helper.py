import os
from fastapi import UploadFile
from werkzeug.utils import secure_filename


def save_file(file: UploadFile):
    if file.filename == "" or not allowed_file(file.filename):
        return False
    original_file = temp(file)
    return f"static/upload/{original_file}"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in [
        "bmp",
        "dib",
        "gif",
        "tif",
        "tiff",
        "jfif",
        "jpe",
        "jpg",
        "jpeg",
        "pbm",
        "pgm",
        "ppm",
        "pnm",
        "png",
        "apng",
        "blp",
        "bufr",
        "cur",
        "pcx",
        "dcx",
        "dds",
        "ps",
        "eps",
        "fit",
        "fits",
        "fli",
        "flc",
        "ftc",
        "ftu",
        "gbr",
        "grib",
        "h5",
        "hdf",
        "jp2",
        "j2k",
        "jpc",
        "jpf",
        "jpx",
        "j2c",
        "icns",
        "ico",
        "im",
        "iim",
        "mpg",
        "mpeg",
        "mpo",
        "msp",
        "palm",
        "pcd",
        "pdf",
        "pxr",
        "psd",
        "bw",
        "rgb",
        "rgba",
        "sgi",
        "ras",
        "tga",
        "icb",
        "vda",
        "vst",
        "webp",
        "wmf",
        "emf",
        "xbm",
        "xpm",
    ]


def temp(file: UploadFile):
    try:
        original_file = secure_filename(file.filename)
        contents = file.file.read()
        with open(f"static/upload/{original_file}", "wb") as f:
            f.write(contents)
    except Exception:
        return False
    finally:
        file.file.close()
    return original_file
