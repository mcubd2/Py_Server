from pytube import YouTube
import re
from flask import Flask, request, jsonify, send_file 
from flask_cors import CORS
from twilio.rest import Client
import requests
import json
import threading
import asyncio



accurl = 'http://prepaid.desco.org.bd/api/tkdes/customer/getBalance?accountNo=14002520&meterNo='
account_sid = 'ACd79ad2ea41e6f1dc51c847c0bed217e5'
auth_token = 'f3e3ed1de8917ead69a8cbafd8f7eb92'



    
    
app = Flask(__name__)
CORS(app)
loop = asyncio.get_event_loop()
api_id = '28863345'
api_hash = '0dae6aefb121ac09f5c2d07f09493452'
phone_number = '+8801703625690'







@app.route("/call",methods=[ 'GET'])
def hello():
    call = client.calls.create(
    to='+8801703625690',  # Destination phone number
    from_='+18605984143',  # Your Twilio phone number
    url='http://your-server.com/twiml')
    print(call.sid)
    return call.sid

@app.route("/voice", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()
    resp.say("Thank you for calling! Have a great day.", voice='Polly.Amy')
    return str(resp)
@app.route('/', methods=['GET'])
def read_item():
	return "request.args.get()"
@app.route('/cheak',methods=['GET'])
def rr():
	response1 = requests.get(accurl)
	print(json.loads(response1.text)['data']['balance'] )
	
	if(json.loads(response1.text)['data']['balance'] < 80):
		response2 = requests.get('https://pipbd.cyclic.app/call')
		return response2.text

@app.route('/sms',methods=['GET'])
def rrrr():
	link="http://bulksmsbd.net/api/smsapi?api_key=uk0KnxYS1HSuilRi7CfB&type=text&number={}&senderid=8809617613445&message={}".format(request.args.get('num'),request.args.get('msg'))
	res = requests.get(link)
	return str(res.status_code)+'-----------'+res.text



@app.route('/yt', methods=['GET'])
def read_itemm():
	video = YouTube(request.args.get('yt'))
	video_streams = video.streams.all()
	title=video_streams[2].title
	text = "This is a sample text."
	mp4_find = "mp4"
	res_find = 'type="video"'
	pro_find='progressive="True"'
	pattern1 = re.compile(f"{mp4_find}")
	pattern2 = re.compile(f"{res_find}")
	pattern3 = re.compile(f"{pro_find}")
	resdict={}
	for i in video_streams:
		matches = pattern1.findall(i.url)
		matches2 = pattern2.findall(str(i))
		m3 = pattern3.findall(str(i))
		if(matches2 and matches and m3):
			print(i.url)
			print(i.resolution)
			resdict.update({i.resolution:i.url})
			#print(resdict) print(resdict.keys())
	#if "1080p" in resdict.keys():
		#hd=resdict['1080p']
		#print(resdict['1080p'])
		#return f"{hd}&title={title}"
	if "720p" in resdict.keys():
		mid=resdict['720p']
		print(resdict['720p'])
		return f"{mid}&title={title}"
	else:
		print(resdict['360p'])
		low=resdict['360p']
		print("360 bro")
		return f"{low}&title={title}"
				
if __name__ == '__main__': app.run(debug=False)
