
from detect_rectangle import *
from detect_currentm import *
import os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = "C:/Anna/CSE/semester1/ML/projects/P2/"  #### "RxT_PVVIH_Benin/"
    input_folders =["RxT_PVVIH_Benin", "RxT_diabetiques_Benin" ]  ### RxT_diabetiques_Benin

    i1 = 0
    i2 = 0
    for input_folder in input_folders:
        input_path = path + input_folder + '/'
        out_path = path + input_folder + "_deleted_label/"
        os.makedirs(out_path, exist_ok=True)

        detect_rectangle(input_path, out_path)
        list_files1 = os.listdir(input_path)
        list_files2 = os.listdir(out_path)

        for img_name in list_files1:
            i1+=1
            name = "without_rect_" + img_name
            if name in list_files2:
                continue
            else: print("missed image: ", img_name)


        for img_name in list_files2:
            i2 += 1

        print("total number of input images = ", i1)
        print("total number of output images = ", i2)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
