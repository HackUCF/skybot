import random
from util import hook

@hook.command
def choose(inp):
    ".choose <choice1>, <choice2>, ... <choicen> -- makes a decision"
    
    choices = filter(bool, inp.split(","))
    
    if len(choices) == 1:
        return 'the decision is up to you'

    return random.choice(choices).strip()
