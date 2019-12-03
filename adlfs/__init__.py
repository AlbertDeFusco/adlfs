from .core import AzureDatalakeFileSystem
from .core import AzureBlobFileSystem, AzureBlobFile
from ._version import get_versions

__all__ = ["AzureBlobFileSystem", "AzureBlobFile", "AzureDatalakeFileSystem"]

__version__ = get_versions()["version"]
del get_versions

from fsspec.registry import known_implementations
known_implementations['abfs'] = {'class':'adlfs.AzureBlobFileSystem'}
