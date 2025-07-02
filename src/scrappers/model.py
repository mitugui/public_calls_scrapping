from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Link:
    title: str
    link: str

@dataclass
class Call:
    title: str
    source: str
    description: str
    inscription: str
    links: List[Link]
    initial_funding: Optional[str] = None
