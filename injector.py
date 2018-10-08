import requests
import time

counter = 0

while True:
    time.sleep(35)

    order_type = 'asks' if counter % 2 == 0 else 'bids'

    print "Creating %s order..." % order_type[:-1]
    response = requests.put("http://localhost:8085/market/%s" % order_type, data={
        "first_asset_amount": 10,
        "second_asset_amount": 10,
        "first_asset_type": "DUM1",
        "second_asset_type": "DUM2",
        "timeout": 60
    })
    if response.status_code != 200:
        print "ERROR OCCURED: " % response.text
        exit(1)
    counter += 1
