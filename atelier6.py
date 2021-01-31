#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# mini compte est bon avec des additions seulement

# --- version récursive ----

class Explorer:
    def __init__(self, ls, target, first_only=False):
        self.ls = ls
        self.target = target
        self._first_only = first_only
        self.trace = []
        self.total = 0
        self.solutions = []

    def explore(self, i=0):
        while not self._first_found() and i < len(self.ls):
            new_total = self.total + self.ls[i]

            if new_total <= self.target:
                self._add_to_trace(i)
                self.explore(i + 1)

                if self._total_reached():
                    self.solutions.append(self.trace[:])

                self._pop_from_trace()
            i += 1

    def get_first_solution(self):
        solution = []
        if self.solutions:
            solution = self.solutions[0]
        return solution

    def get_all_solutions(self):
        return self.solutions

    def _first_found(self):
        return self._first_only and len(self.solutions) == 1

    def _add_to_trace(self, i: int):
        self.trace.append(i)
        self.total += self.ls[i]

    def _pop_from_trace(self):
        if self.trace:
            last = self.trace.pop()
            self.total -= self.ls[last]

    def _total_reached(self):
        return self.total == self.target


# ------------- Version itérative ------------------------
# Chaque noeud génère et retourne le noeud suivant parmis les suivants possibles. Le noeud généré garde une référence
# au noeud parent (précédent) on reviens en arrière quand on est dans un cul de sac (ou qu'on a trouvé une sorite)
# avec Node.step_back  qui retourne le noeud précédent après avoir "fermé" la branche courante.
class Node:
    def __init__(self, lst: list, target: int = 0, total: int = 0, idx: int = -1, previous = None):
        self._lst = lst
        self._target = target
        self._total = total
        self._idx = idx
        self._previous = previous

        self._next_idx = idx + 1

    def find_next(self):
        while self._in_bounds() and self._next_total_too_big():
            self.next_idx()
        return self._in_bounds()

    def next(self):
        total = self._total + self._lst[self._next_idx]
        return Node(lst=self._lst, target=self._target, total=total, idx=self._next_idx, previous=self)

    def has_previous(self):
        return self._previous is not None

    def step_back(self):
        self._previous.next_idx()
        return self._previous

    def target_reached(self):
        return self._total == self._target

    def get_idx(self):
        return self._idx

    def next_idx(self):
        self._next_idx += 1

    def _in_bounds(self):
        return self._next_idx < len(self._lst)

    def _next_total_too_big(self):
        return self._total + self._lst[self._next_idx] > self._target


class Visitor:
    def __init__(self, lst: list, target: int, first_only=False):
        self._start = Node(lst, target)
        self._trace = []
        self._solutions = []
        self._first_only = first_only

    def explore(self):
        current = self._start

        while not self._first_found() and current.find_next():
            current = current.next()
            self._add_to_trace(current)

            if current.target_reached():
                self._add_to_solutions(self._trace[:])
                self._pop_trace()

                if current.has_previous():
                    current = current.step_back()

            while not current.find_next() and current.has_previous():
                current = current.step_back()
                self._pop_trace()

    def _first_found(self):
        """ Indique qu'il faut s'arrêter après avoir trouvé la première solution """
        return self._first_only and len(self._solutions) == 1

    def _add_to_trace(self, node: Node):
        self._trace.append(node.get_idx())

    def _pop_trace(self):
        if self._trace:
            self._trace.pop()

    def _add_to_solutions(self, trace):
        self._solutions.append(trace)

    def get_first_solution(self):
        solution = []
        if self._solutions:
            solution = self._solutions[0]
        return solution

    def get_all_solutions(self):
        return self._solutions



# ------------ Version récurive avec des fonctions uniquemment, pour voir ... ---------------

def compte(ls, cible, first_only=False):
    vars_ = {
        "list": ls,
        "cible": cible,
        "trace": [],
        "solutions": [],
        "total": 0,
        "first_only": first_only
    }
    start = 0

    explore(vars_, start)

    return vars_["solutions"]


def add(vars_, i):
    vars_["total"] += vars_["list"][i]
    vars_["trace"].append(i)


def pop(vars_):
    if vars_["trace"]:
        last = vars_["trace"].pop()
        vars_["total"] -= vars_["list"][last]


def can_continue(vars_):
    return not (vars_["first_only"] and len(vars_["solutions"]) == 1)


def explore(vars_: dict, i: int):
    while can_continue(vars_) and i < len(vars_["list"]):

        if vars_["total"] + vars_["list"][i] <= cible:
            add(vars_, i)

            explore(vars_, i + 1)

            if vars_["total"] == cible:
                vars_["solutions"].append(vars_["trace"][:])

            pop(vars_)

        i += 1

# ------------- Tests ---------------------

nombres = [3, 3, 2, 2, 7, 5, 9, 12]

cible = 12

# --------- récursif classe -----------
trace = Explorer(nombres, cible, first_only=False)
trace.explore()
print(trace.get_all_solutions())

# ------- itération -------------
visitor = Visitor(nombres, cible, first_only=False)
visitor.explore()
print(visitor.get_all_solutions())

# -------- récursif fonctions --------
trace = compte(nombres, cible, first_only=False)
print(trace)



