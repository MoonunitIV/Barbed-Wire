from compiler import *
####################################################################################################################
#  Each quest record contains the following fields:
#  1) Info page id: used for referencing info pages in other files. The prefix ip_ is automatically added before each info page id.
#  2) Info page name: Name displayed in the info page screen.
#
####################################################################################################################
##diplomacy start+
from module_constants import DPLMC_DIPLOMACY_VERSION_STRING
from module_strings import *
##diplomacy end+

info_pages = [
("player", "Player", ""),
("player_party", "Player Party", ""),
("player_party_companions", "Player Companions", ""),
("player_relations", "Player Relations", ""),
("player_score", "Player Score", ""),
]
# modmerger_start version=201 type=2
try:
    component_name = "info_pages"
    var_set = { "info_pages" : info_pages }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
