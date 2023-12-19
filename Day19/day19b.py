import copy
import util

#SOLVE WITH BRANCH BIFURCATION

branches = []

class Condition:
    def __init__(self):
        self.min_values = {'x': 1, 'm': 1, 'a': 1, 's': 1}
        self.max_values = {'x': 4000, 'm': 4000, 'a': 4000, 's': 4000}
        self.accept = None

    def update(self, char, op, num):
        if op == '<':
            self.max_values[char] = min(self.max_values[char], num - 1)
        elif op == '<=':
            self.max_values[char] = min(self.max_values[char], num)
        elif op == '>':
            self.min_values[char] = max(self.min_values[char], num + 1)
        elif op == '>=':
            self.min_values[char] = max(self.min_values[char], num)
        else:
            raise Exception(f"INVALID OP {op=}")

    def set_state(self, state):
        self.accept = state

    def calc(self):
        possibilities = 1
        for key in self.min_values:
            possibilities *= (self.max_values[key] - self.min_values[key] + 1)
        if self.accept:
            return possibilities, 0
        else:
            return 0, possibilities

    def __repr__(self):
        return f"CONDITION WITH {self.calc()=}"

class Rule:
    def __init__(self, rule_str):
        if ':' in rule_str:
            self.check_rule = True
            rule_str, self.target = rule_str.split(':')
            if '<' in rule_str:
                self.op = '<'
                self.char, self.num = rule_str.split('<')
            elif '>' in rule_str:
                self.op = '>'
                self.char, self.num = rule_str.split('>')
            else:
                raise Exception(f"INVALID RULE STR {rule_str}")
            self.num = int(self.num)
        else:
            self.check_rule = False
            self.target = rule_str

        self.rstr = rule_str

    def parse(self, item):
        if self.check_rule:
            if self.op == '>' and item[self.char] > self.num:
                return self.target
            if self.op == '<' and item[self.char] < self.num:
                return self.target
        else:
            return self.target

    def __repr__(self):
        return f"Rule with {self.rstr=}"



def main():
    with open("Day19/day19.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    workflows = {}
    for line in lines:
        if line == '':
            break
        name, workflow = line.replace('}', '').split('{')
        t_rules = list(map(Rule, workflow.split(',')))
        workflows[name] = t_rules

    conditions = []

    def parse_target(target, condition):
        if target == 'A':
            condition.set_state(True)
            conditions.append(condition)
        elif target == 'R':
            condition.set_state(False)
            conditions.append(condition)
        else:
            rrr(workflows[target], condition)


    @util.debug_IO
    def rrr(rules: list[Rule], condition: Condition):
        for rule in rules:
            if rule.check_rule:
                c2 = copy.deepcopy(condition)
                c2.update(rule.char, rule.op, rule.num)
                parse_target(rule.target, c2)

                #Apply inverse condition

            else:
                parse_target(rule.target, condition)

    rrr(workflows['in'], Condition())

    score = 0

    print(conditions)