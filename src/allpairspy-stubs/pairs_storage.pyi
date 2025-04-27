from collections.abc import Collection
from typing import Protocol, TypeVar, type_check_only


_T = TypeVar('_T', covariant=True)


@type_check_only
class Identifiable(Protocol[_T]):
    """
    A protocol meant to indicate a type is "identifiable" via an `id` method, which may
    return a value of a specific type used as an identity.
    """
    @property
    def id(self) -> _T:
        """
        An identifier value for this object.

        Returns:
            An identifier value for this object.
        """
        ...


class Node(Identifiable[int]):
    @property
    def counter(self) -> int: ...

    def __init__(self, node_id: int) -> None: ...

    def __str__(self) -> str: ...

    def inc_counter(self) -> None: ...


key_cache: dict[Collection[Identifiable[str]], tuple[int, ...]]


def key(items: Collection[Identifiable[str]]) -> tuple[int, ...]: ...


_PairStorageCombs = list[set[tuple[int, ...]]]


class PairsStorage:
    def __init__(self, n: int) -> None: ...

    def __len__(self) -> int: ...

    def add_sequence(self, sequence: Collection[Identifiable[str]]) -> None: ...

    def get_node_info(self, item: Identifiable) -> Node: ...

    def get_combs(self) -> _PairStorageCombs: ...
