from modeller import *
from modeller.automodel import *
#from modeller import soap_protein_od
env = environ()
env.io.hetatm = True
a = automodel(env, alnfile='TvLDH-1bdm.ali',
              knowns='1bdm',
              sequence='TvLDH',
              assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))
a.md_level = refine.very_slow
a.starting_model = 1
a.ending_model = 1   #Number of output models
a.final_malign3d = True
a.make()
