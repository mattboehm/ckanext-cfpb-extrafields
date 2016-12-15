from openpyxl import load_workbook

def concat(fields):
    def concat_fields(ws):
        result = ""
        for field in fields:
            result += ws[field].value or ""
        return result
    return concat_fields

"""Maps field name to either a cell or a function that's passed the worksheet and should return the value"""
FIELDS = {
    "access_restrictions": "B17",
    "contact_primary_name": "D7",
    "contact_secondary_name": "B6",
    "data_source_names": "D10",
    "dataset_notes": "B54",
    "dig_id": "B5",
    "initial_purpose_for_intake": "H15",
    "legal_authority_for_collection": "B25",
    "notes": "H4",
    "pra_exclusion": concat(["D38", "B39"]),
    "pra_omb_control_number": "F37",
    "pra_omb_expiration_date": "F38",
    "privacy_contains_pii": "B29",
    "privacy_has_direct_identifiers": "B30",
    "privacy_has_privacy_act_statement": "D30",
    "privacy_pia_notes": "B33",
    "privacy_pia_title": "D32",
    "privacy_sorn_number": "D31",
    "procurement_document_id": "F24",
    "relevant_governing_documents": "D24",
    "sensitivity_level": "B13",
    "title": "B4",
    "transfer_details": "B54",
    "transfer_initial_size": "B47",
    "transfer_method": "B48",
    "update_frequency": "F47",
    "usage_restrictions":  concat(["B18", "B19"]),
    "website_url": "B54",
    "wiki_link": "B54"
}

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
