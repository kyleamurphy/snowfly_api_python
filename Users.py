import requests
import config


def get_users(token, page, per_page):
    # There are a bunch of endpoints feel free to swap out the endpoints as wanted.
    endpoint = "users/"+config.cid
    # This will add some query string parameters to the request.
    query = {'page': page, 'perPage': per_page}
    # setup the authorization header on the request.
    headers = {'Authorization': "Bearer "+str(token)}
    # make the GET request to the endpoint
    request = requests.get(config.url+endpoint, headers=headers, params=query)
    # I would recommend more error handling on the status code returned from the request.
    print(request.status_code)
    # everything returned from the endpoint will be in a json format.
    return_data = request.json()
    # do whatever you want with the results. Good luck.
    print(str(return_data))
    return return_data

