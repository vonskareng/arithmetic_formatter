import re

def error_handling(fn):
    def inner(*args, **kwargs):
        if len(args[0]) > 5:
            return "Error: Too many problems."
        
        for p in args[0]:
            if "+" not in p and "-" not in p:
                return "Error: Operator must be '+' or '-'."
            
            check_if_digits = re.match("^\d*\s*[+|-]\s*\d*$", p)
            if not check_if_digits:
                return "Error: Numbers must only contain digits."
            
            txt = p.split()
            if len(txt[0]) > 4 or len(txt[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
        
        return fn(*args, **kwargs)

    return inner

def calculate_longest_string(problems):
    b = [p.split() for p in problems]
    longest_string = max(max(b, key=len), key=len)
    return (len(longest_string) + 2) * '-'

def format_problem_line(bb, longest_string):
    line1 = bb[0].rjust(len(longest_string))
    line2 = bb[1] + bb[2].rjust(len(longest_string) - len(bb[1]))
    line3 = longest_string
    return line1, line2, line3

def format_solution_line(bb, longest_string):
    solution = str(eval(' '.join(str(x) for x in bb)))
    line4 = solution.rjust(len(longest_string))
    return line4

@error_handling
def arithmetic_arranger(problems, show_answer=False):
    longest_string = calculate_longest_string(problems)
    line1 = line2 = line3 = line4 = ""
    spaces = "    "
    
    for index, bb in enumerate(problems):
        if index == 0:
            line1, line2, line3 = format_problem_line(bb.split(), longest_string)
            
            if show_answer:
                line4 = format_solution_line(bb.split(), longest_string)
            
            continue
        
        line1 += spaces + format_problem_line(bb.split(), longest_string)[0]
        line2 += spaces + format_problem_line(bb.split(), longest_string)[1]
        line3 += spaces + format_problem_line(bb.split(), longest_string)[2]
        
        if show_answer:
            line4 += spaces + format_solution_line(bb.split(), longest_string)
    
    if show_answer:
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    
    return line1 + "\n" + line2 + "\n" + line3

