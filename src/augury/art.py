"""ASCII tarot card art for the Augury system."""

from __future__ import annotations

from typing import Final

CARD_WIDTH: Final[int] = 19
CARD_HEIGHT: Final[int] = 15
_INNER_WIDTH: Final[int] = CARD_WIDTH - 2
_INNER_HEIGHT: Final[int] = CARD_HEIGHT - 2

_MAJOR_NAMES: Final[tuple[str, ...]] = (
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World",
)

_SUIT_ALIASES: Final[dict[str, str]] = {
    "cups": "cups",
    "chalices": "cups",
    "goblets": "cups",
    "swords": "swords",
    "blades": "swords",
    "wands": "wands",
    "staves": "wands",
    "rods": "wands",
    "batons": "wands",
    "pentacles": "pentacles",
    "coins": "pentacles",
    "disks": "pentacles",
    "discs": "pentacles",
}

_RANK_LABELS: Final[dict[int, str]] = {
    1: "ACE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE",
    10: "TEN",
    11: "PAGE",
    12: "KNIGHT",
    13: "QUEEN",
    14: "KING",
}

_PIP_LAYOUTS: Final[dict[int, tuple[int, ...]]] = {
    1: (1,),
    2: (1, 1),
    3: (1, 1, 1),
    4: (2, 2),
    5: (2, 1, 2),
    6: (2, 2, 2),
    7: (2, 3, 2),
    8: (2, 2, 2, 2),
    9: (3, 3, 3),
    10: (3, 2, 3, 2),
}


def _normalize_name(value: str) -> str:
    return " ".join(str(value).strip().lower().replace("-", " ").split())


def _center(value: str) -> str:
    if len(value) > _INNER_WIDTH:
        raise ValueError(f"line too wide for card art: {value!r}")
    return value.center(_INNER_WIDTH)


def _frame(lines: tuple[str, ...]) -> str:
    if len(lines) != _INNER_HEIGHT:
        raise ValueError(f"expected {_INNER_HEIGHT} inner lines, got {len(lines)}")
    rendered = ["┌" + ("─" * _INNER_WIDTH) + "┐"]
    for line in lines:
        if len(line) > _INNER_WIDTH:
            raise ValueError(f"line too wide for card art: {line!r}")
        rendered.append("│" + line.ljust(_INNER_WIDTH) + "│")
    rendered.append("└" + ("─" * _INNER_WIDTH) + "┘")
    return "\n".join(rendered)


def _card(*lines: str) -> str:
    return _frame(tuple(lines))


def _major_aliases() -> dict[str, str]:
    aliases: dict[str, str] = {}
    for name in _MAJOR_NAMES:
        normalized = _normalize_name(name)
        aliases[normalized] = normalized
        if normalized.startswith("the "):
            aliases[normalized[4:]] = normalized
    aliases["judgment"] = "judgement"
    aliases["wheel"] = "wheel of fortune"
    return aliases


CARD_BACK: Final[str] = _card(
    _center("   /\\   /\\   "),
    _center("  /__\\ /__\\  "),
    _center("  \\  X X  /  "),
    _center("   \\/_X_\\/   "),
    _center("   /\\ | /\\   "),
    _center("  /__\\|/__\\  "),
    _center("  \\  /+\\  /  "),
    _center("   \\/_|_\\/   "),
    _center("   /\\   /\\   "),
    _center("  /__\\ /__\\  "),
    _center("  \\  X X  /  "),
    _center("   \\/___\\/   "),
    _center("   cassette   "),
)

