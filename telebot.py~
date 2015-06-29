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
	if(resize==1):
		options="\"resize_keyboard\":true"
	else:
		options="\"resize_keyboard\":false"
	if(once==1):
		options=options+","+"\"one_time_keyboard\":true"
	else:
		options=options+","+"\"one_time_keyboard\":false"
	if(selective==1):
		options=options+","+"\"selective\":1"
	if(selective==2):
		options=options+","+"\"selective\":2"
	print(options)
	return("{\"keyboard\":"+json.dumps(keyboardlist).replace('"', '\"')+","+options+"}")
#sends a message to destroy existing keyboards
def keyboarddestroy(selective=''):
	if(selective==1):
		options=",\"selective\":1"
	if(selective==2):
		options=",\"selective\":2"
	if(selective==''):
		options=''
	return("{\"hide_keyboard\":true"+options+"}")
#sends messages
def sendmessage(chatid,text,replyto='',replymarkup=''):
	updateurl=tokenurl+'sendMessage'
	opts = {'chat_id': chatid, 'text': text, 'reply_to_message_id': replyto,'reply_markup':replymarkup}
	return(json.loads(requests.get(updateurl, params=opts).text))
