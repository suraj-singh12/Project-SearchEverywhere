#!/usr/bin/python3

import os
import subprocess
import sys
from glob import glob
from time import sleep

def text(filename,keyword,dir=''):
    if dir != '':
        os.chdir(dir)

    # keyword = input("Enter keyword: ")
    
    with open("results.txt","w"):
        pass
    # this ensures, results file is empty if exists (otherwise it makes many copies of text when else part of below code works))

    # if single file then find and write the results into 'results.txt' file
    if filename != "*.txt":
        command="cat '" + filename + "' | grep -i '" + keyword + "' > results.txt"
        os.system(command)
    
    # if it is all .txt files to be searched
    else:
        found=list()
        for file in os.listdir():
            if file.endswith(".txt"):
                command="cat '" + file + "' | grep -i '" + keyword + "'" 
                
                proc=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, )
                find=(proc.communicate()[0]).decode("utf-8")
                # print(find)

                if len(find)>1:
                    temp="\n---------"+file.upper()+"-----------\n\n"
                    temp+=find
                    temp+="\n"
                    found.append(temp)
        # for line in found:
        #     print(line,end='')
        with open("results.txt","w") as f:
            f.writelines(found)

    with open("results.txt","r") as f:
        filesize = os.path.getsize("results.txt")
        if filesize == 0:
            print("Oops!!, there's nothing here that matches what you are looking for.")
            again = input("You may try with another keyword. Want to try?(y/n) ")
            if again=='y':
                keyword = input("Enter keyword: ")
                text(filename,keyword)
            else:
                sys.exit()
        else:
            os.system("clear")
            os.system("figlet -c Found This")
            for line in f.readlines():
                print(line,end='') 

def odt_to_txt(filename):
    new_dir="converted-odt/"

    if filename != "*.odt":
        if os.path.exists(filename) == True:
            # note: This command automatically creates "converted-odt" dir and places converted file(s) in it.
            command = "unoconv --format=txt --output='" + new_dir + filename.replace(".odt",".txt") + "' '" + filename + "'"
            os.system(command)
        else:
            print("Error! No such file.")
            sys.exit()
    else:
        files_counter = 0
        for nameOfFile in os.listdir():
            if nameOfFile.endswith(".odt"):
                files_counter += 1
                command = "unoconv --format=txt --output='" + new_dir + nameOfFile.replace(".odt",".txt") + "' '" + nameOfFile + "'"
                os.system(command)

        if files_counter == 0:
            print("No files with .odt extensions in the directory.")
            print("Terminating...")
            sys.exit()
    new_dir=os.path.abspath(new_dir)
    return new_dir

def odp_to_text(filename):
    new_dir="converted-presentations/"

    if filename != "*.odp":
        if os.path.exists(filename) == True:
            # convert odp to pdf
            # note: This command automatically creates "converted-presentations" dir and places converted file(s) in it.
            command = "unoconv --format=pdf --output='" + new_dir + filename.replace(".odp",".pdf") + "' '" + filename + "'"
            os.system(command)

            os.chdir(new_dir)
            # convert pdf to txt
            command= "pdftotext '" + filename.replace(".odp",".pdf") + "'"
            os.system(command)
            command="rm '" + filename.replace(".odp",".pdf") + "'"
            os.system(command)
            os.chdir("../")
        else:
            print("Error! No such file exists!")
            sys.exit()
    else:
        files_counter = 0
        for nameOfFile in os.listdir():
            if nameOfFile.endswith(".odp"):
                files_counter += 1
                # convert odp to pdf
                command = "unoconv --format=pdf --output='" + new_dir + nameOfFile.replace(".odp",".pdf") + "' '" + nameOfFile + "'"
                os.system(command)

                os.chdir(new_dir)
                # convert pdf to txt
                command= "pdftotext '" + nameOfFile.replace(".odp",".pdf") + "'"
                os.system(command)
                command="rm '" + filename.replace(".odp",".pdf") + "'"
                os.system(command)
                os.chdir("../")
        
        if files_counter==0:
            print("No files with .odp extensions in current folder.")
            print("Terminating...")
            sys.exit()

    new_dir=os.path.abspath(new_dir)
    return new_dir
    
