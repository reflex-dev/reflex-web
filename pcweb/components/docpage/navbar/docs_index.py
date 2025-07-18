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
    "name": "UI Overview",
    "parts": [
      "UI",
      "Overview"
    ],
    "url": "docs/ui/overview",
    "description": "UI Overview\n\nComponents are the building blocks for your app's user interface (UI). They are the visual elements that make up your app, like buttons, text, and images.\n\nComponent Basics\n\nComponents are made up of children and props.\n\nLet's take a look at the  component.\n..."
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
    "name": "Vars Var Operations",
    "parts": [
      "Vars",
      "Var Operations"
    ],
    "url": "docs/vars/var-operations",
    "description": "Var Operations\n\nVar operations transform the placeholder representation of the value on the\nfrontend and provide a way to perform basic operations on the Var without having\nto define a computed var.\n\nWithin your frontend components, you cannot use arbitrary Python functions on\nthe state vars. For example, the following code will **not work.**\n\nThis is because we compile the frontend to Javascript, but the value of\n..."
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
    "name": "Database Overview",
    "parts": [
      "Database",
      "Overview"
    ],
    "url": "docs/database/overview",
    "description": "Database\n\nReflex uses sqlmodel to provide a built-in ORM wrapping SQLAlchemy.\n\nThe examples on this page refer specifically to how Reflex uses various tools to\nexpose an integrated database interface.  Only basic use cases will be covered\nbelow, but you can refer to the\nsqlmodel tutorial\nfor more examples and information, just replace  with  and\n with\n..."
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
    "description": ""
  },
  {
    "name": "Enterprise Overview",
    "parts": [
      "Enterprise",
      "Overview"
    ],
    "url": "docs/enterprise/overview",
    "description": "Reflex Enterprise\n\nReflex Enterprise is a package containing paid features built on top of Reflex.\n\nInstallation\n\n must be installed alongside  to access the enterprise features.\n\nYou can install it from pypi with the following command:\n..."
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
    "name": "Enterprise Drag And Drop",
    "parts": [
      "Enterprise",
      "Drag And Drop"
    ],
    "url": "docs/enterprise/drag-and-drop",
    "description": "Drag and Drop\n\nReflex Enterprise provides comprehensive drag and drop functionality for creating interactive UI elements using the  module. Built on top of react-dnd, it offers both high-level components for common use cases and low-level hooks for advanced scenarios.\n\nBasic Usage\n\nSimple Drag and Drop\n\nHere's a basic example showing how to create a draggable item and drop target:\n..."
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
    "name": "Enterprise Single Port Proxy",
    "parts": [
      "Enterprise",
      "Single Port Proxy"
    ],
    "url": "docs/enterprise/single-port-proxy",
    "description": "Single Port Proxy\n\nEnable single-port deployment by proxying the backend to the frontend port.\n\nConfiguration\n\nThis allows your application to run on a single port, which is useful for deployment scenarios where you can only expose one port."
  },
  {
    "name": "Enterprise Mantine Pill",
    "parts": [
      "Enterprise",
      "Mantine",
      "Pill"
    ],
    "url": "docs/enterprise/mantine/pill",
    "description": "Pill\n\n is a wrapping of the mantine component Pill. It is a simple component that can be used to display a small piece of information, such as a tag or a label. It can be used in various contexts, such as in a list of tags or labels, or as a standalone component.\n\nPill Group\n allows grouping multiple  components together, with a predefined layout.\n\nPillsInput\n\n is a wrapping of the mantine component PillsInput. It is an utility component that can be used to display a list of tags or labels. It can be used in various contexts, such as in a form or as a standalone component.\n..."
  },
  {
    "name": "Enterprise Mantine Semi Circle Progress",
    "parts": [
      "Enterprise",
      "Mantine",
      "Semi Circle Progress"
    ],
    "url": "docs/enterprise/mantine/semi-circle-progress",
    "description": "Semi Circle Progress component\n is a component for displaying progress in a semi-circular format. It is useful for visualizing completion percentages or other metrics in a compact and visually appealing way."
  },
  {
    "name": "Enterprise Mantine Spoiler",
    "parts": [
      "Enterprise",
      "Mantine",
      "Spoiler"
    ],
    "url": "docs/enterprise/mantine/spoiler",
    "description": "Spoiler component\n\n is a component that allows you to hide or reveal content. It is useful for displaying additional information or details that may not be immediately relevant to the user."
  },
  {
    "name": "Enterprise Mantine Autocomplete",
    "parts": [
      "Enterprise",
      "Mantine",
      "Autocomplete"
    ],
    "url": "docs/enterprise/mantine/autocomplete",
    "description": "Autocomplete component\n\n is a component for providing suggestions as the user types. It is useful for enhancing user experience by offering relevant options based on input."
  },
  {
    "name": "Enterprise Mantine Timeline",
    "parts": [
      "Enterprise",
      "Mantine",
      "Timeline"
    ],
    "url": "docs/enterprise/mantine/timeline",
    "description": "Timeline component\n is a component for displaying a sequence of events or milestones in a linear format. It is useful for visualizing progress, history, or any sequential information."
  },
  {
    "name": "Enterprise Mantine Index",
    "parts": [
      "Enterprise",
      "Mantine",
      "Index"
    ],
    "url": "docs/enterprise/mantine/index",
    "description": "Mantine\n\nMantine is a React component library that provides a set of high-quality components and hooks for building modern web applications. It is designed to be flexible, customizable, and easy to use, making it a popular choice among developers.\n\nSome of those components have been integrated into Reflex Enterprise, allowing you to use them in your Reflex applications. The following components are available:\n- JsonInput\n- Autocomplete\n- ComboBox\n- Multiselect\n- Pill\n..."
  },
  {
    "name": "Enterprise Mantine Ring Progress",
    "parts": [
      "Enterprise",
      "Mantine",
      "Ring Progress"
    ],
    "url": "docs/enterprise/mantine/ring-progress",
    "description": "Ring Progress component\n\n is a component for displaying progress in a circular format. It is useful for visualizing completion percentages or other metrics in a compact and visually appealing way."
  },
  {
    "name": "Enterprise Mantine Number Formatter",
    "parts": [
      "Enterprise",
      "Mantine",
      "Number Formatter"
    ],
    "url": "docs/enterprise/mantine/number-formatter",
    "description": "Number Formatter component\n is a component for formatting numbers in a user-friendly way. It allows you to specify the format, precision, and other options for displaying numbers."
  },
  {
    "name": "Enterprise Mantine Tags Input",
    "parts": [
      "Enterprise",
      "Mantine",
      "Tags Input"
    ],
    "url": "docs/enterprise/mantine/tags-input",
    "description": "TagsInput\n\n is a wrapping of the mantine component TagsInput. It is an utility component that can be used to display a list of tags or labels. It can be used in various contexts, such as in a form or as a standalone component.\n\nBasic Example\n\nState Example"
  },
  {
    "name": "Enterprise Mantine Multi Select",
    "parts": [
      "Enterprise",
      "Mantine",
      "Multi Select"
    ],
    "url": "docs/enterprise/mantine/multi-select",
    "description": "MultiSelect component\n\n is a component for selecting multiple options from a list. It allows users to choose one or more items, making it suitable for scenarios where multiple selections are required."
  },
  {
    "name": "Enterprise Mantine Tree",
    "parts": [
      "Enterprise",
      "Mantine",
      "Tree"
    ],
    "url": "docs/enterprise/mantine/tree",
    "description": "Tree component\n\n is a component for displaying hierarchical data in a tree structure. It allows users to expand and collapse nodes, making it easy to navigate through large datasets."
  },
  {
    "name": "Enterprise Mantine Collapse",
    "parts": [
      "Enterprise",
      "Mantine",
      "Collapse"
    ],
    "url": "docs/enterprise/mantine/collapse",
    "description": "Collapse component\n\n is a component that allows you to create collapsible sections in your application. It is useful for hiding or showing content based on user interaction, such as clicking a button or a link."
  },
  {
    "name": "Enterprise Mantine JSON Input",
    "parts": [
      "Enterprise",
      "Mantine",
      "JSON Input"
    ],
    "url": "docs/enterprise/mantine/json-input",
    "description": "JSON Input\n\n is a component that allows you to input JSON data in a user-friendly way. It provides validation and formatting features to ensure that the JSON data is correctly structured.\n\nExample"
  },
  {
    "name": "Enterprise Mantine Combobox",
    "parts": [
      "Enterprise",
      "Mantine",
      "Combobox"
    ],
    "url": "docs/enterprise/mantine/combobox",
    "description": "Combobox\n\n is a wrapping of the mantine component Combobox. It is a simple component that can be used to display a list of options, and allows the user to select one or more options from the list. It can be used in various contexts, such as in a form or as a standalone component."
  },
  {
    "name": "Enterprise Mantine Loading Overlay",
    "parts": [
      "Enterprise",
      "Mantine",
      "Loading Overlay"
    ],
    "url": "docs/enterprise/mantine/loading-overlay",
    "description": "Loading Overlay component\n is a component that displays a loading overlay on top of its children. It is useful for indicating that a process is ongoing and prevents user interaction with the underlying content."
  },
  {
    "name": "Enterprise Ag Grid Model Wrapper",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Model Wrapper"
    ],
    "url": "docs/enterprise/ag-grid/model-wrapper",
    "description": "Model Wrapper\n\nA model wrapper is an utility used to wrap a database model and provide a consistent interface over it. It allows automatically adding new rows to the database, updating existing rows, and deleting rows.\n\nDefault Model Wrapper\n\nYou can use the basic functionality of the model wrapper by using the  function. This function takes a database model and returns a wrapper object that can be used to interact with the model.\n\nBy default the model_wrapper use the infinite rows model from AgGrid.\n..."
  },
  {
    "name": "Enterprise Map Index",
    "parts": [
      "Enterprise",
      "Map",
      "Index"
    ],
    "url": "docs/enterprise/map/index",
    "description": "Interactive Maps\n\nThe map components in Reflex Enterprise provide interactive mapping capabilities built on top of **Leaflet**, one of the most popular open-source JavaScript mapping libraries. These components enable you to create rich, interactive maps with markers, layers, controls, and event handling.\n\n🌍 **View Live Demo** - See the map components in action with interactive examples.\n\nInstallation & Setup\n\nMap components are included with . No additional installation is required.\n..."
  },
  {
    "name": "Enterprise Ag Grid Aligned Grids",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Aligned Grids"
    ],
    "url": "docs/enterprise/ag-grid/aligned-grids",
    "description": "AgGrid provides a way to align multiple grids together. This is useful when you want to display related data in a synchronized manner.\n\nYou can do so through the  prop. This prop takes a list of grid IDs that you want to align."
  },
  {
    "name": "Enterprise Ag Grid Value Transformers",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Value Transformers"
    ],
    "url": "docs/enterprise/ag-grid/value-transformers",
    "description": "Value Transformers\n\nAgGrid allow you to apply transformers based on the column of your grid. This allow you to perform operations on the data before displaying it on the grid, without having to pre-process the data on the backend, reducing the load on your application.\n\nTOC:\n- Value Getter\n- Value Formatter\n\nValue Getter\n..."
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
    "name": "Enterprise Ag Grid Column Defs",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Column Defs"
    ],
    "url": "docs/enterprise/ag-grid/column-defs",
    "description": "Column Definitions\n\nBasic Columns\n\nAgGrid allows you to define the columns of your grid, passed to the prop . Each dictionary represents a column.\n\nHere we define a grid with 3 columns:\n\nTo set default properties for all your columns, you can define  in your grid:"
  },
  {
    "name": "Enterprise Ag Grid Theme",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Theme"
    ],
    "url": "docs/enterprise/ag-grid/theme",
    "description": "Themes\n\nYou can style your grid with a theme. AG Grid includes the following themes:\n\n1. \n2. \n3. \n4. \n\nThe grid uses  by default. To use any other theme, set it using the  prop, i.e. .\n..."
  },
  {
    "name": "Enterprise Ag Grid Index",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Index"
    ],
    "url": "docs/enterprise/ag-grid/index",
    "description": "AG Grid\n\nAG Grid Features\n\nYour First Reflex AG Grid\n\nA basic Reflex AG Grid contains column definitions , which define the columns to be displayed in the grid, and , which contains the data to be displayed in the grid.\n\nEach grid also requires a unique , which is needed to uniquely identify the Ag-Grid instance on the page. If you have multiple grids on the same page, each grid must have a unique  so that it can be correctly rendered and managed.\n..."
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
    "name": "API Reference Special Events",
    "parts": [
      "API Reference",
      "Special Events"
    ],
    "url": "docs/api-reference/special-events",
    "description": "Special Events\n\nReflex includes a set of built-in special events that can be utilized as event triggers\nor returned from event handlers in your applications. These events enhance interactivity and user experience.\nBelow are the special events available in Reflex, along with explanations of their functionality:\n\nrx.console_log\n\nPerform a console.log in the browser's console.\n..."
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
    "name": "API Reference Plugins",
    "parts": [
      "API Reference",
      "Plugins"
    ],
    "url": "docs/api-reference/plugins",
    "description": "Plugins\n\nReflex supports a plugin system that allows you to extend the framework's functionality during the compilation process. Plugins can add frontend dependencies, modify build configurations, generate static assets, and perform custom tasks before compilation.\n\nConfiguring Plugins\n\nPlugins are configured in your  file using the  parameter:\n\nBuilt-in Plugins\n..."
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
    "name": "Custom Components Prerequisites For Publishing",
    "parts": [
      "Custom Components",
      "Prerequisites For Publishing"
    ],
    "url": "docs/custom-components/prerequisites-for-publishing",
    "description": "Python Package Index\n\nIn order to publish a Python package, you need to use a publishing utility. Any would work, but we recommend either Twine or (uv)[https://docs.astral.sh/uv/guides/package/#publishing-your-package].\n\nPyPI\n\nIt is straightforward to create accounts and API tokens with PyPI. There is official help on the PyPI website. For a quick reference here, go to the top right corner of the PyPI website and look for the button to register and fill out personal information.\n\nA user can use username and password to authenticate with PyPI when publishing.\n..."
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
    "name": "Library Disclosure Accordion",
    "parts": [
      "Library",
      "Disclosure",
      "Accordion"
    ],
    "url": "docs/library/disclosure/accordion",
    "description": "Accordion\n\nAn accordion is a vertically stacked set of interactive headings that each reveal an associated section of content.\nThe accordion component is made up of , which is the root of the component and takes in an ,\nwhich contains all the contents of the collapsible section.\n\nBasic Example\n\nStyling\n..."
  },
  {
    "name": "Library Disclosure Segmented Control",
    "parts": [
      "Library",
      "Disclosure",
      "Segmented Control"
    ],
    "url": "docs/library/disclosure/segmented-control",
    "description": "Segmented Control\n\nSegmented Control offers a clear and accessible way to switch between predefined values and views, e.g., \"Inbox,\" \"Drafts,\" and \"Sent.\"\n\nWith Segmented Control, you can make mutually exclusive choices, where only one option can be active at a time, clear and accessible. Without Segmented Control, end users might have to deal with controls like dropdowns or multiple buttons that don't clearly convey state or group options together visually.\n\nBasic Example\n\nThe  component is made up of a  which groups .\n..."
  },
  {
    "name": "Library Disclosure Tabs",
    "parts": [
      "Library",
      "Disclosure",
      "Tabs"
    ],
    "url": "docs/library/disclosure/tabs",
    "description": "Tabs\n\nTabs are a set of layered sections of content—known as tab panels that are displayed one at a time.\nThey facilitate the organization and navigation between sets of content that share a connection and exist at a similar level of hierarchy.\n\nBasic Example\n\nThe  component is made up of a  which groups  and  parts.\n\nStyling\n..."
  },
  {
    "name": "Library Forms Input",
    "parts": [
      "Library",
      "Forms",
      "Input"
    ],
    "url": "docs/library/forms/input",
    "description": "Input\n\nThe  component is an input field that users can type into.\n\nBasic Example\n\nThe  event handler is called when focus has left the  for example, it’s called when the user clicks outside of a focused text input.\n\nThe  event handler is called when the  of  has changed.\n..."
  },
  {
    "name": "Library Forms Button",
    "parts": [
      "Library",
      "Forms",
      "Button"
    ],
    "url": "docs/library/forms/button",
    "description": "Button\n\nButtons are essential elements in your application's user interface that users can click to trigger events.\n\nBasic Example\n\nThe  trigger is called when the button is clicked.\n\nLoading and Disabled\n..."
  },
  {
    "name": "Library Forms Slider",
    "parts": [
      "Library",
      "Forms",
      "Slider"
    ],
    "url": "docs/library/forms/slider",
    "description": "Slider\n\nProvides user selection from a range of values. The\n\nBasic Example\n\nThe slider can be controlled by a single value or a range of values. Slider can be hooked to state to control its value. Passing a list of two values creates a range slider.\n\nRange Slider\n..."
  },
  {
    "name": "Library Forms Checkbox",
    "parts": [
      "Library",
      "Forms",
      "Checkbox"
    ],
    "url": "docs/library/forms/checkbox",
    "description": "Checkbox\n\nBasic Example\n\nThe  trigger is called when the  is clicked.\n\nThe  prop is used to set the  as a controlled component."
  },
  {
    "name": "Library Forms Form",
    "parts": [
      "Library",
      "Forms",
      "Form"
    ],
    "url": "docs/library/forms/form",
    "description": "Form\n\nForms are used to collect user input. The  component is used to group inputs and submit them together.\n\nThe form component's children can be form controls such as , , , , ,  or . The controls should have a  attribute that is used to identify the control in the form data. The  event trigger submits the form data as a dictionary to the  event handler.\n\nThe form is submitted when the user clicks the submit button or presses enter on the form controls.\n\nDynamic Forms\n..."
  },
  {
    "name": "Library Forms Select",
    "parts": [
      "Library",
      "Forms",
      "Select"
    ],
    "url": "docs/library/forms/select",
    "description": "Select\n\nDisplays a list of options for the user to pick from—triggered by a button.\n\nThe  event handler acts in a similar way to the  and is called when the open state of the select changes.\n\nSubmitting a form using select\n\nThe  prop is needed to submit with its owning form as part of a name/value pair.\n..."
  },
  {
    "name": "Library Forms Text Area",
    "parts": [
      "Library",
      "Forms",
      "Text Area"
    ],
    "url": "docs/library/forms/text-area",
    "description": "Text Area\n\nA text area is a multi-line text input field.\n\nBasic Example\n\nThe text area component can be controlled by a single value. The  prop can be used to update the value when the text area loses focus.\n\nText Area in forms\n..."
  },
  {
    "name": "Library Forms Upload",
    "parts": [
      "Library",
      "Forms",
      "Upload"
    ],
    "url": "docs/library/forms/upload",
    "description": "File Upload\n\nReflex makes it simple to add file upload functionality to your app. You can let users select files, store them on your server, and display or process them as needed. Below is a minimal example that demonstrates how to upload files, save them to disk, and display uploaded images using application state.\n\nBasic File Upload Example\n\nYou can let users upload files and keep track of them in your app’s state. The example below allows users to upload files, saves them using the backend, and then displays the uploaded files as images.\n\nHow File Upload Works\n..."
  },
  {
    "name": "Library Forms Radio Group",
    "parts": [
      "Library",
      "Forms",
      "Radio Group"
    ],
    "url": "docs/library/forms/radio-group",
    "description": "Radio Group\n\nA set of interactive radio buttons where only one can be selected at a time.\n\nBasic example\n\nSubmitting a form using Radio Group\n\nThe  prop is used to name the group. It is submitted with its owning form as part of a name/value pair.\n..."
  },
  {
    "name": "Library Forms Switch",
    "parts": [
      "Library",
      "Forms",
      "Switch"
    ],
    "url": "docs/library/forms/switch",
    "description": "Switch\n\nA toggle switch alternative to the checkbox.\n\nBasic Example\n\nHere is a basic example of a switch. We use the  trigger to toggle the value in the state.\n\nControl the value\n..."
  },
  {
    "name": "Library Forms Input Low Level",
    "parts": [
      "Library",
      "Forms",
      "Low Level"
    ],
    "url": "docs/library/forms/input/low",
    "description": "Input\n\nA text field is an input field that users can type into. This component uses Radix's text field component.\n\nOverview\n\nThe TextField component is used to capture user input and can include an optional slot for buttons and icons. It is based on the <div> element and supports common margin props.\n\nBasic Example\n..."
  },
  {
    "name": "Library Forms Select Low Level",
    "parts": [
      "Library",
      "Forms",
      "Low Level"
    ],
    "url": "docs/library/forms/select/low",
    "description": "Select\n\nDisplays a list of options for the user to pick from, triggered by a button.\n\nBasic Example\n\nUsage\n\nDisabling\n..."
  },
  {
    "name": "Library Forms Form Low Level",
    "parts": [
      "Library",
      "Forms",
      "Low Level"
    ],
    "url": "docs/library/forms/form/low",
    "description": "Form\n\nForms are used to collect information from your users. Forms group the inputs and submit them together.\n\nBasic Example\n\nHere is an example of a form collecting an email address, with built-in validation on the email. If email entered is invalid, the form cannot be submitted. Note that the  button is not automatically disabled. It is still clickable, but does not submit the form data. After successful submission, an alert window shows up and the form is cleared. There are a few  containers used in the example to control the layout of the form components.\n\nIn this example, the  has an attribute  and the  has the attribute . Those are required for the form to validate the input by its type. The prop  is required when using other components to construct a Form component. This example has used  to construct the Form Control and  the Form Submit.\n..."
  },
  {
    "name": "Library Tables And Data Grids Data Table",
    "parts": [
      "Library",
      "Tables And Data Grids",
      "Data Table"
    ],
    "url": "docs/library/tables-and-data-grids/data-table",
    "description": "Data Table\n\nThe data table component is a great way to display static data in a table format.\nYou can pass in a pandas dataframe to the data prop to create the table.\n\nIn this example we will read data from a csv file, convert it to a pandas dataframe and display it in a data_table.\n\nWe will also add a search, pagination, sorting to the data_table to make it more accessible.\n\nIf you want to add, edit or remove data in your app or deal with anything but static data then the []({library.tables_and_data_grids.table.path}) might be a better fit for your use case.\n..."
  },
  {
    "name": "Library Layout Stack",
    "parts": [
      "Library",
      "Layout",
      "Stack"
    ],
    "url": "docs/library/layout/stack",
    "description": "Stack\n\n is a layout component used to group elements together and apply a space between them.\n\n is used to stack elements in the vertical direction.\n\n is used to stack elements in the horizontal direction.\n\n is used to stack elements in the vertical or horizontal direction.\n..."
  },
  {
    "name": "Library Layout Card",
    "parts": [
      "Library",
      "Layout",
      "Card"
    ],
    "url": "docs/library/layout/card",
    "description": "Card\n\nA Card component is used for grouping related components. It is similar to the Box, except it has a\nborder, uses the theme colors and border radius, and provides a  prop to control spacing\nand margin according to the Radix  -  scale.\n\nThe Card requires less styling than a Box to achieve consistent visual results when used with\nthemes.\n\nBasic Example\n..."
  },
  {
    "name": "Library Tables And Data Grids Data Editor",
    "parts": [
      "Library",
      "Tables And Data Grids",
      "Data Editor"
    ],
    "url": "docs/library/tables-and-data-grids/data-editor",
    "description": "Data Editor\n\nA datagrid editor based on Glide Data Grid\n\nThis component is introduced as an alternative to the datatable to support editing the displayed data.\n\nColumns\n\nThe columns definition should be a  of , each  describing the associated columns.\nProperty of a column dict:\n..."
  },
  {
    "name": "Library Tables And Data Grids Table",
    "parts": [
      "Library",
      "Tables And Data Grids",
      "Table"
    ],
    "url": "docs/library/tables-and-data-grids/table",
    "description": "Table\n\nA semantic table for presenting tabular data.\n\nIf you just want to represent static data then the []({library.tables_and_data_grids.data_table.path}) might be a better fit for your use case as it comes with in-built pagination, search and sorting.\n\nBasic Example\n\nShowing State data (using foreach)\n..."
  },
  {
    "name": "Library Layout Fragment",
    "parts": [
      "Library",
      "Layout",
      "Fragment"
    ],
    "url": "docs/library/layout/fragment",
    "description": "Fragment\n\nA Fragment is a Component that allow you to group multiple Components without a wrapper node.\n\nRefer to the React docs at React/Fragment for more information on its use-case."
  },
  {
    "name": "Library Layout Container",
    "parts": [
      "Library",
      "Layout",
      "Container"
    ],
    "url": "docs/library/layout/container",
    "description": "Container\n\nConstrains the maximum width of page content, while keeping flexible margins\nfor responsive layouts.\n\nA Container is generally used to wrap the main content for a page.\n\nBasic Example"
  },
  {
    "name": "Library Layout Aspect Ratio",
    "parts": [
      "Library",
      "Layout",
      "Aspect Ratio"
    ],
    "url": "docs/library/layout/aspect-ratio",
    "description": "Aspect Ratio\n\nDisplays content with a desired ratio.\n\nBasic Example\n\nSetting the  prop will adjust the width or height\nof the content such that the  divided by the  equals the .\nFor responsive scaling, set the  or  of the content to ."
  },
  {
    "name": "Library Layout Flex",
    "parts": [
      "Library",
      "Layout",
      "Flex"
    ],
    "url": "docs/library/layout/flex",
    "description": "Flex\n\nThe Flex component is used to make flexbox layouts.\nIt makes it simple to arrange  child components in horizontal or vertical directions, apply wrapping,\njustify and align  content, and automatically size components based on available space, making it\nideal for building responsive layouts.\n\nBy default, children are arranged horizontally () without wrapping.\n\nBasic Example\n..."
  },
  {
    "name": "Library Layout Separator",
    "parts": [
      "Library",
      "Layout",
      "Separator"
    ],
    "url": "docs/library/layout/separator",
    "description": "Separator\n\nVisually or semantically separates content.\n\nBasic Example\n\nSize\n\nThe  prop controls how long the separator is. Using  will make\nthe separator fill the parent container. Setting CSS  or  prop to\n..."
  },
  {
    "name": "Library Layout Grid",
    "parts": [
      "Library",
      "Layout",
      "Grid"
    ],
    "url": "docs/library/layout/grid",
    "description": "Grid\n\nComponent for creating grid layouts. Either  or  may be specified.\n\nBasic Example"
  },
  {
    "name": "Library Layout Box",
    "parts": [
      "Library",
      "Layout",
      "Box"
    ],
    "url": "docs/library/layout/box",
    "description": "Box\n\nBox is a generic container component that can be used to group other components.\n\nBy default, the Box component is based on the  and rendered as a block element. It's primary use is for applying styles.\n\nBasic Example\n\nBackground\n..."
  },
  {
    "name": "Library Layout Section",
    "parts": [
      "Library",
      "Layout",
      "Section"
    ],
    "url": "docs/library/layout/section",
    "description": "Section\n\nDenotes a section of page content, providing vertical padding by default.\n\nPrimarily this is a semantic component that is used to group related textual content.\n\nBasic Example"
  },
  {
    "name": "Library Layout Inset",
    "parts": [
      "Library",
      "Layout",
      "Inset"
    ],
    "url": "docs/library/layout/inset",
    "description": "Inset\n\nApplies a negative margin to allow content to bleed into the surrounding container.\n\nBasic Example\n\nNesting an Inset component inside a Card will render the content from edge to edge of the card.\n\nOther Directions\n..."
  },
  {
    "name": "Library Layout Spacer",
    "parts": [
      "Library",
      "Layout",
      "Spacer"
    ],
    "url": "docs/library/layout/spacer",
    "description": "Spacer\n\nCreates an adjustable, empty space that can be used to tune the spacing between child elements within .\n\nAs ,  and  are all built from , it is possible to also use  inside of these components."
  },
  {
    "name": "Library Layout Center",
    "parts": [
      "Library",
      "Layout",
      "Center"
    ],
    "url": "docs/library/layout/center",
    "description": "Center\n\n is a component that centers its children within itself. It is based on the  component and therefore inherits all of its props."
  },
  {
    "name": "Library Other Html Embed",
    "parts": [
      "Library",
      "Other",
      "Html Embed"
    ],
    "url": "docs/library/other/html-embed",
    "description": "HTML Embed\n\nThe HTML component can be used to render raw HTML code.\n\nBefore you reach for this component, consider using Reflex's raw HTML element support instead.\n\nIn this example, we render an image."
  },
  {
    "name": "Library Other Script",
    "parts": [
      "Library",
      "Other",
      "Script"
    ],
    "url": "docs/library/other/script",
    "description": "Script\n\nThe Script component can be used to include inline javascript or javascript files by URL.\n\nIt uses the  component to inject the script and can be safely used with conditional rendering to allow script side effects to be controlled by the state.\n\nComplex inline scripting should be avoided.\nIf the code to be included is more than a couple lines, it is more maintainable to implement it in a separate javascript file in the  directory and include it via the  prop.\n\nThis component is particularly helpful for including tracking and social scripts.\n..."
  },
  {
    "name": "Library Other Clipboard",
    "parts": [
      "Library",
      "Other",
      "Clipboard"
    ],
    "url": "docs/library/other/clipboard",
    "description": "Clipboard\n\n_New in 0.5.6_\n\nThe Clipboard component can be used to respond to paste events with complex data.\n\nIf the Clipboard component is included in a page without children,\n, then it will attach to the document's  event handler\nand will be triggered when data is pasted anywhere into the page.\n..."
  },
  {
    "name": "Library Other Skeleton",
    "parts": [
      "Library",
      "Other",
      "Skeleton"
    ],
    "url": "docs/library/other/skeleton",
    "description": "Skeleton (loading placeholder)\n\n is a loading placeholder component that serves as a visual placeholder while content is loading.\nIt is useful for maintaining the layout's structure and providing users with a sense of progression while awaiting the final content.\n\nWhen using  with text, wrap the text itself instead of the parent element to have a placeholder of the same size.\n\nUse the loading prop to control whether the skeleton or its children are displayed. Skeleton preserves the dimensions of children when they are hidden and disables interactive elements."
  },
  {
    "name": "Library Other Theme",
    "parts": [
      "Library",
      "Other",
      "Theme"
    ],
    "url": "docs/library/other/theme",
    "description": "Theme\n\n The  component is used to change the theme of the application. The  can be set directly in the rx.App.\n\n # Theme Panel\n\n The  component is a container for the  component. It provides a way to change the theme of the application.\n\n The theme panel is closed by default. You can set it open ."
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
    "name": "Library Other Html",
    "parts": [
      "Library",
      "Other",
      "Html"
    ],
    "url": "docs/library/other/html",
    "description": "HTML\n\nReflex also provides a set of HTML elements that can be used to create web pages. These elements are the same as the HTML elements that are used in web development. These elements come unstyled bhy default. You can style them using style props or tailwindcss classes.\n\nThe following is a list of the HTML elements that are available in Reflex:"
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
    "name": "Library Data Display Callout Low Level",
    "parts": [
      "Library",
      "Data Display",
      "Low Level"
    ],
    "url": "docs/library/data-display/callout/low",
    "description": "Callout\n\nA  is a short message to attract user's attention.\n\nThe  component is made up of a , which groups  and  parts. This component is based on the  element and supports common margin props.\n\nThe  provides width and height for the  associated with the . This component is based on the  element. See the **icon** component for all icons that are available.\n\nThe  renders the callout text. This component is based on the  element.\n..."
  },
  {
    "name": "Library Data Display Scroll Area",
    "parts": [
      "Library",
      "Data Display",
      "Scroll Area"
    ],
    "url": "docs/library/data-display/scroll-area",
    "description": "Scroll Area\n\nCustom styled, cross-browser scrollable area using native functionality.\n\nBasic Example\n\nControl the scrollable axes\n\nUse the  prop to limit scrollable axes. This prop can take values .\n..."
  },
  {
    "name": "Library Data Display Code Block",
    "parts": [
      "Library",
      "Data Display",
      "Code Block"
    ],
    "url": "docs/library/data-display/code-block",
    "description": "Code Block\n\nThe Code Block component can be used to display code easily within a website.\nPut in a multiline string with the correct spacing and specify and language to show the desired code."
  },
  {
    "name": "Library Data Display Progress",
    "parts": [
      "Library",
      "Data Display",
      "Progress"
    ],
    "url": "docs/library/data-display/progress",
    "description": "Progress\n\nProgress is used to display the progress status for a task that takes a long time or consists of several steps.\n\nBasic Example\n\n expects the  prop to set the progress value.\n is default to 100%, the width of its parent component.\n\nFor a dynamic progress, you can assign a state variable to the  prop instead of a constant value.\n..."
  },
  {
    "name": "Library Data Display Spinner",
    "parts": [
      "Library",
      "Data Display",
      "Spinner"
    ],
    "url": "docs/library/data-display/spinner",
    "description": "Spinner\n\nSpinner is used to display an animated loading indicator when a task is in progress.\n\nBasic Examples\n\nSpinner can have different sizes.\n\nDemo with buttons\n..."
  },
  {
    "name": "Library Data Display List",
    "parts": [
      "Library",
      "Data Display",
      "List"
    ],
    "url": "docs/library/data-display/list",
    "description": "List\n\nA  is a component that is used to display a list of items, stacked vertically by default. A  can be either  or . It is based on the  component and therefore inherits all of its props.\n\n has bullet points to display the list items.\n\n  has numbers to display the list items.\n\n and  can have no bullet points or numbers by setting the  prop to .\nThis is effectively the same as using the  component.\n..."
  },
  {
    "name": "Library Data Display Callout",
    "parts": [
      "Library",
      "Data Display",
      "Callout"
    ],
    "url": "docs/library/data-display/callout",
    "description": "Callout\n\nA  is a short message to attract user's attention.\n\nThe  prop allows an icon to be passed to the  component. See the **icon** component for all icons that are available.\n\nAs alert\n\nStyle\n..."
  },
  {
    "name": "Library Data Display Data List",
    "parts": [
      "Library",
      "Data Display",
      "Data List"
    ],
    "url": "docs/library/data-display/data-list",
    "description": "Data List\n\nThe  component displays key-value pairs and is particularly helpful for showing metadata.\n\nA  needs to be initialized using  and currently takes in data list items:"
  },
  {
    "name": "Library Data Display Icon",
    "parts": [
      "Library",
      "Data Display",
      "Icon"
    ],
    "url": "docs/library/data-display/icon",
    "description": "Icon\n\nThe Icon component is used to display an icon from a library of icons. This implementation is based on the Lucide Icons where you can find a list of all available icons.\n\nIcons List\n\nBasic Example\n\nTo display an icon, specify the  prop from the list of available icons.\nPassing the tag as the first children is also supported and will be assigned to the  prop.\n..."
  },
  {
    "name": "Library Data Display Avatar",
    "parts": [
      "Library",
      "Data Display",
      "Avatar"
    ],
    "url": "docs/library/data-display/avatar",
    "description": "Avatar\n\nThe Avatar component is used to represent a user, and display their profile pictures or fallback texts such as initials.\n\nBasic Example\n\nTo create an avatar component with an image, pass the image URL as the  prop.\n\nTo display a text such as initials, set the  prop without passing the  prop.\n..."
  },
  {
    "name": "Library Data Display Moment",
    "parts": [
      "Library",
      "Data Display",
      "Moment"
    ],
    "url": "docs/library/data-display/moment",
    "description": "Moment\n\nDisplaying date and relative time to now sometimes can be more complicated than necessary.\n\nTo make it easy, Reflex is wrapping react-moment  under .\n\nExamples\n\nUsing a date from a state var as a value, we will display it in a few different\nway using .\n..."
  },
  {
    "name": "Library Data Display Badge",
    "parts": [
      "Library",
      "Data Display",
      "Badge"
    ],
    "url": "docs/library/data-display/badge",
    "description": "Badge\n\nBadges are used to highlight an item's status for quick recognition.\n\nBasic Example\n\nTo create a badge component with only text inside, pass the text as an argument.\n\nStyling\n..."
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
    "description": "Label\n\nLabel is a component used to display a single label at a specific position within a chart or axis, while LabelList is a component that automatically renders a list of labels for each data point in a chart series, providing a convenient way to display multiple labels without manually positioning each one.\n\nSimple Example\n\nHere's a simple example that demonstrates how you can customize the label of your axis using . The  prop represents the actual text of the label, the  prop specifies where the label is positioned within the axis component, and the  prop is used to fine-tune the label's position.\n\nLabel List Example\n..."
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
    "description": "Reference\n\nThe Reference components in Recharts, including ReferenceLine, ReferenceArea, and ReferenceDot, are used to add visual aids and annotations to the chart, helping to highlight specific data points, ranges, or thresholds for better data interpretation and analysis.\n\nReference Area\n\nThe  component in Recharts is used to highlight a specific area or range on the chart by drawing a rectangular region. It is defined by specifying the coordinates (x1, x2, y1, y2) and can be used to emphasize important data ranges or intervals on the chart.\n\nReference Line\n..."
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
    "description": "Brush\n\nSimple Example\n\nThe brush component allows us to view charts that have a large number of data points. To view and analyze them efficiently, the brush provides a slider with two handles that helps the viewer to select some range of data points to be displayed.\n\nPosition, Size, and Range\n\nThis example showcases ways to set the Position, Size, and Range. The  prop provides the spacing between stops on the brush when the graph will refresh. The  and  props defines the default range of the brush.  prop specifies the width of each handle (\"traveller\" in recharts lingo)."
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
    "description": "Cartesian Grid\n\nThe Cartesian Grid is a component in Recharts that provides a visual reference for data points in charts. It helps users to better interpret the data by adding horizontal and vertical lines across the chart area.\n\nSimple Example\n\nThe  prop in Recharts is used to create dashed or dotted lines for various chart elements like lines, axes, or grids. It's based on the SVG stroke-dasharray attribute. The  prop accepts a comma-separated string of numbers that define a repeating pattern of dashes and gaps along the length of the stroke.\n\n- :  creates a line with 5-pixel dashes and 5-pixel gaps\n- :  creates a more complex pattern with 10-pixel dashes, 5-pixel gaps, 5-pixel dashes, and 5-pixel gaps\n..."
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
    "description": "Axis\n\nThe Axis component in Recharts is a powerful tool for customizing and configuring the axes of your charts. It provides a wide range of props that allow you to control the appearance, behavior, and formatting of the axis. Whether you're working with an AreaChart, LineChart, or any other chart type, the Axis component enables you to create precise and informative visualizations.\n\nBasic Example\n\nMultiple Axes\n\nMultiple axes can be used for displaying different data series with varying scales or units on the same chart. This allows for a more comprehensive comparison and analysis of the data.\n..."
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
    "description": "Tooltip\n\nTooltips are the little boxes that pop up when you hover over something. Tooltips are always attached to something, like a dot on a scatter chart, or a bar on a bar chart.\n\nCustom Styling\n\nThe  component allows for customization of the tooltip's style, position, and layout.  sets the separator between the data key and value.  prop defines the dimensions of the chart's viewbox while  determines whether the tooltip can extend beyond the viewBox horizontally (x) or vertically (y).  prop allows you to style the outer container or wrapper of the tooltip.  prop allows you to style the inner content area of the tooltip.  prop determines if the tooltip animation is active or not."
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
    "description": "Legend\n\nA legend tells what each plot represents. Just like on a map, the legend helps the reader understand what they are looking at. For a line graph for example it tells us what each line represents.\n\nSimple Example\n\nExample with Props\n\nThe style and layout of the legend can be customized using a set of props.  and  set the dimensions of the container that wraps the legend, and  can set the legend to display vertically or horizontally.  and  set the position relative to the chart container. The type and size of icons can be set using  and ."
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
    "description": "Radar Chart\n\nA radar chart shows multivariate data of three or more quantitative variables mapped onto an axis.\n\nSimple Example\n\nFor a radar chart we must define an  component for each set of values we wish to plot. Each  component has a  which clearly states which variable in our data we are plotting. In this simple example we plot the  column of our data against the  column which we set as the  in .\n\nMultiple Radars\n..."
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
    "description": "Bar Chart\n\nA bar chart presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.\n\nFor a bar chart we must define an  component for each set of values we wish to plot. Each  component has a  which clearly states which variable in our data we are tracking. In this simple example we plot  as a bar against the  column which we set as the  in .\n\nSimple Example\n\nMultiple Bars\n..."
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
    "description": "Error Bar\n\nAn error bar is a graphical representation of the uncertainty or variability of a data point in a chart, depicted as a line extending from the data point parallel to one of the axes. The , , , , and  props can be used to customize the appearance and behavior of the error bars, specifying the data source, dimensions, color, and orientation of the error bars."
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
    "description": "Pie Chart\n\nA pie chart is a circular statistical graphic which is divided into slices to illustrate numerical proportion.\n\nFor a pie chart we must define an  component for each set of values we wish to plot. Each  component has a , a  and a  which clearly states which data and which variables in our data we are tracking. In this simple example we plot  column as our  against the  column which we set as our .\nWe also use the  prop to set the color of the pie slices.\n\nWe can also add two pies on one chart by using two  components.\n\nIn this example  and  props are used. They define the doughnut shape of a pie chart:  creates the hollow center (use \"0%\" for a full pie), while  sets the overall size. The  prop, used on the green pie below, adds space between pie slices, enhancing visibility of individual segments.\n..."
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
    "description": "Composed Chart\n\nA  is a higher-level component chart that is composed of multiple charts, where other charts are the children of the . The charts are placed on top of each other in the order they are provided in the  function."
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
    "description": "Funnel Chart\n\nA funnel chart is a graphical representation used to visualize how data moves through a process. In a funnel chart, the dependent variable’s value diminishes in the subsequent stages of the process. It can be used to demonstrate the flow of users through a business or sales process.\n\nSimple Example\n\nEvent Triggers\n\nFunnel chart supports , ,  and  event triggers, allows you to interact with the funnel chart and perform specific actions based on user interactions.\n..."
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
    "description": "Scatter Chart\n\nA scatter chart always has two value axes to show one set of numerical data along a horizontal (value) axis and another set of numerical values along a vertical (value) axis. The chart displays points at the intersection of an x and y numerical value, combining these values into single data points.\n\nSimple Example\n\nFor a scatter chart we must define an  component for each set of values we wish to plot. Each  component has a  prop which clearly states which data source we plot. We also must define  and  so that the graph knows what data to plot on each axis.\n\nMultiple Scatters\n..."
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
    "description": "Area Chart\n\nA Recharts area chart displays quantitative data using filled areas between a line connecting data points and the axis.\n\nBasic Example\n\nSyncing Charts\n\nThe  prop allows you to sync two graphs. In the example, it is set to \"1\" for both charts, indicating that they should be synchronized. This means that any interactions (such as brushing) performed on one chart will be reflected in the other chart.\n..."
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
    "description": "Line Chart\n\nA line chart is a type of chart used to show information that changes over time. Line charts are created by plotting a series of several points and connecting them with a straight line.\n\nSimple Example\n\nFor a line chart we must define an  component for each set of values we wish to plot. Each  component has a  which clearly states which variable in our data we are tracking. In this simple example we plot  and  as separate lines against the  column which we set as the  in .\n\nExample with Props\n..."
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
    "description": "Radial Bar Chart\n\nSimple Example\n\nThis example demonstrates how to use a  with a . The  takes in  and then the  takes in a . A radial bar chart is a circular visualization where data categories are represented by bars extending outward from a central point, with the length of each bar proportional to its value.\n\nAdvanced Example\n\nThe  and  define the circular arc over which the bars are distributed, while  and  determine the radial extent of the bars from the center."
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
    "description": "Pyplot\n\nPyplot () is a graphing library that wraps Matplotlib. Use the  component to display any Matplotlib plot in your app. Check out Matplotlib for more information.\n\nInstallation\n\nInstall the  package using pip.\n\nBasic Example\n..."
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
    "description": "Plotly\n\nPlotly is a graphing library that can be used to create interactive graphs. Use the rx.plotly component to wrap Plotly as a component for use in your web page. Checkout Plotly for more information.\n\nBasic Example\n\nLet's create a line graph of life expectancy in Canada.\n\n3D graphing example\n..."
  },
  {
    "name": "Library Typography Markdown",
    "parts": [
      "Library",
      "Typography",
      "Markdown"
    ],
    "url": "docs/library/typography/markdown",
    "description": "Markdown\n\nThe  component can be used to render markdown text.\nIt is based on Github Flavored Markdown.\n\nMath Equations\n\nYou can render math equations using LaTeX.\nFor inline equations, surround the equation with :\n..."
  },
  {
    "name": "Library Typography Text",
    "parts": [
      "Library",
      "Typography",
      "Text"
    ],
    "url": "docs/library/typography/text",
    "description": "Text\n\nAs another element\n\nUse the  prop to render text as a , ,  or . This prop is purely semantic and does not alter visual appearance.\n\nSize\n\nUse the  prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.\n..."
  },
  {
    "name": "Library Typography Blockquote",
    "parts": [
      "Library",
      "Typography",
      "Blockquote"
    ],
    "url": "docs/library/typography/blockquote",
    "description": "Blockquote\n\nSize\n\nUse the  prop to control the size of the blockquote. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.\n\nWeight\n\nUse the  prop to set the blockquote weight.\n..."
  },
  {
    "name": "Library Typography Heading",
    "parts": [
      "Library",
      "Typography",
      "Heading"
    ],
    "url": "docs/library/typography/heading",
    "description": "Heading\n\nAs another element\n\nUse the  prop to change the heading level. This prop is purely semantic and does not change the visual appearance.\n\nSize\n\nUse the  prop to control the size of the heading. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease\n..."
  },
  {
    "name": "Library Typography Strong",
    "parts": [
      "Library",
      "Typography",
      "Strong"
    ],
    "url": "docs/library/typography/strong",
    "description": "Strong\n\nMarks text to signify strong importance."
  },
  {
    "name": "Library Typography Code",
    "parts": [
      "Library",
      "Typography",
      "Code"
    ],
    "url": "docs/library/typography/code",
    "description": "Code\n\nSize\n\nUse the  prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.\n\nWeight\n\nUse the  prop to set the text weight.\n..."
  },
  {
    "name": "Library Typography Em",
    "parts": [
      "Library",
      "Typography",
      "Em"
    ],
    "url": "docs/library/typography/em",
    "description": "Em (Emphasis)\n\nMarks text to stress emphasis."
  },
  {
    "name": "Library Typography Link",
    "parts": [
      "Library",
      "Typography",
      "Link"
    ],
    "url": "docs/library/typography/link",
    "description": "Link\n\nLinks are accessible elements used primarily for navigation. Use the  prop to specify the location for the link to navigate to.\n\nYou can also provide local links to other pages in your project without writing the full url.\n\nThe  component can be used to wrap other components to make them link to other pages.\n\nYou can also create anchors to link to specific parts of a page using the  prop.\n..."
  },
  {
    "name": "Library Overlay Toast",
    "parts": [
      "Library",
      "Overlay",
      "Toast"
    ],
    "url": "docs/library/overlay/toast",
    "description": "Toast\n\nA  is a non-blocking notification that disappears after a certain amount of time. It is often used to show a message to the user without interrupting their workflow.\n\nUsage\n\nYou can use  as an event handler for any component that triggers an action.\n\nUsage in State\n..."
  },
  {
    "name": "Library Typography Kbd",
    "parts": [
      "Library",
      "Typography",
      "Kbd"
    ],
    "url": "docs/library/typography/kbd",
    "description": "rx.text.kbd (Keyboard)\n\nRepresents keyboard input or a hotkey.\n\nSize\n\nUse the  prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease."
  },
  {
    "name": "Library Typography Quote",
    "parts": [
      "Library",
      "Typography",
      "Quote"
    ],
    "url": "docs/library/typography/quote",
    "description": "Quote\n\nA short inline quotation."
  },
  {
    "name": "Library Overlay Popover",
    "parts": [
      "Library",
      "Overlay",
      "Popover"
    ],
    "url": "docs/library/overlay/popover",
    "description": "Popover\n\nA popover displays content, triggered by a button.\n\nThe  contains all the parts of a popover.\n\nThe  contains the button that toggles the popover.\n\nThe  is the component that pops out when the popover is open.\n..."
  },
  {
    "name": "Library Overlay Hover Card",
    "parts": [
      "Library",
      "Overlay",
      "Hover Card"
    ],
    "url": "docs/library/overlay/hover-card",
    "description": "Hovercard\n\nThe  contains all the parts of a hover card.\n\nThe  wraps the link that will open the hover card.\n\nThe  contains the content of the open hover card.\n\nEvents when the Hovercard opens or closes\n..."
  },
  {
    "name": "Library Overlay Dialog",
    "parts": [
      "Library",
      "Overlay",
      "Dialog"
    ],
    "url": "docs/library/overlay/dialog",
    "description": "Dialog\n\nThe  contains all the parts of a dialog.\n\nThe  wraps the control that will open the dialog.\n\nThe  contains the content of the dialog.\n\nThe  is a title that is announced when the dialog is opened.\n..."
  },
  {
    "name": "Library Overlay Drawer",
    "parts": [
      "Library",
      "Overlay",
      "Drawer"
    ],
    "url": "docs/library/overlay/drawer",
    "description": "Drawer\n\nSidebar Menu with a Drawer and State\n\nThis example shows how to create a sidebar menu with a drawer. The drawer is opened by clicking a button. The drawer contains links to different sections of the page. When a link is clicked the drawer closes and the page scrolls to the section.\n\nThe  component has an  prop that is set by the state variable . Setting the  prop to  allows the user to interact with the rest of the page while the drawer is open and allows the page to be scrolled when a user clicks one of the links."
  },
  {
    "name": "Library Overlay Dropdown Menu",
    "parts": [
      "Library",
      "Overlay",
      "Dropdown Menu"
    ],
    "url": "docs/library/overlay/dropdown-menu",
    "description": "Dropdown Menu\n\nA Dropdown Menu is a menu that offers a list of options that a user can select from. They are typically positioned near a button that will control their appearance and disappearance.\n\nA Dropdown Menu is composed of a , a  and a . The  is the element that the user interacts with to open the menu. It wraps the element that will open the dropdown menu. The  is the component that pops out when the dropdown menu is open.\n\nThe  contains the actual dropdown menu items and sits under the . The  prop is an optional shortcut command displayed next to the item text.\n\nThe  contains all the parts of a submenu. There is a , which is an item that opens a submenu. It must be rendered inside a  component. The  is the component that pops out when a submenu is open. It must also be rendered inside a  component.\n..."
  },
  {
    "name": "Library Overlay Alert Dialog",
    "parts": [
      "Library",
      "Overlay",
      "Alert Dialog"
    ],
    "url": "docs/library/overlay/alert-dialog",
    "description": "Alert Dialog\n\nAn alert dialog is a modal confirmation dialog that interrupts the user and expects a response.\n\nThe  contains all the parts of the dialog.\n\nThe  wraps the control that will open the dialog.\n\nThe  contains the content of the dialog.\n..."
  },
  {
    "name": "Library Overlay Context Menu",
    "parts": [
      "Library",
      "Overlay",
      "Context Menu"
    ],
    "url": "docs/library/overlay/context-menu",
    "description": "Context Menu\n\nA Context Menu is a popup menu that appears upon user interaction, such as a right-click or a hover.\n\nBasic Usage\n\nA Context Menu is composed of a , a  and a . The  contains all the parts of a context menu. The  is the element that the user interacts with to open the menu. It wraps the element that will open the context menu. The  is the component that pops out when the context menu is open.\n\nThe  contains the actual context menu items and sits under the .\n..."
  },
  {
    "name": "Library Overlay Tooltip",
    "parts": [
      "Library",
      "Overlay",
      "Tooltip"
    ],
    "url": "docs/library/overlay/tooltip",
    "description": "Tooltip\n\nA  displays informative information when users hover over or focus on an element.\n\nIt takes a  prop, which is the content associated with the tooltip.\n\nEvents when the Tooltip opens or closes\n\nThe  event is called when the  state of the tooltip changes. It is used in conjunction with the  prop, which is passed to the event handler."
  },
  {
    "name": "Library Media Image",
    "parts": [
      "Library",
      "Media",
      "Image"
    ],
    "url": "docs/library/media/image",
    "description": "Image\n\nThe Image component can display an image given a  path as an argument.\nThis could either be a local path from the assets folder or an external link.\n\nImage composes a box and can be styled similarly.\n\nYou can also pass a  image object as the ."
  },
  {
    "name": "Library Media Video",
    "parts": [
      "Library",
      "Media",
      "Video"
    ],
    "url": "docs/library/media/video",
    "description": "Video\n\nThe video component can display a video given an src path as an argument. This could either be a local path from the assets folder or an external link.\n\nIf we had a local file in the  folder named  we could set  to view the video."
  },
  {
    "name": "Library Media Audio",
    "parts": [
      "Library",
      "Media",
      "Audio"
    ],
    "url": "docs/library/media/audio",
    "description": "Audio\n\nThe audio component can display an audio given an src path as an argument. This could either be a local path from the assets folder or an external link.\n\nIf we had a local file in the  folder named  we could set  to view the audio file."
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
    "name": "AI Builder Faq",
    "parts": [
      "AI Builder",
      "Faq"
    ],
    "url": "docs/ai-builder/faq",
    "description": ""
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
    "description": "Reflex Build's IDE\n\nReflex Build includes a powerful, in-browser IDE designed to streamline the entire development process—from writing code\nto deploying your app. With an intuitive layout, real-time editing, and seamless integration with the rest of the\nplatform, the IDE empowers users to stay focused and productive without ever leaving the browser.\n\nIDE Features\n\nReal-Time Editing\n..."
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
    "name": "AI Builder Overview What Is Reflex Build",
    "parts": [
      "AI Builder",
      "Overview",
      "What Is Reflex Build"
    ],
    "url": "docs/ai-builder/overview/what-is-reflex-build",
    "description": "What Is Reflex Build\n\nReflex Build is an AI-powered platform that empowers users of all skill levels to create full-stack web applications\nwithout writing any code—just by describing their ideas in plain English. Instead of hiring developers, users can\ninstantly generate web apps or websites, turning ideas into functional apps as quickly as possible.\n\nReflex Build provides everything you need to create stunning websites, front-end interfaces, and full-stack web\napplications—all from a single browser tab, with no installation required. It includes AI-powered coding tools,\nreal-time collaboration (currently in beta), and easy project sharing to give you a head start on your app development\njourney.\n..."
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
    "name": "State Structure Overview",
    "parts": [
      "State Structure",
      "Overview"
    ],
    "url": "docs/state-structure/overview",
    "description": "Substates\n\nSubstates allow you to break up your state into multiple classes to make it more manageable. This is useful as your app\ngrows, as it allows you to think about each page as a separate entity. Substates also allow you to share common state\nresources, such as variables or event handlers.\n\nWhen a particular state class becomes too large, breaking it up into several substates can bring performance\nbenefits by only loading parts of the state that are used to handle a certain event.\n\nMultiple States\n..."
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
    "name": "Components Props",
    "parts": [
      "Components",
      "Props"
    ],
    "url": "docs/components/props",
    "description": "Props\n\nProps modify the behavior and appearance of a component. They are passed in as keyword arguments to a component.\n\nComponent Props\n\nThere are props that are shared between all components, but each component can also define its own props.\n\nFor example, the  component has a  prop that specifies the URL of the image to display and an  prop that specifies the alternate text for the image.\n..."
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
    "name": "Wrapping React Local Packages",
    "parts": [
      "Wrapping React",
      "Local Packages"
    ],
    "url": "docs/wrapping-react/local-packages",
    "description": "Assets\n\nIf a wrapped component depends on assets such as images, scripts, or\nstylesheets, these can be kept adjacent to the component code and\nincluded in the final build using the  function.\n\n returns a relative path that references the asset in the compiled\noutput. The target files are copied into a subdirectory of \nbased on the module where they are initially used. This allows third-party\ncomponents to have external assets with the same name without conflicting\n..."
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
    "name": "Wrapping React More Wrapping Examples",
    "parts": [
      "Wrapping React",
      "More Wrapping Examples"
    ],
    "url": "docs/wrapping-react/more-wrapping-examples",
    "description": "More React Libraries \n\nAG Charts\n\nHere we wrap the AG Charts library from the NPM package ag-charts-react. \n\nIn the react code below we can see the first  lines are importing React and ReactDOM, and this can be ignored when wrapping your component.\n\nWe import the  component from the  library on line 5. In Reflex this is wrapped by  and .\n..."
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
    "name": "Wrapping React Step By Step",
    "parts": [
      "Wrapping React",
      "Step By Step"
    ],
    "url": "docs/wrapping-react/step-by-step",
    "description": ""
  },
  {
    "name": "Wrapping React Props",
    "parts": [
      "Wrapping React",
      "Props"
    ],
    "url": "docs/wrapping-react/props",
    "description": "Props\n\nWhen wrapping a React component, you want to define the props that will be accepted by the component.\nThis is done by defining the props and annotating them with a .\n\nBroadly, there are three kinds of props you can encounter when wrapping a React component:\n1. **Simple Props**: These are props that are passed directly to the component. They can be of any type, including strings, numbers, booleans, and even lists or dictionaries.\n2. **Callback Props**: These are props that expect to receive a function. That function will usually be called by the component as a callback. (This is different from event handlers.)\n3. **Component Props**: These are props that expect to receive a components themselves. They can be used to create more complex components by composing them together.\n4. **Event Handlers**: These are props that expect to receive a function that will be called when an event occurs. They are defined as  with a signature function to define the spec of the event.\n..."
  },
  {
    "name": "Wrapping React Library And Tags",
    "parts": [
      "Wrapping React",
      "Library And Tags"
    ],
    "url": "docs/wrapping-react/library-and-tags",
    "description": "Find The Component\n\nThere are two ways to find a component to wrap:\n1. Write the component yourself locally.\n2. Find a well-maintained React library on npm that contains the component you need.\n\nIn both cases, the process of wrapping the component is the same except for the  field.\n\nWrapping the Component\n..."
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
    "name": "Wrapping React Serializers",
    "parts": [
      "Wrapping React",
      "Serializers"
    ],
    "url": "docs/wrapping-react/serializers",
    "description": "Serializers\n\nVars can be any type that can be serialized to JSON. This includes primitive types like strings, numbers, and booleans, as well as more complex types like lists, dictionaries, and dataframes.\n\nIn case you need to serialize a more complex type, you can use the  decorator to convert the type to a primitive type that can be stored in the state. Just define a method that takes the complex type as an argument and returns a primitive type. We use type annotations to determine the type that you want to serialize.\n\nFor example, the Plotly component serializes a plotly figure into a JSON string that can be stored in the state.\n\nWe can then define a var of this type as a prop in our component."
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
    "name": "Styling Theming",
    "parts": [
      "Styling",
      "Theming"
    ],
    "url": "docs/styling/theming",
    "description": "Theming\n\nAs of Reflex , you can now theme your Reflex applications. The core of our theming system is directly based on the Radix Themes library. This allows you to easily change the theme of your application along with providing a default light and dark theme. Themes cause all the components to have a unified color appearance.\n\nOverview\n\nThe  component is used to change the theme of the application. The  can be set directly in your rx.App.\n\nHere are the props that can be passed to the  component:\n..."
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
    "name": "Styling Common Props",
    "parts": [
      "Styling",
      "Common Props"
    ],
    "url": "docs/styling/common-props",
    "description": "Style and Layout Props\n\nAny CSS prop can be used in a component in Reflex. This is a short list of the most commonly used props. To see all CSS props that can be used check out this documentation. \n\nHyphens in CSS property names may be replaced by underscores to use as valid python identifiers, i.e. the CSS prop  would be used as  in Reflex."
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
    "name": "Hosting Self Hosting",
    "parts": [
      "Hosting",
      "Self Hosting"
    ],
    "url": "docs/hosting/self-hosting",
    "description": "Self Hosting\n\nWe recommend using , but if this does not fit your use case then you can also host your apps yourself.\n\nClone your code to a server and install the requirements.\n\nAPI URL\n\nEdit your  file and set  to the publicly accessible IP\naddress or hostname of your server, with the port  at the end. Setting\n..."
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
    "name": "Hosting Tokens",
    "parts": [
      "Hosting",
      "Tokens"
    ],
    "url": "docs/hosting/tokens",
    "description": "Tokens\n\nA token gives someone else all the permissions you have as a User or an Admin. They can run any Reflex Cloud command from the CLI as if they are you using the  flag. A good use case would be for GitHub actions (you store this token in the secrets).\n\nTokens are found on the Project List page under the tab . If you cannot find it click the Reflex Logo in the top left side of the page until it appears as in the image below."
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
    "name": "Hosting Reflex Branding",
    "parts": [
      "Hosting",
      "Reflex Branding"
    ],
    "url": "docs/hosting/reflex-branding",
    "description": "Reflex Branding\n\nRemove Reflex branding from your exported or deployed sites. \n\nBy default, Reflex branding, such as the \"Built with Reflex\" badge, will appear on all your published sites.\n\nHow to remove the Reflex branding from your app\n\nYou can turn off the Reflex branding, when deploying to Reflex Cloud, by adding  to the  in the  file.\n..."
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
    "name": "Utility Methods Other Methods",
    "parts": [
      "Utility Methods",
      "Other Methods"
    ],
    "url": "docs/utility-methods/other-methods",
    "description": "Other Methods\n\n* : set all Vars to their default value for the given state (including substates).\n* : returns the value of a Var **without tracking changes to it**. This is useful\n   for serialization where the tracking wrapper is considered unserializable.\n* : returns all state Vars (and substates) as a dictionary. This is\n  used internally when a page is first loaded and needs to be \"hydrated\" and\n  sent to the client.\n\nSpecial Attributes\n..."
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
    "name": "Events Decentralized Event Handlers",
    "parts": [
      "Events",
      "Decentralized Event Handlers"
    ],
    "url": "docs/events/decentralized-event-handlers",
    "description": "Decentralized Event Handlers\n\nOverview\n\nDecentralized event handlers allow you to define event handlers outside of state classes, providing more flexible code organization. This feature was introduced in Reflex v0.7.10 and enables a more modular approach to event handling.\n\nWith decentralized event handlers, you can:\n- Organize event handlers by feature rather than by state class\n- Separate UI logic from state management\n- Create more maintainable and scalable applications\n..."
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
    "name": "Events Yield Events",
    "parts": [
      "Events",
      "Yield Events"
    ],
    "url": "docs/events/yield-events",
    "description": "Yielding Updates\n\nA regular event handler will send a  when it has finished running. This works fine for basic event, but sometimes we need more complex logic. To update the UI multiple times in an event handler, we can  when we want to send an update.\n\nTo do so, we can use the Python keyword . For every yield inside the function, a  will be sent to the frontend with the changes up to this point in the execution of the event handler.\n\nThis example below shows how to yield 100 updates to the UI.\n\nHere is another example of yielding multiple updates with a loading icon.\n..."
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
    "name": "Client Storage Overview",
    "parts": [
      "Client Storage",
      "Overview"
    ],
    "url": "docs/client-storage/overview",
    "description": "Client-storage\n\nYou can use the browser's local storage to persist state between sessions.\nThis allows user preferences, authentication cookies, other bits of information\nto be stored on the client and accessed from different browser tabs.\n\nA client-side storage var looks and acts like a normal  var, except the\ndefault value is either  or  depending on where the\nvalue should be stored. The key name will be based on the var name, but this\ncan be overridden by passing  as a keyword argument.\n..."
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
    "name": "Pages Dynamic Routing",
    "parts": [
      "Pages",
      "Dynamic Routing"
    ],
    "url": "docs/pages/dynamic-routing",
    "description": "Dynamic Routes\n\nDynamic routes in Reflex allow you to handle varying URL structures, enabling you to create flexible\nand adaptable web applications. This section covers regular dynamic routes, catch-all routes,\nand optional catch-all routes, each with detailed examples.\n\nRegular Dynamic Routes\n\nRegular dynamic routes in Reflex allow you to match specific segments in a URL dynamically. A regular dynamic route is defined by square brackets in a route string / url pattern. For example  or . These dynamic route arguments can be accessed through a state var. For the examples above they would be  and  respectively.\n..."
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
    "name": "Getting Started Basics",
    "parts": [
      "Getting Started",
      "Basics"
    ],
    "url": "docs/getting-started/basics",
    "description": "Reflex Basics\n\nThis page gives an introduction to the most common concepts that you will use to build Reflex apps.\n\nInstall  using pip.\n\nImport the  library to get started.\n\nCreating and nesting components\n..."
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
    "name": "Getting Started Dashboard Tutorial",
    "parts": [
      "Getting Started",
      "Dashboard Tutorial"
    ],
    "url": "docs/getting-started/dashboard-tutorial",
    "description": "Tutorial: Data Dashboard\n\nDuring this tutorial you will build a small data dashboard, where you can input data and it will be rendered in table and a graph. This tutorial does not assume any existing Reflex knowledge, but we do recommend checking out the quick Basics Guide first. \n\nThe techniques you’ll learn in the tutorial are fundamental to building any Reflex app, and fully understanding it will give you a deep understanding of Reflex.\n\nThis tutorial is divided into several sections:\n\n- **Setup for the Tutorial**: A starting point to follow the tutorial\n- **Overview**: The fundamentals of Reflex UI (components and props)\n..."
  },
  {
    "name": "Getting Started Installation",
    "parts": [
      "Getting Started",
      "Installation"
    ],
    "url": "docs/getting-started/installation",
    "description": "Installation\n\nReflex requires Python 3.10+.\n\nVirtual Environment\n\nWe **highly recommend** creating a virtual environment for your project.\n\nvenv is the standard option. conda and poetry are some alternatives.\n..."
  },
  {
    "name": "Getting Started Project Structure",
    "parts": [
      "Getting Started",
      "Project Structure"
    ],
    "url": "docs/getting-started/project-structure",
    "description": "Project Structure\n\nDirectory Structure\n\nLet's create a new app called \n\nThis will create a directory structure like this:\n\nLet's go over each of these directories and files.\n..."
  }
]