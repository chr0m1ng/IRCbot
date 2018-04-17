from imgurpython import ImgurClient

def uploadToImgur(imagePath):
  	"""Upload image to Imgur

	  :param imagePath: Absolute path to the image
	  :type imagePath: String

	  :return: Link to image on Imgur
	"""
	CLIENT_ID = os.environ.get('CLIENT_ID')
	CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

	try:
		client = ImgurClient(CLIENT_ID, CLIENT_SECRET)
		image = client.upload_from_path(imagePath)
		return image['link']
	except Exception as e:
		return "Ocorreu um erro: " + e
