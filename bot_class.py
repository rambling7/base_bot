from requests import get, post
from random import choice

class BaseBot:
	
	def __init__(self, token):
		self.token = token
		self.api_url = 'https://api.telegram.org/bot%s/' % token

	def get_updates(self, offset=None, timeout=30):
		method = 'getUpdates'
		params = {'timeout': timeout, 'offset': offset}
		resp = get(self.api_url + method, params)
		result_json = resp.json()['result']
		return result_json
		
	def send_message(self, chat_id, text):
		params = {'chat_id': chat_id, 'text': text}
		method = 'sendMessage'
		resp = post(self.api_url + method, params)
		return resp

	def get_last_update(self):
		get_result = self.get_updates()
		if len(get_result) > 0:
			last_update = get_result[-1]
		else:
			last_update = None
		return last_update
		
class SimpleResponseBot(BaseBot):
	
	def auto_response(self, response_id):
		response_base = (	'встрой поисковики', 
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
		self.send_message(response_id, choice(response_base))
		
class TestCommandBot(BaseBot):
	pass
	
	
