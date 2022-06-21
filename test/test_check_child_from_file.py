import re 

# pass the element into match tag with namespace
def get_namespace(element):
        # helper func from the internet. only works with 1 ns
        m = re.match('\{.*\}', element.tag)
        return m.group(0) if m else ''

# evaluate the file contains key-values     
def check_child_from_file(root):
    namespace=get_namespace(root)
    
    # To find all the child and keyword : trainList
    if (root.findall(f"./{namespace}trainList/{namespace}train/{namespace}leg")):
        print("Trainlist<Tag> contains train<Object> and leg<child> : Exist\n")
    else:
        raise KeyError('Trainlist<Tag> contains train<Object> and leg<child> : Not Exist')    
    
    # To find all the child and keyword : locationList
    if (root.findall(f"./{namespace}locationList/{namespace}location")):
        print("Locationlist<Tag> contains location<object> : Exist\n")
    else:        
        raise KeyError('Locationlist<Tag> contains location<object> : Not Exist')
    
    # To find all the child and keyword - crewDiagramList
    if (root.findall(f"./{namespace}crewDiagramList")):
        print("crewDiagramList<Tag> : Exist\n")
    else:
        raise KeyError('crewDiagramList<Tag> : Not Exist')