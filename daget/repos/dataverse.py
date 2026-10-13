import requests, urllib.parse

def matches(url_parsed):
  return url_parsed.path in ('/citation', '/dataset.xhtml') and 'persistentId' in urllib.parse.parse_qs(url_parsed.query)

def get_file_list(url_parsed):
  base = url_parsed.scheme + '://' + url_parsed.netloc
  pid = urllib.parse.parse_qs(url_parsed.query)['persistentId'][0]
  r = requests.get(base + '/api/datasets/:persistentId/', params={'persistentId': pid}, headers={'User-Agent': 'daget'})
  meta = r.json()

  files = []
  for f in meta['data']['latestVersion']['files']:
    df = f['dataFile']
    files.append({
      'url'  : '{base}/api/access/datafile/{id}'.format(base = base, id = df['id']),
      'size' : df.get('filesize'),
      'name' : f.get('label') or df.get('filename')
    })
  return files
