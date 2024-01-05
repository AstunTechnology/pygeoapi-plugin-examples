import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

from shapely.geometry import shape, mapping

LOGGER = logging.getLogger(__name__)

#: Process metadata and description
PROCESS_METADATA = {
    'version': '0.1.0',
    'id': 'buffer',
    'title': {
        'en': 'Buffer Geometry'
    },
    'description': {
        'en': 'Accepts a GeoJSON geometry and a buffer distance (in the same units as the geometry CRS) as inputs '
              'outputs a buffered GeoJSON geometry.'
    },
    'jobControlOptions': ['sync-execute', 'async-execute'],
    'keywords': ['geometry', 'example', 'buffer'],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://example.org/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'geometry': {
            'title': 'GeoJSON geometry',
            'description': 'The GeoJSON geometry to buffer',
            'schema': {
                '$ref': 'https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/schemas/geometryGeoJSON.yaml'
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': ['geometry']
        },
        'distance': {
            'title': 'Distance',
            'description': 'Buffer distance in the same units as the geometry CRS',
            'schema': {
                'type': 'float'
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': ['distance']
        }
    },
    'outputs': {
        'geometry': {
            'title': 'Buffered GeoJSON geometry',
            'description': 'GeoJSON geometry buffered by specified distance',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/json'
            }
        }
    },
    'example': {
        'inputs': {
            'geometry': {"type": "Polygon", "coordinates": [[[529739.3803, 179868.9209], [529778.6271, 179914.7657], [529831.3243, 179939.7011], [529838.0743, 179941.8764], [529844.796, 179945.1638], [529861.7705, 179946.71], [529875.2509, 179932.8113], [529876.7534, 179903.9186], [529883.2889, 179898.188], [529880.6071, 179888.9951], [529874.812, 179882.0594], [529849.0582, 179887.0765], [529833.6703, 179877.7816], [529814.4507, 179874.3978], [529813.628, 179871.2611], [529811.5773, 179869.9847], [529808.2886, 179868.2317], [529800.1866, 179875.4802], [529770.1846, 179867.3703], [529762.9924, 179866.1852], [529754.3972, 179857.3978], [529753.6511, 179851.2587], [529743.2636, 179850.1034], [529739.3803, 179868.9209]]]},
            'distance': 50
        }
    }
}


class BufferProcessor(BaseProcessor):
    """Buffer OGC Processes API Process"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi_plugin_examples.processes.buffer.BufferProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):

        mimetype = 'application/json'
        try:
            geom = shape(data.get('geometry'))
        except:
            raise ProcessorExecuteError('Invalid geometry input, a valid GeoJSON is required')

        if geom is None:
            raise ProcessorExecuteError('Cannot process without a geom')

        dist = data.get('distance')
        if dist is None:
            raise ProcessorExecuteError('Cannot process without a distance')

        geom = geom.buffer(dist)
        geom = mapping(geom)

        outputs = {
            'id': 'geometry',
            'value': geom
        }

        return mimetype, outputs

    def __repr__(self):
        return f'<pygeoapi_plugin_examples.processes.buffer.BufferProcessor> {self.name}'

