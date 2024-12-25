with open("input24.txt") as f:
    input = f.read().split("\n\n")
    start_wires = input[0].split("\n")
    gates = input[1].split("\n")


class Gate:
    def __init__(self, type, wire_in1, wire_in2, wire_out ):
        self.type = type
        self.wire_in1 = wire_in1
        self.wire_in2 = wire_in2
        self.wire_out = wire_out
        self.output = None

    def check_input_wires(self):
        print(f"Gate - Checking input values. {[self.wire_in1.get_value(), self.wire_in2.get_value()]}")
        if self.wire_in1.get_value() != None and self.wire_in2.get_value() != None:
            self.calculate_output()
        else:
            pass

    def calculate_output(self):
        wire_in_values = [self.wire_in1.get_value(), self.wire_in2.get_value()]
        print(f"Gate - My type is {self.type}. Input values: {wire_in_values}, for {self.wire_in1.name} and {self.wire_in2.name}")
        input_sum = sum(wire_in_values)
        if self.type == "XOR":
            self.output = input_sum % 2
        elif self.type == "OR":
            self.output = max(wire_in_values)
        elif self.type == "AND":
            self.output = 1 if input_sum == 2 else 0
        print(f"       Output is {self.output}, for {self.wire_out.name}")
        self.wire_out.set_value(self.output)


class Wire:
    def  __init__(self, name):
        self.name = name
        self.value = None
        self.gates = []

    def set_value(self, value):
        print(f"Wire - Name: {self.name}. Setting my value to {value}. ")
        self.value = value
        for g in self.gates:
            g.check_input_wires()

    def get_value(self):
        return self.value

    def set_gate(self, gate):
        self.gates.append(gate)



all_wires = {}
all_gates = []

for g in gates:
    left,output_name = g.split(" -> ")
    input1_name,gate_type,input2_name = left.split(" ")

    for w_name in [input1_name, input2_name]:
        if w_name not in all_wires:
            new_wire = Wire(w_name)
            all_wires[w_name] = new_wire


    if output_name not in all_wires:
        new_wire = Wire(output_name)
        all_wires[output_name] = new_wire
    new_gate = Gate(gate_type, all_wires[input1_name], all_wires[input2_name], all_wires[output_name])
    for w_name in [input1_name, input2_name]:
        all_wires[w_name].set_gate(new_gate)
    all_gates.append(new_gate)


#
# for w in start_wires:
#     name, value = w.split(": ")
#     if name in all_wires:
#         all_wires[name].set_value(int(value))
#     else:
#         print(f"{name} not in wires dict?")
#
# answer = 0
# for w in sorted(all_wires.keys()):
#     print(w, all_wires[w].get_value())
#     if w[0] == "z":
#         answer += pow(2,int(w[1:3])) * all_wires[w].get_value()
#
#
# print(answer)

x=1
y=0
for i in range(45):
    print(bin(x))
    x_wire_name = "x" + "%02d" % (i,)
    y_wire_name = "y" + "%02d" % (i,)
    wire_x = all_wires[x_wire_name]
    wire_y = all_wires[y_wire_name]
