#-------------------------------------------------------------------------
#
# register_report
#
#-------------------------------------------------------------------------
from gramps.version import major_version

register(EXPORT,
  id    = 'ExportParenty',
  name  = _("ExportParenty"),
  description =  _("Export Parenty"),
  version = '1.0.3',
  gramps_target_version = major_version,
  status = STABLE,
  fname = 'ExportParenty.py',
  authors = ["Eric Doutreleau"],
  authors_email = ["eric@doutreleau.fr"],
  export_function = 'export_data',
  export_options = 'ParentyOptionBox',
  export_options_title = _('Export Parenty File'),
  extension = "pf",

)
