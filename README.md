# pygeoapi-plugin-examples

Bare bones package demonstrating packaging a custom OGC Processes API process for use with pygeoapi.

## Install and configuration

Assuming you already have pygeoapi installed within a virtual environment, activate the virtual environment then change to the root of this repository.

Install this package as an editable package:
```sh
pip install -e .
```

Configure pygeoapi to make use of the `HelloAstunProcessor` process:
```yml
    hello-astun:
        type: process
        processor:
            name: pygeoapi_plugin_examples.processes.hello_astun.HelloAstunProcessor
```

Change to the directory that contains your `pygeoapi-config.yml` and update the OpenAPI config to include the new process:
```sh
pygeoapi openapi generate pygeoapi-config.yml > pygeoapi-openapi.yml
```
