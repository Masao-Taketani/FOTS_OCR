from glob import glob
import os
import subprocess

before_dir = "tmp/ICDAR17MLT/"
after_dir = "data/ICDAR17MLT/"

def change_val_file_names(fpath):
    val_dirs = ["val_imgs", "val_gts"]
    for val_dir in val_dirs:
        val_path = os.path.join(before_dir, val_dir, "*")
        val_files = glob(val_path)
        for fpath in val_files:
            dir_name = os.path.dirname(fpath)
            fname = os.path.basename(fpath)
            val_fname = "val_" + fname
            new_path = os.path.join(dir_name, val_fname)
            os.rename(fpath, new_path)

def mv_processed_files():
    cmd = ""

if __name__ == "__main__":


    print("done changing the file names of val imgs & val gts")

    cmd = "
