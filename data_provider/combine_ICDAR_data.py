from glob import glob
import os
import subprocess
import tensorflow as tf

tf.app.flags.DEFINE_string('year',
                           '',
                           'specify the ICDAR year to train. '
                           '13 for ICDAR13; '
                           '15 for ICDAR15; '
                           '17 for ICDAR17MLT; ')

FLAGS = tf.app.flags.FLAGS


def change_file_names(imgs_dir, gts_dir, is_train):
    dirs = [imgs_dir, gts_dir]
    for dir in dirs:
        path = os.path.join(dir, "*")
        files = glob(path)
        for fpath in files:
            dir_name = os.path.dirname(fpath)
            fname = os.path.basename(fpath)
            if fname.split(".")[-1] == "txt":
                if is_train:
                    fname = fname[:3] + imgs_dir.split('/')[1] + "_" + fname[3:]

                    if '13' in imgs_dir.split('/')[1]:
                        change_delimiter(fpath, ',')
                else:
                    fname = fname[:3] + imgs_dir.split('/')[1]  + "_val_" + fname[3:]
            else:
                if is_train:
                    fname = imgs_dir.split('/')[1] + "_" + fname
                else:
                    fname = imgs_dir.split('/')[1] + "_val_" + fname
            new_path = os.path.join(dir_name, fname)
            os.rename(fpath, new_path)


def change_delimiter(fpath, deli):
    with open(fpath, 'r') as fr:
        txt = fr.read()

    new_txt = ''
    for line in txt.splitlines():
        new_txt += deli.join(line.split()) + '\n'

    with open(fpath, 'w') as fw:
        fw.write(new_txt)


def move_files(orig_dir, to_dir):
    check_dir_existence(to_dir)
    cmd = "mv {}/* {}".format(orig_dir, to_dir)
    subprocess.run(cmd, shell=True)


def check_dir_existence(path):
    if not os.path.exists(path):
        os.makedirs(path)


def return_num_of_files(path):
    files = glob(os.path.join(path, "*"))
    return len(files)


def check_num_of_files(paths_1, paths_2):
    files_ct_1 = return_num_of_files(paths_1)
    files_ct_2 = return_num_of_files(paths_2)
    assert files_ct_1 == files_ct_2, "num of imgs are not equal to num of gts"


def process(orig_imgs_dir,
            orig_gts_dir,
            orig_val_imgs_dir,
            orig_val_gts_dir,
            imgs_dir,
            gts_dir):

        check_num_of_files(orig_imgs_dir, orig_gts_dir)
        check_num_of_files(orig_val_imgs_dir, orig_val_gts_dir)
        print("count check passed")

        change_file_names(orig_imgs_dir, orig_gts_dir, True)
        change_file_names(orig_val_imgs_dir, orig_val_gts_dir, False)
        print("changing the names of imgs & gts files is done")

        move_files(orig_imgs_dir, imgs_dir)
        move_files(orig_gts_dir, gts_dir)
        move_files(orig_val_imgs_dir, imgs_dir)
        move_files(orig_val_gts_dir, gts_dir)
        print("moving the files to the specified dirs is done")

        check_num_of_files(imgs_dir, gts_dir)
        print("final count check of imgs and gts is done")


if __name__ == "__main__":
    if FLAGS.year == "13":
        # file paths that are moved from
        orig_imgs_dir = "tmp/ICDAR13/Challenge2_Training_Task12_Images"
        orig_gts_dir = "tmp/ICDAR13/Challenge2_Training_Task1_GT"
        orig_val_imgs_dir = "tmp/ICDAR13/Challenge2_Test_Task12_Images"
        orig_val_gts_dir = "tmp/ICDAR13/Challenge2_Test_Task1_GT"
        # file paths that are moved to
        imgs_dir = "data/ICDAR13/imgs"
        gts_dir = "data/ICDAR13/gts"

    elif FLAGS.year == "15":
        # file paths that are moved from
        orig_imgs_dir = "tmp/ICDAR15/ch4_training_images"
        orig_gts_dir = "tmp/ICDAR15/ch4_training_localization_transcription_gt"
        orig_val_imgs_dir = "tmp/ICDAR15/ch4_test_images"
        orig_val_gts_dir = "tmp/ICDAR15/Challenge4_Test_Task1_GT"
        # file paths that are moved to
        imgs_dir = "data/ICDAR15+13/imgs"
        gts_dir = "data/ICDAR15+13/gts"

    elif FLAGS.year == "17":
        # file paths that are moved from
        orig_imgs_dir = "tmp/ICDAR17MLT/imgs"
        orig_gts_dir = "tmp/ICDAR17MLT/gts"
        orig_val_imgs_dir = "tmp/ICDAR17MLT/val_imgs"
        orig_val_gts_dir = "tmp/ICDAR17MLT/val_gts"
        # file paths that are moved to
        imgs_dir = "data/ICDAR17MLT/imgs"
        gts_dir = "data/ICDAR17MLT/gts"

    else:
        raise ValueError("pick a year from 13,15 or 17: you picked %s"
                         % (FLAGS.year))

    process(orig_imgs_dir,
                orig_gts_dir,
                orig_val_imgs_dir,
                orig_val_gts_dir,
                imgs_dir,
                gts_dir)

    if FLAGS.year == "15":
        # file paths that are moved from
        orig_imgs_dir = "tmp/ICDAR13/Challenge2_Training_Task12_Images"
        orig_gts_dir = "tmp/ICDAR13/Challenge2_Training_Task1_GT"
        orig_val_imgs_dir = "tmp/ICDAR13/Challenge2_Test_Task12_Images"
        orig_val_gts_dir = "tmp/ICDAR13/Challenge2_Test_Task1_GT"

        process(orig_imgs_dir,
                    orig_gts_dir,
                    orig_val_imgs_dir,
                    orig_val_gts_dir,
                    imgs_dir,
                    gts_dir)
