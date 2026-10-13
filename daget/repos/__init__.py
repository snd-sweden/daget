import urllib.parse
from daget.repos import zenodo, figshare, dataverse, schema_org

# Repositories with a dedicated API; anything else falls back to schema.org JSON-LD.
_repos = [zenodo, figshare, dataverse]

def get_file_list_from_repo(url):
  url_parsed = urllib.parse.urlparse(url)

  for repo in _repos:
    if repo.matches(url_parsed):
      return repo.get_file_list(url_parsed)

  return schema_org.get_file_list(url)
