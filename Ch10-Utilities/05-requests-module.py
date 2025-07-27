import requests

url = 'https://jsonplaceholder.typicode.com/posts'
get_response = requests.get(url)
print(f'HTTP GET response: \n{get_response.json()}')

post_data = {
    "title" : "foo",
    "body" : "bar",
    "userId" : 1,
}
post_headers = {
    "Content-Type": "application/json; charset=utf-8",
}
post_response = requests.post(url, json=post_data, headers=post_headers)
print(f'HTTP POST response: \n{post_response.json()}')