import os

# pcweb constants.
API_BASE_URL_LOOPS: str = "https://app.loops.so/api/v1"
REFLEX_DEV_WEB_LANDING_FORM_URL_GET_DEMO: str = (
    "https://cal.com/forms/f87bd9b2-b339-4915-b4d4-0098e2db4394"
)
REFLEX_DEV_WEB_LANDING_FORM_SALES_CALL_WEBHOOK_URL: str = (
    "https://hooks.zapier.com/hooks/catch/20661176/2s1nxp9/"
)

REFLEX_DEV_WEB_NEWSLETTER_FORM_WEBHOOK_URL: str = "https://hkdk.events/t0qopjbznnp2fr"
REFLEX_DEV_WEB_GENERAL_FORM_FEEDBACK_WEBHOOK_URL: str = os.environ.get(
    "REFLEX_DEV_WEB_GENERAL_FORM_FEEDBACK_WEBHOOK_URL"
)

# pcweb urls.
REFLEX_URL = "https://reflex.dev/"
REFLEX_DOCS_URL = "https://reflex.dev/docs/getting-started/introduction/"
PYNECONE_URL = "https://pynecone.io"
REFLEX_CLOUD_URL = os.getenv("REFLEX_CLOUD_URL", "https://cloud.reflex.dev/")
REFLEX_BUILD_URL = os.getenv("REFLEX_BUILD_URL", "https://build.reflex.dev/")

PIP_URL = "https://pypi.org/project/reflex"
GITHUB_URL = "https://github.com/reflex-dev/reflex"
OLD_GITHUB_URL = "https://github.com/pynecone-io/pynecone"
GITHUB_DISCUSSIONS_URL = "https://github.com/orgs/reflex-dev/discussions"
FORUM_URL = "https://forum.reflex.dev"
TWITTER_URL = "https://twitter.com/getreflex"
DISCORD_URL = "https://discord.gg/T5WSbC2YtQ"
CONTACT_URL = "mailto:contact@reflex.dev"
CHAT_APP_URL = "https://github.com/reflex-dev/reflex-chat"
LINKEDIN_URL = "https://www.linkedin.com/company/reflex-dev"
YC_URL = "https://www.ycombinator.com/companies/reflex"
ROADMAP_URL = "https://github.com/reflex-dev/reflex/issues/2727"
CONTRIBUTING_URL = "https://github.com/reflex-dev/reflex/blob/main/CONTRIBUTING.md"
REPORT_A_BUG_URL = "https://github.com/reflex-dev/reflex/issues/new?assignees=&labels=&projects=&template=bug_report.md&title="
FRAGMENT_COMPONENT_INFO_URL = "https://react.dev/reference/react/Fragment"
NOTION_HOSTING_URL = "https://www.notion.so/reflex-dev/Reflex-Hosting-Documentation-57a4dd55d6234858bbae0be75be79ce7?pvs=4"
NEXT_SCRIPT_URL = "https://nextjs.org/docs/app/api-reference/components/script"
GALLERY_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfB30hXB09CZ_H0Zi684w1y1zQSScyT3Qhd1mOUrAAIq9dj3Q/viewform?usp=sf_link"
NPMJS_URL = "https://www.npmjs.com/"
SPLINE_URL = "https://github.com/splinetool/react-spline"
ENTERPRISE_DOCS_URL = "https://enterprise.reflex.dev"
DATABRICKS_NOTION_URL = "https://reflex-dev.notion.site/reflex-x-databricks"
DEMO_VIDEO_URL = "https://www.youtube.com/watch?v=s-kr8v7827g"

# Install urls.
BUN_URL = "https://bun.sh"
NEXTJS_URL = "https://nextjs.org"
NODEJS_URL = "https://nodejs.org/en/"
POETRY_URL = "https://python-poetry.org/"
PIPENV_URL = "https://pipenv.pypa.io/en/latest/"
PIP_URL = "https://pypi.org/project/pip/"
VENV_URL = "https://docs.python.org/3/library/venv.html"
VIRTUALENV_URL = "https://virtualenv.pypa.io/en/latest/"
CONDA_URL = "https://conda.io/"
FASTAPI_URL = "https://fastapi.tiangolo.com"
PYTHON_STANDARD_LIBRARY = "https://docs.python.org/3/library/index.html"
PIP_DOCS = "https://pip.pypa.io/en/stable/installation/#supported-methods"
HOW_TO_INSTALL_PIP = "https://www.makeuseof.com/tag/install-pip-for-python/"
ANACONDA_URL = "https://docs.anaconda.com/free/navigator/"
ANACONDA_INSTALLATION = "https://docs.anaconda.com/free/anaconda/install/windows/"
ANACONDA_SETUP_ENVIRONMENT = "https://docs.anaconda.com/free/navigator/getting-started/#navigator-managing-environments"

# Cloudflare
SCREENSHOT_BUCKET = "https://pub-c14a5dcf674640a6b73fded32bad72ca.r2.dev/"

# Reflex Cloud Backend
RX_CLOUD_BACKEND = os.getenv("RX_CLOUD_BACKEND", "https://cloud-backend.reflex.dev/")
RX_BUILD_BACKEND = os.getenv("RX_BUILD_BACKEND", "https://build-backend.reflex.dev/")

# Stats
GITHUB_STARS = 23000
DISCORD_USERS = 7000
CONTRIBUTORS = 170

MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024
MAX_IMAGES_COUNT = 5

PROMPT_MAP = {
    "Use an Image": "Build an app from a reference image",
    "Chat App": "A chat app hooked up to an LLM",
    "Live Dashboard": "Live stream data on a real-time dashboard",
}

CONTRIBUTION_URL = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22"
BUGS_URL = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue"

SPLINE_SCENE_URL = "https://prod.spline.design/Br2ec3WwuRGxEuij/scene.splinecode"
SPLINE_RUNTIME_VERSION = "1.5.5"

REFLEX_DOMAIN_URL = "https://reflex.dev/"
REFLEX_DOMAIN = "reflex.dev"
TWITTER_CREATOR = "@getreflex"

# Posthog
POSTHOG_API_KEY = os.getenv("POSTHOG_API_KEY")

SLACK_DEMO_WEBHOOK_URL: str = os.environ.get("SLACK_DEMO_WEBHOOK_URL")