from wox import Wox
import requests
import json 

class NotionAPI(Wox):

    

    # query is default function to receive realtime keystrokes from wox launcher
    def query(self, query):
        results = []
        results.append({
            "Title": "New page: {}".format(query),
            "SubTitle": "Create new Notion page",
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

        with open("config.json", "r") as f:
            my_vars = json.load(f)

        payload = json.dumps({
        "parent": {
            "database_id": my_vars["database_id"]
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
        }
        })
        headers = {
        'Authorization': my_vars["integration_secret"],
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return None

if __name__ == "__main__":
    NotionAPI()
