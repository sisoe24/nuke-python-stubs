import FnCyclone
import hiero.core.log

from . import FnEdlImporter

hiero.core.log.info('Loading Python hiero.importers package')


# Register importers
FnCyclone.registerImporter(importer=FnEdlImporter.EdlImporter())
