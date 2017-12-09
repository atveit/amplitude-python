[![CircleCI](https://circleci.com/gh/atveit/amplitude-python.svg?style=svg&circle-token=dfb7391f33d23ac3dad467b60ca34b36e7a37ebb)](https://circleci.com/gh/atveit/amplitude-python)

# amplitude-python
Python API for Amplitude Analytics Logging - https://amplitude.com

This API is a simple (unofficial) wrapper for the [Amplitude HTTP API](https://amplitude.zendesk.com/hc/en-us/articles/204771828-HTTP-API)

## 1. Install amplitude-python

Potential preparation before installing: create and activate virtualenv or conda environment

### 1.1 Install from pypi with conda or pip
```bash
pip install amplitude-python
```

### 1.2 Install from github
```bash
$ git clone https://github.com/atveit/amplitude-python.git
$ cd amplitude-python
$ python setup.py instal
```

## 2. Logging to Amplitude with amplitude-python
Recommend having a look at [Amplitude HTTP API Documentation](https://amplitude.zendesk.com/hc/en-us/articles/204771828-HTTP-API) before start logging.

```python
import amplitude	

# initialize amplitude logger
amplitude_logger = amplitude.AmplitudeLogger(api_key = "SOME_API_KEY_STRING")

# example event
event_args = {"device_id":"somedeviceid", "event_type":"justtesting", 
              "event_properties":{"property1":"somevalue", "propertyN":"anothervalue"}
event = amplitude_logger.create_event(**event_args)

# send event to amplitude
amplitude_logger.log_event(event)

```

## 3. Test amplitude-python module
```
python setup.py test
```