_MAJOR_ART: Final[dict[str, str]] = {
    "the fool": _card(
        _center("\\  |  /"),
        _center(" -- * --"),
        _center("  .-."),
        _center(" (o o)"),
        _center(" /|_|\\\\"),
        _center(" / \\\\"),
        _center("   /  \\\\__"),
        _center("  / cliff \\\\"),
        _center(" /_________\\\\"),
        _center("     /\\\\"),
        _center("    /  \\\\ ^^"),
        _center("     dog"),
        _center("0"),
    ),
    "the magician": _card(
        _center("oo"),
        _center(".-^^-."),
        _center("(.. )"),
        _center(" /|"),
        _center("/ |"),
        _center("___|___"),
        _center("| () + * |"),
        _center("| /\\\\ \\/ |"),
        _center("|  altar  |"),
        _center("  / \\\\"),
        _center(" /___\\\\"),
        "",
        _center("I"),
    ),
    "the high priestess": _card(
        _center("(( _ ))"),
        _center("B| | |J"),
        _center(" | | |"),
        _center(" |/ \\\\|"),
        _center(" /_#_\\\\"),
        _center("  ###"),
        _center("  ###"),
        _center(" /___\\\\"),
        _center("  (_)"),
        _center(" / | \\\\"),
        _center("/__|__\\\\"),
        "",
        _center("II"),
    ),
    "the empress": _card(
        _center(" _._._._"),
        _center("/_/_|_\\\\_\\\\"),
        _center("\\\\_  V  _//"),
        _center(" /|^^^|\\\\"),
        _center("/_|___|_\\\\"),
        _center("   /|||\\\\"),
        _center("  /_|||_\\\\"),
        _center(" ~~~|||~~~"),
        _center(" ~~~|||~~~"),
        _center("    | |"),
        _center("   _| |_"),
        _center("  /_____\\\\"),
        _center("III"),
    ),
    "the emperor": _card(
        _center(" _.^._"),
        _center("__(   )__"),
        _center(" /_#_\\\\"),
        _center("|\\\\___/|"),
        _center("|| I ||"),
        _center("||-O-||"),
        _center("||___||"),
        _center("/_|___|_\\\\"),
        _center("  / | \\\\"),
        _center(" /  |  \\\\"),
        _center("/___|___\\\\"),
        "",
        _center("IV"),
    ),
    "the hierophant": _card(
        _center(".-^^^-."),
        _center("/_|||_\\\\"),
        _center("  |=|"),
        _center(".-===-."),
        _center("|  +  |"),
        _center("| /_\\\\ |"),
        _center("|  |  |"),
        _center(" / | \\\\"),
        _center("/_ | _\\\\"),
        _center(" _/ \\\\_"),
        _center("acolytes"),
        "",
        _center("V"),
    ),
    "the lovers": _card(
        _center("\\  |  /"),
        _center(" -- * --"),
        _center(".-^^-."),
        _center("  /|\\\\"),
        _center("o  |  o"),
        _center("|\\\\ | /|"),
        _center("/ \\\\|/ \\\\"),
        _center("  / \\\\"),
        _center(" /___\\\\"),
        _center("tree tree"),
        "",
        "",
        _center("VI"),
    ),
    "the chariot": _card(
        _center("  ______"),
        _center("_/|_[]_|\\\\_"),
        _center("/_  ___  _\\\\"),
        _center(" |(o o)|"),
        _center(" |  ^  |"),
        _center(" | [_] |"),
        _center("/|_____|\\\\"),
        _center("/_ /   \\\\ _\\\\"),
        _center(" /_/ \\\\_\\\\"),
        _center("_^_   _v_"),
        _center("/___\\\\ /___\\\\"),
        "",
        _center("VII"),
    ),
    "strength": _card(
        _center("oo"),
        _center(".(  )."),
        _center(" ||"),
        _center("o-/ \\\\-o"),
        _center("/|  ^  |\\\\"),
        _center(" | /_\\\\ |"),
        _center(" | \\\\_/ |"),
        _center(" |  _  |"),
        _center("/| / \\\\ |\\\\"),
        _center("/_/     \\\\_\\\\"),
        _center(" lion"),
        "",
        _center("VIII"),
    ),
    "the hermit": _card(
        _center(" _"),
        _center("/_\\\\"),
        _center("\\*/"),
        _center("/|"),
        _center("/ \\\\"),
        _center("/|"),
        _center("/ |"),
        _center("/  |"),
        _center("/___|___"),
        _center("   |"),
        _center("  / \\\\"),
        "",
        _center("IX"),
    ),
    "wheel of fortune": _card(
        _center(".-.-."),
        _center(".-(  O  )-."),
        _center("/  ROTA   \\\\"),
        _center("|  /-+-\\\\  |"),
        _center("|  | X |  |"),
        _center("|  \\\\-+-/  |"),
        _center("\\   O    /"),
        _center(" '-.__.-'"),
        _center("  /|\\\\"),
        _center(" /_|_\\\\"),
        _center("   |"),
        "",
        _center("X"),
    ),
    "justice": _card(
        _center(" _|_"),
        _center(" /_\\\\"),
        _center("  |"),
        _center(".--+--."),
        _center("/  |  \\\\"),
        _center("o  |  o"),
        _center("  |"),
        _center("___|___"),
        _center("| ___ |"),
        _center("||___||"),
        _center("|_____|"),
        "",
        _center("XI"),
    ),
    "the hanged man": _card(
        _center("_______"),
        _center("|     |"),
        _center("|  /| |"),
        _center("| / | |"),
        _center("|   | |"),
        _center("|  / \\\\|"),
        _center("| /___\\\\"),
        _center("|   | |"),
        _center("|  ( )|"),
        _center("| /___\\\\"),
        _center("|_____|"),
        "",
        _center("XII"),
    ),
    "death": _card(
        _center("  __"),
        _center("_/oo\\\\_"),
        _center("/_====_\\\\"),
        _center("  |  |"),
        _center("___|__|___"),
        _center("/  /  \\\\  \\\\"),
        _center("\\__/____\\\\_/"),
        _center(" /| || |\\\\"),
        _center("/_|_||_|_\\\\"),
        _center("   ||"),
        _center("  _||_"),
        "",
        _center("XIII"),
    ),
    "temperance": _card(
        _center("\\\\|//"),
        _center(".-^^-."),
        _center("/(o o)\\\\"),
        _center("\\\\_=_//"),
        _center(" /|\\\\"),
        _center("__/ \\\\__"),
        _center("(__   __)"),
        _center("  ) ("),
        _center(" /___\\\\"),
        _center("~  |  ~"),
        _center("  / \\\\"),
        "",
        _center("XIV"),
    ),
    "the devil": _card(
        _center("/^^^^\\\\"),
        _center("( oo )"),
        _center("/_==_\\\\"),
        _center(" /||\\\\"),
        _center("__/||\\\\__"),
        _center("( o||||o )"),
        _center("\\\\_||||_//"),
        _center("|  ||  |"),
        _center("|_/  \\\\_|"),
        _center("  /  \\\\"),
        _center(" _/  \\\\_"),
        "",
        _center("XV"),
    ),
    "the tower": _card(
        _center("    /\\\\"),
        _center("   /!!\\\\"),
        _center("  /_!!_\\\\"),
        _center("   ||||"),
        _center("  _||||_"),
        _center(" | |||| |"),
        _center(" | |||| |"),
        _center(" | |||| |"),
        _center("/\\\\|_||||_|"),
        _center("/ / /  \\\\ \\\\"),
        _center("v  v  v  v"),
        "",
        _center("XVI"),
    ),
    "the star": _card(
        _center("    *"),
        _center("*   \\\\|/   *"),
        _center("  --*--"),
        _center("*   /|\\\\   *"),
        _center("    *"),
        _center("  _/\\\\_"),
        _center(" / o  \\\\"),
        _center("/|\\\\   /\\\\"),
        _center("/ \\\\  /  \\\\"),
        _center("~~~~ /____\\\\"),
        _center(" ~~~~~~~"),
        "",
        _center("XVII"),
    ),
    "the moon": _card(
        _center(" _..._"),
        _center(".( _ )."),
        _center("\\\\_\\\\/_//"),
        _center("_/ / \\\\ \\\\_"),
        _center("/_ /___\\\\ _\\\\"),
        _center("  |  |  |"),
        _center("/\\\\  |  /\\\\"),
        _center("/  \\\\|/  \\\\"),
        _center("   / \\\\"),
        _center("  /___\\\\"),
        _center("   ||"),
        "",
        _center("XVIII"),
    ),
    "the sun": _card(
        _center("\\  |  |  /"),
        _center("-- \\\\|// --"),
        _center("  --*--"),
        _center("-- /|\\\\ --"),
        _center("/  |  |  \\\\"),
        _center("   \\\\o/"),
        _center("    /|"),
        _center("   / \\\\"),
        _center("__/___\\\\__"),
        _center("| _ _ _ |"),
        _center("|_|_|_|_|"),
        "",
        _center("XIX"),
    ),
    "judgement": _card(
        _center("  /|\\\\"),
        _center(" /_|_\\\\"),
        _center("   |"),
        _center(".--+--."),
        _center("  / \\\\"),
        _center("o /_\\\\ o"),
        _center("/|\\\\   /|\\\\"),
        _center("/ \\\\   / \\\\"),
        _center("___   ___"),
        _center("|_|   |_|"),
        _center(" sound"),
        "",
        _center("XX"),
    ),
    "the world": _card(
        _center(".-~~~~~-."),
        _center(".'  o o  '."),
        _center("/ o  X  o \\\\"),
        _center("| o / \\\\ o |"),
        _center("|   /o\\\\   |"),
        _center("|  /   \\\\  |"),
        _center("|  \\\\   /  |"),
        _center("|   \\\\_/   |"),
        _center("\\ o     o /"),
        _center("'.  o o  .'"),
        _center(" '-._.-'"),
        _center("[ ]   [ ]"),
        _center("XXI"),
    ),
}

