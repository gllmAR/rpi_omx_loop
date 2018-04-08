pkgname=rpi_omx_loop
pkgver=0
pkgrel=1
pkgdesc="rpi_omx_player"
arch=('any')
depends=('omxplayer')
source=("$pkgname.service" "$pkgname.sh" "omx_dbus_ctl.sh")
install=$pkgname.install
md5sums=('SKIP' 'SKIP' 'SKIP')

package() 
{
msg "this is my directory `pwd`"
SCRIPTPATH="$(dirname `pwd`)"
INSTALLPATH=/etc/systemd/system
SERVICEPATH=$srcdir/$pkgname.service
EXECPATH="$SCRIPTPATH/$pkgname.sh"

touch $SERVICEPATH
echo [Unit] > $SERVICEPATH
echo Description=$APPNAME >> $SERVICEPATH
echo After=syslog.target network.target >> $SERVICEPATH
echo [Service] >> $SERVICEPATH
echo User=$LOGNAME >> $SERVICEPATH
echo Environment=DISPLAY=:0 >> $SERVICEPATH
echo ExecStart=$EXECPATH >> $SERVICEPATH
echo Restart=on-failure >>$SERVICEPATH
echo [Install] >>$SERVICEPATH
echo WantedBy=multi-user.target >>$SERVICEPATH

msg "packaging service"
  for f in *.service; do
    install -D -m 644 "$f" "$pkgdir/etc/systemd/system/$f"
  done

install -D -m 755 "omx_dbus_ctl.sh" "$pkgdir/usr/local/bin/omx_dbus_ctl"

}
