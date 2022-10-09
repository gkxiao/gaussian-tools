%oldchk=CONF_01.chk
%chk=CONF_01_ECD.chk
#P td=(nstates=100) APFD/6-311+g(2d,p) guess=read geom=allcheck scrf=check
 
