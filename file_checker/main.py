from extract_and_parse_file_from_zip import extract_and_parse_file_from_zip

inputfile = "10th to 16th april 2022.zip"
destination = "unzipped"                        
extract = "unzipped/10th to 16th april 2022/"   

extract_and_parse_file_from_zip(inputfile,destination,extract)

inputfile = "10th to 16th april 2022"
destination = "unzipped"
extract = "unzipped/10th to 16th april 2022/"

extract_and_parse_file_from_zip(inputfile,destination,extract)