try:
    from cStringIO import StringIO
except ImportError:
    from stringIO import StringIO
import json

from ckan.plugins.toolkit import BaseController, render, request, response
import ckanapi

from ckanext.cfpb_extrafields.digutils import make_rec

# def get_datasets(rows=10000):
    # api = ckanapi.LocalCKAN()
    # result = api.call_action(
        # "package_search",
        # {
            # "q": "",
            # "rows": rows,
        # }
    # )
    # return result

class ImportController(BaseController):
    def index(self):
        return render('ckanext/cfpb-extrafields/import_index.html')

    def upload(self):
        dig = request.POST["file"]
        rec = make_rec(dig)

        return json.dumps(rec)
