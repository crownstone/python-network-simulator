from enum import Enum

class MessageState(Enum):
    DELIVERED = "DELIVERED"
    FAILED = "FAILED"
    DELAYED = "DELAYED"
    ALREADY_DELIVERED = "ALREADY_DELIVERED"
    SKIPPED = "SKIPPED"
    UNREACHABLE = "UNREACHABLE"