_MAJOR_ALIASES: Final[dict[str, str]] = _major_aliases()


def get_card_art(card_name: str) -> str:
    """Return the ASCII art for a Major Arcana card by name."""

    normalized = _normalize_name(card_name)
    canonical = _MAJOR_ALIASES.get(normalized)
    if canonical is None:
        raise ValueError(f"unknown major arcana card: {card_name!r}")
    return _MAJOR_ART[canonical]


def _suit_rows(symbol: str, count: int) -> list[str]:
    rows: list[str] = []
    for row_count in _PIP_LAYOUTS[count]:
        rows.append(_center(" ".join(symbol for _ in range(row_count))))
    return rows


def get_suit_art(suit: str, number: int) -> str:
    """Return a simpler parameterized minor-arcana card face."""

    normalized = _SUIT_ALIASES.get(_normalize_name(suit))
    if normalized is None:
        raise ValueError(f"unknown suit: {suit!r}")
    if number not in _RANK_LABELS:
        raise ValueError(f"minor arcana number must be 1-14, got {number!r}")

    symbols = {
        "cups": "()",
        "swords": "<>",
        "wands": "!!",
        "pentacles": "[]",
    }
    accents = {
        "cups": ("  .-._.-.  ", "    \\_/    "),
        "swords": ("    /|\\    ", "    /_\\    "),
        "wands": ("   \\\\ | //   ", "    \\\\|/    "),
        "pentacles": ("   .-+-.,   ", "    \\_/    "),
    }

    lines: list[str] = [_center(_RANK_LABELS[number]), ""]
    if number <= 10:
        lines.extend(_suit_rows(symbols[normalized], number))
    else:
        court_marks = {11: "  page  ", 12: " knight ", 13: " queen  ", 14: "  king  "}
        lines.append(_center(symbols[normalized] + " " + symbols[normalized]))
        lines.append(_center(court_marks[number]))
        lines.append(_center(symbols[normalized] + " " + symbols[normalized]))

    lines.append("")
    lines.append(_center(accents[normalized][0]))
    lines.append(_center(accents[normalized][1]))
    while len(lines) < _INNER_HEIGHT - 2:
        lines.append("")
    lines.append(_center(normalized.upper()))
    lines.append(_center(str(number).rjust(2, "0")))
    return _frame(tuple(lines))


