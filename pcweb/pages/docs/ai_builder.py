from pcweb.templates.docpage import docpage

quickstart_page = docpage("/ai-builder/quickstart/", "AI Builder Quickstart")(
    lambda: "Quickstart content from markdown"
)
quickstart_page.title = "Quickstart"

integration_page = docpage("/ai-builder/integration/", "AI Builder Integration")(
    lambda: "Integration content from markdown"
)
integration_page.title = "Integration"


pages = [quickstart_page, integration_page]
