from flask import Flask, request, jsonify, send_file
from pytube import YouTube
from playwright.sync_api import sync_playwright
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#from flask import Flask, request, jsonify, send_file
#from pytube import YouTube
#from selenium.webdriver import Chrome
#from playwright.sync_api import sync_playwright
#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
app = Flask(__name__)
service = Service(executable_path=r'/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(service=service, options=options)



#chrome_options = Options()
#chrome_options.add_argument("--headless")

৳browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

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
	driver = webdriver.Chrome()
	return "send_file('/1.py')"
		
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
