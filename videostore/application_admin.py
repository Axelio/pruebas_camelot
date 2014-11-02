
from camelot.view.art import Icon
from camelot.admin.application_admin import ApplicationAdmin
from camelot.admin.section import Section
from camelot.core.utils import ugettext_lazy as _

class MyApplicationAdmin(ApplicationAdmin):
  
    name = 'VideoStore'
    application_url = 'http://www.python-camelot.com'
    help_url = 'http://www.python-camelot.com/docs.html'
    author = 'Axelio'
    domain = 'mydomain.com'
    
    def get_sections(self):
        from camelot.model.memento import Memento
        from camelot.model.i18n import Translation
        from videostore.model import Movie
        return [ Section( _('Movie'),
                         self,
                         Icon('tango/22x22/apps/system-users.png'),
                         items = [Movie] ),
                 Section( _('Configuration'),
                         self,
                         Icon('tango/22x22/categories/preferences-system.png'),
                         items = [Memento, Translation] )
                 Section( 'Movies',
                          self,
                          Icon( 'tango/22x22/mimetypes/x-office-presentation.png' ),
                          items = [ Movie, Director ])
               ]

