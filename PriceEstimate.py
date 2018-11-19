import requests
import time
import csv
from datetime import datetime


Tracker = 0

while True:
	try:
		Tracker = Tracker + 1
		print('Recursions',Tracker)
		headers = {
			'Authorization': 'Bearer JA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAG8AAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAkAAAABwAAAAEAAAAEAAAAE3raF-rWvNAn9rhWrXhckdsAAAAdieZf6DAq8XGl3wt2VQ9k2wFnHEmNK4iAI5Wwpc7C-psIEUUQRSe12O3VWMqiZf3ALVRag_IuSaGe4GgK8MxFJnvNdyYhh6WneGCOd-QJSRMXUo3dircxURwCNCTptZWZ98CBhe02-vXP3RtDAAAALFQO7nTljfCPYXbUiQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU',
			'Accept-Language': 'en_US',
			'Content-Type': 'application/json',
		}

		# product = requests.get('https://api.uber.com/v1.2/products?latitude=37.85159&longitude=-122.22931', headers=headers)
		# product_dict = product.json().get('products')

		"""
		List Index
		6 - UberPool
		7 - UberX
		"""
		current_time = str(datetime.now())

		# UberPool = product_dict[6]
		# UberX = product_dict[7]

		# UberPool_ID = UberPool.get('product_id')
		# UberX_ID = UberX.get('product_id')
		# print("UberPool ID",UberPool_ID)
		# print("UberX ID", UberX_ID)

		"""
		Uber Pool Estimates
		"""

		dataPool = '{\n		  "product_id": "26546650-e557-4a7b-86e7-6a3942445247",\
				 	 \n       "start_latitude": 37.85159,\
					 \n       "start_longitude": -122.22931,\
					 \n       "end_latitude": 37.875015,\
					 \n       "end_longitude": -122.260116\
					 \n     }'


		responsePool = requests.post('https://api.uber.com/v1.2/requests/estimate', headers=headers, data=dataPool)

		ResponsePool = responsePool.json()
		estimatesPool = ResponsePool.get('fare')

		expires_at_P = estimatesPool.get('expires_at')
		price_P = estimatesPool.get('value')
		duration_P = ResponsePool.get('trip').get('duration_estimate')
		distance_miles_P = ResponsePool.get('trip').get('distance_estimate')
		pickup_estimate_P = int(ResponsePool.get('pickup_estimate'))



		"""
		Uber X Estimates
		"""

		dataX = '{\n	   "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",\
				  \n       "start_latitude": 37.85159,\
				  \n       "start_longitude": -122.22931,\
				  \n       "end_latitude": 37.875015,\
			      \n       "end_longitude": -122.260116\
				  \n     }'

		responseX = requests.post('https://api.uber.com/v1.2/requests/estimate', headers=headers, data=dataX)

		ResponseX = responseX.json()
		estimatesX = ResponseX.get('fare')

		expires_at_X = estimatesX.get('expires_at')
		price_X = estimatesX.get('value')
		duration_X = ResponseX.get('trip').get('duration_estimate')
		distance_miles_X = ResponseX.get('trip').get('distance_estimate')
		pickup_estimate_X = int(ResponseX.get('pickup_estimate'))

	
		"""
		Save to CV File
		"""

		rowPool = [current_time,expires_at_P,price_P,duration_P,distance_miles_P,pickup_estimate_P]

		with open('UberPriceTrackPool.csv', 'a') as csvFilePool:
			writer = csv.writer(csvFilePool)
			writer.writerow(rowPool)

		csvFilePool.close()


		rowX = [current_time,expires_at_X,price_X,duration_X,distance_miles_X,pickup_estimate_X]

		with open('UberPriceTrackX.csv', 'a') as csvFileX:
			writer = csv.writer(csvFileX)
			writer.writerow(rowX)

		csvFileX.close()

		print('current_timeP',current_time)
		print('expire_timeP',expires_at_P)
		print('priceP',price_P)
		print('durationP',duration_P)
		print('distance_milesP',distance_miles_P) 
		print('pickup_estimateP',pickup_estimate_P)
		print('--------------------------------------')
		print('current_timeX',current_time)
		print('expire_timeX',expires_at_X)
		print('priceX',price_X)
		print('durationX',duration_X)
		print('distance_milesX',distance_miles_X) 
		print('pickup_estimateX',pickup_estimate_X)

		time.sleep(60)

	except Exception:
		pass 
		
	except KeyboardInterrupt:
		print('Manual break by user')
		























