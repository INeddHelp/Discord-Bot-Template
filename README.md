# Discord-Bot-Template
#
# Guide on how to set up your discord bot

- First off download the file 'bot.py' from here: 

- Go to https://discord.com/developers/applications
    - Click on 'New Application'
    - Give a name to your discord bot and click on 'Create'

---

- Once you did that you are free to edit the description or the icon of your bot, after that go to 'Bot' on the left
- After clicking on 'Bot' on the left, click 'Add Bot'
- Make sure to click on 'View Token' and 'Copy'
- Now open the file 'bot.py' and paste in the last line between the apostrophes
- Save the file
    
---

- Head over to the 'OAuth2' bar
- Click on 'URL generator'
- Tick 'Bot'
- Allow everything in 'TEXT PERMISSION'
- Copy the URL and save it somewhere safe like a URL.txt file in your computer

---

- Now go to https://uptimerobot.com/ and register
- After doing so click on 'Add New Monitor'
- In 'Monitor Type' select HTTP(s)
- (Don't close the page) Go to https://gist.github.com/INeddHelp/de3f0f8c292eb64b1ab7d562bab673bc/raw/discord_bot.py , right click and click on 'Save as'
- Now take the token you put in bot.py and place it in discord_bot.py always in the last line between the apostrophes
- Save the file as a .py file 
- Go to https://gist.github.com/
- Create a new gist
- Paste the code and save it as discord_bot.py
- Now put in the URL section of uptimerrobot.com the URL of your gist (YOU HAVE GOT TO MODIFY THE URL, ADD TO THE END /raw/<NAME_OF_THE_GIST.py)
- Now click on 'Create Monitor'

---

- Now go on Discord
- Create a new server
- Use the link you copied before and paste it on google
- Invite your bot to the server 
- Now type in chat @the-name-you-gave-your-bot and it should print out 'Hello!'
