#!/usr/bin/env python3
import os, argparse
from importlib.metadata import version, PackageNotFoundError
from daget.utils import *
from daget.api import download
from daget.exceptions import ResolveError, DestinationError

# test dataset with subdirs: https://doi.org/10.5878/331q-3p13

def main():
  parser = argparse.ArgumentParser(
            prog='daget',
            description='Download dataset via DOI or landing page url',
            epilog='To improve or report a bug https://github.com/snd-sweden/daget'
  )

  try:
    daget_version = version('daget')
  except PackageNotFoundError:
    daget_version = 'unknown'

  parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {daget_version}')
  parser.add_argument('url', help="URL/DOI to the dataset")
  parser.add_argument('destination', help="Full or relative path to destination directory") 
  parser.add_argument("-l", "--list-only", action="store_true", help="Skip download")

  args = parser.parse_args()

  total_size = 0

  def on_start(landing_page, destination):
    print(f'landing page: {landing_page}')
    print(f'destination: {destination}')

  def on_file(file):
    nonlocal total_size
    size = file['size'] or 0
    total_size += size
    print(bcolors.OKBLUE, size_as_string(size).strip(), bcolors.ENDC, file['name'])

  try:
    download(args.url, args.destination, list_only=args.list_only,
             on_start=on_start, on_file=on_file, progress=show_progress)
  except ResolveError:
    print(bcolors.FAIL, f'error resolving {args.url}', bcolors.ENDC)
    exit(1)
  except DestinationError as err:
    print(bcolors.FAIL, err, bcolors.ENDC)
    exit(1)

  print(bcolors.OKGREEN, bcolors.BOLD, size_as_string(total_size), bcolors.ENDC, "downloaded ")

if __name__ == "__main__":
    main()