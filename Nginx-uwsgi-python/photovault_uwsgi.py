import cherrypy
import re
import os
sys.path.append('/home/yuva/photovault/prototypes/PVprototypes/Nginx-uwsgi-python')
def noBodyProcess():
    """Sets cherrypy.request.process_request_body = False, giving
    us direct control of the file upload destination. By default
    cherrypy loads it to memory, we are directing it to disk."""
    cherrypy.request.process_request_body = False

cherrypy.tools.noBodyProcess = cherrypy.Tool('before_request_body', noBodyProcess)


class server(object):

    @cherrypy.expose
    def default(self,*args,**kwargs):
        url = cherrypy.request.path_info
        uploadsDir = "/files/pvss/"
        if cherrypy.request.method == "POST":                
            match = re.search("[/]$", url )
            if match:
                raise cherrypy.HTTPError("403 Forbidden", "You are not allowed to do this operation in this URI")
            else:
                x = url.split('/')
                filename =  x[(len(x)-1)]
                fileLocation = uploadsDir + url
                folderLocation = uploadsDir + (url.replace(filename , ""))
                print folderLocation
                d = os.path.dirname(folderLocation)
                if not os.path.exists(d):
                    print " Making Directory!!!"
                    os.makedirs(d)
                if os.path.exists(fileLocation):
                    raise cherrypy.HTTPError("403 Forbidden", "You are not allowed to do this operation in this URI")
#                if os.path.exists(fileLocation):
#                    raise cherrypy.HTTPError("403 Forbidden", "You are not allowed to do this operation in this URI")
#                cl = cherrypy.request.headers['Content-Length']
#                rawbody = cherrypy.request.body.read(int(cl))
                size = 0 
                uploadFile = open(fileLocation,"wb")
                while True:
                    data = cherrypy.request.body.read(8192)
                    if not data:
                        break
                    size += len(data)
                    uploadFile.write(data)
                uploadFile.close()
                return "File SuccessFully Uploaded to " + url
        
        else:
            return "I am Not Supposed to be invoked using *** method"
#       
#    def handleUrl(self,url):
#       


# remove any limit on the request body size; cherrypy's default is 100MB
# (maybe we should just increase it ?)
cherrypy.server.max_request_body_size = 0

# increase server socket timeout to 60s; we are more tolerant of bad
# quality client-server connections (cherrypy's defult is 10s)
cherrypy.server.socket_timeout = 60
cherrypy.response.timeout = 3600       

def application(environ, start_response):
  cherrypy.tree.mount(server(), '/', None)
  return cherrypy.tree(environ, start_response)

    
#import os.path
#config = os.path.join(os.path.dirname(__file__), 'server.conf')

#if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to all URI
#    cherrypy.quickstart(server(), config=config)
#else:
    # This branch is for the test suite; you can ignore it.
    #cherrypy.tree.mount(server(), config=config)
