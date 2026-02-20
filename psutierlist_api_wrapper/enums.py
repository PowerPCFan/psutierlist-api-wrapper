from enum import Enum, auto
from typing import NamedTuple


class WattageData(NamedTuple):
    wattages: list[Wattage]
    min_max: WattageMinMax


class Wattage(NamedTuple):
    w: int
    psu_tierlist_affiliate_link: str | None


class WattageMinMax(NamedTuple):
    min: int | None
    max: int | None


class Topology(NamedTuple):
    primary_conversion: PrimaryConversion
    secondary_rectifier: SecondaryRectifier
    secondary_regulation: SecondaryRegulation


class Series(NamedTuple):
    series: str
    sub_series_1: str | None
    sub_series_2: str | None


class Size(Enum):
    ATX = auto()
    SFX = auto()
    SFX_L = auto()
    OTHER = auto()
    UNKNOWN = auto()

    @classmethod
    def from_str(cls, size: str) -> "Size":
        try:
            return Size[size.strip().upper().replace("-", "_")]
        except KeyError:
            return cls.UNKNOWN


class Modularity(Enum):
    NON_MODULAR = auto()
    SEMI_MODULAR = auto()
    FULLY_MODULAR = auto()
    UNKNOWN = auto()

    @classmethod
    def from_str(cls, mod: str) -> "Modularity":
        try:
            return Modularity[mod.strip().upper().replace("-", "_").replace(" ", "_")]
        except KeyError:
            return cls.UNKNOWN


class Tier(Enum):
    A_plus = auto()
    A = auto()
    A_minus = auto()
    B_plus = auto()
    B = auto()
    B_minus = auto()
    C_plus = auto()
    C = auto()
    C_minus = auto()
    D_plus = auto()
    D = auto()
    D_minus = auto()
    E_plus = auto()
    E = auto()
    E_minus = auto()
    F_plus = auto()
    F = auto()
    F_minus = auto()

    UNKNOWN = auto()

    @classmethod
    def from_str(
        cls,
        name: str,
        modifier: str = ""
    ) -> "Tier":
        enum_name = name.upper()

        if enum_name not in ["A", "B", "C", "D", "E", "F"]:
            return Tier.UNKNOWN

        if modifier and modifier in ["-", "+"]:
            if modifier == "+":
                enum_name += "_plus"
            elif modifier == "-":
                enum_name += "_minus"

        try:
            return Tier[enum_name.strip()]
        except KeyError:
            return Tier.UNKNOWN


class EightyPlusRating(Enum):
    NONE = auto()
    UNKNOWN = auto()
    BASE = auto()

    BRONZE = auto()
    SILVER = auto()
    GOLD = auto()
    PLATINUM = auto()
    TITANIUM = auto()

    @classmethod
    def from_str(cls, rating: str) -> "EightyPlusRating":
        rating = rating.strip().upper()

        if not rating or rating == "NONE":
            return cls.NONE

        if rating == "80 PLUS":
            return cls.BASE

        rating = rating.replace("80 PLUS ", "")

        try:
            return EightyPlusRating[rating]
        except KeyError:
            return cls.UNKNOWN


class PrimaryConversion(Enum):
    DF = auto()
    ACRF = auto()
    LLC = auto()
    PSR = auto()
    OTHER_OR_UNKNOWN = auto()

    @classmethod
    def from_str(cls, conversion: str) -> "PrimaryConversion":
        try:
            return PrimaryConversion[conversion.strip().upper()]
        except KeyError:
            return cls.OTHER_OR_UNKNOWN


class SecondaryRectifier(Enum):
    SSR = auto()
    SR = auto()
    PR = auto()
    OTHER_OR_UNKNOWN = auto()

    @classmethod
    def from_str(cls, rect: str) -> "SecondaryRectifier":
        try:
            return SecondaryRectifier[rect.strip().upper()]
        except KeyError:
            return cls.OTHER_OR_UNKNOWN


class SecondaryRegulation(Enum):
    DMA = auto()
    DC_DC = auto()
    GR = auto()
    OTHER_OR_UNKNOWN = auto()

    @classmethod
    def from_str(cls, reg: str) -> "SecondaryRegulation":
        try:
            return SecondaryRegulation[reg.strip().upper().replace("-", "_").replace(" (D2D)", "")]
        except KeyError:
            return cls.OTHER_OR_UNKNOWN
