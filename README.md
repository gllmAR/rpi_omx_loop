# rpi_omx_loop
raspberry pi omx video player on boot 

usage : 
	* mod rpi_omx_loop.sh 
	* (re)install using `makepkg -srif`

require:
	* samba share at /var/lib/samba/usershares/medias

[samba_config](https://wiki.archlinux.org/index.php/Samba#Creating_a_share)

```
mkdir -p /var/lib/samba/usershares
groupadd -r sambashare
chown root:sambashare /var/lib/samba/usershares
chmod 1770 /var/lib/samba/usershares
gpasswd sambashare -a your_username_1
gpasswd sambashare -a your_username_2
chgrp -R sambashare /var/lib/samba/usershares/medias
```

`/etc/samba/smb.conf`
```
[medias]
   comment = medias folder
   path = /var/lib/samba/usershares/medias
   valid users = @sambashare, @users
   public = no
   writable = yes
   printable = no
#   create mask = 0765
```
