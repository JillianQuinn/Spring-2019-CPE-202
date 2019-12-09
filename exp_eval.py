from stack_array import Stack


# You do not need to change this class
class PostfixFormatException(Exception):
    pass


def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    input_list = input_str.split(" ")
    operators = ["*", "+", "-", "/", "**", "<<", ">>"]
    operator_count = 0
    int_count = 0
    for i in input_list:
        if i in operators:
            operator_count += 1
        else:
            int_count += 1
    if int_count - 1 > operator_count:
        raise PostfixFormatException("Too many operands")
    elif int_count - 1 < operator_count:
        raise PostfixFormatException("Insufficient operands")
    operands = Stack(len(input_list))
    for i in input_list:
        if i in operators:
            if operands.num_items > 1:
                op1 = operands.pop()
                op2 = operands.pop()
            # else:
                # raise PostfixFormatException("Insufficient operands")
                if op1 == 0 and i == "/":
                    raise ValueError
                try:
                    operands.push(eval("{0}{1}{2}".format(op2, i, op1)))
                except TypeError:
                    raise PostfixFormatException("Illegal bit shift operand")
        else:
            try:
                operands.push(float(i))
            except ValueError:
                raise PostfixFormatException("Invalid token")
    return operands.pop()


def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""
    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    input_list = input_str.split(" ")
    operators = ["*", "+", "-", "/", "**", "<<", ">>"]
    RPN = ""
    op_st = Stack(len(input_list))
    for i in input_list:
        if i == "(":
            op_st.push("(")
        elif i == ")":
            not_paren = True
            while not_paren and not op_st.is_empty():
                value = op_st.pop()
                if value != "(":
                    RPN += (value + " ")
                else:
                    not_paren = False
        elif i in operators:
            is_operator = True
            while is_operator and not op_st.is_empty():
                o2 = op_st.pop()
                if o2 not in operators:
                    op_st.push(o2)
                    is_operator = False
                else:
                    if i == "**" and (o2 == "<<" or o2 == ">>") and o2 != "(":
                        RPN += (o2 + " ")
                    elif (i == "*" or i == "/") and (o2 != "+" and o2 != "-") and o2 != "(":
                        RPN += (o2 + " ")
                    elif (i == "+" or i == "-") and o2 != "(":
                        RPN += (o2 + " ")
                    else:
                        op_st.push(o2)
                        is_operator = False
            op_st.push(i)
        else:
            RPN += (i + " ")
    for j in range(op_st.num_items):
        op = op_st.pop()
        if op in operators:
            RPN += (op + " ")
    return RPN[0:len(RPN) - 1]


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    input_list = input_str.split(" ")
    operators = ["*", "+", "-", "/", "**", "<<", ">>"]
    pStack = Stack(len(input_list))
    for i in range(len(input_list) - 1, -1, -1):
        if input_list[i] in operators and pStack.num_items > 1:
            op1 = pStack.pop()
            op2 = pStack.pop()
            string = op1 + " " + op2 + " " + input_list[i]
            pStack.push(string)
        else:
            pStack.push(input_list[i])
    return pStack.pop()



