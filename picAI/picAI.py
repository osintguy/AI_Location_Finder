import requests
import json
import base64
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    args = parser.parse_args()
    
    
    url = "https://picarta.ai/classify"
    api_token = "GF1MCL0FGSB4A6X7AQWS"  #register to get the token 
    headers = {"Content-Type": "application/json"}
    
    # Read the image from a local file, comment out the next two lines if you read from URL 
    with open(args.filepath, "rb") as image_file:
        img_path = base64.b64encode(image_file.read()).decode('utf-8')
    
    # OR  
    
    # from a URL, comment out the next line if you read from a local file
    #img_path = "https://upload.wikimedia.org/wikipedia/commons/8/83/San_Gimignano_03.jpg"
    
    # Prepare the payload 
    payload = {"TOKEN": api_token,
            "IMAGE":  img_path}
    
    # Send the POST request with the payload as JSON data
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        print(result)
        print("Google Link to estimated location: ", f"https://www.google.com/maps/@{result['ai_lat']},{result['ai_lon']},18z")
    else:
        print("Request failed with status code:", response.status_code)
                                        
if __name__ == '__main__':
    main()
