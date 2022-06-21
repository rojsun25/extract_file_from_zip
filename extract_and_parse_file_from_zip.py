from parse_xml_file import parse
import os, fnmatch
from extract_file_from_zip import extract_file_from_zip

def extract_and_parse_file_from_zip(inputfile,destination,extract):
    # find File ending with .zip from the extract directory
    if inputfile.endswith('.zip'):
        extract_file_from_zip(inputfile,destination)
        fileDirectory = os.listdir(f'{extract}')
        pattern = "*crew*diagram*.xml"

        # print the files with the extension .xml
        file = [file_name for file_name in fileDirectory if fnmatch.fnmatch(file_name, pattern)]
        print("Files found =",file)
        
        # Parsing the xml file 
        if any(".xml" in file_check for file_check in file):
            parse(extract,file)
        else:
            raise FileNotFoundError('zipfile has no crew diagram file')
    else:
        raise Exception("The zip file had an unexpected format.")