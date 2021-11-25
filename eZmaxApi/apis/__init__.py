
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.global_customer_api import GlobalCustomerApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from eZmaxApi.api.global_customer_api import GlobalCustomerApi
from eZmaxApi.api.module_authenticate_api import ModuleAuthenticateApi
from eZmaxApi.api.module_list_api import ModuleListApi
from eZmaxApi.api.module_sspr_api import ModuleSsprApi
from eZmaxApi.api.module_user_api import ModuleUserApi
from eZmaxApi.api.object_activesession_api import ObjectActivesessionApi
from eZmaxApi.api.object_apikey_api import ObjectApikeyApi
from eZmaxApi.api.object_ezsignbulksend_api import ObjectEzsignbulksendApi
from eZmaxApi.api.object_ezsigndocument_api import ObjectEzsigndocumentApi
from eZmaxApi.api.object_ezsignfolder_api import ObjectEzsignfolderApi
from eZmaxApi.api.object_ezsignfoldersignerassociation_api import ObjectEzsignfoldersignerassociationApi
from eZmaxApi.api.object_ezsignfoldertype_api import ObjectEzsignfoldertypeApi
from eZmaxApi.api.object_ezsignsignature_api import ObjectEzsignsignatureApi
from eZmaxApi.api.object_ezsigntemplatepackage_api import ObjectEzsigntemplatepackageApi
from eZmaxApi.api.object_franchisebroker_api import ObjectFranchisebrokerApi
from eZmaxApi.api.object_franchiseoffice_api import ObjectFranchiseofficeApi
from eZmaxApi.api.object_franchisereferalincome_api import ObjectFranchisereferalincomeApi
from eZmaxApi.api.object_period_api import ObjectPeriodApi