def _validate_art_block(name: str, art: str) -> None:
    lines = art.splitlines()
    if len(lines) != CARD_HEIGHT:
        raise RuntimeError(f"{name} art should be {CARD_HEIGHT} lines, got {len(lines)}")
    for index, line in enumerate(lines, start=1):
        if len(line) != CARD_WIDTH:
            raise RuntimeError(
                f"{name} line {index} should be {CARD_WIDTH} chars wide, got {len(line)}"
            )


def _validate_deck() -> None:
    if set(_MAJOR_ART) != {name.lower() for name in _MAJOR_NAMES}:
        raise RuntimeError("major arcana art coverage is incomplete")
    if len(set(_MAJOR_ART.values())) != len(_MAJOR_ART):
        raise RuntimeError("major arcana art must be unique per card")
    _validate_art_block("CARD_BACK", CARD_BACK)
    for name, art in _MAJOR_ART.items():
        _validate_art_block(name, art)
    for suit_name in ("cups", "swords", "wands", "pentacles"):
        _validate_art_block(f"{suit_name}-ace", get_suit_art(suit_name, 1))
        _validate_art_block(f"{suit_name}-king", get_suit_art(suit_name, 14))


_validate_deck()

__all__ = ["CARD_BACK", "get_card_art", "get_suit_art"]
