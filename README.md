<h2>gaussian-tools</h2>

<ol>
<li>RDKitSdf2Gau.py</li>   
<p>convert MDL SDF file (single molecule) into Gaussian input file </p>

<li>g2slurm.py</li>
<p>Generate SLURM script for Gaussian input file</p>

<li>G16Scan2CONF.py</li>
<p>Extract conformer from Gaussian scan output file</p>
<pre line="1" lang="python">
python G16Scan2CONF.py foo.log
</pre>
<p>For each conformer, a Gaussian input file for torsion-fixed optimization will be generated.</p>

<li>torsionreport.py</li>
<p>extract dihedral angle and energy from dihedral scan calculation.
 
<li>tddft2specdis.py</li>
<p>The script can be use to extract heat and ecd spectra from Gaussian 09/16 output file. The extracted heat and spectra can be read by software SpecDis to plot ECD spectra.</p>   
</ol>
