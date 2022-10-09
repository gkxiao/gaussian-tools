<h2>gaussian-tools</h2>

<ol>
<li>RDKitSdf2Gau.py</li>   
<p>convert MDL SDF file (single molecule) into Gaussian input file </p>

<li>g2slurm.py/g2pbs.py</li>
<p>Generate SLURM/PBS script for Gaussian input file</p>

<li>G16Scan2CONF.py</li>
<p>Extract conformer from Gaussian scan output file</p>
<pre line="1" lang="python">
python G16Scan2CONF.py foo.log
</pre>
<p>For each conformer, a Gaussian input file for torsion-fixed optimization will be generated.</p>

<li>torsionreport.py</li>
<p>extract dihedral angle and energy from dihedral scan calculation.</p>

<li>RDKitSDF2GaussOptInSolvent.py</li>
<p>Generate Opt & Freq calculation input file:.</p>
<pre line="1" lang="python">
RDKitSDF2GaussOptInSolvent.py CONF_01.sdf CONF_01_opt_freq.com 'APFD/6-311+g(2d,p)' methanol
</pre>

<li>Chk2ECD.py</li>
<p>Generate TD-DTF calculation input file to simulate ECD spectra.</p>
<pre line="1" lang="python">
Chk2ECD.py CONF_01.chk CONF_01_ECD.chk CONF_01_ECD.com 'APFD/6-311+g(2d,p)'
</pre>

<li>Chk2VCD.py</li>
<p>Generate input file to simulate VCD spectra.</p>
<pre line="1" lang="python">
Chk2ECD.py CONF_01.chk CONF_01_VCD.chk CONF_01_VCD.com 'APFD/6-311+g(2d,p)'
</pre>

<li>Chk2NMR.py</li>
<p>Generate input file to simulate NMR spectra at mPW1PW91/6-311+g(2d,p) level.</p>
<pre line="1" lang="python">
Chk2NMR.py CONF_01.chk CONF_01_NMR.chk CONF_01_NMR.com
</pre>

<li>tddft2specdis.py</li>
<p>The script can be use to extract heat and ecd spectra from Gaussian 09/16 output file. The extracted heat and spectra can be read by software SpecDis to plot ECD spectra.</p>   
</ol>
