#Examples

# Keyboard Examples

First of all, to actually design our keyboard, we should understand the structure of keyboards.
With this library we can generate keyboards from python lists.

Start with one list :
> []

Then add a list inside :
> [ [] ]

You now have a single-row keyboard, lets add some options to it
> [ ["Yes", "No"] ]

Your Keyboard will now look like this :

|  |  |
|:---:|:--:|
| Yes | No |

Want Multiple Rows ? Simply add another List inside your list
> [ ["Yes", "No"], ["Maybe","I'm not sure"]]
|  |  |
|:---:|:--:|
| Yes | No |
| Maybe | I'm not sure |


So the full command to use if you want to recreate the previous example is
>tb.sendmessage('chatid',"message to send",'',tb.keyboardmake([ ["Yes", "No"], ["Maybe","I'm not sure"]],1,1))
