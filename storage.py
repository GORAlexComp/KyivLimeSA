import os, dotenv as de

dp = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dp): de.load_dotenv(dp)

def s(el):
	st = {
		'api_id': os.environ.get('app_id'),
		'api_hash': os.environ.get('hash'),
		'news_channel': os.environ.get('news_channel'),
		'control_channel': os.environ.get('control_channel'),
		'alarm_server': os.environ.get('alarm_server'),
		'bottom': '\n\n〰️〰️〰️\n' +
			'[💌 Підписатись](https://t.me/' +
			os.environ.get('news_channel') + ') | [💬 Чат](https://t.me/' +
			os.environ.get('news_channel') + 'chat)\n' + 
			'✏️ Запропонувати новину',
		'alert_start_control': {
			'find': os.environ.get('alert_command_s')
		},
		'alert_end_control': {
			'find': os.environ.get('alert_command_e')
		},
		'alert_start': {
			'find': '‼️ ATTENTION! Air raid sirens in Kyiv!',
			'mess': '#повітрянатривога #оголошення',
			'img': os.environ.get('main_server') +
				os.environ.get('alert_s_img')
		},
		'alert_end': {
			'find': '❕Air siren all clear!',
			'mess': '#повітрянатривога #відбій',
			'img': os.environ.get('main_server') +
				os.environ.get('alert_e_img')
		},
		'minute_of_silence': {
			'mess': '#хвилинамовчання',
			'img': os.environ.get('main_server') +
				os.environ.get('minute_img')
		},
		'curfew_start': {
			'mess': '#комендантськагодина #початок',
			'img': os.environ.get('main_server') +
				os.environ.get('curfew_s_img')
		},
		'curfew_end': {
			'mess': '#комендантськагодина #кінець',
			'img': os.environ.get('main_server') +
				os.environ.get('curfew_e_img')
		}
	}

	return st[el]
