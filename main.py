import requests
import json

answer = input('What is your face shape? Choose from: round, oval, heart, diamond, square, triangle, long: ')

def get_suggested_hairstyle(answer):
    response = requests.get("http://127.0.0.1:5001/hairstyle/{}".format(answer)
                            )
    print(response.json())
    return response

if __name__ == '__main__':
    get_suggested_hairstyle(answer)
