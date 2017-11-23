import ox
import click

@click.command()
@click.argument('source', type=click.File('r'))

def lexer_parser(source):    

    lexer = ox.make_lexer([
        ('RIGHT', r'right'),
        ('LEFT', r'left'),
        ('INC', r'inc'),
        ('DEC', r'dec'),
        ('PRINT', r'print'),
        ('READ', r'read'),
        ('DO',r'do'),
        ('ADD',r'add'),
        ('SUB',r'sub'),
        ('LOOP', r'loop'),
        ('DEF', r'def'),
        ('NUMBER', r'\d+'),
        ('PARENTESE_A', r'\('),
        ('PARENTESE_F', r'\)'),
        ('NAME', r'[-a-zA-Z]+'),
        ('COMMENT', r';.*'),
        ('NEWLINE', r'\n'),
        ('SPACE', r'\s+')
    ])

    tokens = ['RIGHT', 'LEFT', 'INC', 'DEC', 'SUB', 'ADD', 'NUMBER','PRINT', 'LOOP',
                'READ','DEF','PARENTESE_F','PARENTESE_A','DO','NAME']
    
    operator = lambda type_op: (type_op)
    op = lambda op: (op)
    opr = lambda op, num: (op, num)    

    parser = ox.make_parser([
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
    ], tokens)

    program = source.read()

    tokens = lexer(program)

    parser_tokens = [token for token in tokens if token.type != 'COMMENT' and token.type != 'SPACE']

    tree = parser(parser_tokens)
    print('\n\nTree\n\n')
    print(tree,'\n\n')

if __name__ == '__main__':
    lexer_parser()