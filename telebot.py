import requests
import json
#remembers bot token and creates a URL that can be used to connect to the API
def authorise(authtoken):
	global tokenurl
	tokenurl = 'https://api.telegram.org/bot'+authtoken+'/'

#gets updates from the API and returns them as python readable data
def getupdates(offset='',timeout=0,debug=0):
	updateurl=tokenurl+'getUpdates'
	opts = {'offset': offset, 'timeout': timeout}
	return(json.loads(requests.get(updateurl, params=opts).text))
#gets bot name and info, returns as python readable data
def getme():
	updateurl=tokenurl+'getMe'
	return(json.loads(requests.get(updateurl).text))
#generates keyboards
def keyboardmake(keyboardlist,resize=1,once=1,selective=''):
	return("{\"keyboard\":"+json.dumps(keyboardlist).replace('"', '\"')+"}")
#sends messages
def sendmessage(chatid,text,replyto='',replymarkup=''):
	updateurl=tokenurl+'sendMessage'
	opts = {'chat_id': chatid, 'text': text, 'reply_to_message_id': replyto,'reply_markup':replymarkup}
	return(json.loads(requests.get(updateurl, params=opts).text))
