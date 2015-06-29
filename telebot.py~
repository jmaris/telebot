import requests
import json
def authorise(authtoken):
	global token
	token = authtoken
def getupdates(updateid,timeout,debug):
	updateurl='https://api.telegram.org/bot'+token+'/getUpdates?timeout=100'
	opts = {'updateid': updateid, 'timeout': timeout}
	return(json.loads(requests.get(updateurl, params=opts).text))
	 
