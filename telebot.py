import requests
import json
def authorise(authtoken):
	global tokenurl
	tokenurl = 'https://api.telegram.org/bot'+authtoken+'/'
def getupdates(updateid,timeout,debug):
	updateurl=tokenurl+'getUpdates'
	opts = {'update_id': updateid, 'timeout': timeout}
	return(json.loads(requests.get(updateurl, params=opts).text))
def getme():
	updateurl=tokenurl+'getMe'
	return(json.loads(requests.get(updateurl).text))
