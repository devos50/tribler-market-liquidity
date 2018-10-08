import requests
import time

while True:
    time.sleep(9)
    print "Creating order..."
    response = requests.put("http://localhost:8085/market/asks", data={
        "first_asset_amount": 10,
        "second_asset_amount": 10,
        "first_asset_type": "DUM1",
        "second_asset_type": "DUM2",
        "timeout": 10
    })
    if response.status_code != 200:
        print "ERROR OCCURED: " % response.text
        exit(1)
