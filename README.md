# Azure DevPy

## Requirements
You need a file called **azuredevpy.ini**

Below is an example of what the file looks like.

Override the items for to match your AzureDevOps

```
[DEFAULT]
URL = https://dev.azure.com/<organization>
PAT = <peronal access token>
PROJECT=<project name>

[API_VERSION]
DEFAULT =api-version=6.1-preview.1
BUILD =api-version=6.1-preview.6
```

## Installation

```
python -m pip install -e .
```

## Virtual Enviroment (recommended)
```
python -m pipenv shell
```

## Install Requirements

```
python -m pip install -r requirements.txt
```

## Testing

```
python -m pytest
```