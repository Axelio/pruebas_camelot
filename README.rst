Installation
------------

Iniciando un entorno virtual con python y el sistema de archivos del equipo, es necesario contar con pyqt4::

$ virtualenv virtualenv --system-site-packages
$ . virtualenv/bin/activate

Instalamos pyqt4::
# aptitude install python-dev python-qt4

Instalamos los requerimientos::
$ pip install -r requirements.txt

Iniciando el proyecto
---------------------

``$ python -m camelot.bin.camelot_admin``

Eso desplegará una ventana para asignar valores de configuración a nuestra aplicación
