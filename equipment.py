from dataclasses import dataclass
from typing import List, Optional
from random import uniform
import marshmallow_dataclass
import json


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self) -> float:
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    # содержит 2 списка - с оружием и с броней
    weapons: List[Weapon]
    armors: List[Armor]


class Equipment:

    def __init__(self) -> str:
        self.equipment = self._get_equipment_data()

    def get_weapon(self, name: str) -> Optional[Weapon]:
        # возвращает объект оружия по имени
        for weapon in self.equipment.weapons:
            if weapon.name == name:
                return weapon
        return None

    def get_armor(self, name: str) -> Optional[Armor]:
        # возвращает объект брони по имени
        for armor in self.equipment.armors:
            if armor.name == name:
                return armor
        return None

    def get_weapons_names(self) -> list[str]:
        # возвращаем список с оружием
        return [
            weapon.name
            for weapon in self.equipment.weapons
        ]

    def get_armors_names(self) -> list[str]:
        # возвращаем список с броней
        return [
            armor.name
            for armor in self.equipment.armors
        ]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        # этот метод загружает json в переменную EquipmentData
        with open("./data/equipment.json", encoding='UTF-8') as equipment_file:
            data = json.load(equipment_file)
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
            return equipment_schema().load(data)
