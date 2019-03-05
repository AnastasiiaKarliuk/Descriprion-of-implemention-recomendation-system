# from urllib.request import urlopen, quote
# import json
#
#
# def main():
#     token = 'EAAERuEnX25YBAI5fT3gdfU3AbZAHvOWqOPhisAPC4kr9xom5SsbqtJ9HIvnx4bVHhNLHPUecCpvNj6z33WLwrDXW6IyNmzeqPQRhjQP0gYjlp00Fn6Av3ORh5GkdEffZAU9ZASL5BW1sH6L5sqRO1EVuoL4iStaTlCQc3wPXAL9iwWlf44uUKcfuxBeuFQZD'
#
#
#     list_companies = ["pg/arianagrande/events/"]
#     graph_url = "http://graph.facebook.com/"
#
#     for company in list_companies:
#         current_page = graph_url + company
#
#         web_response = urlopen(current_page)
#         readable_page = web_response.read()
#         json_fbpage = json.loads(readable_page)
#
#         print(company + " page")
#         print(json_fbpage["id"])
#         print(json_fbpage["likes"])
#         print(json_fbpage["talking_about_count"])
#         print(json_fbpage["username"]+'\n')
#
#
# if __name__ == "__main__":
#     main()


from urllib import request
import json


def get_page_data(page_id, access_token):
    api_endpoint = "https://www.facebook.com/pg/arianagrande/events/"
    fb_graph_url = api_endpoint + page_id + "?fields=id,name,likes,link&access_token=" + access_token
    try:
        api_request = request.Request(fb_graph_url)
        api_response = request.urlopen(api_request)

        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError as e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason


page_id = "100004460293468"  # username or id
token = "300958187248534|ut3aXylJ-sUjDV67sGcSSg4ROlI"  # Access Token
page_data = get_page_data(page_id, token)

print(page_data)

print("Page Name:" + page_data['name'])
print("Likes:" + str(page_data['likes']))
print("Link:" + page_data['link'])