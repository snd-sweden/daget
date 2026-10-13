import requests

def matches(url_parsed):
  return 'figshare' in (url_parsed.hostname or '')

def get_file_list(url_parsed):
  id = url_parsed.path.split('/')[-2]
  version = url_parsed.path.split('/')[-1]
  url = "https://api.figshare.com/v2/articles/{id}/versions/{version}".format(id = id, version = version)
  r = requests.get(url, headers={'Host': 'localhost', 'User-Agent' : 'daget', 'Accept' : '*/*'})
  meta = r.json()

  files = []
  for file in meta['files']:
    files.append({
      'url'  : file['download_url'],
      'size' : file['size'],
      'name' : file['name']
    })
  return files
