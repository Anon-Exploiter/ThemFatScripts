import requests 
import base64
import os

with open('token.inc', 'r') as f: SLACK_TOKEN = base64.b64decode(f.read().strip()).decode().strip()

def listDirectory(path):
	images 		= os.listdir(path)
	_images 	= []

	for imageNames in images:
		extension 	= imageNames.split(".")[::-1][0]

		if (extension == "png" or extension == "jpg" or extension == "gif" or extension == "svg" or extension == "jpeg"):
			_images.append(imageNames)

	return(_images)

def changeProfilePicture(pictures, slackToken):
	for picture in pictures:
		request 	= requests.post(
			f"https://slack.com/api/users.setPhoto?token={SLACK_TOKEN}&pretty=1",
			headers = {
				"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
				"Accept": "*/*",
				"Origin": "https://api.slack.com",
				"Sec-Fetch-Site": "same-site",
				"Sec-Fetch-Mode": "cors",
				"Accept-Encoding": "gzip, deflate",
				"Accept-Language": "en-US,en;q=0.9,la;q=0.8",
				"Connection": "close",
			},
			files = {
				'image': open(picture, 'rb')
			},
		)

		print(request.text)

def main():
	currentDirectory 	= os.getcwd()
	filesInDirectory 	= listDirectory( currentDirectory )
	changeProfilePicture(filesInDirectory, SLACK_TOKEN)

if __name__ == '__main__':
    main()
