# Quickstart Guide

## Overview of ConfigBuddy
ConfigBuddy is a Python package designed to simplify the handling of configuration files across various formats. It provides a unified interface for reading, writing, and validating configuration data, making it easy for developers to manage application settings and preferences.

## Introduction
ConfigBuddy is a powerful configuration management library designed to simplify the handling of configuration files across various formats, including YAML, JSON, INI, and TOML. It provides an intuitive interface for reading, writing, and validating configuration data, making it easy for developers to manage application settings and preferences.

## Features
- Supports multiple configuration formats.
- Easy-to-use API for accessing and modifying configuration data.
- Validation of configuration data against defined schemas.
- Dynamic attribute access for seamless integration with Python applications.

## Getting Started
To get started with ConfigBuddy, follow the installation instructions provided in the installation guide.

## How to Use ConfigBuddy

Here are some basic examples of how to use the ConfigBuddy library:

### 1. Creating a ConfigBuddy Instance
To start using ConfigBuddy, create an instance by providing the path to your configuration file:
```python
from ConfigBuddy import ConfigBuddy

config = ConfigBuddy('path/to/your/config.yaml')
```

### 2. Accessing Configuration Values
You can access configuration values using dot notation or by key:
```python
# Using dot notation
value = config.key1

# Using key access
value = config['key1']
```

### 3. Modifying Configuration Values
To modify a configuration value, simply assign a new value:
```python
config.key1 = 'new_value'
# or
config['key1'] = 'new_value'
```

### 4. Saving Changes
After modifying the configuration, save the changes back to the file:
```python
config.save_config()
```

### 5. Validating Configuration
You can validate your configuration against a schema:
```python
schema = {'key1': str, 'key2': int}
config.validate_config(schema)
```

### Conclusion
With these basic operations, you can effectively manage your application's configuration using ConfigBuddy.