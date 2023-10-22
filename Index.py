from pytube import YouTube
import re
from flask import Flask, request, jsonify, send_file 
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def read_item():
	return "request.args.get()"
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
