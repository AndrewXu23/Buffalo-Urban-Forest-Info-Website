# Web server code
import bottle
import json
import getInfoApp
#these are functions I built, which will be used to be called by bottle
@bottle.route('/')
def index():
    return bottle.static_file("index.html", root=".")


@bottle.route('/getinfo.js')
def ratings():
    return bottle.static_file("getinfo.js", root=".")


@bottle.route('/ajax.js')
def ajax():
    return bottle.static_file("ajax.js", root=".")


@bottle.post('/getTree')
def getTree():
    jsonBlob = bottle.request.body.read().decode()
    content = json.loads(jsonBlob)
    result = getInfoApp.get_Tree(content)
    resultJSON = json.dumps(result)
    print(resultJSON)
    return resultJSON; 

bottle.run(host="0.0.0.0", port=8080, debug=True)
