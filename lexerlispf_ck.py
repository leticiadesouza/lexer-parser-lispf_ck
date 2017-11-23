import ox
import click

#enter the file
@click.command()
@click.argument('source', type=click.File('r'))

def lexer_parser(source):

    #making lexer

    lexer = ox.make_lexer([        
        ('NUMBER', r'\d+'),
        ('NAME', r'[-a-zA-Z]+'),
        ('COMMENT', r';.*'),
        ('NEWLINE', r'\n'),
        ('SPACE', r'\s+'),
        ('RIGHT', r'right'),
        ('LEFT', r'left'),
        ('INC', r'inc'),
        ('DEC', r'dec'),
        ('ADD',r'add'),
        ('SUB',r'sub'),
        ('PRINT', r'print'),
        ('READ', r'read'),
        ('DO',r'do'),
        ('LOOP', r'loop'),
        ('DEF', r'def'),
        ('PARENTHESIS_B', r'\('),
        ('PARENTHESIS_A', r'\)')        
    ])

    #Seting tokens
    tokens = ['NUMBER','INC', 'DEC','SUB', 'ADD','RIGHT', 'LEFT','PRINT','DO','NAME','LOOP',
                'READ','DEF','PARENTHESIS_A','PARENTHESIS_B']

    op = lambda op: (op)
    operator = lambda type_op: (type_op)

    #making parser
    parser = ox.make_parser([
        ('program : PARENTHESIS_B expr PARENTHESIS_A', lambda x,y,z: y),
        ('program : PARENTHESIS_B PARENTHESIS_A', lambda x,y: '()'),
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

    #reading the program source
    program = source.read()

    #seting the tokens with lexer
    tokens = lexer(program)

    #removing comments and spaces of tokens to make the tree
    parser_tokens = [token for token in tokens if token.type != 'COMMENT' and token.type != 'SPACE']

    #running the parser and making the tree
    tree = parser(parser_tokens)
    print('\n\nTree\n\n')
    print(tree,'\n\n')

if __name__ == '__main__':
    lexer_parser()
