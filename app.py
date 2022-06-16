from apscheduler.schedulers.asyncio import AsyncIOScheduler as sch, asyncio as asi
from telethon import TelegramClient as tc, events as e
import requests as req, json as j, warnings as war
from storage import s

war.filterwarnings("ignore", category=DeprecationWarning)

client = tc('app', s('api_id'), s('api_hash'))

scheduler = sch(timezone="Europe/Kiev")

async def curfew_end():
	await client.send_message(
		s('news_channel'),
		s('curfew_end')['mess'] + s('bottom'),
		file=s('curfew_end')['img'],
		silent=True,
		parse_mode='md')
scheduler.add_job(
	func=curfew_end,
	trigger="cron",
	day_of_week='0-6',
	hour=5,
	minute=0,
	second=0)

async def minute_of_silence():
	await client.send_message(
		s('news_channel'),
		s('minute_of_silence')['mess'] + s('bottom'),
		file=s('minute_of_silence')['img'],
		silent=False,
		parse_mode='md')
scheduler.add_job(
	func=minute_of_silence,
	trigger="cron",
	day_of_week='0-6',
	hour=9,
	minute=0,
	second=0)

async def curfew_start():
	await client.send_message(
		s('news_channel'),
		s('curfew_start')['mess'] + s('bottom'),
		file=s('curfew_start')['img'],
		silent=False,
		parse_mode='md')
scheduler.add_job(
	func=curfew_start,
	trigger="cron",
	day_of_week='0-6',
	hour=23,
	minute=0,
	second=0)

client.start()
scheduler.start()

old = ''
first = 0

async def alarm():
	while True:
		global old, loop, first

		now = j.loads(req.get(s('alarm_server')).content)['Kyiv City']

		if (first != 0):
			if (now != old):
				if ('None' in str(now)):
					await client.send_message(
						s('news_channel'),
						s('alert_end')['mess'] + s('bottom'),
						file=s('alert_end')['img'],
						silent=True,
						parse_mode='md')

				elif ('full' in str(now)):
					await client.send_message(
						s('news_channel'),
						s('alert_start')['mess'] + s('bottom'),
						file=s('alert_start')['img'],
						silent=True,
						parse_mode='md')

		old = now
		first = 1
		await asi.sleep(10)

@client.on(e.NewMessage(chats=s('control_channel')))
async def normal_handler(event):
	if s('alert_start_control')['find'] in str(event.message):
		await client.send_message(
			s('news_channel'),
			s('alert_start')['mess'] + s('bottom'),
			file=s('alert_start')['img'],
			silent=True,
			parse_mode='md')

	if s('alert_end_control')['find'] in str(event.message):
		await client.send_message(
			s('news_channel'),
			s('alert_end')['mess'] + s('bottom'),
			file=s('alert_end')['img'],
			silent=True,
			parse_mode='md')

loop = asi.get_event_loop()
loop.create_task(alarm())
loop.run_forever()

client.run_until_disconnected()
