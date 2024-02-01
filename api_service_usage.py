import requests
import json
import time

if __name__ == "__main__":

    url = "http://0.0.0.0/v1/completions"

    headers = {"Content-Type": "application/json"}

    prompt = ''' 
    写一个斐波那契额的算法demo？
    '''
    data = {"prompt": prompt}

    start_time = time.time()
    response = requests.post(url, headers=headers, data=json.dumps(data))
    end_time = time.time()
    print(response.text)

