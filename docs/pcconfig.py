import pynecone as pc


class DocsConfig(pc.Config):
    pass


config = DocsConfig(
    app_name="docs",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    tailwind={},
)
