## Levitate Change Event Registration

This Rust script is used to register a change event with the Levitate API.

### Requirements

- rustc
- cargo

### Setup

``` shell
cargo build
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
cargo run
```

If the change event is registered successfully, the script will print "Change event registered successfully". If there is an error, an exception will be raised with a message indicating the cause of the error.
