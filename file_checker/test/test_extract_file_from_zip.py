import zipfile

# extract zipfile
def extract_file_from_zip(inputfile,destination): 
    # Open the zip file and extract the XML file to the "unzipped" path
    with zipfile.ZipFile(inputfile,mode='r') as zip_file:
        # Inspect the contents of zipfile
        files = zip_file.namelist()    
        print("\nNumber of files in the zip file = ",len(files),"\n")
        # list the files present in the zipfile
        for filename in files:        
            print("\t", filename)
        zip_file.extractall(destination)
        print("\nFile Extracted: Successfully\n")
    # Close the archive releasing it from memory
    zip_file.close()