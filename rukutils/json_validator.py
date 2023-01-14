# -*- coding: utf-8 -*-
'''
A snippet module that loads JSON files and validates them with a JSON schema.
'''
import sys
import logging
import json
import jsonschema
import coloredlogs

coloredlogs.install(fmt='%(asctime)s - %(filename)s:'
                    '%(funcName)s:%(lineno)s | '
                    '%(levelname)s | %(message)s')

def main(json_path, schema_path):
    '''
    Main Function. Loads and validates the JSON file and returns the loaded file.
    '''

    with open(json_path, encoding="utf-8") as json_file, \
        open(schema_path, encoding="utf-8") as schema_file:
        json_config = json.load(json_file)
        json_schema = json.load(schema_file)
        logging.info("JSON files open and load... Ok!")

    try:
        jsonschema.validate(instance=json_config, schema=json_schema)
        logging.info("JSON validation ... Ok!")
    except jsonschema.exceptions.ValidationError as exception_error:
        logging.error('%s \n JSON does not follow the schema specification.', exception_error.args)
        sys.exit()
    except jsonschema.exceptions.SchemaError as exception_error:
        logging.error('%s \n JSON Schema is invalid.', exception_error.args)
        sys.exit()

    return json_config
