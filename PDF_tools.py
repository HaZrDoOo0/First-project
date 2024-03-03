# QNQ
# EZZ
# HZRD

import PyPDF2
import os


def check_number(number, pages):
    try:
        valid = int(number)
        if valid > 0 and valid <= pages:
            return True
    except ValueError:
        return False


def check_file(pdf):
    while True:
        if pdf.lower().endswith(".pdf") and os.path.isfile(pdf) and os.path.exists(pdf):
            return True
        else:
            return False


def merge_2_files(file1, file2):
    mergeFile = PyPDF2.PdfMerger()
    mergeFile.append(PyPDF2.PdfReader(file1))
    mergeFile.append(PyPDF2.PdfReader(file2))
    mergeFile.write("NewMergedFile.pdf")

    print("your merged pdf in", os.path.abspath("NewMergedFile.pdf"))


def extract_one_page(file, page_num):
    pdf = PyPDF2.PdfReader(file)
    page = pdf.pages[int(page_num) - 1]
    new_pdf = PyPDF2.PdfWriter()
    new_pdf.add_page(page)

    file = open("NewFile.pdf", "wb")
    new_pdf.write(file)
    print("your pdf in", os.path.abspath("NewFile.pdf"))


def split_to_pages(directory, file):
    basename = file.replace(".pdf", "")
    os.mkdir(f"{basename} split pages")
    output_folder = os.path.join(directory, f"{basename} split pages")

    read = PyPDF2.PdfReader(file)
    for page in range(len(read.pages)):
        pageObj = read.pages[page]
        write = PyPDF2.PdfWriter()
        write.add_page(pageObj)
        with open(os.path.join(output_folder, "{0}-{1}.pdf".format(basename, page + 1)), "wb") as f:
            write.write(f)
    print("Your pdf is split into pages in", os.path.abspath(output_folder))


def main():
    # display Welcome message and menu to user
    while True:
        print("|----- Welcome to our program -----|")
        print("1) Merge two files ----------------|")
        print("2) Extract a page from file -------|")
        print("3) Split file into separate pages -|")
        print("4) Exit program -------------------|")

        # while loop to know if user want to continue or not
        while True:
            valid_choice = input("please enter your choice [1, 2, 3, 4]: ")
            if valid_choice not in ['1', '2', '3', '4']:
                print("---- Please enter a valid choice ----")
            elif valid_choice in ['1', '2', '3']:
                break
            else:
                print()
                print("----------------------------------------")
                print(" Thank you, I hope you have a good time")
                print("----------------------------------------")
                exit()

        print()
        DIRECTORY = input("Please enter the Directory: ")
        while True:
            if os.path.exists(DIRECTORY) and os.path.isdir(DIRECTORY):
                os.chdir(DIRECTORY)
                break
            else:
                print("Directory does not exist or is not a directory")
                DIRECTORY = input("Please enter the Directory: ")

        print()
        file1 = input("Enter the path to the pdf file: ")
        while not check_file(file1):
            print("File does not exist or is not a pdf file")
            file1 = input("Enter the path to the pdf file: ")
        i = len(PyPDF2.PdfReader(file1).pages)
        print(i)

        if valid_choice == '1':
            file2 = check_file("Enter the path to the second pdf file: ")
            while not check_file(file2):
                print("File does not exist or is not a pdf file")
                file2 = input("Enter the path to the second pdf file: ")
            merge_2_files(file1, file2)
        elif valid_choice == '2':
            num = input("please enter the page number: ")
            pages = len(PyPDF2.PdfReader(file1).pages)
            while not check_number(num, pages):
                print("Invalid page number")
                num = input("please enter the page number: ")
            extract_one_page(file1, num)
        else:
            split_to_pages(DIRECTORY,file1)



main()
