import ox
import click

lexer = ox.make_lexer(lexer_rules)

lexer_rules = [
    ('NAME', r'[a-zA-Z]+'),
    ('NUMBER', r'\d+(\.\d)'),
    ('OPEN_PAREN', r'\('),
    ('CLOSE_PAREN', r'\)'),
    ('COMMA', r'\,')
    ('SPACE', r'\s+'),
]

lexer = ox.make_lexer(lexer_rules)

token_list = ['NUMBER', 'NAME', 'OPEN_PAREN', 'CLOSE_PAREN', 'COMMA']

parser = ox.make_parser(parser_rules)

parser_rules = [

    (),

]

@click.command()
@click.argument()

def parser()
