from enum import Enum

class BitCategory(Enum):
    SCREW  = "scrw_bits"
    DRILL  = "drill_bits"
    DOUBLE = "double_ended_bits"

class BitCondition(Enum):
    NEW     = "new"
    CLEANED = "cleaned"
    WORN    = "worn"