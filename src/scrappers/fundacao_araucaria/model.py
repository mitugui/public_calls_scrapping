from dataclasses import dataclass
from typing import List

@dataclass
class Link:
    title: str
    link: str

@dataclass
class Call:
    title: str
    description: str
    inscription: str
    initial_funding: str
    links: List[Link]
