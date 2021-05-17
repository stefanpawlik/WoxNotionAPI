from wox import Wox
import requests
import json 

class NotionAPI(Wox):

    # query is default function to receive realtime keystrokes from wox launcher
    def query(self, query):
        results = []
        results.append({
            "Title": "Hello World",
            "SubTitle": "Query: {}".format(query),
            "IcoPath":"Images/app.png",
            "ContextData": "ctxData",
            "JsonRPCAction": {
                'method': 'take_action',
                'parameters': ["{}".format(query)],
                'dontHideAfterAction': False
            }
        })
        return results

    def take_action(self, query):
        
        url = "https://api.notion.com/v1/pages"

        payload = json.dumps({
        "parent": {
            "database_id": "---"
        },
        "properties": {
            "Name": {
            "title": [
                {
                "type": "text",
                "text": {
                    "content": query,
                }
                }
            ]
            },
            "HP": {
            "id": "IdQh",
            "type": "select",
            "select": {
                "id": "---",
                "name": "YES",
                "color": "red"
            }
            }
        }
        })
        headers = {
        'Authorization': 'Bearer ---',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return None

if __name__ == "__main__":
    NotionAPI()
