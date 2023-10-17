import os
from pcweb.templates.docpage import docpage
import openai
from pcweb import flexdown

# If it's in environment, no need to hardcode (openai SDK will pick it up)
if "OPENAI_API_KEY" not in os.environ:
    openai.api_key = "YOUR_OPENAI_KEY"


@docpage()
def adding_state():
    return flexdown.render_file("docs/tutorial/adding-state.md")
