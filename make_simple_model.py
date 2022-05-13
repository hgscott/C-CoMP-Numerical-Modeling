# Make a simple model and save it as a JSON file for d3flux examples

import cobra

model = cobra.core.Model('simple_model')

A = cobra.core.Metabolite('A')
B = cobra.core.Metabolite('B')
C = cobra.core.Metabolite('C')
D = cobra.core.Metabolite('D')
E = cobra.core.Metabolite('E')
P = cobra.core.Metabolite('P')

R1 = cobra.core.Reaction('R1')
R2 = cobra.core.Reaction('R2')
R3 = cobra.core.Reaction('R3')
R4 = cobra.core.Reaction('R4')
R5 = cobra.core.Reaction('R5')
R6 = cobra.core.Reaction('R6')
R7 = cobra.core.Reaction('R7')
R8 = cobra.core.Reaction('R8')
R9 = cobra.core.Reaction('R9')
R10 = cobra.core.Reaction('R10')

model.add_metabolites([A, B, C, D, E, P])
model.add_reactions([R1, R2, R3, R4, R5, R6, R7, R8, R9, R10])

model.reactions.R1.build_reaction_from_string('--> A')
model.reactions.R2.build_reaction_from_string('<--> B')
model.reactions.R3.build_reaction_from_string('P -->')
model.reactions.R4.build_reaction_from_string('E -->')
model.reactions.R5.build_reaction_from_string('A --> B')
model.reactions.R6.build_reaction_from_string('A --> C')
model.reactions.R7.build_reaction_from_string('A --> D')
model.reactions.R8.build_reaction_from_string('B <--> C')
model.reactions.R9.build_reaction_from_string('B --> P')
model.reactions.R10.build_reaction_from_string('C + D --> E + P')

A.notes['map_info'] = {}
A.notes['map_info']['x'] = 150.
A.notes['map_info']['y'] = 50.

B.notes['map_info'] = {}
B.notes['map_info']['x'] = 80.
B.notes['map_info']['y'] = 130.

C.notes['map_info'] = {}
C.notes['map_info']['x'] = 150.
C.notes['map_info']['y'] = 130.

D.notes['map_info'] = {}
D.notes['map_info']['x'] = 220.
D.notes['map_info']['y'] = 130.

P.notes['map_info'] = {}
P.notes['map_info']['x'] = 150.
P.notes['map_info']['y'] = 200.

E.notes['map_info'] = {}
E.notes['map_info']['x'] = 220.
E.notes['map_info']['y'] = 200.

cobra.io.save_json_model(model, "simple_model.json")