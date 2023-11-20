from slackclient import SlackClient
sc = SlackClient("xoxp-********************************")
   "chat.postMessage",
   channel="#general", 
   text="送信したいメッセージ"
)
