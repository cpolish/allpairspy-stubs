import abc
from collections import OrderedDict
from collections.abc import Callable, Collection, Sequence
from typing import Any, Generic, Literal, overload, Self, TypeVar

from .pairs_storage import Identifiable


_S = TypeVar('_S')
_T = TypeVar('_T')
_TParameterType = TypeVar(
    '_TParameterType',
    bound=OrderedDict[str, Collection[Any]] | Collection[Collection[Any]],
)


class Item(Generic[_T], Identifiable[str]):
    @property
    def value(self) -> _T: ...

    @property
    def weights(self) -> list[int]: ...

    def __init__(self, item_id: str, value: _T) -> None: ...

    def __str__(self) -> str: ...

    def set_weights(self, weights: list[int]) -> None: ...


def get_max_combination_number(prameter_matrix: Collection[Collection[_T]], n: int
                               ) -> int:
    ...


def cmp_item(lhs: Item[object], rhs: Item[object]) -> Literal[-1, 0, 1]: ...


class _PairsTuple(Sequence[_T], metaclass=abc.ABCMeta):
    def __getattr__(self, name: str) -> _T: ...


class AllPairs(Generic[_T, _TParameterType]):
    @overload
    def __init__(
        self: AllPairs[_S, OrderedDict[str, Collection[_S]]],
        parameters: OrderedDict[str, Collection[_S]],
        filter_func: Callable[[_S], bool] = lambda _x: True,
        previously_tested: Collection[Collection[_S]] | None = None,
        n: int = 2,
    ) -> None: ...

    @overload
    def __init__(
        self: AllPairs[_S, Collection[Collection[_S]]],
        parameters: Collection[Collection[_S]],
        filter_func: Callable[[_S], bool] = lambda _x: True,
        previously_tested: Collection[Collection[_S]] | None = None,
        n: int = 2,
    ) -> None: ...

    def __iter__(self) -> Self: ...

    @overload
    def next(self: AllPairs[_S, Collection[Collection[_S]]]) -> list[_S]: ...

    @overload
    def next(self: AllPairs[_S, OrderedDict[str, Collection[_S]]]) -> _PairsTuple: ...

    @overload
    def __next__(self: AllPairs[_S, Collection[Collection[_S]]]) -> list[_S]: ...

    @overload
    def __next__(self: AllPairs[_S, OrderedDict[str, Collection[_S]]]
                 ) -> _PairsTuple:
        ...
