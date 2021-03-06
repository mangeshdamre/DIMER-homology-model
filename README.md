# DIMER-homology-model
How to use MODELLER to build DIMER homology model with ligand?

## Procedure:
- Get Fasta sequence from UNIPROT database.
- Predict sequence alignment from HHPRED (**<a href="https://toolkit.tuebingen.mpg.de/tools/hhpred" target="_blank">HHpred</a>**)
- Install modeller (**<a href="https://salilab.org/modeller/download_installation.html" target="_blank">Download & Installation</a>**)
- Prepare INPUT files for MODELLER as below:

Use the following code: (**<a href="https://github.com/mangeshdamre/DIMER-homology-model/blob/main/model-dimer.py" target="_blank">model-dimer.py</a>**)
```ruby
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
```

Use the following alignment (Alignment taken from SALI LAB): (**<a href="https://github.com/mangeshdamre/DIMER-homology-model/blob/main/TvLDH-1bdm.ali" target="_blank">TvLDH-1bdm.ali</a>**)
```ruby
>P1;1bdm
structureX:1bdm.pdb: 0: A: 333: B:undefined:undefined:-1.00:-1.00
MKAPVRVAVTGAAGQIGYSLLFRIAAGEMLGKDQPVILQLLEIPQAMKALEGVVMELEDCAFPLL
AGLEATDDPDVAFKDADYALLVGAAPR---------LQVNGKIFTEQGRALAEVAKKDVKVLVVG
NPANTNALIAYKNAPGLNPRNFTAMTRLDHNRAKAQLAKKTGTGVDRIRRMTVWGNHSSIMFPDL
FHAEV----DGRPALELVDMEWYEKVFIPTVAQRGAAIIQARGASSAASAANAAIEHIRDWALGT
PEGDWVSMAVP--SQGEYGIPEGIVYSFPVTA-KDGAYRVVEGLEINEFARKRMEITAQELLDEM
EQVKALGLI----./
MKAPVRVAVTGAAGQIGYSLLFRIAAGEMLGKDQPVILQLLEIPQAMKALEGVVMELEDCAFPLL
AGLEATDDPDVAFKDADYALLVGAAPRKAGMERRDLLQVNGKIFTEQGRALAEVAKKDVKVLVVG
NPANTNALIAYKNAPGLNPRNFTAMTRLDHNRAKAQLAKKTGTGVDRIRRMTVWGNHSSIMFPDL
FHAEV----DGRPALELVDMEWYEKVFIPTVAQRGAAIIQARGASSAASAANAAIEHIRDWALGT
PEGDWVSMAVP--SQGEYGIPEGIVYSFPVTA-KDGAYRVVEGLEINEFARKRMEITAQELLDEM
EQVKALGLI----.*
>P1;TvLDH
sequence:TvLDH:::::::0.00:0.00
MSEAAHVLITGAAGQIGYILSHWIASGELYG-DRQVYLHLLDIPPAMNRLTALTMELEDCAFPHL
AGFVATTDPKAAFKDIDCAFLVASMPLKPGQVRADLISSNSVIFKNTGEYLSKWAKPSVKVLVIG
NPDNTNCEIAMLHAKNLKPENFSSLSMLDQNRAYYEVASKLGVDVKDVHDIIVWGNHGESMVADL
TQATFTKEGKTQKVVDVLDHDYVFDTFFKKIGHRAWDILEHRGFTSAASPTKAAIQHMKAWLFGT
APGEVLSMGIPVPEGNPYGIKPGVVFSFPCNVDKEGKIHVVEGFKVNDWLREKLDFTEKDLFHEK
EI--ALNHLAQGG./
MSEAAHVLITGAAGQIGYILSHWIASGELYG-DRQVYLHLLDIPPAMNRLTALTMELEDCAFPHL
AGFVATTDPKAAFKDIDCAFLVASMPLKPGQVRADLISSNSVIFKNTGEYLSKWAKPSVKVLVIG
NPDNTNCEIAMLHAKNLKPENFSSLSMLDQNRAYYEVASKLGVDVKDVHDIIVWGNHGESMVADL
TQATFTKEGKTQKVVDVLDHDYVFDTFFKKIGHRAWDILEHRGFTSAASPTKAAIQHMKAWLFGT
APGEVLSMGIPVPEGNPYGIKPGVVFSFPCNVDKEGKIHVVEGFKVNDWLREKLDFTEKDLFHEK
EI--ALNHLAQGG.*
```

In the alignment file dot **( . )** represents the ligand and slash **( / )** represents the chain break.

## Precautions to be taken:
Make sure ligand is at the end of each chain before **TER** in the template PDB (here **<a href="https://www.rcsb.org/structure/1bdm" target="_blank">1bdm.pdb</a>**) and delete all other molecules (for example: *Water*).
- Execute modeller in the linux terminal
```sh
mod9.17 model-dimer.py
```
OR  for higher version of modeller
```sh
mod9.18 model-dimer.py
```

That's all. You are ready to analyze models.
