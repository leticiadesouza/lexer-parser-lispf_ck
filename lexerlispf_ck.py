import ox
import click

@click.command()
@click.argument('source', type=click.File('r'))

def entry_tree(source):

    program = source.read()

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

    tokens = lexer(program)

    parser_rules = [
        ('program : PARENTESE_A expr PARENTESE_F', lambda x,y,z: y),
        ('program : PARENTESE_A PARENTESE_F', lambda x,y: '()'),
        ('expr : operator expr', lambda x,y: (x,) + y),
        ('expr : operator', lambda x: (x,)),
        ('operator : program', op),
        ('operator : LOOP', operator),
        ('operator : DO', operator),
        ('operator : RIGHT', operator),
        ('operator : LEFT', operator),
        ('operator : READ', operator),
        ('operator : INC', operator),
        ('operator : DEC', operator),
        ('operator : DEF', operator),
        ('operator : PRINT', operator),
        ('operator : ADD', operator),
        ('operator : SUB', operator),
        ('operator : NAME', operator),
        ('operator : NUMBER', operator),
    ]

    parser = ox.make_parser(parser_rules)
    
    

if __name__ == '__main__':
    entry_tree()