# sh3rlock

## Installation

```
bash install.sh
pip install -r requirements.txt
apt-get install xvfb
apt-get install tor
```
* The tool works by launching a Firefox (version 52+) in headless mode to check for XSS alerts, so make sure you have it installed.

*  You can upgrade your Firefox ESR using this command, but only do this when you are aware of what you doing 

```
bash firefox-update.sh
```

* Tested On: Kali Linux, Parrot Security, Ubuntu, Debian.

## Usage

```
python main.py -u txt_with_urls_you_want_to_check_for_xss.txt
```

## Disclaimer

Sh3rlock framework is intended to be used for legal security purposes only, and you should only use it to protect networks/hosts you own or have permission to test. Any other use is not the responsibility of the developer(s). Be sure that you understand and are complying with the Sh3rlock licenses and laws in your area. In other words, don't be stupid, don't be an asshole, and use this tool responsibly and legally.
