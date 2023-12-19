import util

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
    items = []
    add_to_items = False
    for line in lines:
        if line == '':
            add_to_items = True
            continue

        if add_to_items:
            line = line.replace('{', '').replace('}', '')
            kvs = line.split(',')
            d = {}
            for kv in kvs:
                k, v = kv.split('=')
                d[k] = int(v)
            items.append(d)
        else:
            name, workflow = line.replace('}', '').split('{')
            rules = list(map(Rule, workflow.split(',')))
            workflows[name] = rules

    score = 0

    for item in items:
        done = False
        cwork = 'in'
        while not done:
            for rule in workflows[cwork]:
                result = rule.parse(item)
                if result == 'A':
                    print(f"Accepting {item}")
                    score += sum(item.values())
                    done = True
                    break
                elif result == 'R':
                    print(f"Rejecting {item}")
                    done = True
                    break
                elif result is None:
                    continue
                else:
                    print(f"Sending {item=} to {result}")
                    cwork = result
                    break

    print(score)