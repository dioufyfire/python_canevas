#coding:utf-8

"""

import <nom_module>        =>  pour appel fonction : "module.fonction"
from <nom_module> import <nom_fonction1>    =>  pour appel fonction "fonction1" seulement : "fonction1"
from <nom_module> import *    =>  pour appel fonction : "fonction"
"""

#exemple module dans un sous repertoire include

import includes.players

includes.players.au_revoir();

#### on peut optimiser l'appel par : "import includes.players as players => players.au_revoir(); "