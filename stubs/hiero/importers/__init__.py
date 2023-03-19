import FnCyclone
import hiero.core.log

from . import FnEdlImporter, FnOTIOImporter

hiero.core.log.info('Loading Python hiero.importers package')


# Register importers
FnCyclone.registerImporter(importer=FnEdlImporter.EdlImporter())
FnCyclone.registerImporter(importer=FnOTIOImporter.OtioImporter())
