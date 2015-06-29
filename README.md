# Telebot
*A Python interface for the Telegram Bot API*

**Please not that telebot is currently under heavy development and is not ready for use in production yet.**

## Usage Instructions
Telebot is a library (module) that facilitates the creation of Telegram bots.
It is split into two parts : 
- A Communications library which handles the delivery and return of data between your bot and your users (which leverages Telegram's Bots API)
- A "concurrency" library which allows your bot to interact with different users differently (aka it launches a seperate instance per chat) **Please note that this library does not yet work and has not been developed**

## Status
#### Communications Library
| **Telegram Bot API Method** | **_Supported ?_** |
|:---------------------------:|:-----------------:|
|            getMe            |        Yes        |
|         sendMessage         |        Yes        |
|        forwardMessage       |         No        |
|          sendPhoto          |         No        |
|          sendAudio          |         No        |
|         sendDocument        |         No        |
|         sendSticker         |         No        |
|          sendVideo          |         No        |
|         sendLocation        |         No        |
|        sendChatAction       |         No        |
|     getUserProfilePhotos    |         No        |
|          getUpdates         |        Yes        |
|          setWebhook         |         No        |

## Usage
####Getting Started
First of all you need to import the module and authorise. Put it in the same directory as your script and run
```python
import telebot as tb
tb.authorise('your telegram bot token here')
```
- the _tb_ in the above code can be replaced by whatever you wish, What we are doing here is creating a python object that will communicate with telegram's bot API for us. In this documentation the object will be named tb throughout.
- You will need to replace yourtelegrambottokenhere by your telegram bot token (obviously). In order to learn more about obtaining one, I recommend you check out telegrams Introduction to bots (https://core.telegram.org/bots).

####Checking everything's working
Before starting to code, we recommend you ensure that your token is working as expected, the best way to do this is using the getme function.
```python
tb.getme()
```
This should return something along the lines of : 
> {'ok': True, 'result': {'id': **your bots ID**, 'first_name': '**your bots name**', 'username': '**your bots username**'}}

####Getting Updates
When a user interacts with your bot, that interaction is stored on telegrams server, in order to get the interactions and act on them we have to send a specific call to the server, the server returns JSON, but this library converts it into python variables and lists.

```python
tb.getupdates(*offset*, *timeout*, *debug*)
```
  - **offset** :
    - Default : *None*
    - Required : *No*
    - Each update has an ID, offset defines the ID from which updates are displayed. Once you have chosen an offset, all updates before that one are wiped from telegrams servers. For an example of this please see the wiki.
  - **timeout** :
    - Default : *0*
    - Required : *No*
    - The default behaviour for updates is based on *polling*, this means we ask the server if there are updates availible once in a while. This is heavy on resources both for us and for telegrams servers. Therefore I recommend setting a timeout. A timeout mimics push style communications by opening a link to telegrams servers, telegrams servers will only reply when there is an update. The timeout is the time for which your bot will wait for data from telegrams servers before giving up.
  - **debug** :
    - Default : *0*
    - Required : *No*
    - Though Debug has not yet been implemented, in the future it will return the JSON output to the user.

#### Sending Messages
Sending messages is pretty simple.
```python
tb.sendmessage(*chatid*,*text*,*replyto*,*replymarkup*)
```
  - **chatid** :
    - Default : *None*
    - Required : *Yes*
    - Updates will contain messages from different chat's, each chat has a chatid so you can easily respond to the chat.

  - **text** :
    - Default : *None*
    - Required : *Yes*
    - The text to be sent.

  - **replyto** :
    - Default : *None*
    - Required : *No*
    - In the event that you are replying to a message, you can put the messages ID here, Then telegram will treat it as a reply.

  - **replymarkup** :
    - Default : *None*
    - Required : *No*
    - replymarkup contains extra things to be sent with your reply. These are detailed on The Telegram Bot API website, The Primary thing you can do with them is create a custom keyboard for the users of your bot (With Buttons). In order to simplify the task of creating keyboards we have created 2 functions, one to create and one to remove a keyboard. They are detailed below.
