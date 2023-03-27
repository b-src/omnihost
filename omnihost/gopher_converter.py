from enum import auto, Enum

from omnihost.gemtext_parser import GemLine, LineType


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


_gopher_character_map = {
    GopherType.TEXT: "0",
    GopherType.SUBMENU: "1",
    GopherType.CCSO_NAMESERVER: "2",
    GopherType.ERROR_CODE: "3",
    GopherType.BINHEX: "4",
    GopherType.DOS: "5",
    GopherType.UUENCODED_FILE: "6",
    GopherType.FULL_TEXT_SEARCH: "7",
    GopherType.TELNET: "8",
    GopherType.BINARY: "9",
    GopherType.MIRROR: "+",
    GopherType.GIF: "g",
    GopherType.CANONICAL_IMAGE: "I",
    GopherType.TELNET_3270: "T",
    # Gopher+ Types:
    GopherType.BITMAP: ":",
    GopherType.MOVIE: ";",
    GopherType.GOPHER_PLUS_SOUND: "<",
    # Non-canonical Types:
    GopherType.DOC: "d",
    GopherType.HTML: "h",
    GopherType.INFO: "i",
    GopherType.NON_CANONICAL_IMAGE: "p",
    GopherType.RTF: "r",
    GopherType.NON_CANONICAL_SOUND: "s",
    GopherType.PDF: "P",
    GopherType.XML: "X",
}


class GopherConverter:
    def __init__(self) -> None:
        pass

    def convert_gemlines_to_gopher(self, gemlines: list[GemLine], title: str) -> str:
        for gemline in gemlines:
            if gemline.line_type == LineType.PREFORMATTED_ALT_TEXT:
                pass
            elif gemline.line_type == LineType.PREFORMATTED:
                pass
            elif gemline.line_type == LineType.END_PREFORMATTED:
                pass
            elif gemline.line_type == LineType.LISTITEM:
                pass
            elif gemline.line_type == LineType.TEXT:
                pass
            elif gemline.line_type == LineType.HEADING:
                pass
            elif gemline.line_type == LineType.SUBHEADING:
                pass
            elif gemline.line_type == LineType.SUBSUBHEADING:
                pass
            elif gemline.line_type == LineType.LINK:
                pass
            elif gemline.line_type == LineType.BLOCKQUOTE:
                pass


class GopherConverterException(Exception):
    """Represents errors that occur within the GopherConverter."""
    pass

