try:
    from cStringIO import StringIO
except ImportError:
    from stringIO import StringIO
import json

from ckan.plugins.toolkit import BaseController, render, request, response
import ckanapi
from openpyxl import load_workbook

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
"""Maps field name to either a cell or a function that's passed the worksheet and should return the value"""
FIELDS = {}

def get_field(worksheet, field, fields=FIELDS):
    cell_or_func = fields[field]
    if hasattr(cell_or_func, "__call__"):
        return cell_or_func(worksheet)
    else:
        return worksheet[cell_or_func].value

def make_rec(excel_file):
    wb = load_workbook(excel_file, read_only=True)
    ws = wb.worksheets[0]
    result = {field: get_field(ws, field) for field in FIELDS}
    #TODO add name, owner_org?
    #TODO add validators?
    return result



class ImportController(BaseController):
    def index(self):
        return render('ckanext/cfpb-extrafields/import_index.html')

    def upload(self):
        dig = request.POST["file"]

        return "OK"
