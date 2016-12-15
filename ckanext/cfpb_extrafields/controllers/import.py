try:
    from cStringIO import StringIO
except ImportError:
    from stringIO import StringIO
import json

from ckan.plugins.toolkit import BaseController, render, response
import ckanapi

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
        return "OK"
