import util

class MType:
    broadcaster = 0
    flipflop = 1
    conjunction = 2
    output = 3

class Module:
    def __init__(self, s):
        name, outputs = s.split(' -> ')
        self.outputs = outputs.split(', ')
        if '%' in name:
            self.name = name.replace('%', '')
            self.mtype = MType.flipflop
        elif '&' in name:
            self.name = name.replace('&', '')
            self.mtype = MType.conjunction
        elif name == 'broadcaster':
            self.name = name
            self.mtype = MType.broadcaster
        else:
            self.name = name
            self.mtype = MType.output

        self.ff_state = False #off
        self.con_input_state = {}

    def get_name(self):
        return self.name

def main():
    with open("Day20/day20.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    modules = {}
    for line in lines:
        m = Module(line)
        modules[m.get_name()] = m

    for mname, m in list(modules.items()):
        for out in m.outputs:
            if out not in modules:
                modules[out] = Module(f"{out} -> ?") #auto sets to output

            if m.mtype != MType.output and modules[out].mtype == MType.conjunction:
                modules[out].con_input_state[mname] = False #remember low pulse

    pulses = []

    def send_pulse(sender, reciever, pulse):
        module = modules[reciever]
        if module.mtype == MType.broadcaster:
            for subname in module.outputs:
                pulses.append((reciever, subname, pulse)) #send low pulse

        if module.mtype == MType.flipflop:
            if not pulse: #flip-flop only cares about low pulse
                for subname in module.outputs:
                    pulses.append((reciever, subname, not module.ff_state))  # send opposite of state pulse
                module.ff_state = not module.ff_state

        if module.mtype == MType.conjunction:
            module.con_input_state[sender] = pulse
            print(module.con_input_state)
            p_to_send = not all(module.con_input_state.values())
            for subname in module.outputs:
                pulses.append((reciever, subname, p_to_send))  # send opposite of state pulse


    total_low = 0
    total_high = 0
    for i in range(1000):
        send_pulse('broadcaster', 'broadcaster', False) #low pulse
        low_count = 1 # b/c button
        high_count = 0
        while pulses:
            p_sender, p_reciever, p_value = pulses.pop(0)
            print(f"Sending pulse: {p_sender} -> {p_value} to {p_reciever}")
            send_pulse(p_sender, p_reciever, p_value)

            if p_value:
                high_count += 1
            else:
                low_count += 1
        print(high_count, low_count)
        total_high += high_count
        total_low += low_count
        print()

    print(total_low * total_high)