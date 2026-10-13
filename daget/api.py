import os
from daget.utils import get_redirect_url, download_file
from daget.repos import get_file_list_from_repo
from daget.exceptions import DestinationError, RepoError

def list_files(url):
  """Return [{'name', 'url', 'size'}, ...] for a DOI or landing page url."""
  return get_file_list_from_repo(get_redirect_url(url))

def download(url, destination, list_only=False, on_start=None, on_file=None, progress=None):
  """Download all files of a dataset into an empty or new directory.

  Returns the file list, each entry with an added 'path' key.
  on_start(landing_page, destination) and on_file(file) are optional callbacks,
  progress is a urllib reporthook (block_num, block_size, total_size).
  """
  landing_page = get_redirect_url(url)
  destination = os.path.realpath(destination)

  if os.path.exists(destination) and os.listdir(destination):
    raise DestinationError(f'{destination} must be a empty directory or new directory path')
  os.makedirs(destination, exist_ok=True)

  if on_start:
    on_start(landing_page, destination)

  files = get_file_list_from_repo(landing_page)

  for file in files:
    path = os.path.realpath(os.path.join(destination, file['name']))
    # file names come from the remote repository, keep them inside destination
    if not path.startswith(destination + os.sep):
      raise RepoError(f"unsafe file name {file['name']!r}")
    file['path'] = path

    if on_file:
      on_file(file)
    if not list_only:
      os.makedirs(os.path.dirname(path), exist_ok=True)
      download_file(file['url'], path, progress)

  return files
