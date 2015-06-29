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
- You will need to replace yourtelegrambottokenhere by your telegram bot token (obviously). In order to learn more about obtaining one, We recommend you check out telegrams Introduction to bots (https://core.telegram.org/bots).

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
tb.getupdates( offset, timeout, debug )
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
tb.sendmessage( chatid, text, replyto, replymarkup )
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

### Reply Markup Functions
Telegram's Bot API allows for certain "special markups" on messages, for example markup to display a special keyboard with buttons of your choice. Normally you need to send your keyboard layout in JSON, however to simplify the process we have coded 2 functions that act as variables for the replymarkup variable of sendmessage. 
**Please Note that these functions do not work alone, but rather as part of a sendmessage(). Examples of this are in the examples file.**

#### Creating a Custom Keyboard
```python
keyboardmake(keyboardlist,resize,once,selective)
```
  - **keyboardlist** :
    - Default : *None*
    - Required : *Yes*
    - keyboardlist is a python List containing at least one other python list that defines the layout of your keyboard, The best way of explaining this is with examples, please see the Keyboard examples in the example file.

  - **resize** :
    - Default : *1*
    - Required : *No*
      - When resize is set to 1, the keyboard will resize to fit the buttons you put on it.
      - When it is set to 0 it will remain the same size as your normal keyboard.

  - **once** :
    - Default : *1*
    - Required : *No*
     - When once is set to 1, the keyboard will hide itsself after a decision has been made by the user.
     - When it is set to 0 the keyboard will remain visible after the user has decided.

  - **selective** :
    - Default : *None*
    - Required : *No*
    - Selective allows the keyboard to be displayed only to a select few.
      - When selective is empty, the keyboard will be displayed to all users in the chat to which the message is sent.
      - When selective is set to 1 users that are @mentioned in the text of the Message will see the keyboard
      - When selective is set to 2, only users who are being replied to by the bot will see the keyboard.

#### Removing an existing keyboard
Keyboards are not "removed" when a button is pressed, they are simply hidden and can be brought back up at the click of a button, to remove a keyboard you must send a message with the keyboarddestroy function as replymarkup. Once again examples can be found in the examples file.

```python
keyboarddestroy(selective)
```
  - **selective** :
    - Default : *None*
    - Required : *No*
    - Selective allows the keyboard to be removed for only for a select few.
      - When selective is empty, the keyboard will be removed for all users in the chat to which the message is sent.
      - When selective is set to 1, the keyboard will be removed for users that are @mentioned in the text of the Message.
      - When selective is set to 2, the keyboard will be removed for users who are being replied to by the bot.
