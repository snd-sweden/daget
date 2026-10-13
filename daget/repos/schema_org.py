import requests, json
from bs4 import BeautifulSoup

def get_file_list(url):
  daget_headers={'User-Agent' : 'daget', 'Accept' : 'application/ld+json'}

  result = requests.get(url, headers=daget_headers)

  # retry with host header
  if not result.ok:
    daget_headers['Host'] = 'localhost'
    result = requests.get(url, headers=daget_headers)

  try:
    schema_org = result.json()
  except:
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    text = "".join(soup.find('script', {'type':'application/ld+json'}).contents)

    schema_org = json.loads(text)

  schema_files = schema_org['distribution']
  if not isinstance(schema_files, list):
    schema_files = [schema_files]

  files = []
  for f in schema_files:
    size = f.get('contentSize', None)
    if isinstance(size, str) and size.lower().endswith('b'):
      size = size.lower().replace('b', '').strip()

    file={
      'url'  : f.get('contentUrl', None),
      'size' : int(size) if size else None,
      'name' : f.get('name', None)
    }
    files.append(file)

  return files
