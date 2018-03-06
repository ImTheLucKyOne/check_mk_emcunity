# check_mk_emcunity
Check_MK Extensions for Dell EMC Unity Storages

!!! Tested with following unity systems: Unity 300, Unity 450F (thanks to christian.marscheck@comlineag.de for confirming this)  !!!

# About:
If you are searching for check_mk plugins to monitor your Dell EMC Unity Storage System, this project is one place to look for.

# Disclaimer:
I am not a professional programmer and I know there are some design and coding flaws in my python code. I try to keep track of what to do/change here https://github.com/ImTheLucKyOne/check_mk_emcunity/issues. Please let me know if you have useful hints regarding changes or fixes.

# Prerequisites / Installation:
The special agent makes use of the Dell CLI tool "uemcli" (documentation: https://www.emc.com/collateral/TechnicalDocument/docu69330.pdf). You can download it from the dell support website ("https://support.emc.com").
1) It has to be installed on your check_mk server.
2) The user running the agent needs a home directory.
3) The user running the agent (the CMK/OMD user) needs to connect to your EMC Unity system at least once over CLI to confirm the certificate and cache that information into its home directory. See the EMC documentation for details about how to connect to your Unity over CLI.
4) Download and install the latest emcunity300-x.mkp Check_MK package from this github site.
5) Create a new WATO rule "Datasource Programs - Check state of EMC Unity 300 storage systems"
6) Enter an admin user and the password for this user to connect to the EMC Unity

# emcunity300.mkp content:
- special agent "agent_emcunity" plus according WATO rule
- check plugins
- man pages
- pnp-templates for lun, pool, vmfs, fs
- metrics and perfometer for lun, pool, vmfs, fs
