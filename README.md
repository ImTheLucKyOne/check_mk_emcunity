# These plugins are no longer in "development". Issues won't get addressed or fixed by me. Feel free to use the code to write you own plugins.

# check_mk_emcunity
Check_MK Extensions for Dell EMC Unity Storages

!!! Tested with following unity systems: Unity 300, Unity 400VL (thanks to kazatelm for confirming this), Unity 450F (thanks to Christian M. for confirming this), Unity 500 and Unity600 (thanks to elisalepida for confirming this)  !!!

# About:
If you are searching for check_mk plugins to monitor your Dell EMC Unity Storage System, this project is one place to look for.

# Disclaimer:
I am not a professional programmer and I know there are some design and coding flaws in my python code. I try to keep track of what to do/change here https://github.com/ImTheLucKyOne/check_mk_emcunity/issues. Please let me know if you have useful hints regarding changes or fixes.

# Prerequisites / Installation:
- The latest version of the cmk package does not work with cmk versions < 1.6.0.
- Use the package 2.2.1 for cmk 1.5.x.
- Use the package 1.2.4 for cmk < 1.5.x.

The special agent makes use of the Dell CLI tool "uemcli" (documentation: https://www.emc.com/collateral/TechnicalDocument/docu69330.pdf).
https://www.dell.com/support/home/de-de/product-support/product/unity-300/drivers
You will need the keyword search "uem cli" to find the correct downloads.
At the moment it is not possible to find or download the downloads without logging in to the Dell support page.

1) Install uemcli on your cmk server
2) Create a (local) user on your Unity with Operator role (read only) - do not use your admin account for monitoring!
3) Execute on you cmk server with your site user (Connection with cmk only works after one time usage on command line)
   ```uemcli -d hostname -u username -securePassword -sslPolicy store /sys/general show```
5) Download and install the latest emcunity-x.mkp Check_MK package from this github site.
6) Create a new WATO rule "Datasource Programs - Check state of EMC Unity storage systems"
7) Enter user and the password for this user to connect to the EMC Unity

# emcunity.mkp content:
- special agent "agent_emcunity" plus according WATO rule
- check plugins
- man pages
- pnp-templates for lun, pool, vmfs, fs
- metrics and perfometer for lun, pool, vmfs, fs

# Credits:
Special thanks to the users who are helping me to improve this extension are going to:
- Marco Lenhardt
- goam03
- Christian M.
- kazatelm
- Marcel Werner
- pdcemulator
- Bob (cadencep45)
- elisalepida
- Andreas Döhler
