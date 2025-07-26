import argparse
import requests

def download_file(url, output):
    if not output:
        output = url.split('/')[-1]
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(f'data/{output}', 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

parser = argparse.ArgumentParser()

parser.add_argument('url', type=str, help='The URL to get data from.')
parser.add_argument('-o', '--output', type=str, default=None, help='Output file name')
args = parser.parse_args()

url = args.url
output = args.output
print(f'URL: {url}')
print(f'Output: {output}')
download_file(url, output)


# python3 10-command-line-util.py https://www.bu.edu/csmet/files/2018/05/CS201_C1_Spring-2017.pdf out.pdf
# python3 10-command-line-util.py https://www.bu.edu/csmet/files/2018/05/CS201_C1_Spring-2017.pdf -o result.pdf
# python3 10-command-line-util.py https://www.bu.edu/csmet/files/2018/05/CS201_C1_Spring-2017.pdf