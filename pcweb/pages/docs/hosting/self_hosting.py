import reflex as rx

from pcweb.templates.docpage import (
    doccode,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)


@docpage()
def self_hosting():
    from pcweb.pages.docs.getting_started import installation

    return rx.box(
        docheader("Self Hosting", first=True),
        doctext(
            "We recommend using ",
            rx.code("reflex deploy"),
            " but you can also host your apps yourself.",
        ),
        doctext(
            "Clone your code to a server and install the ",
            doclink("requirements", href=installation.path),
            ".",
        ),
        subheader("API URL"),
        doctext(
            "Edit your ",
            rx.code("rxconfig.py"),
            " file and set ",
            rx.code("api_url"),
            " to the publicly accessible IP address or hostname of your server, with the port ",
            rx.code(":8000"),
            " at the end. Setting this correctly is essential for the frontend to interact with the backend state.",
        ),
        doctext(
            "For example if your server is at app.example.com, your config would look like this:"
        ),
        doccode(
            """config = rx.Config(
    app_name="your_app_name",
    api_url="http://app.example.com:8000",
)
""",
        ),
        doctext(
            "It is also possible to set the environment variable ",
            rx.code("API_URL"),
            " at run time or export time to retain the default for local development.",
        ),
        subheader("Production Mode"),
        doctext("Then run your app in production mode:"),
        doccode("$ reflex run --env prod", language="bash"),
        doctext(
            " Production mode creates an optimized build of your app.",
            " By default, the static frontend of the app (HTML, Javascript, CSS) will be"
            " exposed on port ",
            rx.code("3000"),
            " and the backend (event handlers) will be listening on port ",
            rx.code("8000"),
            ".",
        ),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.box(
                    rx.alert_title("Reverse Proxy and Websockets"),
                    rx.alert_description(
                        "Because the backend uses websockets, some reverse proxy servers, ",
                        "like ",
                        rx.link(
                            "nginx",
                            href="https://nginx.org/en/docs/http/websocket.html",
                        ),
                        " or ",
                        rx.link(
                            "apache",
                            href="https://httpd.apache.org/docs/2.4/mod/mod_proxy.html#protoupgrade",
                        ),
                        ", must be configured to pass the ",
                        rx.code("Upgrade"),
                        " header to allow backend connectivity.",
                    ),
                ),
                status="warning",
            ),
        ),
        subheader("Exporting a Static Build"),
        doctext(
            "Exporting a static build of the frontend allows the app to be served ",
            "using a static hosting provider, like Netlify or Github Pages. Be sure ",
            rx.code("api_url"),
            " is set to an accessible backend URL when the frontend is exported.",
        ),
        doccode(
            """$ API_URL=http://app.example.com:8000 reflex export""",
            language="bash",
        ),
        doctext(
            "This will create a ",
            rx.code("frontend.zip"),
            " file with your app's minified HTML, Javascript, and CSS build that can be uploaded to your static hosting service.",
        ),
        doctext(
            "It also creates a ",
            rx.code("backend.zip"),
            " file with your app's backend python code to upload to your server and run.",
        ),
        doctext(
            "You can export only the frontend or backend by passing in the ",
            rx.code("--frontend-only"),
            " or ",
            rx.code("--backend-only"),
            " flags.",
        ),
        doctext(
            "It is also possible to export the components without zip it separate. To do this, use the ",
            rx.code("--no-zip"),
            " parameter. ",
            "This provides the frontend in the ",
            rx.code(".web/_static/"),
            " directory and the backend can be found in the root directory of the project. ",
        ),
        subheader("Reflex Container Service"),
        doctext(
            "Another option is to run your Reflex service in a container. ",
            "For this purpose, a ",
            rx.code("Dockerfile"),
            " and additional documentation is available in the Reflex project in the directory ",
            rx.code("docker-example"),
            ". ",
        ),
        doctext(
            "For the build of the container image it is necessary to edit the ",
            rx.code("rxconfig.py"),
            " and the add the ",
            rx.code("requirements.txt"),
            " to your project folder. The following changes are necessary in ",
            rx.code("rxconfig.py"),
            ":",
        ),
        doccode(
            """config = rx.Config(
    app_name="app",
    api_url="http://app.example.com:8000",
)
""",
        ),
        doctext(
            "Notice that the ",
            rx.code("api_url"),
            " should be set to the externally accessible hostname or IP, as the client browser must ",
            "be able to connect to it directly to establish interactivity.",
        ),
        doctext(
            "You can find the ",
            rx.code("requirements.txt"),
            " in the ",
            rx.code("docker-example"),
            " folder of the project too.",
        ),
        doctext(
            "The project structure should looks like this:",
        ),
        doccode(
            """hello
├── .web
├── assets
├── hello
│   ├── __init__.py
│   └── hello.py
├── rxconfig.py
├── Dockerfile
└── requirements.txt""",
            language="bash",
        ),
        doctext(
            "After all changes have been made, the container image can now be created as follows.",
        ),
        doccode(
            """$ docker build -t reflex-project:latest .""",
            language="bash",
        ),
        doctext(
            "Finally, you can start your Reflex container service as follows.",
        ),
        doccode(
            """$ docker run -d -p 3000:3000 -p 8000:8000 --name app reflex-project:latest""",
            language="bash",
        ),
    )
