## Levitate Change Event Registration

This Python script is used to register a change event with the Levitate API.

### Requirements

- Python
- requests library

### Setup

Set up a virtual environment and activate it:

``` shell
python3 -m venv venv
source venv/bin/activate
```

Install the required Python libraries:

``` shell
pip install -r requirements.txt
```

Set the required environment variables:

``` shell
export LEVITATE_REFRESH_TOKEN=
export LEVITATE_ORG=
```

Follow the instructions [here](https://docs.last9.io/docs/change-events) to obtain the values of the environment variables.

### Usage

Run the script:

``` shell
python change_event.py
```

If the change event is registered successfully, the script will print "Change event registered successfully". If there is an error, an exception will be raised with a message indicating the cause of the error.
