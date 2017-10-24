from bot_class import SimpleResponseBot
from config import token

def main(my_bot):	
	new_offset = None
	while 1:
		my_bot.get_updates(new_offset)
		cur_update = my_bot.get_last_update()
		if cur_update != None:
			cur_update_id = cur_update['update_id']
			cur_chat_id = cur_update['message']['chat']['id']
			my_bot.auto_response(cur_chat_id)
			new_offset = cur_update_id + 1
		else:
			continue
	
if __name__ == '__main__':
	try:
		test_bot = SimpleResponseBot(token)
		main(test_bot)
	except KeyboardInterrupt:
		exit()
		
