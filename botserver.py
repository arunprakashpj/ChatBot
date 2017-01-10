from flask import Flask
from flask import request
from flask import make_response
import json
import actions

app = Flask(__name__)

def processRequest(req):
    #replace with the entity you have trained for
    action = req.get("result").get("action")
    response_message = ""

    if  action == "get_info":#<YOUR ACTION NAME>:
        entity = req.get("result").get("parameters")#.get("your entity name")
        response_message = actions.get_info(entity)

    return {"speech": response_message,
            "displayText": response_message,
            # "data": data,
            # "contextOut":  [{"name":"company name", "lifespan":2, "parameters":{"city":"Rome"}}],
            "source": "webbot-api"
            }

@app.route('/',methods = ["POST"])
def sitebot_webook_handler():
    req = request.get_json(silent=True, force=True)

    # print("Request:")
    # print(json.dumps(req, indent=4))
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    # print res
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
