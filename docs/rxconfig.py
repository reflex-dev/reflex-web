import reflex as rx

class DocsConfig(rx.Config):
    pass


config = DocsConfig(
    app_name="docs",
    db_url="sqlite:///pynecone.db",
    env=rx.Env.DEV,
    tailwind={},
)
