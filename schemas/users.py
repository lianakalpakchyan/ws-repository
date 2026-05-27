from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    email: str
    age: int
    id: int | None = field(default=None)