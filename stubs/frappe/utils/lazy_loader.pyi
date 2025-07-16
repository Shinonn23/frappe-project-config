from types import ModuleType
from typing import Optional

def lazy_import(name: str, package: Optional[str] = None) -> ModuleType: ...