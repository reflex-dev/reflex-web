import pynecone as pc

config = pc.Config(
    port=3000,
    app_name="pcweb",
    db_url="sqlite:///pynecone.db",
    frontend_packages=[
        "react-confetti",
        "react-colorful",
        "react-copy-to-clipboard",
    ]
)
