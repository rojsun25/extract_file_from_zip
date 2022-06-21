import extract_and_parse_file_from_zip as ex

inputfile = "10th to 16th april 2022.zip"
destination = "unzipped"                        
extract = "unzipped/10th to 16th april 2022/" 

ex.extract_and_parse_file_from_zip(inputfile,destination,extract)
