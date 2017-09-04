# check_mk_emcunity
Check_MK Extensions for Dell EMC Unity Storages

!!! Only tested with EMC Unity 300 !!!
!!! Latest (08/17) Firmware Update 4.2.0.9476662 mandatory !!!

# About:
If you are searching for check_mk plugins to monitor your Dell EMC Unity Storage System, this project is one place to look for.

# Prerequisites / Installation:
The special agent makes use of the Dell CLI tool "uemcli" (documentation: https://www.emc.com/collateral/TechnicalDocument/docu69330.pdf). You can download it from the dell support website ("https://support.emc.com").
1) It has to be installed on your check_mk server.
2) The user running the agent needs a home directory.
3) The user running the agent (the CMK/OMD user) needs to connect to your EMC Unity system at least once over CLI to confirm the certificate and cache that information into its home directory. See the EMC documentation for details about how to connect to your Unity over CLI.
4) Download and install the emcunity300.mkp Check_MK Package (http://mathias-kettner.de/checkmk_packaging.html)
5) Create a new WATO rule "Datasource Programs - Individual Program Call..."
6) Enter the command line to be executed (e.g.: /usr/local/check_mk/agents/special/agent_emcunity IP user password)

# emcunity300.mkp content:
- special agent "agent_emcunity"
- check plugins
- man pages
- pnp-templates for lun, pool, vmfs
- metrics and perfometer for lun, pool, vmfs
