import ox
import click

lexer = ox.make_lexer(lexer_rules)

lexer_rules = [
    ('NAME', r'[a-zA-Z]+'),
    ('NUMBER', r'\d+'),
    ('RIGHT', r'right'),
    ('LEFT', r'left'),
    ('OPEN_PAREN', r'\('),
    ('CLOSE_PAREN', r'\)'),
    ('INCR', r'incr'),
    ('COMMA', r'\,')
    ('SPACE', r'\s+'),
    ('NEWLINE', r'\n'),
    ('DEF', r'def'),
]

lexer = ox.make_lexer(lexer_rules)

token_list = [
    'NAME',
    'NUMBER',
    'RIGHT',
    'LEFT',
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'INCR',
    'COMMA',
    'SPACE',
    'NEWLINE',
    'DEF'
]

parser = ox.make_parser(parser_rules)

parser = ox.make_parser([

],    token_list)



lisp_entry = []
for data in source:
    lisp_entry = []
    for data in source:
        lisp_entry.append(data)

tokens = lexer(lisp_entry)
print('Tokens:\n', tokens)

@click.command()
@click.argument()

def entry_tree(source):
    program = source.read()
    print()
