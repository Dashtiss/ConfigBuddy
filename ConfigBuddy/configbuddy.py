import yaml
import json
import configparser
import tomllib
import tomli_w
from typing import Any, Dict


class ConfigBuddy:
    ValidConfigFormats = ['json', 'yaml', 'ini', 'toml']

    def __init__(self, config_file: str):
        self.config_file = config_file
        if self.config_file.split('.')[-1] not in ConfigBuddy.ValidConfigFormats:
            raise ValueError(
                f"Invalid config format: {self.config_file.split('.')[-1]}"
                )

    def read_config(self) -> Dict[str, Any]:
        try:
            with open(self.config_file, 'r') as f:
                if self.config_file.endswith('json'):
                    return json.load(f)
                elif self.config_file.endswith('yaml'):
                    return yaml.safe_load(f)
                elif self.config_file.endswith('ini'):
                    config = configparser.ConfigParser()
                    config.read(f)
                    return {s: dict(config[s]) for s in config.sections()}
                elif self.config_file.endswith('toml'):
                    return tomllib.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.config_file}")
        except Exception as e:
            raise ValueError(f"Error reading config: {e}")

    def save_config(self, config: Dict[str, Any]) -> None:
        with open(self.config_file, 'w') as f:
            if self.config_file.endswith('json'):
                json.dump(config, f, indent=4)
            elif self.config_file.endswith('yaml'):
                yaml.dump(config, f)
            elif self.config_file.endswith('ini'):
                config_parser = configparser.ConfigParser()
                config_parser.read_dict(config)
                config_parser.write(f)
            elif self.config_file.endswith('toml'):
                tomli_w.dump(config, f)


    def valididate_config(self, schema: dict[str, type]) -> None:
        conf = self.read_config()
        for key, value in schema.items():
            if key not in conf:
                raise ValueError(f"Missing key: {key}")
            if not isinstance(conf[key], value):
                raise ValueError(f"Invalid type for key: {key}")

    def __getattr__(self, name):
        conf = self.read_config()
        if name in conf:
            return conf[name]
        raise AttributeError(f"'ConfigBuddy' object has no attribute '{name}'")

    def __getitem__(self, key):
        conf = self.read_config()
        return conf[key]

    def __setitem__(self, key, value):
        conf = self.read_config()
        conf[key] = value
        self.save_config(conf)
