from pcweb.templates.docpage import docpage

cloud_overview = docpage("/cloud/overview/", "Cloud Overview")(
    lambda: "Cloud overview content from markdown"
)
cloud_overview.title = "Overview"

cloud_sample_page = docpage("/cloud/sample/", "Cloud Sample")(
    lambda: "Cloud sample content from markdown"
)
cloud_sample_page.title = "Sample"


pages = [cloud_overview, cloud_sample_page]
