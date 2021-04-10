f = open("bot_conf.py", "w")
print ("The following script will create the files necessary for your bot to operate.");
print ("Please have the following ready before you begin:");
print ("1. Telegram bot token");
print ("2. Telegram bot name");
print ("3. Facebook page tag names");
print ("Press enter when you are ready to proceed...")
ENTER = input()
print ('Enter your TOKEN:')
TOKEN = input()
f.write("# the following has been entered using the setup.py script")
f.write("\n")
f.write("TOKEN = '")
f.write(TOKEN)
f.write("'")
f.write("\n")
print ('Enter the Telegram Channel name your posts will be sent to:')
chat_id = input()
f.write("chat_id = '@")
f.write(chat_id)
f.write("'")
f.close()
f = open("fbpages.csv", "w")
f.write("telegram_name,fbpage_tag,last_post_date")
f.write("\n")
print ("Give your Telegram posts a title name, eg: Scouts Posts:")
telegram_name = input()
print ("What is the URL tag for the Facebook page?")
fbpage_tag = input()
f.write(telegram_name)
f.write(",")
f.write(fbpage_tag)
f.write(",")
import datetime
currentDT = datetime.datetime.now()
f.write(currentDT.strftime("%Y-%m-%d %H:%M:%S"))
f.close()
def additional():
	while True:
		print ("Would you like to enter another Facebook page? y/n")
		another = input()
		if "y" in another:
			f = open("fbpages.csv", "a")
			f.write("\n")
			print ("Give your Telegram posts a title name, eg: Scouts Posts:")
			telegram_name = input()
			print ("What is the URL tag for the Facebook page?")
			fbpage_tag = input()
			f.write(telegram_name)
			f.write(",")
			f.write(fbpage_tag)
			f.write(",")
			import datetime
			currentDT = datetime.datetime.now()
			f.write(currentDT.strftime("%Y-%m-%d %H:%M:%S"))
			f.close()
		elif "n" in another:
			print ("Thank you, you have successfully connected your bot.")
			return
		else:
			print ("Please type y or n... ")
			continue
additional()
