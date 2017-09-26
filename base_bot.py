import requests
import datetime
import random

class BaseBot:
	
	def __init__(self, token):
		self.token = token
		self.api_url = 'https://api.telegram.org/bot%s/' % token

	def get_updates(self, offset=None, timeout=30):
		method = 'getUpdates'
		params = {'timeout': timeout, 'offset': offset}
		resp = requests.get(self.api_url + method, params)
		result_json = resp.json()['result']
		return result_json
		
	def send_message(self, chat_id, text):
		params = {'chat_id': chat_id, 'text': text}
		method = 'sendMessage'
		resp = requests.post(self.api_url + method, params)
		return resp

	def get_last_update(self):
		get_result = self.get_updates()
		if len(get_result) > 0:
			last_update = get_result[-1]
		else:
			last_update = get_result(len(get_result))
		return last_update

m_bot = BaseBot('451270396:AAFXlo_QyZ2x9a5OWIGhL4XSdgTWOY7S_2Y')


'''
#TEST
json = m_bot.get_updates()

print(json)
'''


motivations = ('встрой поисковики', 
			'взбодрись и продолжай', 
			'читай книги',
			'не тупи, делай',
			'ты молодец',
			'изучай апи',
			'изучай линукс',
			'изучай питон',
			'решай задачи',
			'доделай меня',
			'изучай машинное обучение')
			
advice = 'совет'

now = datetime.datetime.now()

def main():
	new_offset = None

	while 1:
		m_bot.get_updates(new_offset)
		last_update = m_bot.get_last_update()
		
		last_update_id = last_update['update_id']
		last_chat_text = last_update['message']['text']
		last_chat_id = last_update['message']['chat']['id']
		last_chat_name = last_update['message']['chat']['first_name']
		
		if last_chat_text.lower() == advice:
			m_bot.send_message(last_chat_id, random.choice(motivations))
	
		new_offset = last_update_id + 1
		

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
		 

