pkgname=rpi_omx_loop
pkgver=0
pkgrel=1
pkgdesc="rpi_omx_player"
arch=('any')
depends=('omxplayer')
source=("$pkgname.service" "$pkgname.sh")
install=$pkgname.install
md5sums=('SKIP' 'SKIP')

package() 
{
msg "this is my directory `pwd`"
INSTALLPATH=/etc/systemd/system
SERVICEPATH=$srcdir/$pkgname.service
EXECPATH="$srcdir/$pkgname.sh"

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


}
