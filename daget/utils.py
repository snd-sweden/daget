import urllib, urllib.error
from daget.exceptions import RepoError, ResolveError


def get_redirect_url(url):
  # if url provided is a shorthand doi (TODO: check with regex)
  if not url.startswith(('http://', 'https://')):
    url = 'https://doi.org/' + url

  opener = urllib.request.build_opener()
  opener.addheaders = [('User-Agent', 'daget')]
  urllib.request.install_opener(opener)
  try:  
    r = urllib.request.urlopen(url)
    return r.geturl()
  except urllib.error.HTTPError:
    raise ResolveError(f"{url} not found") 
  
def download_file(url, target, progress=None):
  opener = urllib.request.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0'), ('Accept', '*/*')]
  urllib.request.install_opener(opener)
  urllib.request.urlretrieve(url, target, progress)

def size_as_string(bytes, suffix="B"):
  for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
    if abs(bytes) < 1024.0:
      return f"{bytes:3.1f}{unit}{suffix}"
    bytes /= 1024.0
  return f"{bytes:.1f}Yi{suffix}"

def show_progress(block_num, block_size, total_size):
  print(bcolors.OKGREEN, round(block_num * block_size / total_size *100, 1), "%", bcolors.ENDC, end="\r")

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'