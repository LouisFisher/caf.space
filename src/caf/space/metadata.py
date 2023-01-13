import datetime
from pathlib import Path
import sys

sys.path.append('..')

import config_base

class WeightMetadata(config_base.BaseConfig):
    """
    Class for storing metadata about weighting date.
    This is not currently used but could be part of a GUI.
    """
    data_col: str
    id_col: str
    year: int
    type: str
    
class ShapefileMetadata(config_base.BaseConfig):
    """
    Class for creating, storing and loading metadata relating to shapefiles used for 
    translations. This is not currently used but could be part of a GUI.
    """
    name: str
    path: Path
    id_col: str
    weighting_data: WeightMetadata = None

class SpatialTransLog(config_base.BaseConfig):
    """
    Output log of a spatial translation, mainly used for the lower
    translations used in weighted translations.
    Parameters
    ----------
    zone_shapefile: Path to the primary zone shapefile used in the
    translation this metadata corresponds to.
    lower_shapefile: Path to the lower shapefile used in the translation
    this metadata corresponds to.
    date: The date this translation took place.
    """
    zone_shapefile: Path
    lower_shapefile: Path
    date: datetime.datetime

class LowerMetadata(config_base.BaseConfig):
    """
    Class for storing metadata for all translations between two zones.
    Every time a translation is run between two zones info about that
    translation should be added to an instance of this class saved as
    'metadata.yml'.
    Parameters
    ----------
    translations: A list of SpatialTransLog classes for all translations
    for a given pair of zone systems.
    """
    translations : list[SpatialTransLog]