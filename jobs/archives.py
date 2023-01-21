"""
jobs.archives
~~~~~~~~~~~~~

Maxquant searched output file named 'peptides.txt'
peptides.txt contains about a hundred of columns.
To easily inquire, columns are clustered in few divisions.

* Default (No fractions) Set: 56
<Division1>'Sequence', 'N-term cleavage window', 'C-term cleavage window',
<Division2>'Amino acid before', 'First amino acid', 'Second amino acid', 'Second last amino acid', 'Last amino acid', 'Amino acid after',
<Division3>
'A Count', 'R Count', 'N Count', 'D Count', 'C Count', 'Q Count', 'E Count', 'G Count', 'H Count', 'I Count', 'L Count',
'K Count', 'M Count','F Count', 'P Count', 'S Count', 'T Count', 'W Count', 'Y Count', 'V Count', 'U Count', 'O Count',
<Division4>'Length', 'Missed cleavages', 'Mass', 'Proteins', 'Leading razor protein', 'Start position', 'End position',
<Division5>'Gene names', 'Protein names', 'Unique (Groups)', 'Unique (Proteins)', 'Charges', 'PEP', 'Score',
<Division7>'Intensity',
<Division8>'Reverse', 'Potential contaminant', 'id', 'Protein group IDs', 'Mod. peptide IDs', 'Evidence IDs', 'MS/MS IDs', 'Best MS/MS', 'Oxidation (M) site IDs', 'MS/MS Count'

* N Fractioned Set: 3+N (Here, N is in [0,8])
<Division6-1: Fraction>
'Fraction Average', 'Fraction Std. Dev.', 'Fraction 0', 'Fraction 1', ..., 'Fraction 8'

* N Replication Set: N
<Division6-2: Experiment>
'Experiment 1st', 'Experiment 2nd', 'Experiment 3rd'

* TMT-(N)plex + n replication Set: 
<Division7: (N)plexTMT>
(N*3)+(N*3*n)+(1+n)=3N(n+1)+(n+1)=(3N+1)(n+1)
'Reporter intensity corrected <1,2,3>', 'Reporter intensity <1,2,3>', 'Reporter intensity count <1,2,3>',
'Reporter intensity corrected <1,2,3> 1st', 'Reporter intensity <1,2,3> 1st', 'Reporter intensity count <1,2,3> 1st',
'Reporter intensity corrected <1,2,3> 2nd', 'Reporter intensity <1,2,3> 2nd', 'Reporter intensity count <1,2,3> 2nd',
'Reporter intensity corrected <1,2,3> 3rd', 'Reporter intensity <1,2,3> 3rd', 'Reporter intensity count <1,2,3> 3rd',
'Intensity', 'Intensity 1st', 'Intensity 2nd', 'Intensity 3rd'

* SILAC Set: 

* Organize
<Potent remained>
'Sequence', 'Missed Cleavages', 'Leading razor protein', 'Start position',
'Gene names', 'Protein names', 'Charges' ,'PEP', 'Score', 'Intensity', 'Reporter intensity', 'id',
'Protein group IDs', 'Evidence IDs', 'MS/MS IDs', 'Best MS/MS'

<Certainly dropped>
'N-term cleavage window', 'C-term cleavage window',
'Amino acid before', 'First amino acid', 'Second amino acid', 'Second last amino acid', 'Last amino acid', 'Amino acid after',
'A Count', 'R Count', 'N Count', 'D Count', 'C Count', 'Q Count', 'E Count', 'G Count', 'H Count', 'I Count', 'L Count',
'K Count', 'M Count','F Count', 'P Count', 'S Count', 'T Count', 'W Count', 'Y Count', 'V Count', 'U Count', 'O Count',
'Length', 'Mass', 'Proteins', 'End position', 'Unique (Groups)', 'Unique (Proteins)'

<Newly created>
'Normalized Reporter intensities'
"""
import pandas as pd
