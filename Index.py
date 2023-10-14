from flask import Flask, request, jsonify, send_file
from pytube import YouTube

app = Flask(__name__)

# Sample data for demonstration
items = []

# Create an endpoint to add items
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    items.append(data)
    return jsonify(data), 201

# Create an endpoint to get all items
@app.route('/<yt_link>', methods=['GET'])
def read_items(yt_link):
	#yt= YouTube(yt_link)

#print(yt.streams.all()[0].url)
	#return yt.streams.all()[0].url
	return send_file('/1.py')
@app.route('/',methods=['POST'])
def run():
	data=request.get_json()
	yt= YouTube("https://youtu.be/uRYHX4EwYYA?si=-DMcyaFRQqyloGIP")
	return yt.streams.all()[0].url

# Create an endpoint to get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def read_item(item_id):
    if item_id < len(items):
        return jsonify(items[item_id])
    else:
        return "Item not found", 404



if __name__ == '__main__':
    app.run(debug=False)
