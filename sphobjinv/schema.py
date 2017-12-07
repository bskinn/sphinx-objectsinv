"""
Defines JSON schemas to validate dictionaries generated by Inventory objects.

Name:        schema.py
Exposes:     schema_flat (dict)    -- Defines JSON structure for flat_dict
                                      Inventory export
             subschema_flat (dict) -- JSON structure for individual data
                                      objects, within `schema_flat`

Author:      Brian Skinn (bskinn@alum.mit.edu)

Created:     7 Dec 2017
Copyright:   (c) Brian Skinn 2016-2017
License:     The MIT License; see "LICENSE.txt" for full license terms
             and contributor agreement.

This file is part of Sphinx Objects.inv Encoder/Decoder, a toolkit for
encoding and decoding objects.inv files for use with intersphinx.

http://www.github.com/bskinn/sphobjinv

"""

from .data import DataFields

# For jsonschema Draft 4.
# Presume will relocate once inventory development is done.
subschema_flat = {DataFields.Name.value: {'type': 'string'},
                  DataFields.Domain.value: {'type': 'string'},
                  DataFields.Role.value: {'type': 'string'},
                  DataFields.Priority.value: {'type': 'string'},
                  DataFields.URI.value: {'type': 'string'},
                  DataFields.DispName.value: {'type': 'string'}
                  }

schema_flat = {'$schema': "http://json-schema.org/schema#",
               'type': 'object',
               'properties': {'project': {'type': 'string'},
                              'version': {'type': 'string'},
                              'count': {'type': 'integer'},
                              'metadata': {'type': 'object'}
                              },
               'patternProperties': {'^\\d+': {'type': 'object',
                                               'properties': subschema_flat,
                                               'additionalProperties': False,
                                               'required': list(subschema_flat)
                                               }
                                     },
               'additionalProperties': False,
               'required': ['project', 'version', 'count']
               }
