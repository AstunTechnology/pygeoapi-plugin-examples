# pygeoapi-plugin-examples

Bare bones package demonstrating packaging a custom OGC Processes API process for use with pygeoapi.

## Install and configuration

Assuming you already have pygeoapi installed within a virtual environment, activate the virtual environment then change to the root of this repository before installing this package as an editable package:
```sh
pip install -e .
```

Configure pygeoapi to make use of the `BufferProcessor` process found at `pygeoapi_plugin_examples/processes/buffer.py`:
```yml
    buffer:
        type: process
        processor:
            name: pygeoapi_plugin_examples.processes.buffer.BufferProcessor
```

Change to the directory that contains your `pygeoapi-config.yml` and update the OpenAPI config to include the new process:
```sh
pygeoapi openapi generate $PYGEOAPI_CONFIG --output-file $PYGEOAPI_OPENAPI
```
