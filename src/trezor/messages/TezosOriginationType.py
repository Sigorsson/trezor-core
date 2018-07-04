# Automatically generated by pb2py
# fmt: off
import protobuf as p


class TezosOriginationType(p.MessageType):
    FIELDS = {
        1: ('manager_pubkey', p.BytesType, 0),
        2: ('balance', p.UVarintType, 0),
        3: ('spendable', p.BoolType, 0),
        4: ('delegatable', p.BoolType, 0),
        5: ('delegate', p.BytesType, 0),
        6: ('script', p.BytesType, 0),
    }

    def __init__(
        self,
        manager_pubkey: bytes = None,
        balance: int = None,
        spendable: bool = None,
        delegatable: bool = None,
        delegate: bytes = None,
        script: bytes = None,
    ) -> None:
        self.manager_pubkey = manager_pubkey
        self.balance = balance
        self.spendable = spendable
        self.delegatable = delegatable
        self.delegate = delegate
        self.script = script