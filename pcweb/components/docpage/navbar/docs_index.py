# This file was dynamically generated. DO NOT EDIT.

indexed_docs = [
  {
    "name": "Advanced Onboarding Code Structure",
    "parts": [
      "Advanced Onboarding",
      "Code Structure"
    ],
    "url": "docs/advanced-onboarding/code-structure",
    "description": "Project Structure (Advanced)\n\nApp Module\n\nReflex imports the main app module based on the  from the config, which **must define a module-level global named  as an instance of **.\n\nThe main app module is responsible for importing all other modules that make up the app and defining .\n\n**All other modules containing pages, state, and models MUST be imported by the main app module or package** for Reflex to include them in the compiled output.\n..."
  },
  {
    "name": "Advanced Onboarding How Reflex Works",
    "parts": [
      "Advanced Onboarding",
      "How Reflex Works"
    ],
    "url": "docs/advanced-onboarding/how-reflex-works",
    "description": "How Reflex Works\n\nWe'll use the following basic app that displays Github profile images as an example to explain the different parts of the architecture.\n\nThe Reflex Architecture\n\nFull-stack web apps are made up of a frontend and a backend. The frontend is the user interface, and is served as a web page that runs on the user's browser. The backend handles the logic and state management (such as databases and APIs), and is run on a server.\n\nIn traditional web development, these are usually two separate apps, and are often written in different frameworks or languages. For example, you may combine a Flask backend with a React frontend. With this approach, you have to maintain two separate apps and end up writing a lot of boilerplate code to connect the frontend and backend.\n..."
  },
  {
    "name": "Advanced Onboarding Configuration",
    "parts": [
      "Advanced Onboarding",
      "Configuration"
    ],
    "url": "docs/advanced-onboarding/configuration",
    "description": "Configuration\n\nReflex apps can be configured using a configuration file, environment variables, and command line arguments.\n\nConfiguration File\n\nRunning  will create an  file in your root directory.\nYou can pass keyword arguments to the  class to configure your app.\n\nFor example:\n..."
  },
  {
    "name": "UI Overview",
    "parts": [
      "UI",
      "Overview"
    ],
    "url": "docs/ui/overview",
    "description": "UI Overview\n\nComponents are the building blocks for your app's user interface (UI). They are the visual elements that make up your app, like buttons, text, and images.\n\nComponent Basics\n\nComponents are made up of children and props.\n\nLet's take a look at the  component.\n..."
  },
  {
    "name": "Database Tables",
    "parts": [
      "Database",
      "Tables"
    ],
    "url": "docs/database/tables",
    "description": "Tables\n\nTables are database objects that contain all the data in a database.\n\nIn tables, data is logically organized in a row-and-column format similar to a\nspreadsheet. Each row represents a unique record, and each column represents a\nfield in the record.\n\nCreating a Table\n..."
  },
  {
    "name": "Database Queries",
    "parts": [
      "Database",
      "Queries"
    ],
    "url": "docs/database/queries",
    "description": "Queries\n\nQueries are used to retrieve data from a database.\n\nA query is a request for information from a database table or combination of\ntables. A query can be used to retrieve data from a single table or multiple\ntables. A query can also be used to insert, update, or delete data from a table.\n\nSession\n..."
  },
  {
    "name": "Database Overview",
    "parts": [
      "Database",
      "Overview"
    ],
    "url": "docs/database/overview",
    "description": "Database\n\nReflex uses sqlmodel to provide a built-in ORM wrapping SQLAlchemy.\n\nThe examples on this page refer specifically to how Reflex uses various tools to\nexpose an integrated database interface.  Only basic use cases will be covered\nbelow, but you can refer to the\nsqlmodel tutorial\nfor more examples and information, just replace  with  and\n with\n..."
  },
  {
    "name": "Vars Var Operations",
    "parts": [
      "Vars",
      "Var Operations"
    ],
    "url": "docs/vars/var-operations",
    "description": "Var Operations\n\nVar operations transform the placeholder representation of the value on the\nfrontend and provide a way to perform basic operations on the Var without having\nto define a computed var.\n\nWithin your frontend components, you cannot use arbitrary Python functions on\nthe state vars. For example, the following code will **not work.**\n\nThis is because we compile the frontend to Javascript, but the value of\n..."
  },
  {
    "name": "Database Relationships",
    "parts": [
      "Database",
      "Relationships"
    ],
    "url": "docs/database/relationships",
    "description": "Relationships\n\nForeign key relationships are used to link two tables together. For example,\nthe  model may have a field, , with a foreign key of ,\nreferencing a  model. This would allow us to automatically query the  objects\nassociated with a user, or find the  object associated with a .\n\nTo establish bidirectional relationships a model must correctly set the\n keyword argument on the  to the relationship\nattribute in the _other_ model.\n..."
  },
  {
    "name": "Vars Custom Vars",
    "parts": [
      "Vars",
      "Custom Vars"
    ],
    "url": "docs/vars/custom-vars",
    "description": "Custom Vars\n\nAs mentioned in the vars page, Reflex vars must be JSON serializable.\n\nThis means we can support any Python primitive types, as well as lists, dicts, and tuples. However, you can also create more complex var types using dataclasses (recommended), TypedDict, or Pydantic models.\n\nDefining a Type\n\nIn this example, we will create a custom var type for storing translations using a dataclass.\n..."
  },
  {
    "name": "Vars Base Vars",
    "parts": [
      "Vars",
      "Base Vars"
    ],
    "url": "docs/vars/base-vars",
    "description": "Base Vars\n\nVars are any fields in your app that may change over time. A Var is directly\nrendered into the frontend of the app.\n\nBase vars are defined as fields in your State class.\n\nThey can have a preset default value. If you don't provide a default value, you\nmust provide a type annotation.\n..."
  },
  {
    "name": "Enterprise Components",
    "parts": [
      "Enterprise",
      "Components"
    ],
    "url": "docs/enterprise/components",
    "description": "---\ntitle: Enterprise Components\n---"
  },
  {
    "name": "Vars Computed Vars",
    "parts": [
      "Vars",
      "Computed Vars"
    ],
    "url": "docs/vars/computed-vars",
    "description": "Computed Vars\n\nComputed vars have values derived from other properties on the backend. They are\ndefined as methods in your State class with the  decorator. A computed\nvar is recomputed every time an event is processed in your app.\n\nTry typing in the input box and clicking out.\n\nHere,  is a computed var that always holds the upper case version of .\n..."
  },
  {
    "name": "Enterprise Overview",
    "parts": [
      "Enterprise",
      "Overview"
    ],
    "url": "docs/enterprise/overview",
    "description": "---\ntitle: Reflex Enterprise\n---\n\nReflex Enterprise\n\nReflex Enterprise is a package containing paid features built on top of Reflex.\n\nInstallation\n..."
  },
  {
    "name": "Enterprise Built With Reflex",
    "parts": [
      "Enterprise",
      "Built With Reflex"
    ],
    "url": "docs/enterprise/built-with-reflex",
    "description": "Built with Reflex Badge\n\nThe \"Built with Reflex\" badge appears in the bottom right corner of apps using reflex-enterprise components.\n\nRemoving the Badge\n\nTo remove the badge, you need a paid tier:\n- **Cloud**: Pro tier or higher\n- **Self-hosted**: Team tier or higher\n..."
  },
  {
    "name": "Enterprise Drag And Drop",
    "parts": [
      "Enterprise",
      "Drag And Drop"
    ],
    "url": "docs/enterprise/drag-and-drop",
    "description": "---\ntitle: Drag and Drop\n---\n\nDrag and Drop\n\nReflex Enterprise provides comprehensive drag and drop functionality for creating interactive UI elements using the  module. Built on top of react-dnd, it offers both high-level components for common use cases and low-level hooks for advanced scenarios.\n\nBasic Usage\n..."
  },
  {
    "name": "Enterprise Ag Chart",
    "parts": [
      "Enterprise",
      "Ag Chart"
    ],
    "url": "docs/enterprise/ag-chart",
    "description": "AG Chart\n\nAG Chart is a powerful charting library that provides interactive charts and data visualization components for enterprise applications.\n\nFor more detailed documentation, see the AG Chart Documentation."
  },
  {
    "name": "Enterprise Mantine Semi Circle Progress",
    "parts": [
      "Enterprise",
      "Mantine",
      "Semi Circle Progress"
    ],
    "url": "docs/enterprise/mantine/semi-circle-progress",
    "description": "---\ntitle: Semi Circle Progress\n---\n\nSemi Circle Progress component\n is a component for displaying progress in a semi-circular format. It is useful for visualizing completion percentages or other metrics in a compact and visually appealing way."
  },
  {
    "name": "Enterprise Single Port Proxy",
    "parts": [
      "Enterprise",
      "Single Port Proxy"
    ],
    "url": "docs/enterprise/single-port-proxy",
    "description": "Single Port Proxy\n\nEnable single-port deployment by proxying the backend to the frontend port.\n\nConfiguration\n\nThis allows your application to run on a single port, which is useful for deployment scenarios where you can only expose one port."
  },
  {
    "name": "Enterprise Mantine Autocomplete",
    "parts": [
      "Enterprise",
      "Mantine",
      "Autocomplete"
    ],
    "url": "docs/enterprise/mantine/autocomplete",
    "description": "---\ntitle: Autocomplete\n---\n\nAutocomplete component\n\n is a component for providing suggestions as the user types. It is useful for enhancing user experience by offering relevant options based on input."
  },
  {
    "name": "Enterprise Mantine Timeline",
    "parts": [
      "Enterprise",
      "Mantine",
      "Timeline"
    ],
    "url": "docs/enterprise/mantine/timeline",
    "description": "---\ntitle: Timeline\n---\n\nTimeline component\n is a component for displaying a sequence of events or milestones in a linear format. It is useful for visualizing progress, history, or any sequential information."
  },
  {
    "name": "Enterprise Mantine Pill",
    "parts": [
      "Enterprise",
      "Mantine",
      "Pill"
    ],
    "url": "docs/enterprise/mantine/pill",
    "description": "---\ntitle: Pill\n---\n\nPill\n\n is a wrapping of the mantine component Pill. It is a simple component that can be used to display a small piece of information, such as a tag or a label. It can be used in various contexts, such as in a list of tags or labels, or as a standalone component.\n\nPill Group\n allows grouping multiple  components together, with a predefined layout.\n..."
  },
  {
    "name": "Enterprise Mantine Index",
    "parts": [
      "Enterprise",
      "Mantine",
      "Index"
    ],
    "url": "docs/enterprise/mantine/index",
    "description": "---\ntitle: Mantine\norder: 4\n---\n\nMantine\n\nMantine is a React component library that provides a set of high-quality components and hooks for building modern web applications. It is designed to be flexible, customizable, and easy to use, making it a popular choice among developers.\n\nSome of those components have been integrated into Reflex Enterprise, allowing you to use them in your Reflex applications. The following components are available:\n..."
  },
  {
    "name": "Enterprise Mantine Spoiler",
    "parts": [
      "Enterprise",
      "Mantine",
      "Spoiler"
    ],
    "url": "docs/enterprise/mantine/spoiler",
    "description": "---\ntitle: Spoiler\n---\n\nSpoiler component\n\n is a component that allows you to hide or reveal content. It is useful for displaying additional information or details that may not be immediately relevant to the user."
  },
  {
    "name": "Enterprise Mantine Tags Input",
    "parts": [
      "Enterprise",
      "Mantine",
      "Tags Input"
    ],
    "url": "docs/enterprise/mantine/tags-input",
    "description": "---\ntitle: TagsInput\n---\n\nTagsInput\n\n is a wrapping of the mantine component TagsInput. It is an utility component that can be used to display a list of tags or labels. It can be used in various contexts, such as in a form or as a standalone component.\n\nBasic Example\n..."
  },
  {
    "name": "Enterprise Mantine Number Formatter",
    "parts": [
      "Enterprise",
      "Mantine",
      "Number Formatter"
    ],
    "url": "docs/enterprise/mantine/number-formatter",
    "description": "---\ntitle: Number Formatter\n---\n\nNumber Formatter component\n is a component for formatting numbers in a user-friendly way. It allows you to specify the format, precision, and other options for displaying numbers."
  },
  {
    "name": "Enterprise Mantine Ring Progress",
    "parts": [
      "Enterprise",
      "Mantine",
      "Ring Progress"
    ],
    "url": "docs/enterprise/mantine/ring-progress",
    "description": "---\ntitle: Ring Progress\n---\n\nRing Progress component\n\n is a component for displaying progress in a circular format. It is useful for visualizing completion percentages or other metrics in a compact and visually appealing way."
  },
  {
    "name": "Enterprise Mantine Multi Select",
    "parts": [
      "Enterprise",
      "Mantine",
      "Multi Select"
    ],
    "url": "docs/enterprise/mantine/multi-select",
    "description": "---\ntitle: MultiSelect\n---\n\nMultiSelect component\n\n is a component for selecting multiple options from a list. It allows users to choose one or more items, making it suitable for scenarios where multiple selections are required."
  },
  {
    "name": "Enterprise Mantine Combobox",
    "parts": [
      "Enterprise",
      "Mantine",
      "Combobox"
    ],
    "url": "docs/enterprise/mantine/combobox",
    "description": "---\ntitle: Combobox\n---\n\nCombobox\n\n is a wrapping of the mantine component Combobox. It is a simple component that can be used to display a list of options, and allows the user to select one or more options from the list. It can be used in various contexts, such as in a form or as a standalone component."
  },
  {
    "name": "Enterprise Mantine JSON Input",
    "parts": [
      "Enterprise",
      "Mantine",
      "JSON Input"
    ],
    "url": "docs/enterprise/mantine/json-input",
    "description": "---\ntitle: JSON Input\n---\n\nJSON Input\n\n is a component that allows you to input JSON data in a user-friendly way. It provides validation and formatting features to ensure that the JSON data is correctly structured.\n\nExample"
  },
  {
    "name": "Enterprise Mantine Tree",
    "parts": [
      "Enterprise",
      "Mantine",
      "Tree"
    ],
    "url": "docs/enterprise/mantine/tree",
    "description": "---\ntitle: Tree\n---\n\nTree component\n\n is a component for displaying hierarchical data in a tree structure. It allows users to expand and collapse nodes, making it easy to navigate through large datasets."
  },
  {
    "name": "Enterprise Mantine Collapse",
    "parts": [
      "Enterprise",
      "Mantine",
      "Collapse"
    ],
    "url": "docs/enterprise/mantine/collapse",
    "description": "---\ntitle: Collapse\n---\n\nCollapse component\n\n is a component that allows you to create collapsible sections in your application. It is useful for hiding or showing content based on user interaction, such as clicking a button or a link."
  },
  {
    "name": "Enterprise Mantine Loading Overlay",
    "parts": [
      "Enterprise",
      "Mantine",
      "Loading Overlay"
    ],
    "url": "docs/enterprise/mantine/loading-overlay",
    "description": "---\ntitle: Loading Overlay\n---\n\nLoading Overlay component\n is a component that displays a loading overlay on top of its children. It is useful for indicating that a process is ongoing and prevents user interaction with the underlying content."
  },
  {
    "name": "Enterprise Ag Grid Value Transformers",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Value Transformers"
    ],
    "url": "docs/enterprise/ag-grid/value-transformers",
    "description": "---\norder: 2\n---\n\nValue Transformers\n\nAgGrid allow you to apply transformers based on the column of your grid. This allow you to perform operations on the data before displaying it on the grid, without having to pre-process the data on the backend, reducing the load on your application.\n\nTOC:\n- Value Getter\n..."
  },
  {
    "name": "Enterprise Ag Grid Model Wrapper",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Model Wrapper"
    ],
    "url": "docs/enterprise/ag-grid/model-wrapper",
    "description": "---\norder: 6\n---\n\nModel Wrapper\n\nA model wrapper is an utility used to wrap a database model and provide a consistent interface over it. It allows automatically adding new rows to the database, updating existing rows, and deleting rows.\n\nDefault Model Wrapper\n..."
  },
  {
    "name": "Enterprise Map Index",
    "parts": [
      "Enterprise",
      "Map",
      "Index"
    ],
    "url": "docs/enterprise/map/index",
    "description": "---\ntitle: Interactive Maps\n---\n\nInteractive Maps\n\nThe map components in Reflex Enterprise provide interactive mapping capabilities built on top of **Leaflet**, one of the most popular open-source JavaScript mapping libraries. These components enable you to create rich, interactive maps with markers, layers, controls, and event handling.\n\n🌍 **View Live Demo** - See the map components in action with interactive examples.\n..."
  },
  {
    "name": "Enterprise Ag Grid Aligned Grids",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Aligned Grids"
    ],
    "url": "docs/enterprise/ag-grid/aligned-grids",
    "description": "---\ntitle: Aligned Grids\n---\n\nAgGrid provides a way to align multiple grids together. This is useful when you want to display related data in a synchronized manner.\n\nYou can do so through the  prop. This prop takes a list of grid IDs that you want to align."
  },
  {
    "name": "Enterprise Ag Grid Pivot Mode",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Pivot Mode"
    ],
    "url": "docs/enterprise/ag-grid/pivot-mode",
    "description": "Pivot Mode\n\nPivot mode allows you to visualize your data in a different way than how they are originally structured in the data source. When pivoting on a column, the values in that column will be used as column headers. This allows you to see the data in a more compact way, and can be useful when you have a lot of data to display.\n\nTo enable pivot mode, set the  property to  in the grid props. Once pivot mode is enabled, you can define which column to pivot on by setting the  property in a column definition. In addition to the pivot column, at least one column definition must have  property set to  to define the row grouping.\n\nYou can also define how rows are aggregated by passing the  property in the column definition. The  property should be set to a string that represents the aggregation function to use. The built-in aggregation functions are , , , , , , and .\n\nYou can find a live example here: Pivot Mode Example.\n..."
  },
  {
    "name": "Enterprise Ag Grid Index",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Index"
    ],
    "url": "docs/enterprise/ag-grid/index",
    "description": "---\ntitle: \"AgGrid Overview\"\norder: 3\n---\n\nAG Grid\n\nAG Grid Features\n\nYour First Reflex AG Grid\n..."
  },
  {
    "name": "Enterprise Ag Grid Theme",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Theme"
    ],
    "url": "docs/enterprise/ag-grid/theme",
    "description": "---\norder: 3\n---\n\nThemes\n\nYou can style your grid with a theme. AG Grid includes the following themes:\n\n1. \n2.\n..."
  },
  {
    "name": "Enterprise Ag Grid Column Defs",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Column Defs"
    ],
    "url": "docs/enterprise/ag-grid/column-defs",
    "description": "---\norder: 1\n---\n\nColumn Definitions\n\nBasic Columns\n\nAgGrid allows you to define the columns of your grid, passed to the prop . Each dictionary represents a column.\n..."
  },
  {
    "name": "API Reference Browser Storage",
    "parts": [
      "API Reference",
      "Browser Storage"
    ],
    "url": "docs/api-reference/browser-storage",
    "description": "Browser Storage\n\nrx.Cookie\n\nRepresents a state Var that is stored as a cookie in the browser. Currently only supports string values.\n\nParameters\n\n-  : The name of the cookie on the client side.\n- : The cookie path. Use  to make the cookie accessible on all pages.\n..."
  },
  {
    "name": "API Reference Utils",
    "parts": [
      "API Reference",
      "Utils"
    ],
    "url": "docs/api-reference/utils",
    "description": "Utility Functions\n\nReflex provides utility functions to help with common tasks in your applications.\n\nrun_in_thread\n\nThe  function allows you to run a **non-async** function in a separate thread, which is useful for preventing long-running operations from blocking the UI event queue.\n\nParameters\n..."
  },
  {
    "name": "API Reference Var System",
    "parts": [
      "API Reference",
      "Var System"
    ],
    "url": "docs/api-reference/var-system",
    "description": "Reflex's Var System\n\nMotivation\n\nReflex supports some basic operations in state variables on the frontend.\nReflex automatically converts variable operations from Python into a JavaScript equivalent.\n\nHere's an example of a Reflex conditional in Python that returns \"Pass\" if the threshold is equal to or greater than 50 and \"Fail\" otherwise:\n\n The conditional to roughly the following in Javascript:\n..."
  },
  {
    "name": "API Reference CLI",
    "parts": [
      "API Reference",
      "CLI"
    ],
    "url": "docs/api-reference/cli",
    "description": "CLI\n\nThe  command line interface (CLI) is a tool for creating and managing Reflex apps.\n\nTo see a list of all available commands, run .\n\nInit\n\nThe  command creates a new Reflex app in the current directory.\nIf an  file already exists already, it will re-initialize the app with the latest template.\n..."
  },
  {
    "name": "API Reference Special Events",
    "parts": [
      "API Reference",
      "Special Events"
    ],
    "url": "docs/api-reference/special-events",
    "description": "Special Events\n\nReflex includes a set of built-in special events that can be utilized as event triggers\nor returned from event handlers in your applications. These events enhance interactivity and user experience.\nBelow are the special events available in Reflex, along with explanations of their functionality:\n\nrx.console_log\n\nPerform a console.log in the browser's console.\n..."
  },
  {
    "name": "API Reference Plugins",
    "parts": [
      "API Reference",
      "Plugins"
    ],
    "url": "docs/api-reference/plugins",
    "description": "Plugins\n\nReflex supports a plugin system that allows you to extend the framework's functionality during the compilation process. Plugins can add frontend dependencies, modify build configurations, generate static assets, and perform custom tasks before compilation.\n\nConfiguring Plugins\n\nPlugins are configured in your  file using the  parameter:\n\nBuilt-in Plugins\n..."
  },
  {
    "name": "API Reference Browser Javascript",
    "parts": [
      "API Reference",
      "Browser Javascript"
    ],
    "url": "docs/api-reference/browser-javascript",
    "description": "Browser Javascript\n\nReflex compiles your frontend code, defined as python functions, into a Javascript web application\nthat runs in the user's browser. There are instances where you may need to supply custom javascript\ncode to interop with Web APIs, use certain third-party libraries, or wrap low-level functionality\nthat is not exposed via Reflex's Python API.\n\nExecuting Script\n\nThere are four ways to execute custom Javascript code into your Reflex app:\n..."
  },
  {
    "name": "API Reference Event Triggers",
    "parts": [
      "API Reference",
      "Event Triggers"
    ],
    "url": "docs/api-reference/event-triggers",
    "description": "Event Triggers\n\nComponents can modify the state based on user events such as clicking a button or entering text in a field.\nThese events are triggered by event triggers.\n\nEvent triggers are component specific and are listed in the documentation for each component.\n\nComponent Lifecycle Events\n\nReflex components have lifecycle events like  and  that allow you to execute code at specific points in a component's existence. These events are crucial for initializing data, cleaning up resources, and creating dynamic user interfaces.\n..."
  },
  {
    "name": "Custom Components Command Reference",
    "parts": [
      "Custom Components",
      "Command Reference"
    ],
    "url": "docs/custom-components/command-reference",
    "description": "Command Reference\n\nThe custom component commands are under  subcommand. To see the list of available commands, run . To see the manual on a specific command, run , for example, .\n\nreflex component init\n\nBelow is an example of running the  command.\n\nThe  command uses the current enclosing folder name to construct a python package name, typically in the kebab case. For example, if running init in folder , the package name will be . The added prefix reduces the chance of name collision on PyPI (the Python Package Index), and it indicates that the package is a Reflex custom component. The user can override the package name by providing the  option.\n..."
  },
  {
    "name": "Custom Components Overview",
    "parts": [
      "Custom Components",
      "Overview"
    ],
    "url": "docs/custom-components/overview",
    "description": "Custom Components Overview\n\nReflex users create many components of their own: ready to use high level components, or nicely wrapped React components. With **Custom Components**, the community can easily share these components now.\n\nRelease **0.4.3** introduces a series of  commands that help developers wrap react components, test, and publish them as python packages. As shown in the image below, there are already a few custom components published on PyPI, such as , .\n\nCheck out the custom components gallery here.\n\nPrerequisites for Publishing\n..."
  },
  {
    "name": "Custom Components Prerequisites For Publishing",
    "parts": [
      "Custom Components",
      "Prerequisites For Publishing"
    ],
    "url": "docs/custom-components/prerequisites-for-publishing",
    "description": "Python Package Index\n\nIn order to publish a Python package, you need to use a publishing utility. Any would work, but we recommend either Twine or (uv)[https://docs.astral.sh/uv/guides/package/#publishing-your-package].\n\nPyPI\n\nIt is straightforward to create accounts and API tokens with PyPI. There is official help on the PyPI website. For a quick reference here, go to the top right corner of the PyPI website and look for the button to register and fill out personal information.\n\nA user can use username and password to authenticate with PyPI when publishing.\n..."
  },
  {
    "name": "Library Disclosure Accordion",
    "parts": [
      "Library",
      "Disclosure",
      "Accordion"
    ],
    "url": "docs/library/disclosure/accordion",
    "description": "---\ncomponents:\n  - rx.accordion.root\n  - rx.accordion.item\n\nAccordionRoot: |\n  lambda **props: rx.accordion.root(\n      rx.accordion.item(header=\"First Item\", content=\"The first accordion item's content\"),\n      rx.accordion.item(\n          header=\"Second Item\", content=\"The second accordion item's content\",\n..."
  },
  {
    "name": "Library Disclosure Segmented Control",
    "parts": [
      "Library",
      "Disclosure",
      "Segmented Control"
    ],
    "url": "docs/library/disclosure/segmented-control",
    "description": "---\ncomponents:\n    - rx.segmented_control.root\n    - rx.segmented_control.item\n---\n\nSegmented Control\n\nSegmented Control offers a clear and accessible way to switch between predefined values and views, e.g., \"Inbox,\" \"Drafts,\" and \"Sent.\"\n..."
  },
  {
    "name": "Library Disclosure Tabs",
    "parts": [
      "Library",
      "Disclosure",
      "Tabs"
    ],
    "url": "docs/library/disclosure/tabs",
    "description": "---\ncomponents:\n  - rx.tabs.root\n  - rx.tabs.list\n  - rx.tabs.trigger\n  - rx.tabs.content\n\nonly_low_level:\n  - True\n..."
  },
  {
    "name": "Library Forms Input",
    "parts": [
      "Library",
      "Forms",
      "Input"
    ],
    "url": "docs/library/forms/input",
    "description": "---\ncomponents:\n  - rx.input\n  - rx.input.slot\n\nInput: |\n  lambda **props: rx.input(placeholder=\"Search the docs\", **props)\n\nTextFieldSlot: |\n  lambda **props: rx.input(\n..."
  },
  {
    "name": "Library Forms Slider",
    "parts": [
      "Library",
      "Forms",
      "Slider"
    ],
    "url": "docs/library/forms/slider",
    "description": "---\ncomponents:\n  - rx.slider\n\nSlider: |\n  lambda **props: rx.center(rx.slider(default_value=40, height=\"100%\", **props), height=\"4em\", width=\"100%\")\n---\n\nSlider\n..."
  },
  {
    "name": "Library Forms Form",
    "parts": [
      "Library",
      "Forms",
      "Form"
    ],
    "url": "docs/library/forms/form",
    "description": "---\ncomponents:\n  - rx.form\n  - rx.form.root\n  - rx.form.field\n  - rx.form.control\n  - rx.form.label\n  - rx.form.message\n  - rx.form.submit\n..."
  },
  {
    "name": "Library Forms Checkbox",
    "parts": [
      "Library",
      "Forms",
      "Checkbox"
    ],
    "url": "docs/library/forms/checkbox",
    "description": "---\ncomponents:\n  - rx.checkbox\n\nHighLevelCheckbox: |\n  lambda **props: rx.checkbox(\"Basic Checkbox\", **props)\n---\n\nCheckbox\n..."
  },
  {
    "name": "Library Forms Button",
    "parts": [
      "Library",
      "Forms",
      "Button"
    ],
    "url": "docs/library/forms/button",
    "description": "---\ncomponents:\n  - rx.button\n\nButton: |\n  lambda **props: rx.button(\"Basic Button\", **props)\n---\n\nButton\n..."
  },
  {
    "name": "Library Forms Select",
    "parts": [
      "Library",
      "Forms",
      "Select"
    ],
    "url": "docs/library/forms/select",
    "description": "---\ncomponents:\n  - rx.select\n  - rx.select.root\n  - rx.select.trigger\n  - rx.select.content\n  - rx.select.group\n  - rx.select.item\n  - rx.select.label\n  - rx.select.separator\n..."
  },
  {
    "name": "Library Forms Text Area",
    "parts": [
      "Library",
      "Forms",
      "Text Area"
    ],
    "url": "docs/library/forms/text-area",
    "description": "---\ncomponents:\n  - rx.text_area\n\nTextArea: |\n  lambda **props: rx.text_area(**props)\n---\n\nText Area\n..."
  },
  {
    "name": "Library Forms Switch",
    "parts": [
      "Library",
      "Forms",
      "Switch"
    ],
    "url": "docs/library/forms/switch",
    "description": "---\ncomponents:\n  - rx.switch\n\nSwitch: |\n  lambda **props: rx.switch(**props)\n---\n\nSwitch\n..."
  },
  {
    "name": "Library Forms Radio Group",
    "parts": [
      "Library",
      "Forms",
      "Radio Group"
    ],
    "url": "docs/library/forms/radio-group",
    "description": "---\ncomponents:\n  - rx.radio_group\n  - rx.radio_group.root\n  - rx.radio_group.item\n\nHighLevelRadioGroup: |\n  lambda **props: rx.radio_group([\"1\", \"2\", \"3\", \"4\", \"5\"], **props)\n\nRadioGroupRoot: |\n..."
  },
  {
    "name": "Library Forms Upload",
    "parts": [
      "Library",
      "Forms",
      "Upload"
    ],
    "url": "docs/library/forms/upload",
    "description": "---\ncomponents:\n  - rx.upload\n  - rx.upload.root\n\nUpload: |\n  lambda **props: rx.center(rx.upload(id=\"my_upload\", **props))\n---\n\nFile Upload\n..."
  },
  {
    "name": "Library Tables And Data Grids Data Table",
    "parts": [
      "Library",
      "Tables And Data Grids",
      "Data Table"
    ],
    "url": "docs/library/tables-and-data-grids/data-table",
    "description": "---\ncomponents:\n    - rx.data_table\n---\n\nData Table\n\nThe data table component is a great way to display static data in a table format.\nYou can pass in a pandas dataframe to the data prop to create the table.\n..."
  },
  {
    "name": "Library Forms Select Low Level",
    "parts": [
      "Library",
      "Forms",
      "Low Level"
    ],
    "url": "docs/library/forms/select/low",
    "description": "---\ncomponents:\n  - rx.select\n  - rx.select.root\n  - rx.select.trigger\n  - rx.select.content\n  - rx.select.group\n  - rx.select.item\n  - rx.select.label\n  - rx.select.separator\n..."
  },
  {
    "name": "Library Forms Form Low Level",
    "parts": [
      "Library",
      "Forms",
      "Low Level"
    ],
    "url": "docs/library/forms/form/low",
    "description": "---\ncomponents:\n  - rx.form.root\n  - rx.form.field\n  - rx.form.control\n  - rx.form.label\n  - rx.form.message\n  - rx.form.submit\n\nFormRoot: |\n..."
  },
  {
    "name": "Library Forms Input Low Level",
    "parts": [
      "Library",
      "Forms",
      "Low Level"
    ],
    "url": "docs/library/forms/input/low",
    "description": "---\ncomponents:\n    - rx.input\n    - rx.input.slot\n---\n\nInput\n\nA text field is an input field that users can type into. This component uses Radix's text field component.\n..."
  },
  {
    "name": "Library Layout Stack",
    "parts": [
      "Library",
      "Layout",
      "Stack"
    ],
    "url": "docs/library/layout/stack",
    "description": "---\ncomponents:\n    - rx.stack\n    - rx.hstack\n    - rx.vstack\nStack: |\n    lambda **props: rx.stack(\n        rx.card(\"Card 1\", size=\"2\"), rx.card(\"Card 2\", size=\"2\"), rx.card(\"Card 3\", size=\"2\"),\n        width=\"100%\",\n        height=\"20vh\",\n..."
  },
  {
    "name": "Library Tables And Data Grids Data Editor",
    "parts": [
      "Library",
      "Tables And Data Grids",
      "Data Editor"
    ],
    "url": "docs/library/tables-and-data-grids/data-editor",
    "description": "---\ncomponents:\n    - rx.data_editor\n---\n\nData Editor\n\nA datagrid editor based on Glide Data Grid\n\nThis component is introduced as an alternative to the datatable to support editing the displayed data.\n..."
  },
  {
    "name": "Library Layout Card",
    "parts": [
      "Library",
      "Layout",
      "Card"
    ],
    "url": "docs/library/layout/card",
    "description": "---\ncomponents:\n  - rx.card\n\nCard: |\n    lambda **props: rx.card(\"Basic Card \", **props)\n---\n\nCard\n..."
  },
  {
    "name": "Library Tables And Data Grids Table",
    "parts": [
      "Library",
      "Tables And Data Grids",
      "Table"
    ],
    "url": "docs/library/tables-and-data-grids/table",
    "description": "---\ncomponents:\n  - rx.table.root\n  - rx.table.header\n  - rx.table.row\n  - rx.table.column_header_cell\n  - rx.table.body\n  - rx.table.cell\n  - rx.table.row_header_cell\n..."
  },
  {
    "name": "Library Layout Container",
    "parts": [
      "Library",
      "Layout",
      "Container"
    ],
    "url": "docs/library/layout/container",
    "description": "---\ncomponents:\n  - rx.container\n---\n\nContainer\n\nConstrains the maximum width of page content, while keeping flexible margins\nfor responsive layouts.\n..."
  },
  {
    "name": "Library Layout Fragment",
    "parts": [
      "Library",
      "Layout",
      "Fragment"
    ],
    "url": "docs/library/layout/fragment",
    "description": "---\ncomponents:\n    - rx.fragment\n---\n\nFragment\n\nA Fragment is a Component that allow you to group multiple Components without a wrapper node.\n\nRefer to the React docs at React/Fragment for more information on its use-case.\n..."
  },
  {
    "name": "Library Layout Flex",
    "parts": [
      "Library",
      "Layout",
      "Flex"
    ],
    "url": "docs/library/layout/flex",
    "description": "---\ncomponents:\n  - rx.flex\n---\n\nFlex\n\nThe Flex component is used to make flexbox layouts.\nIt makes it simple to arrange  child components in horizontal or vertical directions, apply wrapping,\njustify and align  content, and automatically size components based on available space, making it\n..."
  },
  {
    "name": "Library Layout Aspect Ratio",
    "parts": [
      "Library",
      "Layout",
      "Aspect Ratio"
    ],
    "url": "docs/library/layout/aspect-ratio",
    "description": "---\ncomponents:\n  - rx.aspect_ratio\n---\n\nAspect Ratio\n\nDisplays content with a desired ratio.\n\nBasic Example\n..."
  },
  {
    "name": "Library Layout Box",
    "parts": [
      "Library",
      "Layout",
      "Box"
    ],
    "url": "docs/library/layout/box",
    "description": "---\ncomponents:\n  - rx.box\n---\n\nBox\n\nBox is a generic container component that can be used to group other components.\n\nBy default, the Box component is based on the  and rendered as a block element. It's primary use is for applying styles.\n..."
  },
  {
    "name": "Library Layout Separator",
    "parts": [
      "Library",
      "Layout",
      "Separator"
    ],
    "url": "docs/library/layout/separator",
    "description": "---\ncomponents:\n    - rx.separator\nSeparator: |\n    lambda **props: rx.separator(**props)\n\n---\n\nSeparator\n..."
  },
  {
    "name": "Library Layout Grid",
    "parts": [
      "Library",
      "Layout",
      "Grid"
    ],
    "url": "docs/library/layout/grid",
    "description": "---\ncomponents:\n  - rx.grid\n---\n\nGrid\n\nComponent for creating grid layouts. Either  or  may be specified.\n\nBasic Example\n..."
  },
  {
    "name": "Library Layout Inset",
    "parts": [
      "Library",
      "Layout",
      "Inset"
    ],
    "url": "docs/library/layout/inset",
    "description": "---\ncomponents:\n    - rx.inset\n\nInset: |\n    lambda **props: rx.card(\n        rx.inset(\n            rx.image(src=\"/reflex_banner.png\", height=\"auto\"),\n            **props,\n        ),\n..."
  },
  {
    "name": "Library Layout Section",
    "parts": [
      "Library",
      "Layout",
      "Section"
    ],
    "url": "docs/library/layout/section",
    "description": "---\ncomponents:\n  - rx.section\n---\n\nSection\n\nDenotes a section of page content, providing vertical padding by default.\n\nPrimarily this is a semantic component that is used to group related textual content.\n..."
  },
  {
    "name": "Library Layout Spacer",
    "parts": [
      "Library",
      "Layout",
      "Spacer"
    ],
    "url": "docs/library/layout/spacer",
    "description": "---\ncomponents:\n    - rx.spacer\n---\n\nSpacer\n\nCreates an adjustable, empty space that can be used to tune the spacing between child elements within .\n\nAs ,  and  are all built from , it is possible to also use  inside of these components.\n..."
  },
  {
    "name": "Library Layout Center",
    "parts": [
      "Library",
      "Layout",
      "Center"
    ],
    "url": "docs/library/layout/center",
    "description": "---\ncomponents:\n    - rx.center\n---\n\nCenter\n\n is a component that centers its children within itself. It is based on the  component and therefore inherits all of its props."
  },
  {
    "name": "Library Other Html Embed",
    "parts": [
      "Library",
      "Other",
      "Html Embed"
    ],
    "url": "docs/library/other/html-embed",
    "description": "---\ncomponents:\n    - rx.html\n---\n\nHTML Embed\n\nThe HTML component can be used to render raw HTML code.\n\nBefore you reach for this component, consider using Reflex's raw HTML element support instead.\n..."
  },
  {
    "name": "Library Other Script",
    "parts": [
      "Library",
      "Other",
      "Script"
    ],
    "url": "docs/library/other/script",
    "description": "---\ncomponents:\n    - rx.script\n---\n\nScript\n\nThe Script component can be used to include inline javascript or javascript files by URL.\n\nIt uses the  component to inject the script and can be safely used with conditional rendering to allow script side effects to be controlled by the state.\n..."
  },
  {
    "name": "Library Other Clipboard",
    "parts": [
      "Library",
      "Other",
      "Clipboard"
    ],
    "url": "docs/library/other/clipboard",
    "description": "---\ncomponents:\n  - rx.clipboard\n---\n\nClipboard\n\n_New in 0.5.6_\n\nThe Clipboard component can be used to respond to paste events with complex data.\n..."
  },
  {
    "name": "Library Other Theme",
    "parts": [
      "Library",
      "Other",
      "Theme"
    ],
    "url": "docs/library/other/theme",
    "description": "---\n components:\n     - rx.theme\n     - rx.theme_panel\n---\n\nTheme\n\n The  component is used to change the theme of the application. The  can be set directly in the rx.App.\n..."
  },
  {
    "name": "Library Other Skeleton",
    "parts": [
      "Library",
      "Other",
      "Skeleton"
    ],
    "url": "docs/library/other/skeleton",
    "description": "---\ndescription: Skeleton, a loading placeholder component for content that is not yet available.\ncomponents:\n    - rx.skeleton\n---\n\nSkeleton (loading placeholder)\n\n is a loading placeholder component that serves as a visual placeholder while content is loading.\nIt is useful for maintaining the layout's structure and providing users with a sense of progression while awaiting the final content.\n..."
  },
  {
    "name": "Library Other Html",
    "parts": [
      "Library",
      "Other",
      "Html"
    ],
    "url": "docs/library/other/html",
    "description": "---\ncomponents:\n    - rx.el.A\n    - rx.el.Abbr\n    - rx.el.Address\n    - rx.el.Area\n    - rx.el.Article\n    - rx.el.Aside\n    - rx.el.Audio\n    - rx.el.B\n..."
  },
  {
    "name": "Library Other Memo",
    "parts": [
      "Library",
      "Other",
      "Memo"
    ],
    "url": "docs/library/other/memo",
    "description": "Memo\n\nThe  decorator is used to optimize component rendering by memoizing components that don't need to be re-rendered. This is particularly useful for expensive components that depend on specific props and don't need to be re-rendered when other state changes in your application.\n\nRequirements\n\nWhen using , you must follow these requirements:\n\n1. **Type all arguments**: All arguments to a memoized component must have type annotations.\n2. **Use keyword arguments**: When calling a memoized component, you must use keyword arguments (not positional arguments).\n..."
  },
  {
    "name": "Library Dynamic Rendering Foreach",
    "parts": [
      "Library",
      "Dynamic Rendering",
      "Foreach"
    ],
    "url": "docs/library/dynamic-rendering/foreach",
    "description": "Foreach\n\nThe  component takes an iterable(list, tuple or dict) and a function that renders each item in the list.\nThis is useful for dynamically rendering a list of items defined in a state.\n\nThe function can also take an index as a second argument.\n\nNested foreach components can be used to render nested lists.\n\nWhen indexing into a nested list, it's important to declare the list's type as Reflex requires it for type checking.\n..."
  },
  {
    "name": "Library Dynamic Rendering Match",
    "parts": [
      "Library",
      "Dynamic Rendering",
      "Match"
    ],
    "url": "docs/library/dynamic-rendering/match",
    "description": "Match\n\nThe  feature in Reflex serves as a powerful alternative to  for handling conditional statements.\nWhile  excels at conditionally rendering two components based on a single condition,\n extends this functionality by allowing developers to handle multiple conditions and their associated components.\nThis feature is especially valuable when dealing with intricate conditional logic or nested scenarios,\nwhere the limitations of  might lead to less readable and more complex code.\n\nWith , developers can not only handle multiple conditions but also perform structural pattern matching,\nmaking it a versatile tool for managing various scenarios in Reflex applications.\n..."
  },
  {
    "name": "Library Dynamic Rendering Cond",
    "parts": [
      "Library",
      "Dynamic Rendering",
      "Cond"
    ],
    "url": "docs/library/dynamic-rendering/cond",
    "description": "Cond\n\nThis component is used to conditionally render components.\n\nThe cond component takes a condition and two components.\nIf the condition is , the first component is rendered, otherwise the second component is rendered.\n\nThe second component is optional and can be omitted.\nIf it is omitted, nothing is rendered if the condition is .\n..."
  },
  {
    "name": "Library Data Display Callout Low Level",
    "parts": [
      "Library",
      "Data Display",
      "Low Level"
    ],
    "url": "docs/library/data-display/callout/low",
    "description": "---\ncomponents:\n    - rx.callout.root\n    - rx.callout.icon\n    - rx.callout.text\n---\n\nCallout\n\nA  is a short message to attract user's attention.\n..."
  },
  {
    "name": "Library Dynamic Rendering Auto Scroll",
    "parts": [
      "Library",
      "Dynamic Rendering",
      "Auto Scroll"
    ],
    "url": "docs/library/dynamic-rendering/auto-scroll",
    "description": "Auto Scroll\n\nThe  component is a div that automatically scrolls to the bottom when new content is added. This is useful for chat interfaces, logs, or any container where new content is dynamically added and you want to ensure the most recent content is visible.\n\nBasic Usage\n\nThe  component automatically scrolls to show the newest content when it's added. In this example, each time you click \"Add Message\", a new message is added to the list and the container automatically scrolls to display it.\n\nWhen to Use Auto Scroll\n..."
  },
  {
    "name": "Library Data Display Code Block",
    "parts": [
      "Library",
      "Data Display",
      "Code Block"
    ],
    "url": "docs/library/data-display/code-block",
    "description": "---\ncomponents:\n    - rx.code_block\n---\n\nCode Block\n\nThe Code Block component can be used to display code easily within a website.\nPut in a multiline string with the correct spacing and specify and language to show the desired code."
  },
  {
    "name": "Library Data Display Progress",
    "parts": [
      "Library",
      "Data Display",
      "Progress"
    ],
    "url": "docs/library/data-display/progress",
    "description": "---\ncomponents:\n    - rx.progress\n\nProgress: |\n    lambda **props: rx.progress(value=50, **props)\n---\n\nProgress\n..."
  },
  {
    "name": "Library Data Display Spinner",
    "parts": [
      "Library",
      "Data Display",
      "Spinner"
    ],
    "url": "docs/library/data-display/spinner",
    "description": "---\ncomponents:\n    - rx.spinner\n---\n\nSpinner\n\nSpinner is used to display an animated loading indicator when a task is in progress.\n\nBasic Examples\n..."
  },
  {
    "name": "Library Data Display Scroll Area",
    "parts": [
      "Library",
      "Data Display",
      "Scroll Area"
    ],
    "url": "docs/library/data-display/scroll-area",
    "description": "---\ncomponents:\n    - rx.scroll_area\n\nScrollArea: |\n    lambda **props: rx.scroll_area(\n        rx.flex(\n            rx.text(\n                \"\"\"Three fundamental aspects of typography are legibility, readability, and aesthetics. Although in a non-technical sense \"legible\" and \"readable\"are often used synonymously, typographically they are separate but related concepts.\"\"\",\n                size=\"5\",\n..."
  },
  {
    "name": "Library Data Display List",
    "parts": [
      "Library",
      "Data Display",
      "List"
    ],
    "url": "docs/library/data-display/list",
    "description": "---\ncomponents:\n    - rx.list.item\n    - rx.list.ordered\n    - rx.list.unordered\n---\n\nList\n\nA  is a component that is used to display a list of items, stacked vertically by default. A  can be either  or . It is based on the  component and therefore inherits all of its props.\n..."
  },
  {
    "name": "Library Data Display Data List",
    "parts": [
      "Library",
      "Data Display",
      "Data List"
    ],
    "url": "docs/library/data-display/data-list",
    "description": "---\ncomponents:\n    - rx.data_list.root\n    - rx.data_list.item\n    - rx.data_list.label\n    - rx.data_list.value\nDataListRoot: |\n    lambda **props: rx.data_list.root(\n        rx.foreach(\n            [[\"Status\", \"Authorized\"], [\"ID\", \"U-474747\"], [\"Name\", \"Developer Success\"], [\"Email\", \"foo@reflex.dev\"]],\n..."
  },
  {
    "name": "Library Data Display Callout",
    "parts": [
      "Library",
      "Data Display",
      "Callout"
    ],
    "url": "docs/library/data-display/callout",
    "description": "---\ncomponents:\n    - rx.callout\n    - rx.callout.root\n    - rx.callout.icon\n    - rx.callout.text\n\nCallout: |\n    lambda **props: rx.callout(\"Basic Callout\", icon=\"search\", **props)\n..."
  },
  {
    "name": "Library Data Display Badge",
    "parts": [
      "Library",
      "Data Display",
      "Badge"
    ],
    "url": "docs/library/data-display/badge",
    "description": "---\ncomponents:\n    - rx.badge\n\nBadge: |\n    lambda **props: rx.badge(\"Basic Badge\", **props)\n---\nBadge\n\nBadges are used to highlight an item's status for quick recognition.\n..."
  },
  {
    "name": "Library Data Display Avatar",
    "parts": [
      "Library",
      "Data Display",
      "Avatar"
    ],
    "url": "docs/library/data-display/avatar",
    "description": "---\ncomponents:\n    - rx.avatar\nAvatar: |\n    lambda **props: rx.hstack(rx.avatar(src=\"/logo.jpg\", **props), rx.avatar(fallback=\"RX\", **props), spacing=\"3\")\n---\nAvatar\n\nThe Avatar component is used to represent a user, and display their profile pictures or fallback texts such as initials.\n..."
  },
  {
    "name": "Library Data Display Icon",
    "parts": [
      "Library",
      "Data Display",
      "Icon"
    ],
    "url": "docs/library/data-display/icon",
    "description": "---\ncomponents:\n    - rx.lucide.Icon\n---\n\nIcon\n\nThe Icon component is used to display an icon from a library of icons. This implementation is based on the Lucide Icons where you can find a list of all available icons.\n\nIcons List\n..."
  },
  {
    "name": "Library Data Display Moment",
    "parts": [
      "Library",
      "Data Display",
      "Moment"
    ],
    "url": "docs/library/data-display/moment",
    "description": "---\ncomponents:\n    - rx.moment\n\n---\n\nMoment\n\nDisplaying date and relative time to now sometimes can be more complicated than necessary.\n..."
  },
  {
    "name": "Library Graphing General Label",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Label"
    ],
    "url": "docs/library/graphing/general/label",
    "description": "---\ncomponents:\n    - rx.recharts.Label\n    - rx.recharts.LabelList\n---\n\nLabel\n\nLabel is a component used to display a single label at a specific position within a chart or axis, while LabelList is a component that automatically renders a list of labels for each data point in a chart series, providing a convenient way to display multiple labels without manually positioning each one.\n..."
  },
  {
    "name": "Library Graphing General Reference",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Reference"
    ],
    "url": "docs/library/graphing/general/reference",
    "description": "---\ncomponents:\n    - rx.recharts.ReferenceLine\n    - rx.recharts.ReferenceDot\n    - rx.recharts.ReferenceArea\n---\n\nReference\n\nThe Reference components in Recharts, including ReferenceLine, ReferenceArea, and ReferenceDot, are used to add visual aids and annotations to the chart, helping to highlight specific data points, ranges, or thresholds for better data interpretation and analysis.\n..."
  },
  {
    "name": "Library Graphing General Brush",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Brush"
    ],
    "url": "docs/library/graphing/general/brush",
    "description": "---\ncomponents:\n    - rx.recharts.Brush\n---\n\nBrush\n\nSimple Example\n\nThe brush component allows us to view charts that have a large number of data points. To view and analyze them efficiently, the brush provides a slider with two handles that helps the viewer to select some range of data points to be displayed.\n..."
  },
  {
    "name": "Library Graphing General Cartesiangrid",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Cartesiangrid"
    ],
    "url": "docs/library/graphing/general/cartesiangrid",
    "description": "---\ncomponents:\n    - rx.recharts.CartesianGrid\n    # - rx.recharts.CartesianAxis\n---\n\nCartesian Grid\n\nThe Cartesian Grid is a component in Recharts that provides a visual reference for data points in charts. It helps users to better interpret the data by adding horizontal and vertical lines across the chart area.\n..."
  },
  {
    "name": "Library Graphing General Legend",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Legend"
    ],
    "url": "docs/library/graphing/general/legend",
    "description": "---\ncomponents:\n    - rx.recharts.Legend\n---\n\nLegend\n\nA legend tells what each plot represents. Just like on a map, the legend helps the reader understand what they are looking at. For a line graph for example it tells us what each line represents.\n\nSimple Example\n..."
  },
  {
    "name": "Library Graphing General Axis",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Axis"
    ],
    "url": "docs/library/graphing/general/axis",
    "description": "---\ncomponents:\n  - rx.recharts.XAxis\n  - rx.recharts.YAxis\n  - rx.recharts.ZAxis\n---\n\nAxis\n\nThe Axis component in Recharts is a powerful tool for customizing and configuring the axes of your charts. It provides a wide range of props that allow you to control the appearance, behavior, and formatting of the axis. Whether you're working with an AreaChart, LineChart, or any other chart type, the Axis component enables you to create precise and informative visualizations.\n..."
  },
  {
    "name": "Library Graphing Charts Radarchart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Radarchart"
    ],
    "url": "docs/library/graphing/charts/radarchart",
    "description": "---\ncomponents:\n  - rx.recharts.RadarChart\n  - rx.recharts.Radar\n---\n\nRadar Chart\n\nA radar chart shows multivariate data of three or more quantitative variables mapped onto an axis.\n..."
  },
  {
    "name": "Library Graphing Charts Barchart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Barchart"
    ],
    "url": "docs/library/graphing/charts/barchart",
    "description": "---\ncomponents:\n  - rx.recharts.BarChart\n  - rx.recharts.Bar\n---\n\nBar Chart\n\nA bar chart presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.\n..."
  },
  {
    "name": "Library Graphing General Tooltip",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Tooltip"
    ],
    "url": "docs/library/graphing/general/tooltip",
    "description": "---\ncomponents:\n    - rx.recharts.GraphingTooltip\n---\n\nTooltip\n\nTooltips are the little boxes that pop up when you hover over something. Tooltips are always attached to something, like a dot on a scatter chart, or a bar on a bar chart.\n\nCustom Styling\n..."
  },
  {
    "name": "Library Graphing Charts Piechart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Piechart"
    ],
    "url": "docs/library/graphing/charts/piechart",
    "description": "---\ncomponents:\n  - rx.recharts.PieChart\n  - rx.recharts.Pie\n---\n\nPie Chart\n\nA pie chart is a circular statistical graphic which is divided into slices to illustrate numerical proportion.\n..."
  },
  {
    "name": "Library Graphing Charts Funnelchart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Funnelchart"
    ],
    "url": "docs/library/graphing/charts/funnelchart",
    "description": "---\ncomponents:\n  - rx.recharts.FunnelChart\n  - rx.recharts.Funnel\n---\n\nFunnel Chart\n\nA funnel chart is a graphical representation used to visualize how data moves through a process. In a funnel chart, the dependent variable’s value diminishes in the subsequent stages of the process. It can be used to demonstrate the flow of users through a business or sales process.\n..."
  },
  {
    "name": "Library Graphing Charts Errorbar",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Errorbar"
    ],
    "url": "docs/library/graphing/charts/errorbar",
    "description": "---\ncomponents:\n    - rx.recharts.ErrorBar\n---\n\nError Bar\n\nAn error bar is a graphical representation of the uncertainty or variability of a data point in a chart, depicted as a line extending from the data point parallel to one of the axes. The , , , , and  props can be used to customize the appearance and behavior of the error bars, specifying the data source, dimensions, color, and orientation of the error bars."
  },
  {
    "name": "Library Graphing Charts Composedchart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Composedchart"
    ],
    "url": "docs/library/graphing/charts/composedchart",
    "description": "---\ncomponents:\n    - rx.recharts.ComposedChart\n---\n\nComposed Chart\n\nA  is a higher-level component chart that is composed of multiple charts, where other charts are the children of the . The charts are placed on top of each other in the order they are provided in the  function."
  },
  {
    "name": "Library Graphing Charts Linechart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Linechart"
    ],
    "url": "docs/library/graphing/charts/linechart",
    "description": "---\ncomponents:\n  - rx.recharts.LineChart\n  - rx.recharts.Line\n---\n\nLine Chart\n\nA line chart is a type of chart used to show information that changes over time. Line charts are created by plotting a series of several points and connecting them with a straight line.\n..."
  },
  {
    "name": "Library Graphing Charts Scatterchart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Scatterchart"
    ],
    "url": "docs/library/graphing/charts/scatterchart",
    "description": "---\ncomponents:\n  - rx.recharts.ScatterChart\n  - rx.recharts.Scatter\n---\n\nScatter Chart\n\nA scatter chart always has two value axes to show one set of numerical data along a horizontal (value) axis and another set of numerical values along a vertical (value) axis. The chart displays points at the intersection of an x and y numerical value, combining these values into single data points.\n..."
  },
  {
    "name": "Library Graphing Charts Radialbarchart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Radialbarchart"
    ],
    "url": "docs/library/graphing/charts/radialbarchart",
    "description": "---\ncomponents:\n    - rx.recharts.RadialBarChart\n---\n\nRadial Bar Chart\n\nSimple Example\n\nThis example demonstrates how to use a  with a . The  takes in  and then the  takes in a . A radial bar chart is a circular visualization where data categories are represented by bars extending outward from a central point, with the length of each bar proportional to its value.\n..."
  },
  {
    "name": "Library Graphing Charts Areachart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Areachart"
    ],
    "url": "docs/library/graphing/charts/areachart",
    "description": "---\ncomponents:\n  - rx.recharts.AreaChart\n  - rx.recharts.Area\n---\n\nArea Chart\n\nA Recharts area chart displays quantitative data using filled areas between a line connecting data points and the axis.\n..."
  },
  {
    "name": "Library Typography Markdown",
    "parts": [
      "Library",
      "Typography",
      "Markdown"
    ],
    "url": "docs/library/typography/markdown",
    "description": "---\ncomponents:\n    - rx.markdown\n---\n\nMarkdown\n\nThe  component can be used to render markdown text.\nIt is based on Github Flavored Markdown.\n..."
  },
  {
    "name": "Library Graphing Other Charts Pyplot",
    "parts": [
      "Library",
      "Graphing",
      "Other Charts",
      "Pyplot"
    ],
    "url": "docs/library/graphing/other-charts/pyplot",
    "description": "---\ncomponents:\n  - pyplot\n---\n\nPyplot\n\nPyplot () is a graphing library that wraps Matplotlib. Use the  component to display any Matplotlib plot in your app. Check out Matplotlib for more information.\n\nInstallation\n..."
  },
  {
    "name": "Library Graphing Other Charts Plotly",
    "parts": [
      "Library",
      "Graphing",
      "Other Charts",
      "Plotly"
    ],
    "url": "docs/library/graphing/other-charts/plotly",
    "description": "---\ncomponents:\n  - rx.plotly\n---\n\nPlotly\n\nPlotly is a graphing library that can be used to create interactive graphs. Use the rx.plotly component to wrap Plotly as a component for use in your web page. Checkout Plotly for more information.\n\nBasic Example\n..."
  },
  {
    "name": "Library Typography Text",
    "parts": [
      "Library",
      "Typography",
      "Text"
    ],
    "url": "docs/library/typography/text",
    "description": "---\ncomponents:\n    - rx.text\n    - rx.text.em\n\n---\n\nText\n\nAs another element\n..."
  },
  {
    "name": "Library Typography Strong",
    "parts": [
      "Library",
      "Typography",
      "Strong"
    ],
    "url": "docs/library/typography/strong",
    "description": "---\ncomponents:\n    - rx.text.strong\n---\n\nStrong\n\nMarks text to signify strong importance."
  },
  {
    "name": "Library Typography Blockquote",
    "parts": [
      "Library",
      "Typography",
      "Blockquote"
    ],
    "url": "docs/library/typography/blockquote",
    "description": "---\ncomponents:\n    - rx.blockquote\n---\n\nBlockquote\n\nSize\n\nUse the  prop to control the size of the blockquote. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.\n..."
  },
  {
    "name": "Library Typography Heading",
    "parts": [
      "Library",
      "Typography",
      "Heading"
    ],
    "url": "docs/library/typography/heading",
    "description": "---\ncomponents:\n    - rx.heading\n---\n\nHeading\n\nAs another element\n\nUse the  prop to change the heading level. This prop is purely semantic and does not change the visual appearance.\n..."
  },
  {
    "name": "Library Typography Link",
    "parts": [
      "Library",
      "Typography",
      "Link"
    ],
    "url": "docs/library/typography/link",
    "description": "---\ncomponents:\n    - rx.link\n---\n\nLink\n\nLinks are accessible elements used primarily for navigation. Use the  prop to specify the location for the link to navigate to.\n\nYou can also provide local links to other pages in your project without writing the full url.\n..."
  },
  {
    "name": "Library Typography Em",
    "parts": [
      "Library",
      "Typography",
      "Em"
    ],
    "url": "docs/library/typography/em",
    "description": "---\ncomponents:\n    - rx.text.em\n---\n\nEm (Emphasis)\n\nMarks text to stress emphasis."
  },
  {
    "name": "Library Typography Code",
    "parts": [
      "Library",
      "Typography",
      "Code"
    ],
    "url": "docs/library/typography/code",
    "description": "---\ncomponents:\n    - rx.code\n---\n\nCode\n\nSize\n\nUse the  prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.\n..."
  },
  {
    "name": "Library Typography Kbd",
    "parts": [
      "Library",
      "Typography",
      "Kbd"
    ],
    "url": "docs/library/typography/kbd",
    "description": "---\ncomponents:\n    - rx.text.kbd\n---\n\nrx.text.kbd (Keyboard)\n\nRepresents keyboard input or a hotkey.\n\nSize\n..."
  },
  {
    "name": "Library Typography Quote",
    "parts": [
      "Library",
      "Typography",
      "Quote"
    ],
    "url": "docs/library/typography/quote",
    "description": "---\ncomponents:\n    - rx.text.quote\n---\n\nQuote\n\nA short inline quotation."
  },
  {
    "name": "Library Overlay Toast",
    "parts": [
      "Library",
      "Overlay",
      "Toast"
    ],
    "url": "docs/library/overlay/toast",
    "description": "---\ncomponents:\n  - rx.toast.provider\n---\n\nToast\n\nA  is a non-blocking notification that disappears after a certain amount of time. It is often used to show a message to the user without interrupting their workflow.\n\nUsage\n..."
  },
  {
    "name": "Library Overlay Popover",
    "parts": [
      "Library",
      "Overlay",
      "Popover"
    ],
    "url": "docs/library/overlay/popover",
    "description": "---\ncomponents:\n  - rx.popover.root\n  - rx.popover.content\n  - rx.popover.trigger\n  - rx.popover.close\n\nonly_low_level:\n  - True\n..."
  },
  {
    "name": "Library Overlay Hover Card",
    "parts": [
      "Library",
      "Overlay",
      "Hover Card"
    ],
    "url": "docs/library/overlay/hover-card",
    "description": "---\ncomponents:\n  - rx.hover_card.root\n  - rx.hover_card.content\n  - rx.hover_card.trigger\n\nonly_low_level:\n  - True\n\nHoverCardRoot: |\n..."
  },
  {
    "name": "Library Overlay Drawer",
    "parts": [
      "Library",
      "Overlay",
      "Drawer"
    ],
    "url": "docs/library/overlay/drawer",
    "description": "---\ncomponents:\n  - rx.drawer.root\n  - rx.drawer.trigger\n  - rx.drawer.overlay\n  - rx.drawer.portal\n  - rx.drawer.content\n  - rx.drawer.close\n\nonly_low_level:\n..."
  },
  {
    "name": "Library Overlay Dialog",
    "parts": [
      "Library",
      "Overlay",
      "Dialog"
    ],
    "url": "docs/library/overlay/dialog",
    "description": "---\ncomponents:\n  - rx.dialog.root\n  - rx.dialog.trigger\n  - rx.dialog.title\n  - rx.dialog.content\n  - rx.dialog.description\n  - rx.dialog.close\n\nonly_low_level:\n..."
  },
  {
    "name": "Library Overlay Dropdown Menu",
    "parts": [
      "Library",
      "Overlay",
      "Dropdown Menu"
    ],
    "url": "docs/library/overlay/dropdown-menu",
    "description": "---\ncomponents:\n  - rx.dropdown_menu.root\n  - rx.dropdown_menu.content\n  - rx.dropdown_menu.trigger\n  - rx.dropdown_menu.item\n  - rx.dropdown_menu.separator\n  - rx.dropdown_menu.sub_content\n\nonly_low_level:\n..."
  },
  {
    "name": "Library Overlay Alert Dialog",
    "parts": [
      "Library",
      "Overlay",
      "Alert Dialog"
    ],
    "url": "docs/library/overlay/alert-dialog",
    "description": "---\ncomponents:\n  - rx.alert_dialog.root\n  - rx.alert_dialog.content\n  - rx.alert_dialog.trigger\n  - rx.alert_dialog.title\n  - rx.alert_dialog.description\n  - rx.alert_dialog.action\n  - rx.alert_dialog.cancel\n..."
  },
  {
    "name": "Library Overlay Tooltip",
    "parts": [
      "Library",
      "Overlay",
      "Tooltip"
    ],
    "url": "docs/library/overlay/tooltip",
    "description": "---\ncomponents:\n  - rx.tooltip\n\nTooltip: |\n  lambda **props: rx.tooltip(\n      rx.button(\"Hover over me\"),\n      content=\"This is the tooltip content.\",\n      **props,\n  )\n..."
  },
  {
    "name": "Library Overlay Context Menu",
    "parts": [
      "Library",
      "Overlay",
      "Context Menu"
    ],
    "url": "docs/library/overlay/context-menu",
    "description": "---\ncomponents:\n  - rx.context_menu.root\n  - rx.context_menu.item\n  - rx.context_menu.separator\n  - rx.context_menu.trigger\n  - rx.context_menu.content\n  - rx.context_menu.sub\n  - rx.context_menu.sub_trigger\n  - rx.context_menu.sub_content\n..."
  },
  {
    "name": "Library Media Image",
    "parts": [
      "Library",
      "Media",
      "Image"
    ],
    "url": "docs/library/media/image",
    "description": "---\ncomponents:\n    - rx.image\n---\n\nImage\n\nThe Image component can display an image given a  path as an argument.\nThis could either be a local path from the assets folder or an external link.\n..."
  },
  {
    "name": "Library Media Video",
    "parts": [
      "Library",
      "Media",
      "Video"
    ],
    "url": "docs/library/media/video",
    "description": "---\ncomponents:\n    - rx.video\n---\n\nVideo\n\nThe video component can display a video given an src path as an argument. This could either be a local path from the assets folder or an external link.\n\nIf we had a local file in the  folder named  we could set  to view the video.\n..."
  },
  {
    "name": "Library Media Audio",
    "parts": [
      "Library",
      "Media",
      "Audio"
    ],
    "url": "docs/library/media/audio",
    "description": "---\ncomponents:\n    - rx.audio\n---\n\nAudio\n\nThe audio component can display an audio given an src path as an argument. This could either be a local path from the assets folder or an external link.\n\nIf we had a local file in the  folder named  we could set  to view the audio file.\n..."
  },
  {
    "name": "AI Builder Faq",
    "parts": [
      "AI Builder",
      "Faq"
    ],
    "url": "docs/ai-builder/faq",
    "description": ""
  },
  {
    "name": "AI Builder Overview",
    "parts": [
      "AI Builder",
      "Overview"
    ],
    "url": "docs/ai-builder/overview",
    "description": "Overview"
  },
  {
    "name": "AI Builder Intro",
    "parts": [
      "AI Builder",
      "Intro"
    ],
    "url": "docs/ai-builder/intro",
    "description": "Overview"
  },
  {
    "name": "AI Builder Prompting Breaking Up Complex Prompts",
    "parts": [
      "AI Builder",
      "Prompting",
      "Breaking Up Complex Prompts"
    ],
    "url": "docs/ai-builder/prompting/breaking-up-complex-prompts",
    "description": "Breaking up complex prompts\n\nIncremental Prompting\n\nAsking for incremental, smaller changes leads to better results, rather than asking for everything all in a single huge prompt. It's better to take it step-by-step rather than give the AI complex tasks all at once.\n\nExample 1                      \nToo Complex:\n\nBetter Approach:\n..."
  },
  {
    "name": "AI Builder Prompting Fixing Errors",
    "parts": [
      "AI Builder",
      "Prompting",
      "Fixing Errors"
    ],
    "url": "docs/ai-builder/prompting/fixing-errors",
    "description": "Fixing Errors\n\nStill to come!"
  },
  {
    "name": "AI Builder Features Templates",
    "parts": [
      "AI Builder",
      "Features",
      "Templates"
    ],
    "url": "docs/ai-builder/features/templates",
    "description": "Templates\n\nReflex has many certified templates, seen on the  tab of the Reflex Build, that can be used to kickstart your app. You can also use any app created by the community as a template. \n\nUsing a Template\n\nTo use a template, simply click the template and then in the bottom right corner of the app click the  button. This will create a copy of the template in your own account. You can then edit the app as you like with further prompting.\n\nBelow is an example of how to use a template:\n..."
  },
  {
    "name": "AI Builder Features Download App",
    "parts": [
      "AI Builder",
      "Features",
      "Download App"
    ],
    "url": "docs/ai-builder/features/download-app",
    "description": "Download your App\n\nIt is easy to download your app to work on locally or self-host. (It is recommended to use the GitHub integration, but if this is not possible, you can download your app to work on locally.) \n\nSimply click the  button in the bottom right corner of Reflex Build, as shown below:"
  },
  {
    "name": "AI Builder Features Image As Prompt",
    "parts": [
      "AI Builder",
      "Features",
      "Image As Prompt"
    ],
    "url": "docs/ai-builder/features/image-as-prompt",
    "description": "Use Images as a prompt\n\nUploading an image (screenshot) of a website (web) app of what you are looking to build gives the AI really good context. \n\n*This is the recommended way to start an app generation.*\n\nBelow is a GIF showing how to upload an image to the AI Builder:\n\nThe advised prompt to use is:"
  },
  {
    "name": "AI Builder Features Environment Variables",
    "parts": [
      "AI Builder",
      "Features",
      "Environment Variables"
    ],
    "url": "docs/ai-builder/features/environment-variables",
    "description": "Environment Variables (Secrets)\n\nIt is possible to add environment variables to your app. This is useful for storing secrets such as API keys, and other sensitive information.\n\nAdding Environment Variables\n\nYou can add environment variables to your app by clicking the  button at the bottom of the chat input box, as seen below:\n\nAfter you add the environment variables the AI now has context of these and you can prompt it to use them in your code.\n..."
  },
  {
    "name": "AI Builder Features Deploy App",
    "parts": [
      "AI Builder",
      "Features",
      "Deploy App"
    ],
    "url": "docs/ai-builder/features/deploy-app",
    "description": "Deploy your App\n\nIt is easy to deploy your app into production from Reflex Build to Reflex Cloud. \n\nSimply click the  button in the bottom right corner of Reflex Build, as shown below:\n\nWhen deploying you can set the following options:\n- **App Name**: The name of your app\n- **Hostname**: Set your url by setting your hostname, i.e. if you set  as your hostname, your app will be available at \n- **Region**: The regions where your app will be deployed\n..."
  },
  {
    "name": "AI Builder Features Ide",
    "parts": [
      "AI Builder",
      "Features",
      "Ide"
    ],
    "url": "docs/ai-builder/features/ide",
    "description": "Reflex Build's IDE\n\nReflex Build includes a powerful, in-browser IDE designed to streamline the entire development process—from writing code\nto deploying your app. With an intuitive layout, real-time editing, and seamless integration with the rest of the\nplatform, the IDE empowers users to stay focused and productive without ever leaving the browser.\n\n<div class=\"p-1 my-4 rounded-lg bg-slate-5\">\n  <iframe\n    width=\"100%\"\n    height=\"400\"\n..."
  },
  {
    "name": "AI Builder Features Installing External Packages",
    "parts": [
      "AI Builder",
      "Features",
      "Installing External Packages"
    ],
    "url": "docs/ai-builder/features/installing-external-packages",
    "description": "Installing External Packages\n\nReflex Build allows you to install external python packages to use in your app. This is useful if you want to use a package that is not included in the default Reflex Build environment. Examples might include , , , etc.\n\nThere are two ways to install external packages:\n\n1. **Through the Chat Interface**: You can ask the AI to install a package for you.\n2. **Add to the  file**: You can add the package to the  file and then save the app. This will install the package in your app's environment.\n\nInstalling through the Chat Interface\n..."
  },
  {
    "name": "AI Builder Integrations Github",
    "parts": [
      "AI Builder",
      "Integrations",
      "Github"
    ],
    "url": "docs/ai-builder/integrations/github",
    "description": "Connecting to Github\n\nThe Github integration is important to make sure that you don't lose your progress. It also allows you to revert to previous versions of your app. \n\nThe GitHub integration allows you to:\n\n- Save your app progress\n- Work on your code locally and push your local changes back to Reflex.Build\n\nGithub Commit History\n..."
  },
  {
    "name": "AI Builder Overview What Is Reflex Build",
    "parts": [
      "AI Builder",
      "Overview",
      "What Is Reflex Build"
    ],
    "url": "docs/ai-builder/overview/what-is-reflex-build",
    "description": "What Is Reflex Build\n\n<div class=\"p-1 my-4 rounded-lg bg-slate-5\">\n  <iframe\n    width=\"100%\"\n    height=\"400\"\n    src=\"https://www.youtube.com/embed/s-kr8v7827g \"\n    title=\"Reflex Build\"\n    frameborder=\"0\"\n    allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\"\n..."
  },
  {
    "name": "AI Builder Integrations Database",
    "parts": [
      "AI Builder",
      "Integrations",
      "Database"
    ],
    "url": "docs/ai-builder/integrations/database",
    "description": "Connecting to a Database\n\nConnecting to a database is critical to give your app access to real data. This section will cover how to connect to a database using the AI Builder. \n\nTo connect to a database you will need a . Reflex.build currently supports  and  databases.\n\nThis is what it looks like for a Postgres database:\n\nYou can also use a MySQL database. The connection string looks like this:\n..."
  },
  {
    "name": "AI Builder Overview Frequently Asked Questions",
    "parts": [
      "AI Builder",
      "Overview",
      "Frequently Asked Questions"
    ],
    "url": "docs/ai-builder/overview/frequently-asked-questions",
    "description": "FAQs\n\nStill to come!"
  },
  {
    "name": "AI Builder Overview Quickstart",
    "parts": [
      "AI Builder",
      "Overview",
      "Quickstart"
    ],
    "url": "docs/ai-builder/overview/quickstart",
    "description": "Quickstart\n\nStill to come!"
  },
  {
    "name": "State Overview",
    "parts": [
      "State",
      "Overview"
    ],
    "url": "docs/state/overview",
    "description": "State\n\nState allows us to create interactive apps that can respond to user input.\nIt defines the variables that can change over time, and the functions that can modify them.\n\nState Basics\n\nYou can define state by creating a class that inherits from :\n\nA state class is made up of two parts: vars and event handlers.\n..."
  },
  {
    "name": "Components Html To Reflex",
    "parts": [
      "Components",
      "Html To Reflex"
    ],
    "url": "docs/components/html-to-reflex",
    "description": "Convert HTML to Reflex\n\nTo convert HTML, CSS, or any design into Reflex code, use our AI-powered build tool at Reflex Build.\n\nSimply paste your HTML, CSS, or describe what you want to build, and our AI will generate the corresponding Reflex code for you.\n\nHow to use Reflex Build\n\n1. Go to Reflex Build\n2. Paste your HTML/CSS code or describe your design\n..."
  },
  {
    "name": "State Structure Component State",
    "parts": [
      "State Structure",
      "Component State"
    ],
    "url": "docs/state-structure/component-state",
    "description": "Component State\n\n_New in version 0.4.6_.\n\nDefining a subclass of  creates a special type of state that is tied to an\ninstance of a component, rather than existing globally in the app. A Component State combines\nUI code with state Vars and\nEvent Handlers,\nand is useful for creating reusable components which operate independently of each other.\n..."
  },
  {
    "name": "State Structure Overview",
    "parts": [
      "State Structure",
      "Overview"
    ],
    "url": "docs/state-structure/overview",
    "description": "Substates\n\nSubstates allow you to break up your state into multiple classes to make it more manageable. This is useful as your app\ngrows, as it allows you to think about each page as a separate entity. Substates also allow you to share common state\nresources, such as variables or event handlers.\n\nWhen a particular state class becomes too large, breaking it up into several substates can bring performance\nbenefits by only loading parts of the state that are used to handle a certain event.\n\nMultiple States\n..."
  },
  {
    "name": "Components Props",
    "parts": [
      "Components",
      "Props"
    ],
    "url": "docs/components/props",
    "description": "Props\n\nProps modify the behavior and appearance of a component. They are passed in as keyword arguments to a component.\n\nComponent Props\n\nThere are props that are shared between all components, but each component can also define its own props.\n\nFor example, the  component has a  prop that specifies the URL of the image to display and an  prop that specifies the alternate text for the image.\n..."
  },
  {
    "name": "Components Rendering Iterables",
    "parts": [
      "Components",
      "Rendering Iterables"
    ],
    "url": "docs/components/rendering-iterables",
    "description": "Rendering Iterables\n\nRecall again from the basics that we cannot use Python  loops when referencing state vars in Reflex. Instead, use the  component to render components from a collection of data.\n\nFor dynamic content that should automatically scroll to show the newest items, consider using the auto scroll component together with .\n\nHere's the same example using a lambda function.\n\nYou can also use lambda functions directly with components without defining a separate function.\n..."
  },
  {
    "name": "API Routes Overview",
    "parts": [
      "API Routes",
      "Overview"
    ],
    "url": "docs/api-routes/overview",
    "description": "API Transformer\n\nIn addition to your frontend app, Reflex uses a FastAPI backend to serve your app. The API transformer feature allows you to transform or extend the ASGI app that serves your Reflex application.\n\nOverview\n\nThe API transformer provides a way to:\n\n1. Integrate existing FastAPI or Starlette applications with your Reflex app\n2. Apply middleware or transformations to the ASGI app\n..."
  },
  {
    "name": "Components Conditional Rendering",
    "parts": [
      "Components",
      "Conditional Rendering"
    ],
    "url": "docs/components/conditional-rendering",
    "description": "Conditional Rendering\n\nRecall from the basics that we cannot use Python  statements when referencing state vars in Reflex. Instead, use the  component to conditionally render components or set props based on the value of a state var.\n\nBelow is a simple example showing how to toggle between two text components by checking the value of the state var .\n\nIf  is  then the first component is rendered (in this case the blue text). Otherwise the second component is rendered (in this case the red text).\n\nConditional Props\n..."
  },
  {
    "name": "Wrapping React More Wrapping Examples",
    "parts": [
      "Wrapping React",
      "More Wrapping Examples"
    ],
    "url": "docs/wrapping-react/more-wrapping-examples",
    "description": "More React Libraries \n\nAG Charts\n\nHere we wrap the AG Charts library from the NPM package ag-charts-react. \n\nIn the react code below we can see the first  lines are importing React and ReactDOM, and this can be ignored when wrapping your component.\n\nWe import the  component from the  library on line 5. In Reflex this is wrapped by  and .\n..."
  },
  {
    "name": "Wrapping React Local Packages",
    "parts": [
      "Wrapping React",
      "Local Packages"
    ],
    "url": "docs/wrapping-react/local-packages",
    "description": "---\ntitle: Wrapping Local Packages\n---\n\nAssets\n\nIf a wrapped component depends on assets such as images, scripts, or\nstylesheets, these can be kept adjacent to the component code and\nincluded in the final build using the  function.\n..."
  },
  {
    "name": "Wrapping React Overview",
    "parts": [
      "Wrapping React",
      "Overview"
    ],
    "url": "docs/wrapping-react/overview",
    "description": "Wrapping React\n\nOne of Reflex's most powerful features is the ability to wrap React components and take advantage of the vast ecosystem of React libraries.\n\nIf you want a specific component for your app but Reflex doesn't provide it, there's a good chance it's available as a React component. Search for it on npm, and if it's there, you can use it in your Reflex app. You can also create your own local React components and wrap them in Reflex.\n\nOnce you wrap your component, you publish it to the Reflex library so that others can use it.\n\nSimple Example\n..."
  },
  {
    "name": "Wrapping React Example",
    "parts": [
      "Wrapping React",
      "Example"
    ],
    "url": "docs/wrapping-react/example",
    "description": "Complex Example\n\nIn this more complex example we will be wrapping  a library for building node based applications like flow charts, diagrams, graphs, etc.\n\nImport\n\nLets start by importing the library reactflow. Lets make a separate file called  and add the following code:\n\nNotice we also use the  method to import the css file that is needed for the styling of the library.\n..."
  },
  {
    "name": "Wrapping React Props",
    "parts": [
      "Wrapping React",
      "Props"
    ],
    "url": "docs/wrapping-react/props",
    "description": "---\ntitle: Props - Wrapping React \n---\n\nProps\n\nWhen wrapping a React component, you want to define the props that will be accepted by the component.\nThis is done by defining the props and annotating them with a .\n\nBroadly, there are three kinds of props you can encounter when wrapping a React component:\n..."
  },
  {
    "name": "Wrapping React Library And Tags",
    "parts": [
      "Wrapping React",
      "Library And Tags"
    ],
    "url": "docs/wrapping-react/library-and-tags",
    "description": "---\ntitle: Library and Tags\n---\n\nFind The Component\n\nThere are two ways to find a component to wrap:\n1. Write the component yourself locally.\n2. Find a well-maintained React library on npm that contains the component you need.\n..."
  },
  {
    "name": "Wrapping React Step By Step",
    "parts": [
      "Wrapping React",
      "Step By Step"
    ],
    "url": "docs/wrapping-react/step-by-step",
    "description": ""
  },
  {
    "name": "Wrapping React Custom Code And Hooks",
    "parts": [
      "Wrapping React",
      "Custom Code And Hooks"
    ],
    "url": "docs/wrapping-react/custom-code-and-hooks",
    "description": "When wrapping a React component, you may need to define custom code or hooks that are specific to the component. This is done by defining the or  methods in your component class.\n\nCustom Code\n\nCustom code is any JS code that need to be included in your page, but not necessarily in the component itself. This can include things like CSS styles, JS libraries, or any other code that needs to be included in the page.\n\nThe above example will render the following JS code in the page:\n\nCustom Hooks\nCustom hooks are any hooks that need to be included in your component. This can include things like , , or any other hooks from the library you are wrapping.\n..."
  },
  {
    "name": "Wrapping React Imports And Styles",
    "parts": [
      "Wrapping React",
      "Imports And Styles"
    ],
    "url": "docs/wrapping-react/imports-and-styles",
    "description": "Styles and Imports\n\nWhen wrapping a React component, you may need to define styles and imports that are specific to the component. This is done by defining the  and  methods in your component class.\n\nImports\n\nSometimes, the component you are wrapping will need to import other components or libraries. This is done by defining the  method in your component class.\nThat method should return a dictionary of imports, where the keys are the names of the packages to import and the values are the names of the components or libraries to import.\n\nValues can be either a string or a list of strings. If the import needs to be aliased, you can use the  object to specify the alias and whether the import should be installed as a dependency.\n..."
  },
  {
    "name": "Recipes Auth Signup Form",
    "parts": [
      "Recipes",
      "Auth",
      "Signup Form"
    ],
    "url": "docs/recipes/auth/signup-form",
    "description": "Sign up Form\n\nThe sign up form is a common component in web applications. It allows users to create an account and access the application's features. This page provides a few examples of sign up forms that you can use in your application.\nDefault\n\nIcons\n\nThird-party auth\n\nMultiple third-party auth\n..."
  },
  {
    "name": "Recipes Auth Login Form",
    "parts": [
      "Recipes",
      "Auth",
      "Login Form"
    ],
    "url": "docs/recipes/auth/login-form",
    "description": "Login Form\n\nThe login form is a common component in web applications. It allows users to authenticate themselves and access their accounts. This recipe provides examples of login forms with different elements, such as third-party authentication providers.\n\nDefault\n\nIcons\n\nThird-party auth\n..."
  },
  {
    "name": "Wrapping React Serializers",
    "parts": [
      "Wrapping React",
      "Serializers"
    ],
    "url": "docs/wrapping-react/serializers",
    "description": "---\ntitle: Serializers\n---\n\nSerializers\n\nVars can be any type that can be serialized to JSON. This includes primitive types like strings, numbers, and booleans, as well as more complex types like lists, dictionaries, and dataframes.\n\nIn case you need to serialize a more complex type, you can use the  decorator to convert the type to a primitive type that can be stored in the state. Just define a method that takes the complex type as an argument and returns a primitive type. We use type annotations to determine the type that you want to serialize.\n..."
  },
  {
    "name": "Recipes Layout Footer",
    "parts": [
      "Recipes",
      "Layout",
      "Footer"
    ],
    "url": "docs/recipes/layout/footer",
    "description": "Footer Bar\n\nA footer bar is a common UI element located at the bottom of a webpage. It typically contains information about the website, such as contact details and links to other pages or sections of the site.\n\nBasic\n\nNewsletter form\n\nThree columns"
  },
  {
    "name": "Recipes Others Dark Mode Toggle",
    "parts": [
      "Recipes",
      "Others",
      "Dark Mode Toggle"
    ],
    "url": "docs/recipes/others/dark-mode-toggle",
    "description": "Dark Mode Toggle\n\nThe Dark Mode Toggle component lets users switch between light and dark themes."
  },
  {
    "name": "Recipes Layout Navbar",
    "parts": [
      "Recipes",
      "Layout",
      "Navbar"
    ],
    "url": "docs/recipes/layout/navbar",
    "description": "Navigation Bar\n\nA navigation bar, also known as a navbar, is a common UI element found at the top of a webpage or application.\nIt typically provides links or buttons to the main sections of a website or application, allowing users to easily navigate and access the different pages.\n\nNavigation bars are useful for web apps because they provide a consistent and intuitive way for users to navigate through the app.\nHaving a clear and consistent navigation structure can greatly improve the user experience by making it easy for users to find the information they need and access the different features of the app.\n\nBasic\n..."
  },
  {
    "name": "Recipes Layout Sidebar",
    "parts": [
      "Recipes",
      "Layout",
      "Sidebar"
    ],
    "url": "docs/recipes/layout/sidebar",
    "description": "Sidebar\n\nSimilar to a navigation bar, a sidebar is a common UI element found on the side of a webpage or application. It typically contains links to different sections of the site or app.\n\nBasic\n\nBottom user profile\n\nTop user profile"
  },
  {
    "name": "Recipes Others Speed Dial",
    "parts": [
      "Recipes",
      "Others",
      "Speed Dial"
    ],
    "url": "docs/recipes/others/speed-dial",
    "description": "Speed Dial\n\nA speed dial is a component that allows users to quickly access frequently used actions or pages. It is often used in the bottom right corner of the screen.\n\nVertical\n\nHorizontal\n\nVertical with text\n..."
  },
  {
    "name": "Recipes Others Checkboxes",
    "parts": [
      "Recipes",
      "Others",
      "Checkboxes"
    ],
    "url": "docs/recipes/others/checkboxes",
    "description": "Smart Checkboxes Group\n\nA smart checkboxes group where you can track all checked boxes, as well as place a limit on how many checks are possible.\n\nRecipe\n\nThis recipe use a  for the checkboxes state tracking.\nAdditionally, the limit that prevent the user from checking more boxes than allowed with a computed var."
  },
  {
    "name": "Recipes Others Pricing Cards",
    "parts": [
      "Recipes",
      "Others",
      "Pricing Cards"
    ],
    "url": "docs/recipes/others/pricing-cards",
    "description": "Pricing Cards\n\nA pricing card shows the price of a product or service. It typically includes a title, description, price, features, and a purchase button.\n\nBasic\n\nComparison cards"
  },
  {
    "name": "Recipes Others Chips",
    "parts": [
      "Recipes",
      "Others",
      "Chips"
    ],
    "url": "docs/recipes/others/chips",
    "description": "Chips\n\nChips are compact elements that represent small pieces of information, such as tags or categories. They are commonly used to select multiple items from a list or to filter content.\n\nStatus\n\nSingle selection\n\nMultiple selection\n..."
  },
  {
    "name": "Recipes Content Forms",
    "parts": [
      "Recipes",
      "Content",
      "Forms"
    ],
    "url": "docs/recipes/content/forms",
    "description": "Forms\n\nForms are a common way to gather information from users. Below are some examples.\n\nFor more details, see the form docs page.\n\nEvent creation\n\nContact"
  },
  {
    "name": "Recipes Content Stats",
    "parts": [
      "Recipes",
      "Content",
      "Stats"
    ],
    "url": "docs/recipes/content/stats",
    "description": "Stats\n\nStats cards are used to display key metrics or data points. They are typically used in dashboards or admin panels.\n\nVariant 1\n\nVariant 2"
  },
  {
    "name": "Recipes Content Top Banner",
    "parts": [
      "Recipes",
      "Content",
      "Top Banner"
    ],
    "url": "docs/recipes/content/top-banner",
    "description": "Top Banner\n\nTop banners are used to highlight important information or features at the top of a page. They are typically designed to grab the user's attention and can be used for announcements, navigation, or key messages.\n\nBasic\n\nSign up\n\nGradient\n..."
  },
  {
    "name": "Recipes Content Grid",
    "parts": [
      "Recipes",
      "Content",
      "Grid"
    ],
    "url": "docs/recipes/content/grid",
    "description": "Grid\n\nA simple responsive grid layout. We specify the number of columns to the  property as a list. The grid will automatically adjust the number of columns based on the screen size.\n\nFor details, see the responsive docs page.\n\nCards\n\nInset cards"
  },
  {
    "name": "Recipes Content Multi Column Row",
    "parts": [
      "Recipes",
      "Content",
      "Multi Column Row"
    ],
    "url": "docs/recipes/content/multi-column-row",
    "description": "Multi-column and row layout\n\nA simple responsive multi-column and row layout. We specify the number of columns/rows to the  property as a list. The layout will automatically adjust the number of columns/rows based on the screen size.\n\nFor details, see the responsive docs page.\n\nColumn\n\nRow"
  },
  {
    "name": "Styling Overview",
    "parts": [
      "Styling",
      "Overview"
    ],
    "url": "docs/styling/overview",
    "description": "Styling\n\nReflex components can be styled using the full power of CSS.\n\nThere are three main ways to add style to your app and they take precedence in the following order:\n\n1. **Inline:** Styles applied to a single component instance.\n2. **Component:** Styles applied to components of a specific type.\n3. **Global:** Styles applied to all components.\n..."
  },
  {
    "name": "Styling Tailwind",
    "parts": [
      "Styling",
      "Tailwind"
    ],
    "url": "docs/styling/tailwind",
    "description": "Tailwind\n\nReflex supports Tailwind CSS through a plugin system that provides better control and supports multiple Tailwind versions.\n\nPlugin-Based Configuration\n\nThe recommended way to use Tailwind CSS is through the plugin system:\n\nYou can customize the Tailwind configuration by passing a config dictionary to the plugin:\n..."
  },
  {
    "name": "Styling Responsive",
    "parts": [
      "Styling",
      "Responsive"
    ],
    "url": "docs/styling/responsive",
    "description": "Responsive\n\nReflex apps can be made responsive to look good on mobile, tablet, and desktop.\n\nYou can pass a list of values to any style property to specify its value on different screen sizes.\n\nThe text will change color based on your screen size. If you are on desktop, try changing the size of your browser window to see the color change.\n\n_New in 0.5.6_\n..."
  },
  {
    "name": "Styling Common Props",
    "parts": [
      "Styling",
      "Common Props"
    ],
    "url": "docs/styling/common-props",
    "description": "Style and Layout Props\n\nAny CSS prop can be used in a component in Reflex. This is a short list of the most commonly used props. To see all CSS props that can be used check out this documentation. \n\nHyphens in CSS property names may be replaced by underscores to use as valid python identifiers, i.e. the CSS prop  would be used as  in Reflex."
  },
  {
    "name": "Styling Theming",
    "parts": [
      "Styling",
      "Theming"
    ],
    "url": "docs/styling/theming",
    "description": "Theming\n\nAs of Reflex , you can now theme your Reflex applications. The core of our theming system is directly based on the Radix Themes library. This allows you to easily change the theme of your application along with providing a default light and dark theme. Themes cause all the components to have a unified color appearance.\n\nOverview\n\nThe  component is used to change the theme of the application. The  can be set directly in your rx.App.\n\nHere are the props that can be passed to the  component:\n..."
  },
  {
    "name": "Styling Layout",
    "parts": [
      "Styling",
      "Layout"
    ],
    "url": "docs/styling/layout",
    "description": "Layout Components\n\nLayout components such as , , , etc. are used to organize and structure the visual presentation of your application. This page gives a breakdown of when and how each of these components might be used.\n\nBox\n\n is a generic component that can apply any CSS style to its children. It's a building block that can be used to apply a specific layout or style property.\n\n**When to use:** Use  when you need to apply specific styles or constraints to a part of your interface.\n..."
  },
  {
    "name": "Styling Custom Stylesheets",
    "parts": [
      "Styling",
      "Custom Stylesheets"
    ],
    "url": "docs/styling/custom-stylesheets",
    "description": "Custom Stylesheets\n\nReflex allows you to add custom stylesheets. Simply pass the URLs of the stylesheets to :\n\nLocal Stylesheets\n\nYou can also add local stylesheets. Just put the stylesheet under []({assets.upload_and_download_files.path}) and pass the path to the stylesheet to :\n\nStyling with CSS\n..."
  },
  {
    "name": "Hosting Custom Domains",
    "parts": [
      "Hosting",
      "Custom Domains"
    ],
    "url": "docs/hosting/custom-domains",
    "description": "Custom Domains\n\nWith the Pro tier of Reflex Cloud you can use your own custom domain to host your app. \n\nPrerequisites\n\nYou must purchase a domain from a domain registrar such as GoDaddy, Cloudflare, Namecheap, or AWS. \n\nFor this tutorial we will use GoDaddy and the example domain .\n..."
  },
  {
    "name": "Hosting Secrets Environment Vars",
    "parts": [
      "Hosting",
      "Secrets Environment Vars"
    ],
    "url": "docs/hosting/secrets-environment-vars",
    "description": "Secrets (Environment Variables)\n\nAdding Secrets through the CLI\n\nBelow is an example of how to use an environment variable file. You can pass the  flag with the path to the env file. For example:\n\nIn this example the path to the file is .\n\nIf you prefer to pass the environment variables manually below is deployment command example:\n..."
  },
  {
    "name": "Hosting Machine Types",
    "parts": [
      "Hosting",
      "Machine Types"
    ],
    "url": "docs/hosting/machine-types",
    "description": "Machine Types\n\nTo scale your app you can choose different VMTypes. VMTypes are different configurations of CPU and RAM.\n\nTo scale your VM in the Cloud UI, click on the  tab in the Cloud UI on the app page, and then click on the  tab as shown below. Clicking on the  button will allow you to scale your app.\n\nVMTypes in the CLI\n\nTo get all the possible VMTypes you can run the following command:\n..."
  },
  {
    "name": "Hosting Deploy Quick Start",
    "parts": [
      "Hosting",
      "Deploy Quick Start"
    ],
    "url": "docs/hosting/deploy-quick-start",
    "description": "Reflex Cloud - Quick Start\n\nSo far, we have been running our apps locally on our own machines.\nBut what if we want to share our apps with the world? This is where\nthe hosting service comes in.\n\nQuick Start\n\nReflex’s hosting service makes it easy to deploy your apps without worrying about configuring the infrastructure.\n..."
  },
  {
    "name": "Hosting Self Hosting",
    "parts": [
      "Hosting",
      "Self Hosting"
    ],
    "url": "docs/hosting/self-hosting",
    "description": "Self Hosting\n\nWe recommend using , but if this does not fit your use case then you can also host your apps yourself.\n\nClone your code to a server and install the requirements.\n\nAPI URL\n\nEdit your  file and set  to the publicly accessible IP\naddress or hostname of your server, with the port  at the end. Setting\n..."
  },
  {
    "name": "Hosting Logs",
    "parts": [
      "Hosting",
      "Logs"
    ],
    "url": "docs/hosting/logs",
    "description": "View Logs\n\nTo view the app logs follow the arrow in the image below and press on the  dropdown.\n\nView Deployment Logs and Deployment History\n\nTo view the deployment history follow the arrow in the image below and press on the .\n\nThis brings you to the page below where you can see the deployment history of your app. Click on deployment you wish to explore further.\n..."
  },
  {
    "name": "Hosting Compute",
    "parts": [
      "Hosting",
      "Compute"
    ],
    "url": "docs/hosting/compute",
    "description": "Compute Usage\n\nReflex Cloud is billed on a per second basis so you only pay for when your app is being used by your end users. When your app is idle, you are not charged. \n\nThis allows you to deploy your app on larger sizes and multiple regions without worrying about paying for idle compute. We bill on a per second basis so you only pay for the compute you use.\n\nBy default your app stays alive for 5 minutes after the no users are connected. After this time your app will be considered idle and you will not be charged. Start up times usually take less than 1 second for you apps to come back online.\n\nWarm vs Cold Start\n- Apps below  are considered warm starts and are usually less than 1 second.\n..."
  },
  {
    "name": "Hosting Billing",
    "parts": [
      "Hosting",
      "Billing"
    ],
    "url": "docs/hosting/billing",
    "description": "Overview \n\nBilling for Reflex Cloud is monthly per project. Project owners and admins are able to view and manage the billing page. \n\nThe billing for a project is comprised of two parts - number of  and . \n\nSeats\n\nProjects on a paid plan can invite collaborators to join their project.\n..."
  },
  {
    "name": "Hosting Config File",
    "parts": [
      "Hosting",
      "Config File"
    ],
    "url": "docs/hosting/config-file",
    "description": "What is reflex cloud config?\n\nThe following command:\n\ngenerates a  configuration file used to deploy your Reflex app to the Reflex cloud platform. This file tells Reflex how and where to run your app in the cloud.\n\nConfiguration File Structure\n\nThe  file uses YAML format and supports the following structure. **All fields are optional** and will use sensible defaults if not specified:\n..."
  },
  {
    "name": "Hosting Databricks",
    "parts": [
      "Hosting",
      "Databricks"
    ],
    "url": "docs/hosting/databricks",
    "description": "Deploy Reflex to Databricks\n\nThis guide walks you through deploying a Reflex web application on Databricks using the Apps platform.\n\nPrerequisites\n\n- Databricks workspace with Unity Catalog enabled\n- GitHub repository containing your Reflex application\n- Reflex Enterprise license (for single-port deployment)\n..."
  },
  {
    "name": "Hosting Adding Members",
    "parts": [
      "Hosting",
      "Adding Members"
    ],
    "url": "docs/hosting/adding-members",
    "description": "Project\n\nA project is a collection of applications (apps / websites).\n\nEvery project has its own billing page that are accessible to Admins.\n\nAdding Team Members\n\nTo see the team members of a project click on the  tab in the Cloud UI on the project page.\n..."
  },
  {
    "name": "Hosting App Management",
    "parts": [
      "Hosting",
      "App Management"
    ],
    "url": "docs/hosting/app-management",
    "description": "App\n\nIn Reflex Cloud an \"app\" (or \"application\" or \"website\") refers to a web application built using the Reflex framework, which can be deployed and managed within the Cloud platform. \n\nYou can deploy an app using the  command.\n\nThere are many actions you can take in the Cloud UI to manage your app. Below are some of the most common actions you may want to take.\n\nStopping an App\n..."
  },
  {
    "name": "Hosting Deploy With Github Actions",
    "parts": [
      "Hosting",
      "Deploy With Github Actions"
    ],
    "url": "docs/hosting/deploy-with-github-actions",
    "description": "Deploy with Github Actions\n\nThis GitHub Action simplifies the deployment of Reflex applications to Reflex Cloud. It handles setting up the environment, installing the Reflex CLI, and deploying your app with minimal configuration.\n\n**Features:**\n- Deploy Reflex apps directly from your GitHub repository to Reflex Cloud.\n- Supports subdirectory-based app structures.\n- Securely uses authentication tokens via GitHub Secrets.\n\nUsage\n..."
  },
  {
    "name": "Hosting Tokens",
    "parts": [
      "Hosting",
      "Tokens"
    ],
    "url": "docs/hosting/tokens",
    "description": "Tokens\n\nA token gives someone else all the permissions you have as a User or an Admin. They can run any Reflex Cloud command from the CLI as if they are you using the  flag. A good use case would be for GitHub actions (you store this token in the secrets).\n\nTokens are found on the Project List page under the tab . If you cannot find it click the Reflex Logo in the top left side of the page until it appears as in the image below."
  },
  {
    "name": "Hosting Reflex Branding",
    "parts": [
      "Hosting",
      "Reflex Branding"
    ],
    "url": "docs/hosting/reflex-branding",
    "description": "Reflex Branding\n\nRemove Reflex branding from your exported or deployed sites. \n\nBy default, Reflex branding, such as the \"Built with Reflex\" badge, will appear on all your published sites.\n\nHow to remove the Reflex branding from your app\n\nYou can turn off the Reflex branding, when deploying to Reflex Cloud, by adding  to the  in the  file.\n..."
  },
  {
    "name": "Hosting Regions",
    "parts": [
      "Hosting",
      "Regions"
    ],
    "url": "docs/hosting/regions",
    "description": "Regions\n\nTo scale your app you can choose different regions. Regions are different locations around the world where your app can be deployed. \n\nTo scale your app to multiple regions in the Cloud UI, click on the  tab in the Cloud UI on the app page, and then click on the  tab as shown below. Clicking on the  button will allow you to scale your app to multiple regions.\n\nThe images below show all the regions that can be deployed in.\n\nSelecting Regions to Deploy in the CLI\n..."
  },
  {
    "name": "Utility Methods Other Methods",
    "parts": [
      "Utility Methods",
      "Other Methods"
    ],
    "url": "docs/utility-methods/other-methods",
    "description": "Other Methods\n\n* : set all Vars to their default value for the given state (including substates).\n* : returns the value of a Var **without tracking changes to it**. This is useful\n   for serialization where the tracking wrapper is considered unserializable.\n* : returns all state Vars (and substates) as a dictionary. This is\n  used internally when a page is first loaded and needs to be \"hydrated\" and\n  sent to the client.\n\nSpecial Attributes\n..."
  },
  {
    "name": "Utility Methods Lifespan Tasks",
    "parts": [
      "Utility Methods",
      "Lifespan Tasks"
    ],
    "url": "docs/utility-methods/lifespan-tasks",
    "description": "Lifespan Tasks\n\n_Added in v0.5.2_\n\nLifespan tasks are coroutines that run when the backend server is running. They\nare useful for setting up the initial global state of the app, running periodic\ntasks, and cleaning up resources when the server is shut down.\n\nLifespan tasks are defined as async coroutines or async contextmanagers. To avoid\nblocking the event thread, never use  or perform non-async I/O within\n..."
  },
  {
    "name": "Utility Methods Exception Handlers",
    "parts": [
      "Utility Methods",
      "Exception Handlers"
    ],
    "url": "docs/utility-methods/exception-handlers",
    "description": "Exception handlers\n\n_Added in v0.5.7_\n\nExceptions handlers are functions that can be assigned to your app to handle exceptions that occur during the application runtime.\nThey are useful for customizing the response when an error occurs, logging errors, and performing cleanup tasks.\n\nTypes\n\nReflex support two type of exception handlers  and .\n..."
  },
  {
    "name": "Utility Methods Router Attributes",
    "parts": [
      "Utility Methods",
      "Router Attributes"
    ],
    "url": "docs/utility-methods/router-attributes",
    "description": "State Utility Methods\n\nThe state object has several methods and attributes that return information\nabout the current page, session, or state.\n\nRouter Attributes\n\nThe  attribute has several sub-attributes that provide various information:\n\n* : data about the current page and route\n..."
  },
  {
    "name": "Events Background Events",
    "parts": [
      "Events",
      "Background Events"
    ],
    "url": "docs/events/background-events",
    "description": "Background Tasks\n\nA background task is a special type of  that may run\nconcurrently with other  functions. This enables long-running\ntasks to execute without blocking UI interactivity.\n\nA background task is defined by decorating an async  method with\n.\n\nWhenever a background task needs to interact with the state, **it must enter an\n..."
  },
  {
    "name": "Events Setters",
    "parts": [
      "Events",
      "Setters"
    ],
    "url": "docs/events/setters",
    "description": "Setters\n\nEvery base var has a built-in event handler to set it's value for convenience, called .\n\nSay you wanted to change the value of the select component. You could write your own event handler to do this:\n\nOr you could could use a built-in setter for conciseness.\n\nIn this example, the setter for  is . Both of these examples are equivalent.\n..."
  },
  {
    "name": "Events Chaining Events",
    "parts": [
      "Events",
      "Chaining Events"
    ],
    "url": "docs/events/chaining-events",
    "description": "Chaining events\n\nCalling Event Handlers From Event Handlers\n\nYou can call other event handlers from event handlers to keep your code modular. Just use the  syntax to run another event handler. As always, you can yield within your function to send incremental updates to the frontend.\n\nReturning Events From Event Handlers\n\nSo far, we have only seen events that are triggered by components. However, an event handler can also return events.\n..."
  },
  {
    "name": "Events Decentralized Event Handlers",
    "parts": [
      "Events",
      "Decentralized Event Handlers"
    ],
    "url": "docs/events/decentralized-event-handlers",
    "description": "Decentralized Event Handlers\n\nOverview\n\nDecentralized event handlers allow you to define event handlers outside of state classes, providing more flexible code organization. This feature was introduced in Reflex v0.7.10 and enables a more modular approach to event handling.\n\nWith decentralized event handlers, you can:\n- Organize event handlers by feature rather than by state class\n- Separate UI logic from state management\n- Create more maintainable and scalable applications\n..."
  },
  {
    "name": "Events Event Actions",
    "parts": [
      "Events",
      "Event Actions"
    ],
    "url": "docs/events/event-actions",
    "description": "Event Actions\n\nIn Reflex, an event action is a special behavior that occurs during or after\nprocessing an event on the frontend.\n\nEvent actions can modify how the browser handles DOM events or throttle and\ndebounce events before they are processed by the backend.\n\nAn event action is specified by accessing attributes and methods present on all\nEventHandlers and EventSpecs.\n..."
  },
  {
    "name": "Events Event Arguments",
    "parts": [
      "Events",
      "Event Arguments"
    ],
    "url": "docs/events/event-arguments",
    "description": "Event Arguments\n\nThe event handler signature needs to match the event trigger definition argument count. If the event handler takes two arguments, the event trigger must be able to provide two arguments.\n\nHere is a simple example:\n\nThe event trigger here is  and it is called when the value changes at the end of an interaction. This event trigger passes one argument, which is the value of the slider. The event handler which is triggered by the event trigger must therefore take one argument, which is  here.\n\nHere is a form example:\n..."
  },
  {
    "name": "Events Special Events",
    "parts": [
      "Events",
      "Special Events"
    ],
    "url": "docs/events/special-events",
    "description": "Special Events\n\nReflex also has built-in special events can be found in the reference.\n\nFor example, an event handler can trigger an alert on the browser.\n\nSpecial events can also be triggered directly in the UI by attaching them to an event trigger."
  },
  {
    "name": "Events Events Overview",
    "parts": [
      "Events",
      "Events Overview"
    ],
    "url": "docs/events/events-overview",
    "description": "Events Overview\n\nEvents are composed of two parts: Event Triggers and Event Handlers.\n\n- **Events Handlers** are how the State of a Reflex application is updated. They are triggered by user interactions with the UI, such as clicking a button or hovering over an element. Events can also be triggered by the page loading or by other events.\n\n- **Event triggers** are component props that create an event to be sent to an event handler.\nEach component supports a set of events triggers. They are described in each component's documentation in the event trigger section.\n\nExample\n..."
  },
  {
    "name": "Events Page Load Events",
    "parts": [
      "Events",
      "Page Load Events"
    ],
    "url": "docs/events/page-load-events",
    "description": "Page Load Events\n\nYou can also specify a function to run when the page loads. This can be useful for fetching data once vs on every render or state change.\nIn this example, we fetch data when the page loads:\n\nAnother example would be checking if the user is authenticated when the page loads. If the user is not authenticated, we redirect them to the login page. If they are authenticated, we don't do anything, letting them access the page. This  event would be placed on every page that requires authentication to access."
  },
  {
    "name": "Events Yield Events",
    "parts": [
      "Events",
      "Yield Events"
    ],
    "url": "docs/events/yield-events",
    "description": "Yielding Updates\n\nA regular event handler will send a  when it has finished running. This works fine for basic event, but sometimes we need more complex logic. To update the UI multiple times in an event handler, we can  when we want to send an update.\n\nTo do so, we can use the Python keyword . For every yield inside the function, a  will be sent to the frontend with the changes up to this point in the execution of the event handler.\n\nThis example below shows how to yield 100 updates to the UI.\n\nHere is another example of yielding multiple updates with a loading icon.\n..."
  },
  {
    "name": "Assets Overview",
    "parts": [
      "Assets",
      "Overview"
    ],
    "url": "docs/assets/overview",
    "description": "Assets\n\nStatic files such as images and stylesheets can be placed in  folder of the project. These files can be referenced within your app.\n\nReferencing Assets\n\nThere are two ways to reference assets in your Reflex app:\n\n1. Direct Path Reference\n..."
  },
  {
    "name": "Assets Upload And Download Files",
    "parts": [
      "Assets",
      "Upload And Download Files"
    ],
    "url": "docs/assets/upload-and-download-files",
    "description": "Files\n\nIn addition to any assets you ship with your app, many web app will often need to receive or send files, whether you want to share media, allow user to import their data, or export some backend data.\n\nIn this section, we will cover all you need to know for manipulating files in Reflex.\n\nAssets vs Upload Directory\n\nBefore diving into file uploads and downloads, it's important to understand the difference between assets and the upload directory in Reflex:\n..."
  },
  {
    "name": "Pages Overview",
    "parts": [
      "Pages",
      "Overview"
    ],
    "url": "docs/pages/overview",
    "description": "Pages\n\nPages map components to different URLs in your app. This section covers creating pages, handling URL arguments, accessing query parameters, managing page metadata, and handling page load events.\n\nAdding a Page\n\nYou can create a page by defining a function that returns a component.\nBy default, the function name will be used as the route, but you can also specify a route.\n\nIn this example we create three pages:\n..."
  },
  {
    "name": "Pages Dynamic Routing",
    "parts": [
      "Pages",
      "Dynamic Routing"
    ],
    "url": "docs/pages/dynamic-routing",
    "description": "Dynamic Routes\n\nDynamic routes in Reflex allow you to handle varying URL structures, enabling you to create flexible\nand adaptable web applications. This section covers regular dynamic routes, catch-all routes,\nand optional catch-all routes, each with detailed examples.\n\nRegular Dynamic Routes\n\nRegular dynamic routes in Reflex allow you to match specific segments in a URL dynamically. A regular dynamic route is defined by square brackets in a route string / url pattern. For example  or . These dynamic route arguments can be accessed through a state var. For the examples above they would be  and  respectively.\n..."
  },
  {
    "name": "Authentication Authentication Overview",
    "parts": [
      "Authentication",
      "Authentication Overview"
    ],
    "url": "docs/authentication/authentication-overview",
    "description": "Authentication Overview\n\nMany apps require authentication to manage users. There are a few different ways to accomplish this in Reflex:\n\nWe have solutions that currently exist outside of the core framework:\n\n1. Local Auth: Uses your own database: https://github.com/masenf/reflex-local-auth\n2. Google Auth: Uses sign in with Google: https://github.com/masenf/reflex-google-auth\n3. Captcha: Generates tests that humans can pass but automated systems cannot: https://github.com/masenf/reflex-google-recaptcha-v2\n4. Magic Link Auth: A passwordless login method that sends a unique, one-time-use URL to a user's email: https://github.com/masenf/reflex-magic-link-auth\n..."
  },
  {
    "name": "Client Storage Overview",
    "parts": [
      "Client Storage",
      "Overview"
    ],
    "url": "docs/client-storage/overview",
    "description": "Client-storage\n\nYou can use the browser's local storage to persist state between sessions.\nThis allows user preferences, authentication cookies, other bits of information\nto be stored on the client and accessed from different browser tabs.\n\nA client-side storage var looks and acts like a normal  var, except the\ndefault value is either  or  depending on where the\nvalue should be stored. The key name will be based on the var name, but this\ncan be overridden by passing  as a keyword argument.\n..."
  },
  {
    "name": "Getting Started Introduction",
    "parts": [
      "Getting Started",
      "Introduction"
    ],
    "url": "docs/getting-started/introduction",
    "description": "Introduction\n\n**Reflex** is an open-source framework for quickly building beautiful, interactive web applications in **pure Python**.\n\nGoals\n\nAn example: Make it count\n\nHere, we go over a simple counter app that lets the user count up or down.\n..."
  },
  {
    "name": "Getting Started Basics",
    "parts": [
      "Getting Started",
      "Basics"
    ],
    "url": "docs/getting-started/basics",
    "description": "Reflex Basics\n\nThis page gives an introduction to the most common concepts that you will use to build Reflex apps.\n\nInstall  using pip.\n\nImport the  library to get started.\n\nCreating and nesting components\n..."
  },
  {
    "name": "Getting Started Dashboard Tutorial",
    "parts": [
      "Getting Started",
      "Dashboard Tutorial"
    ],
    "url": "docs/getting-started/dashboard-tutorial",
    "description": "Tutorial: Data Dashboard\n\nDuring this tutorial you will build a small data dashboard, where you can input data and it will be rendered in table and a graph. This tutorial does not assume any existing Reflex knowledge, but we do recommend checking out the quick Basics Guide first. \n\nThe techniques you’ll learn in the tutorial are fundamental to building any Reflex app, and fully understanding it will give you a deep understanding of Reflex.\n\nThis tutorial is divided into several sections:\n\n- **Setup for the Tutorial**: A starting point to follow the tutorial\n- **Overview**: The fundamentals of Reflex UI (components and props)\n..."
  },
  {
    "name": "Getting Started Chatapp Tutorial",
    "parts": [
      "Getting Started",
      "Chatapp Tutorial"
    ],
    "url": "docs/getting-started/chatapp-tutorial",
    "description": "Interactive Tutorial: AI Chat App\n\nThis tutorial will walk you through building an AI chat app with Reflex. This app is fairly complex, but don't worry - we'll break it down into small steps.\n\nYou can find the full source code for this app here.\n\nWhat You'll Learn\n\nIn this tutorial you'll learn how to:\n..."
  },
  {
    "name": "Getting Started Project Structure",
    "parts": [
      "Getting Started",
      "Project Structure"
    ],
    "url": "docs/getting-started/project-structure",
    "description": "Project Structure\n\nDirectory Structure\n\nLet's create a new app called \n\nThis will create a directory structure like this:\n\nLet's go over each of these directories and files.\n..."
  },
  {
    "name": "Getting Started Installation",
    "parts": [
      "Getting Started",
      "Installation"
    ],
    "url": "docs/getting-started/installation",
    "description": "Installation\n\nReflex requires Python 3.10+.\n\nVirtual Environment\n\nWe **highly recommend** creating a virtual environment for your project.\n\nvenv is the standard option. conda and poetry are some alternatives.\n..."
  }
]
