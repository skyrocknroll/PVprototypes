import re
import os
import random
import datetime

def application(environ, start_response):
    input = environ['wsgi.input']
    path = environ['PATH_INFO']
    if(os.environ.get('currentDisk') is None):
        os.environ['currentDisk'] = '1'
    
    selectedDisk = "sdev" + os.environ['currentDisk']
    #print "SelectedDisk "+selectedDisk
    path = path.replace("sdevx",selectedDisk)
    #print path
    nextDisk = int(os.environ['currentDisk'])+1
    if nextDisk == 9:
        nextDisk = 1
    os.environ['currentDisk'] = str(nextDisk)
    #print "Current Disk "+os.environ['currentDisk']
    method = environ['REQUEST_METHOD']
    uploadsDir = "/files"
    if method == "POST":        
        match = re.search("[/]$", path )
        if match:
            start_response('403 Forbidden', [('content-type', 'text/plain')])
            return("You need to provide valid RESTFUL URL for an item to be uploaded. For Item upload, URL should not end with / ",)
        else:
            x = path.split('/')
            filename =  x[(len(x)-1)]
            randfileName = datetime.datetime.now().strftime("%Y%m%d%H%M%s%s") + str(random.random()).split(".")[1]+filename
            folderLocation = uploadsDir + (path.replace(filename , ""))
            fileLocation = folderLocation + randfileName
            #fileLocation = folderLocation + filename
            #print folderLocation
            d = os.path.dirname(folderLocation)
            if not os.path.exists(d):
                print " Making Directory!!!"+d
                os.makedirs(d)
            if os.path.exists(fileLocation):
                start_response('403 Forbidden', [('content-type', 'text/plain')])
                return("File already exists",)
        uploadFile = open(fileLocation,"wb")
        while True:
            data = input.read(1024)
            if not data:
                break
            uploadFile.write(data)
        uploadFile.close()
        start_response('200 OK', [('content-type', 'text/plain')])
        return "File SuccessFully Uploaded to " + path
    
    else:
        start_response('405 METHOD NOT ALLOWED',[('content-type', 'text/plain')])
        return "I am not supposed to be invoked using "+method+" method"
    
  
  
    #start_response('403 Forbidden', [('content-type', 'text/plain')])
    #return ('Hello world!',)
