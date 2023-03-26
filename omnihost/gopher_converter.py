from enum import auto, Enum


class GopherType(Enum):
    # Canonical Types
    TEXT = auto()
    SUBMENU = auto()
    CCSO_NAMESERVER = auto()
    ERROR_CODE = auto()
    BINHEX = auto()
    DOS = auto()
    UUENCODED_FILE = auto()
    FULL_TEXT_SEARCH = auto()
    TELNET = auto()
    BINARY = auto()
    MIRROR = auto()
    GIF = auto()
    # TODO: what image types are acceptable here?
    CANONICAL_IMAGE = auto()
    TELNET_3270 = auto()
    # Gopher+ Types
    BITMAP = auto()
    MOVIE = auto()
    # TODO: what find types are acceptable here?
    GOPHER_PLUS_SOUND = auto()
    # Non-canonical Types
    DOC = auto()
    HTML = auto()
    INFO = auto()
    # TODO: what image types are acceptable here?
    NON_CANONICAL_IMAGE = auto()
    RTF = auto()
    # TOOD: what file types are acceptable here?
    NON_CANONICAL_SOUND = auto()
    PDF = auto()
    XML = auto()

