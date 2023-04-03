from abc import ABCMeta, abstractmethod
from typing import List

from src.models.umbrella import Umbrella
from src.schemas.umbrella import UmbrellaDTO


class UmbrellaBase(metaclass=ABCMeta):

    @abstractmethod
    def add_umbrella(self, request_umbrella: UmbrellaDTO) -> str: pass

    @abstractmethod
    def update_umbrella(self, request_umbrella: UmbrellaDTO) -> str: pass

    @abstractmethod
    def delete_umbrella(self, umb_id: int) -> str: pass

    @abstractmethod
    def find_all_umbrellas(self) -> List[Umbrella]: pass

    @abstractmethod
    def find_umbrella_by_id(self, umb_id: int) -> UmbrellaDTO: pass

    @abstractmethod
    def count_all_umbrellas(self) -> int: pass
