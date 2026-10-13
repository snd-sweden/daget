import requests

def matches(url_parsed):
  return url_parsed.hostname == 'zenodo.org'

def get_file_list(url_parsed):
  id = url_parsed.path.split('/')[-1]
  url = "https://zenodo.org/api/records/{id}".format(id = id)
  r = requests.get(url, headers={'Host': 'localhost', 'User-Agent' : 'daget', 'Accept' : '*/*'})
  meta = r.json()

  files = []
  for file in meta['files']:
    files.append({
      'url'  : file['links']['self'],
      'size' : file['size'],
      'name' : file['key']
    })
  return files
