import requests
import json
#remembers bot token and creates a URL that can be used to connect to the API
def authorise(authtoken):
	global tokenurl
	tokenurl = 'https://api.telegram.org/bot'+authtoken+'/'

#gets updates from the API and returns them as python readable data
def getupdates(offset,timeout,debug):
	updateurl=tokenurl+'getUpdates'
	opts = {'offset': offset, 'timeout': timeout}
	return(json.loads(requests.get(updateurl, params=opts).text))
#gets bot name and info, returns as python readable data
def getme():
	updateurl=tokenurl+'getMe'
	return(json.loads(requests.get(updateurl).text))
#sends messages,optional parameters still need to be added (see API Documentation)
def sendmessage(chatid,text,):
	
