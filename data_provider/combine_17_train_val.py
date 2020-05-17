from glob import glob
import os
import subprocess

# file paths that are moved from
orig_imgs_dir = "tmp/ICDAR17MLT/imgs"
orig_gts_dir = "tmp/ICDAR17MLT/gts"
orig_val_imgs_dir = "tmp/ICDAR17MLT/val_imgs"
orig_val_gts_dir = "tmp/ICDAR17MLT/val_gts"
# file paths that are moved to
imgs_dir = "data/ICDAR17MLT/imgs"
gts_dir = "data/ICDAR17MLT/gts"

def change_val_file_names():
    val_dirs = [orig_val_imgs_dir, orig_val_gts_dir]
    for val_dir in val_dirs:
        val_path = os.path.join(val_dir, "*")
        val_files = glob(val_path)
        for fpath in val_files:
            dir_name = os.path.dirname(fpath)
            fname = os.path.basename(fpath)
            if fname.split(".")[-1] == "txt":
                val_fname = fname[:3] + "val_" + fname[3:]
            else:
                val_fname = "val_" + fname
            new_path = os.path.join(dir_name, val_fname)
            os.rename(fpath, new_path)

def move_files(orig_dir, to_dir):
    cmd = "mv {}/* {}".format(orig_dir, to_dir)
    subprocess.run(cmd.split())

def return_num_of_files(path):
    files = glob(os.path.join(path, "*"))
    return len(files)

def check_num_of_files(paths_1, paths_2):
    files_ct_1 = return_num_of_files(paths_1)
    files_ct_2 = return_num_of_files(paths_2)
    assert files_ct_1 == files_ct_2, "num of imgs are not equal to num of gts"


if __name__ == "__main__":
    check_num_of_files(orig_imgs_dir, orig_gts_dir)
    check_num_of_files(orig_val_imgs_dir, orig_val_gts_dir)
    print("count check passed")

    change_val_file_names()
    print("changing the file names of val imgs & val gts is done")

    move_files(orig_imgs_dir, imgs_dir)
    move_files(orig_gts_dir, gts_dir)
    move_files(orig_val_imgs_dir, imgs_dir)
    move_files(orig_val_gts_dir, gts_dir)
    print("moving the files to the specified dirs is done")

    check_num_of_files(imgs_dir, gts_dir)
    print("final count check of imgs and gts is done")
