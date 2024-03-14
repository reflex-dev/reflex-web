<div align="center">
<img src="https://raw.githubusercontent.com/reflex-dev/reflex/main/docs/images/reflex_dark.svg#gh-light-mode-only" alt="Reflex Logo" width="300px">
<img src="https://raw.githubusercontent.com/reflex-dev/reflex/main/docs/images/reflex_light.svg#gh-dark-mode-only" alt="Reflex Logo" width="300px">

<hr>

### **✨ Performant, customizable web apps in pure Python. Deploy in seconds. ✨**
[![PyPI version](https://badge.fury.io/py/reflex.svg)](https://badge.fury.io/py/reflex)
![tests](https://github.com/pynecone-io/pynecone/actions/workflows/integration.yml/badge.svg)
![versions](https://img.shields.io/pypi/pyversions/reflex.svg)
[![Documentation](https://img.shields.io/badge/Documentation%20-Introduction%20-%20%23007ec6)](https://reflex.dev/docs/getting-started/introduction/)
[![Discord](https://img.shields.io/discord/1029853095527727165?color=%237289da&label=Discord)](https://discord.gg/T5WSbC2YtQ)
</div>

# Overview

A public repository which contains the source code of the reflex.dev website.

- It's built with [Reflex](https://reflex.dev/), a framework to build web apps in pure Python.
- You can find everything related to Reflex at [reflex.dev](https://reflex.dev/).

## About Reflex

Reflex is a full-stack web framework that allows developers to build their app in pure Python, and deploy with a single command. Its open-source core framework ensures flexibility for projects of any scale. Explore the future of web development at [reflex.dev](https://reflex.dev/).

## Requirements

The only requirement is that you have installed `Python 3.8` or higher in your local machine.

## Setup Locally

1. Fork this repository by clicking on the `Fork` button on the top right.

2. Clone the forked repository to your local machine.

    ```bash 
    git clone https://github.com/<USERNAME>/reflex-web.git
    ```

3. Navigate to the project directory.

    ```bash
    cd reflex-web
    ```

4. Create a virtual environment.

    ```bash
    python3 -m venv venv
    ```

5. Activate the virtual environment.

    ```bash
    source venv/bin/activate
    ```

6. Install the dependencies.

    ```bash
    python -m pip install -r requirements.txt
    ```

7. Initialize the reflex project.

    ```bash
    reflex init
    ```

8. Run the project.

    ```bash
    reflex run
    ```

    *Open the browser and go to `http://localhost:3000/` to see the website.*

## Contributing

We welcome contributions of any size! Below are some good ways to get started in the Reflex community.

-   **Join Our Discord**: Our [Discord](https://discord.gg/T5WSbC2YtQ) is the best place to get help on your Reflex project and to discuss how you can contribute.
-   **GitHub Discussions**: A great way to talk about features you want added or things that are confusing/need clarification.
-   **GitHub Issues**: [Issues](https://github.com/reflex-dev/reflex/issues) are an excellent way to report bugs. Additionally, you can try and solve an existing issue and submit a PR.

We are actively looking for contributors, no matter your skill level or experience. To contribute check out [CONTIBUTING.md](https://github.com/reflex-dev/reflex-web/blob/main/CONTRIBUTING.md)

## License

Reflex is open-source and licensed under the [Apache License 2.0](LICENSE).