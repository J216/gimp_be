echo GIMP Memory:
pmap -x `pgrep gimp` |  tail -1
echo GIMP Python Memory:
pmap -x `pgrep python2.7` | tail -1
