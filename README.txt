[CircleCI]



AMPLITUDE-PYTHON


Python API for Amplitude Analytics Logging - https://amplitude.com

This API is a simple (unofficial) wrapper for the Amplitude HTTP API


1. Install amplitude-python

Potential preparation before installing: create and activate virtualenv or conda environment

1.1 Install from pypi with conda or pip

    pip install amplitude-python

1.2 Install from github

    $ git clone https://github.com/atveit/amplitude-python.git
    $ cd amplitude-python
    $ python setup.py instal


2. Logging to Amplitude with amplitude-python

Recommend having a look at Amplitude HTTP API Documentation before start logging.

    import amplitude    

    # initialize amplitude logger
    amplitude_logger = amplitude.AmplitudeLogger(api_key = "SOME_API_KEY_STRING")

    # example event
    event_args = {"device_id":"somedeviceid", "event_type":"justtesting", 
                  "event_properties":{"property1":"somevalue", "propertyN":"anothervalue"}
    event = amplitude_logger.create_event(**event_args)

    # send event to amplitude
    amplitude_logger.log_event(event)


3. Test amplitude-python module

    python setup.py test
