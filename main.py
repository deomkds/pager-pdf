import os
import sys
import pdf2image


def list_files_in(path):
    all_files = os.scandir(path)
    receipt_files = []

    for one_file in all_files:
        if one_file.name.endswith(".pdf"):
            receipt_files.append(one_file)

    return receipt_files


if __name__ == "__main__":

    working_dir = sys.argv[1]

    files = list_files_in(working_dir)

    for num, file in enumerate(files):

        amount = len(files)
        position = num + 1
        full_path = f"{working_dir}/{file.name}"
        print(f"{position:02} of {amount:02}: {file.name}")

        document = pdf2image.convert_from_path(full_path)
        document[0].save(f"{working_dir}/{file.name[:-4]}.png")




