def define_loops(code):
    start_loop_positions_list = []
    loops_dict = {}
    for index, symbol in enumerate(code):
        if symbol == '[':
            start_loop_positions_list.append(index)
        if symbol == ']':
            start_index = start_loop_positions_list.pop()
            loops_dict[start_index] = index
            loops_dict[index] = start_index

    return loops_dict


def brain_fuck(code):
    cell_pointer = 0 # index of pointer  in turing tape
    i = 0 #index of pointer position in the code

    turing_tape = [0]*30000
    loops = define_loops(code)

    while i < len(code):
        symbol = code[i]

        if symbol == '<':
            cell_pointer -= 1

        elif symbol == '>':
            cell_pointer += 1

        elif symbol == "+":
            turing_tape[cell_pointer] += 1 if turing_tape[cell_pointer] < 255 else 0

        elif symbol == "-":
            turing_tape[cell_pointer] -= 1 if turing_tape[cell_pointer] > 0 else 255

        elif symbol == ".":
            print chr(turing_tape[cell_pointer])

        elif symbol == ',':
            pass

        elif symbol == "[":
            if not turing_tape[cell_pointer]:
                i = loops[i]

        elif symbol == "]":
            if turing_tape[cell_pointer]:
                i = loops[i]
        i += 1

if __name__ == '__main__':

    #print "hello world"
    brain_fuck('+++++++++++>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++\
<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]\
]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[+++++++++++++++++\
+++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]\
<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]')




