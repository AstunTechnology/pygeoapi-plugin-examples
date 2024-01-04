# pygeoapi-plugin-examples

Bare bones package demonstrating packaging a custom OGC Processes API process for use with pygeoapi.

## Install and configuration

Assuming you already have pygeoapi installed within a virtual environment, activate the virtual environment then change to the root of this repository.

Install this package as an editable package:
```
pip install -e .
```

Configure pygeoapi to make use of the `HelloAstunProcessor` process:
```yml
    hello-astun:
        type: process
        processor:
            name: pygeoapi_plugin_examples.processes.hello_astun.HelloAstunProcessor
```
