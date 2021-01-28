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

</ol>
