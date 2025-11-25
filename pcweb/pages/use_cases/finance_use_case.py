from pcweb.pages.use_cases.finance_landing import finance_landing_page
from pcweb.templates.webpage import webpage


@webpage(path="/use-cases/finance", title="Finance Use Case - Reflex")
def finance_use_case_page():
    return finance_landing_page()
