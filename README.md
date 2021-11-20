# AutoSS
AutoSS is an automated screenshot capturing took. This Script takes a screenshot every N seconds.

## Installation

#### Set up a virtualenv environment
```bash
pip install virtualenv
```
Create a virtualenv
```bash
virtualenv env
```
Activate the created environment
```bash
source env/bin/activate 
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `requirements.txt`.

```bash
pip install -r requirements.txt
```

## Usage

Run `autoss.py` and enter the interval (in minutes) between which screenshots are to be taken.
It will be creating a folder named `screenshots` in the same directory to save the captured screenshots.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



## License
[MIT](https://choosealicense.com/licenses/mit/)