def pdf_to_text(filename):
    new_dir="converted-pdfs"
    if os.path.exists(new_dir) == False:
        os.mkdir(new_dir)

    if filename != "*.pdf":
        if os.path.exists(filename) == True:
            # convert pdf to text
            command= "pdftotext '" + filename + "'"
            os.system(command)
            # go into new_dir
            os.chdir(new_dir)
            # move the filename.txt to this new_dir
            command="mv " + "'../" + filename.replace(".pdf",".txt") + "' " + "./"
            os.system(command)
            os.chdir("../") # back to base directory
        else:
            print("Error! No such file exists!")
            sys.exit()
    else:
        # copy all pdfs from base dir into converted-pdfs dir
        for file in os.listdir():
            if file.endswith(".pdf"):
                os.system("cp " + file + " " +new_dir)
        os.chdir(new_dir)   # now work in new_dir

        files_counter=0
        for nameOfFile in os.listdir():
            if nameOfFile.endswith(".pdf"):
                print("Listdir()")
                files_counter+=1
                command="pdftotext '" + nameOfFile + "'"
                os.system(command) 
        os.chdir("../")     #back to base directory

        if files_counter==0:
            print("No files with .pdf extensions in current folder")
            print("Terminating...")
            sys.exit()
    
    new_dir=os.path.abspath(new_dir)
    return new_dir

def usage():
    print("Usage:  SearchEverywhere [FILE] [keyword(s)]  or    SearchEverywhere -[extension] [keyword(s)]\n\
Example: SearchEverywhere myfile.txt urgent\n\
         SearchEverywhere -txt [keyword(s)]\n\
         SearchEverywhere - [keyword(s)]\n")
    print("This program lists all the lines with [keyword] in them from the specified FILES")
    print("It displays the result as well as stores it in a results.txt file to allow you to use it later.")
    print("Program Version: 1.0")
    print("\nDeveloped by: Suraj Singh (https://github.com/suraj-singh12)\n")
    sys.exit()

def main():
    if len(sys.argv)<=2:
        usage()
    # set the filename, and keyword
    elif len(sys.argv)==3:
        if sys.argv[1] == '-':
            filename="*"
        elif str(sys.argv[1])[0]=='-':
            filename = "*." + str(sys.argv[1])[1:]
        else:
            filename= sys.argv[1]
        keyword = sys.argv[2]
        # print(keyword)
    else:
        usage()

    print("------------------------")
    # filename = input("Enter filename: ")
    
    if filename == '*':
        # skip if converted folder already exists
        if os.path.exists("converted"):
            text("*.txt",keyword,os.path.abspath("converted"))
            sys.exit()
        
        # * means files of all types (txt, pdf, odt, odp)
        odp_dir=''
        odt_dir=''
        pdf_dir=''
        print("Processing all files... Required only during first run.")
        #first do all conversions (odp,odt,pdf->txt)
        for file in os.listdir():
            if file.endswith(".odp"):
                odp_dir=odp_to_text(file)
            elif file.endswith(".odt"):
                odt_dir=odt_to_txt(file)
            elif file.endswith(".pdf"):
                pdf_dir=pdf_to_text(file)
        
        if os.path.exists("converted") == True:
            os.system("rm -rf converted")
        # in this dir we will copy everything that's converted to text
        os.mkdir("converted")

        if odt_dir!='':
            os.chdir("converted-odt")
            # copy everything from converted-odt/ dir into 'converted' dir in base dir
            os.system("cp * ../converted/")
            os.chdir("../")
            # now delete converted-odt/ dir (cleanup)
            os.system("rm -rf converted-odt")
        if odp_dir!='':
            os.chdir("converted-presentations")
            # copy everything from converted-presentations/ dir into 'converted' dir in base dir
            os.system("cp * ../converted/")
            os.chdir("../")
            # now delete converted-presentations/ dir (cleanup)
            os.system("rm -rf converted-presentations")
        if pdf_dir!='':
            os.chdir("converted-pdfs")
            # copy everything from converted-pdfs/ dir into into 'converted' dir in base dir
            os.system("cp * ../converted")
            os.chdir("../")
            # cleanup
            os.system("rm -rf converted-pdfs")

        # copy all .txt files from base to converted directory if exists
        if glob("*.txt"):
            os.system("cp *txt converted/")

        os.chdir("converted")
        if len(os.listdir()) == 0:
            print("No files to process!!")
            print("Exiting...")
            sys.exit()

        print("And here we go...")
        sleep(1)
        text("*.txt",keyword)
        os.chdir("../")

    elif filename.endswith(".txt") or filename == "*.txt":
        text(filename,keyword)
    elif filename.endswith(".odt") or filename == "*.odt":
        odt_dir = odt_to_txt(filename)
        filename = filename.replace(".odt",".txt")
        text(filename,keyword,odt_dir)
        os.chdir("../")
    elif filename.endswith(".odp") or filename == "*.odp":
        odp_dir=odp_to_text(filename)
        filename = filename.replace(".odp",".txt")
        text(filename,keyword,odp_dir)
        os.chdir("../")
    elif filename.endswith(".pdf") or filename == "*.pdf":
        pdf_dir=pdf_to_text(filename)
        filename= filename.replace(".pdf",".txt")
        text(filename,keyword,pdf_dir)
        os.chdir("../")
    else:
        print("Try again!")

    print("\n------------------------")


if __name__ == "__main__":
    main()
