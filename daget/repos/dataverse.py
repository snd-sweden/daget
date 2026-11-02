import requests, urllib.parse
from daget.exceptions import RepoError

def matches(url_parsed):
  return url_parsed.path in ('/citation', '/dataset.xhtml') and 'persistentId' in urllib.parse.parse_qs(url_parsed.query)

def get_file_list(url_parsed):
  base = url_parsed.scheme + '://' + url_parsed.netloc
  pid = urllib.parse.parse_qs(url_parsed.query)['persistentId'][0]
  r = requests.get(
    base + '/api/datasets/:persistentId/', 
    params={'persistentId': pid}, 
    headers={'User-Agent': 'daget'}
  )

  r.raise_for_status()

  meta = r.json()

  if meta.get('status') != 'OK':
    raise RepoError(
        f"Dataverse API error: {meta.get('message', 'Unknown error')}"
    )

  files = []
  for f in meta['data']['latestVersion']['files']:
    df = f['dataFile']
    files.append({
      'url'  : '{base}/api/access/datafile/{id}'.format(base = base, id = df['id']),
      'size' : df.get('filesize'),
      'name' : f.get('label') or df.get('filename')
    })
  return files
