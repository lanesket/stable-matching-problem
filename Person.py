from __future__ import annotations
from typing import List


class Person:
    def __init__(self, name, preferences=[]):
        self.name = name
        self.is_free = True
        self.relationships = []
        self.preferences = preferences

    def start_relationship(self, p: Person) -> None:
        """
        Updates the relationship status.

        Args:
            p: person to engage with 
        """
        self.is_free = False
        p.is_free = False

        self.relationships.append(p)
        p.relationships.append(self)

    def engaged_with(self) -> Person | None:
        """ 
        Returns:
            Person if there.
        """
        if not len(self.relationships):
            return None
        if self.is_free:
            return None
        else:
            return self.relationships[-1]

    @staticmethod
    def still_free_man(m_list: List, w_m_count: int) -> Person | None:
        """
        Args:
            m_list: list of males
            w_m_count: count of males and females

        Returns:
            Returns not engaged man (Person) in case if there is some one.
            Otherwise None. 
        """
        for m in m_list:
            if m.is_free and len(m.relationships) < w_m_count and len(m.preferences):
                return m
        return None
