# 🗃️ DaGet

Simple utility to download datasets from data respositories.

The goal of this project is to explore machine readable metadata and learn more about writing python packages.

⚠️ __script is in early development and needs testing__ ⚠️ 

## Installation

![PyPI](https://img.shields.io/pypi/v/daget)

to install daget using pip: 

```
pip install daget
```

## Usage

Download dataset via DOI or landing page url:

`daget https://doi.org/10.5878/10.5878/z8wq-5q93 ./destination`

or short form doi:

`daget 10.5878/10.5878/z8wq-5q93 ./destination`

### Example
```text
$ daget 10.7910/DVN/LFH4H8 ./test
destination:   /home/user/test
landing page:  https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/LFH4H8
 355.4KiB  Annex.pdf
 115.6KiB  List of items for measuring conceptions of democracy.csv
 81.1KiB  List of items for measuring conceptions of democracy.xlsx
 11.5KiB  Script - Part 1 Conceptions of democracy.R
 3.0KiB  Script - Part 2 Analyze items used to measure conceptions of democracy.R
 73.3KiB  Spreadsheet - Conceptions of democracy 10-2021.csv
 64.9KiB  Spreadsheet - Conceptions of democracy 10-2021.xlsx
 704.8KiB  downloaded 
```

### Use in a python script

```python
import daget

# download into an empty or new directory, returns the file list (with local 'path')
files = daget.download("10.7910/DVN/LFH4H8", "./destination")

# only list the files, nothing is downloaded
files = daget.list_files("10.7910/DVN/LFH4H8")  # [{'name', 'url', 'size'}, ...]
```

## Supported data respositories with file metadata
* schema.org/Dataset
  * https://dataverse.harvard.edu
  * https://dataverse.no
  * https://researchdata.se/catalogue
* figshare
  * https://su.figshare.com
  * https://figshare.scilifelab.se
* zenodo 
  * https://zenodo.org

## Alternatives

* [datahugger](https://github.com/J535D165/datahugger/) - wider repository suport

## Improve the script

Adding suport for additional repositories requires test cases and investigation arround how to get file metadata from the landing page.

Please help by testing and reporting [issues](https://github.com/borsna/daget/issues)

## Development

* Check out this repository and open a terminal in this directory
* Install dependecies: `pip install pyproject.toml`
* Run the module without installing it: `python3 -m daget`

## TODO

- [ ] Add error handling
- [x] Check empty destination directory
- [ ] Improve documentation
- [x] Package script for pip
