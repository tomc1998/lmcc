import lexer

test_program = \
"""
let x = 0;
let y = 10;
let z = x + y;
out z;
"""
lexer.lex(test_program);

