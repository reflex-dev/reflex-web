indexed_docs = [
  {
    "name": "Configuration",
    "parts": [
      "Advanced Onboarding",
      "Configuration"
    ],
    "url": "docs/advanced-onboarding/configuration",
    "description": "Configuration\n\nReflex apps can be configured using a configuration file, environment variables, and command line arguments.\n\nConfiguration File\n\nRunning  will create an  file in your root directory.\nYou can pass keyword arguments to the  class to configure your app.\n\nFor example:\n\nSee the config reference for all the parameters available.\n\nEnvironment Variables\n\nYou can override the configuration file by setting environment variables.\nFor example, to override the  setting, you can set the  environment variable.\n\nCommand Line Arguments\n\nFinally, you can override the configuration file and environment variables by passing command line arguments to .\n\nSee the CLI reference for all the arguments available.\n\nCustomizable App Data Directory\n\nThe  environment variable can be set, which allows users to set the location where Reflex writes helper tools like Bun and NodeJS.\n\nBy default we use Platform specific directories:\n\nOn windows,  is used.\n\nOn macOS,  is used.\n\nOn linux,  is used."
  },
  {
    "name": "Code Structure",
    "parts": [
      "Advanced Onboarding",
      "Code Structure"
    ],
    "url": "docs/advanced-onboarding/code-structure",
    "description": "Project Structure (Advanced)\n\nApp Module\n\nReflex imports the main app module based on the  from the config, which **must define a module-level global named  as an instance of **.\n\nThe main app module is responsible for importing all other modules that make up the app and defining .\n\n**All other modules containing pages, state, and models MUST be imported by the main app module or package** for Reflex to include them in the compiled output.\n\nBreaking the App into Smaller Pieces\n\nAs applications scale, effective organization is crucial. This is achieved by breaking the application down into smaller, manageable modules and organizing them into logical packages that avoid circular dependencies.\n\nIn the following documentation there will be an app with an  of . The main module would be .\n\nIn the Putting it all together section there is a visual of the project folder structure to help follow along with the examples below.\n\nPages Package: \n\nAll complex apps will have multiple pages, so it is recommended to create  as a package.\n\n1. This package should contain one module per page in the app.\n2. If a particular page depends on the state, the substate should be defined in the same module as the page.\n3. The page-returning function should be decorated with  to have it added as a route in the app.\n\nTemplating: \n\nMost applications maintain a consistent layout and structure across pages. Defining this common structure in a separate module facilitates easy sharing and reuse when constructing individual pages.\n\n**Best Practices**\n\n1. Factor out common frontend UI elements into a function that returns a component.\n2. If a function accepts a function that returns a component, it can be used as a decorator as seen below.\n\nThe  decorator should appear below the  decorator and above the page-returning function. See the Posts Page code for an example.\n\nState Management\n\nMost pages will use State in some capacity. You should avoid adding vars to a\nshared state that will only be used in a single page. Instead, define a new\nsubclass of  and keep it in the same module as the page.\n\nAccessing other States\n\nAs of Reflex 0.4.3, any event handler can get access to an instance of any other\nsubstate via the  API. From a practical perspective, this means that\nstate can be split up into smaller pieces without requiring a complex\ninheritance hierarchy to share access to other states.\n\nIn previous releases, if an app wanted to store settings in  with\na page or component for modifying them, any other state with an event handler\nthat needed to access those settings would have to inherit from ,\neven if the other state was mostly orthogonal. The other state would also now\nalways have to load the settings, even for event handlers that didn't need to\naccess them.\n\nA better strategy is to load the desired state on demand from only the event\nhandler which needs access to the substate.\n\nA Settings Component: \n\nA Post Page: \n\nThis page loads the  to determine how many posts to display per page\nand how often to refresh.\n\nCommon State: \n\n_Common_ states and substates that are shared by multiple pages or components\nshould be implemented in a separate module to avoid circular imports. This\nmodule should not import other modules in the app.\n\nComponent Reusability\n\nThe primary mechanism for reusing components in Reflex is to define a function that returns\nthe component, then simply call it where that functionality is needed.\n\nComponent functions typically should not take any State classes as arguments, but prefer\nto import the needed state and access the vars on the class directly.\n\nMemoize Functions for Improved Performance\n\nIn a large app, if a component has many subcomponents or is used in a large number of places, it can improve compile and runtime performance to memoize the function with the  decorator.\n\nTo memoize the  component to avoid re-creating it many times simply add  to the function definition, and the component will only be created once per unique set of arguments.\n\nexample_big_app/components\n\nThis package contains reusable parts of the app, for example headers, footers,\nand menus. If a particular component requires state, the substate may be defined\nin the same module for locality. Any substate defined in a component module\nshould only contain fields and event handlers pertaining to that individual\ncomponent.\n\nExternal Components\n\nReflex 0.4.3 introduced support for the  CLI commands, which makes it easy\nto bundle up common functionality to publish on PyPI as a standalone Python package\nthat can be installed and used in any Reflex app.\n\nWhen wrapping npm components or other self-contained bits of functionality, it can be helpful\nto move this complexity outside the app itself for easier maintenance and reuse in other apps.\n\nDatabase Models: \n\nIt is recommended to implement all database models in a single file to make it easier to define relationships and understand the entire schema.\n\nHowever, if the schema is very large, it might make sense to have a  package with individual models defined in their own modules.\n\nAt any rate, defining the models separately allows any page or component to import and use them without circular imports.\n\nTop-level Package: \n\nThis is a great place to import all state, models, and pages that should be part of the app.\nTypically, components and helpers do not need to imported, because they will be imported by\npages that use them (or they would be unused).\n\nIf any pages are not imported here, they will not be compiled as part of the app.\n\nexample_big_app/example_big_app.py\n\nThis is the main app module. Since everything else is defined in other modules, this file becomes very simple.\n\nFile Management\n\nThere are two categories of non-code assets (media, fonts, stylesheets,\ndocuments) typically used in a Reflex app.\n\nassets\n\nThe  directory is used for **static** files that should be accessible\nrelative to the root of the frontend (default port 3000). When an app is deployed in\nproduction mode, changes to the assets directory will NOT be available at runtime!\n\nWhen referencing an asset, always use a leading forward slash, so the\nasset can be resolved regardless of the page route where it may appear.\n\nuploaded_files\n\nIf an app needs to make files available dynamically at runtime, it is\nrecommended to set the target directory via \nenvironment variable (default ), write files relative to the\npath returned by , and create working links via\n.\n\nUploaded files are served from the backend (default port 8000) via\n\nPutting it all together\n\nBased on the previous discussion, the recommended project layout look like this.\n\nKey Takeaways\n\n- Like any other Python project, **split up the app into modules and packages** to keep the codebase organized and manageable.\n- Using smaller modules and packages makes it easier to **reuse components and state** across the app\n  without introducing circular dependencies.\n- Create **individual functions** to encapsulate units of functionality and **reuse them** where needed."
  },
  {
    "name": "How Reflex Works",
    "parts": [
      "Advanced Onboarding",
      "How Reflex Works"
    ],
    "url": "docs/advanced-onboarding/how-reflex-works",
    "description": "How Reflex Works\n\nWe'll use the following basic app that displays Github profile images as an example to explain the different parts of the architecture.\n\nThe Reflex Architecture\n\nFull-stack web apps are made up of a frontend and a backend. The frontend is the user interface, and is served as a web page that runs on the user's browser. The backend handles the logic and state management (such as databases and APIs), and is run on a server.\n\nIn traditional web development, these are usually two separate apps, and are often written in different frameworks or languages. For example, you may combine a Flask backend with a React frontend. With this approach, you have to maintain two separate apps and end up writing a lot of boilerplate code to connect the frontend and backend.\n\nWe wanted to simplify this process in Reflex by defining both the frontend and backend in a single codebase, while using Python for everything. Developers should only worry about their app's logic and not about the low-level implementation details.\n\nTLDR\n\nUnder the hood, Reflex apps compile down to a React frontend app and a FastAPI backend app. Only the UI is compiled to Javascript; all the app logic and state management stays in Python and is run on the server. Reflex uses WebSockets to send events from the frontend to the backend, and to send state updates from the backend to the frontend.\n\nThe diagram below provides a detailed overview of how a Reflex app works. We'll go through each part in more detail in the following sections.\n\nFrontend\n\nWe wanted Reflex apps to look and feel like a traditional web app to the end user, while still being easy to build and maintain for the developer. To do this, we built on top of mature and popular web technologies.\n\nWhen you  your app, Reflex compiles the frontend down to a single-page Next.js app and serves it on a port (by default ) that you can access in your browser.\n\nThe frontend's job is to reflect the app's state, and send events to the backend when the user interacts with the UI. No actual logic is run on the frontend.\n\nComponents\n\nReflex frontends are built using components that can be composed together to create complex UIs. Instead of using a templating language that mixes HTML and Python, we just use Python functions to define the UI.\n\nIn our example app, we have components such as , , and . These components can have different **props** that affect their appearance and functionality - for example the  component has a  prop to display the default text.\n\nWe can make our components respond to user interactions with events such as , which we will discuss more below.\n\nUnder the hood, these components compile down to React components. For example, the above code compiles down to the following React code:\n\nMany of our core components are based on Radix, a popular React component library. We also have many other components for graphing, datatables, and more.\n\nWe chose React because it is a popular library with a huge ecosystem. Our goal isn't to recreate the web ecosystem, but to make it accessible to Python developers.\n\nThis also lets our users bring their own components if we don't have a component they need. Users can wrap their own React components and then publish them for others to use. Over time we will build out our third party component ecosystem so that users can easily find and use components that others have built.\n\nStyling\n\nWe wanted to make sure Reflex apps look good out of the box, while still giving developers full control over the appearance of their app.\n\nWe have a core theming system that lets you set high level styling options such as dark mode and accent color throughout your app to give it a unified look and feel.\n\nBeyond this, Reflex components can be styled using the full power of CSS. We leverage the Emotion library to allow \"CSS-in-Python\" styling, so you can pass any CSS prop as a keyword argument to a component. This includes responsive props by passing a list of values.\n\nBackend\n\nNow let's look at how we added interactivity to our apps.\n\nIn Reflex only the frontend compiles to Javascript and runs on the user's browser, while all the state and logic stays in Python and is run on the server. When you , we start a FastAPI server (by default on port ) that the frontend connects to through a websocket.\n\nAll the state and logic are defined within a  class.\n\nThe state is made up of **vars** and **event handlers**.\n\nVars are any values in your app that can change over time. They are defined as class attributes on your  class, and may be any Python type that can be serialized to JSON. In our example,  and  are vars.\n\nEvent handlers are methods in your  class that are called when the user interacts with the UI. They are the only way that we can modify the vars in Reflex, and can be called in response to user actions, such as clicking a button or typing in a text box. In our example,  is an event handler that updates the  and  vars.\n\nSince event handlers are run on the backend, you can use any Python library within them. In our example, we use the  library to make an API call to Github to get the user's profile image.\n\nEvent Processing\n\nNow we get into the interesting part - how we handle events and state updates.\n\nNormally when writing web apps, you have to write a lot of boilerplate code to connect the frontend and backend. With Reflex, you don't have to worry about that - we handle the communication between the frontend and backend for you. Developers just have to write their event handler logic, and when the vars are updated the UI is automatically updated.\n\nYou can refer to the diagram above for a visual representation of the process. Let's walk through it with our Github profile image example.\n\nEvent Triggers\n\nThe user can interact with the UI in many ways, such as clicking a button, typing in a text box, or hovering over an element. In Reflex, we call these **event triggers**.\n\nIn our example we bind the  event trigger to the  event handler. This means that when the user types in the input field and then clicks away, the  event handler is called.\n\nEvent Queue\n\nOn the frontend, we maintain an event queue of all pending events. An event consists of three major pieces of data:\n\n- **client token**: Each client (browser tab) has a unique token to identify it. This let's the backend know which state to update.\n- **event handler**: The event handler to run on the state.\n- **arguments**: The arguments to pass to the event handler.\n\nLet's assume I type my username \"picklelo\" into the input. In this example, our event would look something like this:\n\nOn the frontend, we maintain an event queue of all pending events.\n\nWhen an event is triggered, it is added to the queue. We have a  flag to make sure only one event is processed at a time. This ensures that the state is always consistent and there aren't any race conditions with two event handlers modifying the state at the same time.\n\nOnce the event is ready to be processed, it is sent to the backend through a WebSocket connection.\n\nState Manager\n\nOnce the event is received, it is processed on the backend.\n\nReflex uses a **state manager** which maintains a mapping between client tokens and their state. By default, the state manager is just an in-memory dictionary, but it can be extended to use a database or cache. In production we use Redis as our state manager.\n\nEvent Handling\n\nOnce we have the user's state, the next step is to run the event handler with the arguments.\n\nIn our example, the  event handler is run on the user's state. This makes an API call to Github to get the user's profile image, and then updates the state's  and  vars.\n\nState Updates\n\nEvery time an event handler returns (or yields), we save the state in the state manager and send the **state updates** to the frontend to update the UI.\n\nTo maintain performance as your state grows, internally Reflex keeps track of vars that were updated during the event handler (**dirty vars**). When the event handler is done processing, we find all the dirty vars and create a state update to send to the frontend.\n\nIn our case, the state update may look something like this:\n\nWe store the new state in our state manager, and then send the state update to the frontend. The frontend then updates the UI to reflect the new state. In our example, the new Github profile image is displayed."
  },
  {
    "name": "Tables",
    "parts": [
      "Database",
      "Tables"
    ],
    "url": "docs/database/tables",
    "description": "Tables\n\nTables are database objects that contain all the data in a database.\n\nIn tables, data is logically organized in a row-and-column format similar to a\nspreadsheet. Each row represents a unique record, and each column represents a\nfield in the record.\n\nCreating a Table\n\nTo create a table, make a class that inherits from .\n\nThe following example shows how to create a table called .\n\nThe  argument tells Reflex to create a table in the database for\nthis class.\n\nPrimary Key\n\nBy default, Reflex will create a primary key column called  for each table.\n\nHowever, if an  defines a different field with , then the\ndefault  field will not be created. A table may also redefine  as needed.\n\nIt is not currently possible to create a table without a primary key.\n\nAdvanced Column Types\n\nSQLModel automatically maps basic python types to SQLAlchemy column types, but\nfor more advanced use cases, it is possible to define the column type using\n directly. For example, we can add a last updated timestamp to the\npost example as a proper  field with timezone.\n\nTo make the  model more usable on the frontend, a  method may be provided\nthat converts any fields to a JSON serializable value. In this case, the dict method is\noverriding the default  serializer to strip off the microsecond part."
  },
  {
    "name": "Overview",
    "parts": [
      "Ui",
      "Overview"
    ],
    "url": "docs/ui/overview",
    "description": "UI Overview\n\nComponents are the building blocks for your app's user interface (UI). They are the visual elements that make up your app, like buttons, text, and images.\n\nComponent Basics\n\nComponents are made up of children and props.\n\nLet's take a look at the  component.\n\nHere  is the child text to display, while  and  are props that modify the appearance of the text.\n\nAnother Example\n\nNow let's take a look at a more complex component, which has other components nested inside it. The  component is a container that arranges its children vertically with space between them.\n\nSome props are specific to a component. For example, the  and  props of the  component show the heading and accordion content details of the accordion respectively.\n\nStyling props like  are shared across many components.\n\nPages\n\nReflex apps are organized into pages, each of which maps to a different URL.\n\nPages are defined as functions that return a component. By default, the function name will be used as the path, but you can also specify a route explicitly.\n\nIn this example we add a page called  at the root route.\nIf you  the app, you will see the  page at .\nSimilarly, the  page will be available at ."
  },
  {
    "name": "Queries",
    "parts": [
      "Database",
      "Queries"
    ],
    "url": "docs/database/queries",
    "description": "Queries\n\nQueries are used to retrieve data from a database.\n\nA query is a request for information from a database table or combination of\ntables. A query can be used to retrieve data from a single table or multiple\ntables. A query can also be used to insert, update, or delete data from a table.\n\nSession\n\nTo execute a query you must first create a . You can use the session\nto query the database using SQLModel or SQLAlchemy syntax.\n\nThe  statement will automatically close the session when the code\nblock is finished. **If  is not called, the changes will be\nrolled back and not persisted to the database.** The code can also explicitly\nrollback without closing the session via .\n\nThe following example shows how to create a session and query the database.\nFirst we create a table called .\n\nSelect\n\nThen we create a session and query the User table.\n\nThe  method will query the database for all users that contain the\nvalue of the state var .\n\nInsert\n\nSimilarly, the  method to add a new record to the\ndatabase or persist an existing object.\n\nUpdate\n\nTo update the user, first query the database for the object, make the desired\nmodifications,  the object to the session and finally call .\n\nDelete\n\nTo delete a user, first query the database for the object, then call\n on the session and finally call .\n\nORM Object Lifecycle\n\nThe objects returned by queries are bound to the session that created them, and cannot generally\nbe used outside that session. After adding or updating an object, not all fields are automatically\nupdated, so accessing certain attributes may trigger additional queries to refresh the object.\n\nTo avoid this, the  method can be used to update the object explicitly and\nensure all fields are up to date before exiting the session.\n\nNow the  object will have a correct reference to the autogenerated\nprimary key, , even though this was not provided when the object was created\nfrom the form data.\n\nIf  needs to be modified or used in another query in a new session,\nit must be added to the session. Adding an object to a session does not\nnecessarily create the object, but rather associates it with a session where it\nmay either be created or updated accordingly.\n\nIf an ORM object will be referenced and accessed outside of a session, you\nshould call  on it to avoid stale object exceptions.\n\nUsing SQL Directly\n\nAvoiding SQL is one of the main benefits of using an ORM, but sometimes it is\nnecessary for particularly complex queries, or when using database-specific\nfeatures.\n\nSQLModel exposes the  method that can be used to execute raw\nSQL strings.  If parameter binding is needed, the query may be wrapped in\n[](https://docs.sqlalchemy.org/en/14/core/sqlelement.html#sqlalchemy.sql.expression.text),\nwhich allows colon-prefix names to be used as placeholders.\n\nAsync Database Operations\n\nReflex provides an async version of the session function called  for asynchronous database operations. This is useful when you need to perform database operations in an async context, such as within async event handlers.\n\nThe  function returns an async SQLAlchemy session that must be used with an async context manager. Most operations against the  must be awaited.\n\nAsync Select\n\nThe following example shows how to query the database asynchronously:\n\nAsync Insert\n\nTo add a new record to the database asynchronously:\n\nAsync Update\n\nTo update a user asynchronously:\n\nAsync Delete\n\nTo delete a user asynchronously:\n\nAsync Refresh\n\nSimilar to the regular session, you can refresh an object to ensure all fields are up to date:\n\nAsync SQL Execution\n\nYou can also execute raw SQL asynchronously:"
  },
  {
    "name": "Overview",
    "parts": [
      "Database",
      "Overview"
    ],
    "url": "docs/database/overview",
    "description": "Database\n\nReflex uses sqlmodel to provide a built-in ORM wrapping SQLAlchemy.\n\nThe examples on this page refer specifically to how Reflex uses various tools to\nexpose an integrated database interface.  Only basic use cases will be covered\nbelow, but you can refer to the\nsqlmodel tutorial\nfor more examples and information, just replace  with  and\n with \n\nFor advanced use cases, please see the\nSQLAlchemy docs (v1.4).\n\nConnecting\n\nReflex provides a built-in SQLite database for storing and retrieving data.\n\nYou can connect to your own SQL compatible database by modifying the\n file with your database url.\n\nFor more examples of database URLs that can be used, see the SQLAlchemy\ndocs.\nBe sure to install the appropriate DBAPI driver for the database you intend to\nuse.\n\nTables\n\nTo create a table make a class that inherits from  with and specify\nthat it is a table.\n\nMigrations\n\nReflex leverages alembic\nto manage database schema changes.\n\nBefore the database feature can be used in a new app you must call \nto initialize alembic and create a migration script with the current schema.\n\nAfter making changes to the schema, use\n\nto generate a script in the  directory that will update the\ndatabase schema.  It is recommended that generated scripts be inspected before applying them.\n\nBear in mind that your newest models will not be detected by the \ncommand unless imported and used somewhere within the application.\n\nThe  command is used to apply migration scripts to bring the\ndatabase up to date. During app startup, if Reflex detects that the current\ndatabase schema is not up to date, a warning will be displayed on the console.\n\nQueries\n\nTo query the database you can create a \nwhich handles opening and closing the database connection.\n\nYou can use normal SQLAlchemy queries to query the database."
  },
  {
    "name": "Relationships",
    "parts": [
      "Database",
      "Relationships"
    ],
    "url": "docs/database/relationships",
    "description": "Relationships\n\nForeign key relationships are used to link two tables together. For example,\nthe  model may have a field, , with a foreign key of ,\nreferencing a  model. This would allow us to automatically query the  objects\nassociated with a user, or find the  object associated with a .\n\nTo establish bidirectional relationships a model must correctly set the\n keyword argument on the  to the relationship\nattribute in the _other_ model.\n\nForeign Key Relationships\n\nTo create a relationship, first add a field to the model that references the\nprimary key of the related table, then add a  attribute\nwhich can be used to access the related objects.\n\nDefining relationships like this requires the use of  objects as\nseen in the example.\n\nSee the SQLModel Relationship Docs for more details.\n\nQuerying Relationships\n\nInserting Linked Objects\n\nThe following example assumes that the flagging user is stored in the state as a\n instance and that the post  is provided in the data submitted in the\nform.\n\nHow are Relationships Dereferenced?\n\nBy default, the relationship attributes are in **lazy loading** or \nmode, which generates a query _on access_ to the relationship attribute. Lazy\nloading is generally fine for single object lookups and manipulation, but can be\ninefficient when accessing many linked objects for serialization purposes.\n\nThere are several alternative loading mechanisms available that can be set on\nthe relationship object or when performing the query.\n\n* \"joined\" or  - generates a single query to load all related objects\n  at once.\n* \"subquery\" or  - generates a single query to load all related\n  objects at once, but uses a subquery to do the join, instead of a join in the\n  main query.\n* \"selectin\" or  - emits a second (or more) SELECT statement which\n  assembles the primary key identifiers of the parent objects into an IN clause,\n  so that all members of related collections / scalar references are loaded at\n  once by primary key\n\nThere are also non-loading mechanisms, \"raise\" and \"noload\" which are used to\nspecifically avoid loading a relationship.\n\nEach loading method comes with tradeoffs and some are better suited for different\ndata access patterns.\nSee SQLAlchemy: Relationship Loading Techniques\nfor more detail.\n\nQuerying Linked Objects\n\nTo query the  table and include all  and  objects up front,\nthe  interface will be used to specify  for the required\nrelationships. Using this method, the linked objects will be available for\nrendering in frontend code without additional steps.\n\nThe loading methods create new query objects and thus may be linked if the\nrelationship itself has other relationships that need to be loaded. In this\nexample, since  references , the  relationship must be\nchain loaded from the  relationship.\n\nSpecifying the Loading Mechanism on the Relationship\n\nAlternatively, the loading mechanism can be specified on the relationship by\npassing  to ,\nwhich will use the given loading mechanism in all queries by default."
  },
  {
    "name": "Var Operations",
    "parts": [
      "Vars",
      "Var Operations"
    ],
    "url": "docs/vars/var-operations",
    "description": "Var Operations\n\nVar operations transform the placeholder representation of the value on the\nfrontend and provide a way to perform basic operations on the Var without having\nto define a computed var.\n\nWithin your frontend components, you cannot use arbitrary Python functions on\nthe state vars. For example, the following code will **not work.**\n\nThis is because we compile the frontend to Javascript, but the value of \nis only known at runtime.\n\nIn this example below we use a var operation to concatenate a  with a , meaning we do not have to do in within state as a computed var.\n\nSupported Operations\n\nVar operations allow us to change vars on the front-end without having to create more computed vars on the back-end in the state.\n\nSome simple examples are the  var operator, which is used to check if two vars are equal and the  var operator, which is used to convert a var to a string.\n\nNegate, Absolute and Length\n\nThe  operator is used to get the negative version of the var. The  operator is used to get the absolute value of the var. The  operator is used to get the length of a list var.\n\nComparisons and Mathematical Operators\n\nAll of the comparison operators are used as expected in python. These include , , , , , .\n\nThere are operators to add two vars , subtract two vars , multiply two vars  and raise a var to a power .\n\nTrue Division, Floor Division and Remainder\n\nThe operator  represents true division. The operator  represents floor division. The operator  represents the remainder of the division.\n\nAnd, Or and Not\n\nIn Reflex the  operator represents the logical AND when used in the front end. This means that it returns true only when both conditions are true simultaneously.\nThe  operator represents the logical OR when used in the front end. This means that it returns true when either one or both conditions are true.\nThe  operator is used to invert a var. It is used on a var of type  and is equivalent to the  operator.\n\nContains, Reverse and Join\n\nThe 'in' operator is not supported for Var types, we must use the  instead. When we use , the var must be of type: , ,  or .\n checks if a var contains the object that we pass to it as an argument.\n\nWe use the  operation to reverse a list var. The var must be of type .\n\nFinally we use the  operation to join a list var into a string.\n\nLower, Upper, Split\n\nThe  operator converts a string var to lowercase. The  operator converts a string var to uppercase. The  operator splits a string var into a list.\n\nGet Item (Indexing)\n\nIndexing is only supported for strings, lists, tuples, dicts, and dataframes. To index into a state var strict type annotations are required.\n\nIn the code above you would expect to index into the first index of the list_1 state var. In fact the code above throws the error:  This is because the type of the items inside the list have not been clearly defined in the state. To fix this you change the list_1 definition to \n\nUsing with Foreach\n\nErrors frequently occur when using indexing and .\n\nThe code above throws the error \n\nWe must change  =>  because while projects is annotated, the item in project[\"technologies\"] is not.\n\nThe previous example had only a single type for each of the dictionaries  and . For complex multi-type data, you need to use a dataclass, as shown below.\n\nSetting the type of  to be  would fail as it cannot be understood that the  for the  is actually a .\n\nCombine Multiple Var Operations\n\nYou can also combine multiple var operations together, as seen in the next example.\n\nWe could have made a computed var that returns the parity of , but\nit can be simpler just to use a var operation instead.\n\nVar operations may be generally chained to make compound expressions, however\nsome complex transformations not supported by var operations must use computed vars\nto calculate the value on the backend."
  },
  {
    "name": "Custom Vars",
    "parts": [
      "Vars",
      "Custom Vars"
    ],
    "url": "docs/vars/custom-vars",
    "description": "Custom Vars\n\nAs mentioned in the vars page, Reflex vars must be JSON serializable.\n\nThis means we can support any Python primitive types, as well as lists, dicts, and tuples. However, you can also create more complex var types using dataclasses (recommended), TypedDict, or Pydantic models.\n\nDefining a Type\n\nIn this example, we will create a custom var type for storing translations using a dataclass.\n\nOnce defined, we can use it as a state var, and reference it from within a component.\n\nAlternative Approaches\n\nUsing TypedDict\n\nYou can also use TypedDict for defining custom var types:\n\nUsing Pydantic Models\n\nPydantic models are another option for complex data structures:\n\nFor complex data structures, dataclasses are recommended as they provide a clean, type-safe way to define custom var types with good IDE support."
  },
  {
    "name": "Base Vars",
    "parts": [
      "Vars",
      "Base Vars"
    ],
    "url": "docs/vars/base-vars",
    "description": "Base Vars\n\nVars are any fields in your app that may change over time. A Var is directly\nrendered into the frontend of the app.\n\nBase vars are defined as fields in your State class.\n\nThey can have a preset default value. If you don't provide a default value, you\nmust provide a type annotation.\n\nIn this example  and  are base vars in the app, which can be modified at runtime.\n\nAccessing state variables on different pages\n\nState is just a python class and so can be defined on one page and then imported and used on another. Below we define  class on the page  and then import it and use it on the page .\n\nBackend-only Vars\n\nAny Var in a state class that starts with an underscore () is considered backend\nonly and will **not be synchronized with the frontend**. Data associated with a\nspecific session that is _not directly rendered on the frontend should be stored\nin a backend-only var_ to reduce network traffic and improve performance.\n\nThey have the advantage that they don't need to be JSON serializable, however\nthey must still be pickle-able to be used with redis in prod mode. They are\nnot directly renderable on the frontend, and **may be used to store sensitive\nvalues that should not be sent to the client**.\n\nFor example, a backend-only var is used to store a large data structure which is\nthen paged to the frontend using cached vars.\n\nUsing rx.field / rx.Field to improve type hinting for vars\n\nWhen defining state variables you can use  to annotate the variable's type. Then, you can initialize the variable using , where  is an instance of type . \n\nThis approach makes the variable's type explicit, aiding static analysis tools in type checking. In addition, it shows you what methods are allowed to modify the variable in your frontend code, as they are listed in the type hint.\n\nBelow are two examples:\n\nHere , as it is typed correctly as a  var, gets better code completion, i.e. here we get options such as  or .\n\nHere , as it is typed correctly as a  of  to  of  var, gets better code completion, i.e. here we get options such as , , ,  or ."
  },
  {
    "name": "Components",
    "parts": [
      "Enterprise",
      "Components"
    ],
    "url": "docs/enterprise/components",
    "description": "---\ntitle: Enterprise Components\n---"
  },
  {
    "name": "Computed Vars",
    "parts": [
      "Vars",
      "Computed Vars"
    ],
    "url": "docs/vars/computed-vars",
    "description": "Computed Vars\n\nComputed vars have values derived from other properties on the backend. They are\ndefined as methods in your State class with the  decorator. A computed\nvar is recomputed every time an event is processed in your app.\n\nTry typing in the input box and clicking out.\n\nHere,  is a computed var that always holds the upper case version of .\n\nWe recommend always using type annotations for computed vars.\n\nCached Vars\n\nA cached var, decorated as  is a special type of computed var\nthat is only recomputed when the other state vars it depends on change. This is\nuseful for expensive computations, but in some cases it may not update when you\nexpect it to.\nPrevious versions of Reflex had a  decorator, which is now replaced\nby the new  argument of .\n\nIn this example  is a normal computed var, which updates any\ntime the state is modified.  is a computed var that only\ndepends on , so it only gets recomputed when  has changes.\nSimilarly  only depends on , and thus is\nupdated only when  changes.\n\nAsync Computed Vars\n\nAsync computed vars allow you to use asynchronous operations in your computed vars.\nThey are defined as async methods in your State class with the same  decorator.\nAsync computed vars are useful for operations that require asynchronous processing, such as:\n\n- Fetching data from external APIs\n- Database operations\n- File I/O operations\n- Any other operations that benefit from async/await\n\nIn this example,  is an async computed var that returns the count multiplied by 2 after a simulated delay.\nWhen the count changes, the async computed var is automatically recomputed.\n\nCaching Async Computed Vars\n\nJust like regular computed vars, async computed vars can also be cached. This is especially\nuseful for expensive async operations like API calls or database queries.\n\nIn this example,  is a cached async computed var that simulates fetching user data.\nIt is only recomputed when  changes, not when other state variables like  change.\nThis demonstrates how caching works with async computed vars to optimize performance for expensive operations."
  },
  {
    "name": "Overview",
    "parts": [
      "Enterprise",
      "Overview"
    ],
    "url": "docs/enterprise/overview",
    "description": "---\ntitle: Reflex Enterprise\n---\n\nReflex Enterprise\n\nReflex Enterprise is a package containing paid features built on top of Reflex.\n\nInstallation\n\n must be installed alongside  to access the enterprise features.\n\nYou can install it from pypi with the following command:\n\nFeatures\n\nUsage of reflex_enterprise.\n\nUsing  as your  is required to use any of the components provided by the enterprise package, as well as config options provided by .\n\nIn the main file\n\nInstead of the usual  to create your app, use the following:\n\nIn rxconfig.py"
  },
  {
    "name": "Ag Chart",
    "parts": [
      "Enterprise",
      "Ag Chart"
    ],
    "url": "docs/enterprise/ag-chart",
    "description": "AG Chart\n\nAG Chart is a powerful charting library that provides interactive charts and data visualization components for enterprise applications.\n\nFor more detailed documentation, see the AG Chart Documentation."
  },
  {
    "name": "Built With Reflex",
    "parts": [
      "Enterprise",
      "Built With Reflex"
    ],
    "url": "docs/enterprise/built-with-reflex",
    "description": "Built with Reflex Badge\n\nThe \"Built with Reflex\" badge appears in the bottom right corner of apps using reflex-enterprise components.\n\nRemoving the Badge\n\nTo remove the badge, you need a paid tier:\n- **Cloud**: Pro tier or higher\n- **Self-hosted**: Team tier or higher\n\nConfiguration"
  },
  {
    "name": "Single Port Proxy",
    "parts": [
      "Enterprise",
      "Single Port Proxy"
    ],
    "url": "docs/enterprise/single-port-proxy",
    "description": "Single Port Proxy\n\nEnable single-port deployment by proxying the backend to the frontend port.\n\nConfiguration\n\nThis allows your application to run on a single port, which is useful for deployment scenarios where you can only expose one port."
  },
  {
    "name": "Semi Circle Progress",
    "parts": [
      "Enterprise",
      "Mantine",
      "Semi Circle Progress"
    ],
    "url": "docs/enterprise/mantine/semi-circle-progress",
    "description": "---\ntitle: Semi Circle Progress\n---\n\nSemi Circle Progress component\n is a component for displaying progress in a semi-circular format. It is useful for visualizing completion percentages or other metrics in a compact and visually appealing way."
  },
  {
    "name": "Drag And Drop",
    "parts": [
      "Enterprise",
      "Drag And Drop"
    ],
    "url": "docs/enterprise/drag-and-drop",
    "description": "---\ntitle: Drag and Drop\n---\n\nDrag and Drop\n\nReflex Enterprise provides comprehensive drag and drop functionality for creating interactive UI elements using the  module. Built on top of react-dnd, it offers both high-level components for common use cases and low-level hooks for advanced scenarios.\n\nBasic Usage\n\nSimple Drag and Drop\n\nHere's a basic example showing how to create a draggable item and drop target:\n\nMulti-Position Drag and Drop\n\nCreate a draggable item that can be moved between multiple drop targets:\n\nAdvanced Features\n\nState Tracking with Collected Parameters\n\nAccess drag and drop state information using collected parameters:\n\nDynamic Lists with Drag and Drop\n\nCreate dynamic draggable lists using :\n\nCore Components\n\nDraggable\n\nThe  component makes any element draggable:\n\n**Key Properties:**\n- : String identifier for drag type matching\n- : Data object passed to drop handlers\n- : Called when drag operation ends\n\nDrop Target\n\nThe  component creates areas that accept draggable items:\n\n**Key Properties:**\n- : List of drag types this target accepts\n- : Called when item is dropped\n- : Called when item hovers over target\n\nCollected Parameters\n\nAccess real-time drag/drop state:\n\n**Draggable Parameters ():**\n- : Boolean indicating if item is being dragged\n\n**Drop Target Parameters ():**\n- : Boolean indicating if draggable is hovering\n- : Boolean indicating if drop is allowed\n\nAPI Reference\n\nrxe.dnd.draggable\n\nCreates a draggable component that can be moved around the interface.\n\n**Parameters:**\n\n- **** (str, required): String identifier that must match the  list of drop targets\n- **** (dict | Callable): Data object passed to drop handlers. Can be a static dictionary or a function that receives a  and returns data\n- **** (dict): Configuration for the drag preview appearance\n- **** (dict): Additional drag source options like \n- **** (EventHandler): Event handler called when drag operation completes\n- **** (Callable): Function that determines if the item can be dragged\n- **** (Callable): Function to override the default dragging state detection\n- **** (Callable): Function to collect custom properties from the drag monitor\n\nrxe.dnd.drop_target\n\nCreates a drop target that can receive draggable items.\n\n**Parameters:**\n\n- **** (str | list[str], required): Drag type(s) this target accepts\n- **** (dict): Additional drop target configuration options\n- **** (EventHandler): Event handler called when an item is dropped, receives the  data\n- **** (EventHandler): Event handler called when an item hovers over the target\n- **** (Callable): Function that determines if a specific item can be dropped\n- **** (Callable): Function to collect custom properties from the drop monitor\n\nMonitor Classes\n\nDragSourceMonitor\n\nProvides information about the drag operation state:\n\n- ****: Returns  if this item is currently being dragged\n- ****: Returns  if the item can be dragged\n- ****: Returns the item data being dragged\n- ****: Returns the drag type string\n- ****: Returns the drop result (available in )\n- ****: Returns  if the item was successfully dropped\n\nDropTargetMonitor\n\nProvides information about the drop target state:\n\n- ****: Returns  if a draggable item is hovering over this target\n- ****: Returns  if the hovering item can be dropped\n- ****: Returns the item data of the hovering draggable\n- ****: Returns the drag type of the hovering item\n\nDefault Collected Parameters\n\nDraggable.collected_params\n\nDropTarget.collected_params\n\nAdvanced Usage Examples\n\nData Passing with Item Parameter\n\nThe  parameter allows you to pass data from draggable components to drop handlers:\n\nCustom Collect Functions\n\nThe  parameter allows you to access drag and drop state information in real-time:\n\nProvider\n\nDrag and drop functionality requires the  component to wrap your app. The provider is automatically added when using  or  components.\n\nFor manual control:\n\nBest Practices\n\n1. **Always use ** on functions containing draggable components\n2. **Use descriptive type names** for better debugging\n3. **Handle edge cases** in drop handlers (invalid items, etc.)\n4. **Provide visual feedback** using collected parameters\n5. **Test on mobile devices** with touch backend\n6. **Keep item data lightweight** for better performance\n\n---\n\n← Back to main documentation"
  },
  {
    "name": "Pill",
    "parts": [
      "Enterprise",
      "Mantine",
      "Pill"
    ],
    "url": "docs/enterprise/mantine/pill",
    "description": "---\ntitle: Pill\n---\n\nPill\n\n is a wrapping of the mantine component Pill. It is a simple component that can be used to display a small piece of information, such as a tag or a label. It can be used in various contexts, such as in a list of tags or labels, or as a standalone component.\n\nPill Group\n allows grouping multiple  components together, with a predefined layout.\n\nPillsInput\n\n is a wrapping of the mantine component PillsInput. It is an utility component that can be used to display a list of tags or labels. It can be used in various contexts, such as in a form or as a standalone component.\nBy itself it does not include any logic, it only renders given children.\n\nExample"
  },
  {
    "name": "Autocomplete",
    "parts": [
      "Enterprise",
      "Mantine",
      "Autocomplete"
    ],
    "url": "docs/enterprise/mantine/autocomplete",
    "description": "---\ntitle: Autocomplete\n---\n\nAutocomplete component\n\n is a component for providing suggestions as the user types. It is useful for enhancing user experience by offering relevant options based on input."
  },
  {
    "name": "Timeline",
    "parts": [
      "Enterprise",
      "Mantine",
      "Timeline"
    ],
    "url": "docs/enterprise/mantine/timeline",
    "description": "---\ntitle: Timeline\n---\n\nTimeline component\n is a component for displaying a sequence of events or milestones in a linear format. It is useful for visualizing progress, history, or any sequential information."
  },
  {
    "name": "Index",
    "parts": [
      "Enterprise",
      "Mantine",
      "Index"
    ],
    "url": "docs/enterprise/mantine/index",
    "description": "---\ntitle: Mantine\norder: 4\n---\n\nMantine\n\nMantine is a React component library that provides a set of high-quality components and hooks for building modern web applications. It is designed to be flexible, customizable, and easy to use, making it a popular choice among developers.\n\nSome of those components have been integrated into Reflex Enterprise, allowing you to use them in your Reflex applications. The following components are available:\n- JsonInput\n- Autocomplete\n- ComboBox\n- Multiselect\n- Pill\n- PillsInput\n- TagsInput\n- Tree\n- RingProgress\n- SemiCircleProgress\n- LoadingOverlay\n- NumberFormatter\n- Spoiler\n- Timeline\n- Collapse"
  },
  {
    "name": "Spoiler",
    "parts": [
      "Enterprise",
      "Mantine",
      "Spoiler"
    ],
    "url": "docs/enterprise/mantine/spoiler",
    "description": "---\ntitle: Spoiler\n---\n\nSpoiler component\n\n is a component that allows you to hide or reveal content. It is useful for displaying additional information or details that may not be immediately relevant to the user."
  },
  {
    "name": "Ring Progress",
    "parts": [
      "Enterprise",
      "Mantine",
      "Ring Progress"
    ],
    "url": "docs/enterprise/mantine/ring-progress",
    "description": "---\ntitle: Ring Progress\n---\n\nRing Progress component\n\n is a component for displaying progress in a circular format. It is useful for visualizing completion percentages or other metrics in a compact and visually appealing way."
  },
  {
    "name": "Tags Input",
    "parts": [
      "Enterprise",
      "Mantine",
      "Tags Input"
    ],
    "url": "docs/enterprise/mantine/tags-input",
    "description": "---\ntitle: TagsInput\n---\n\nTagsInput\n\n is a wrapping of the mantine component TagsInput. It is an utility component that can be used to display a list of tags or labels. It can be used in various contexts, such as in a form or as a standalone component.\n\nBasic Example\n\nState Example"
  },
  {
    "name": "Number Formatter",
    "parts": [
      "Enterprise",
      "Mantine",
      "Number Formatter"
    ],
    "url": "docs/enterprise/mantine/number-formatter",
    "description": "---\ntitle: Number Formatter\n---\n\nNumber Formatter component\n is a component for formatting numbers in a user-friendly way. It allows you to specify the format, precision, and other options for displaying numbers."
  },
  {
    "name": "Multi Select",
    "parts": [
      "Enterprise",
      "Mantine",
      "Multi Select"
    ],
    "url": "docs/enterprise/mantine/multi-select",
    "description": "---\ntitle: MultiSelect\n---\n\nMultiSelect component\n\n is a component for selecting multiple options from a list. It allows users to choose one or more items, making it suitable for scenarios where multiple selections are required."
  },
  {
    "name": "Tree",
    "parts": [
      "Enterprise",
      "Mantine",
      "Tree"
    ],
    "url": "docs/enterprise/mantine/tree",
    "description": "---\ntitle: Tree\n---\n\nTree component\n\n is a component for displaying hierarchical data in a tree structure. It allows users to expand and collapse nodes, making it easy to navigate through large datasets."
  },
  {
    "name": "Combobox",
    "parts": [
      "Enterprise",
      "Mantine",
      "Combobox"
    ],
    "url": "docs/enterprise/mantine/combobox",
    "description": "---\ntitle: Combobox\n---\n\nCombobox\n\n is a wrapping of the mantine component Combobox. It is a simple component that can be used to display a list of options, and allows the user to select one or more options from the list. It can be used in various contexts, such as in a form or as a standalone component."
  },
  {
    "name": "JSON Input",
    "parts": [
      "Enterprise",
      "Mantine",
      "JSON Input"
    ],
    "url": "docs/enterprise/mantine/json-input",
    "description": "---\ntitle: JSON Input\n---\n\nJSON Input\n\n is a component that allows you to input JSON data in a user-friendly way. It provides validation and formatting features to ensure that the JSON data is correctly structured.\n\nExample"
  },
  {
    "name": "Loading Overlay",
    "parts": [
      "Enterprise",
      "Mantine",
      "Loading Overlay"
    ],
    "url": "docs/enterprise/mantine/loading-overlay",
    "description": "---\ntitle: Loading Overlay\n---\n\nLoading Overlay component\n is a component that displays a loading overlay on top of its children. It is useful for indicating that a process is ongoing and prevents user interaction with the underlying content."
  },
  {
    "name": "Collapse",
    "parts": [
      "Enterprise",
      "Mantine",
      "Collapse"
    ],
    "url": "docs/enterprise/mantine/collapse",
    "description": "---\ntitle: Collapse\n---\n\nCollapse component\n\n is a component that allows you to create collapsible sections in your application. It is useful for hiding or showing content based on user interaction, such as clicking a button or a link."
  },
  {
    "name": "Value Transformers",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Value Transformers"
    ],
    "url": "docs/enterprise/ag-grid/value-transformers",
    "description": "---\norder: 2\n---\n\nValue Transformers\n\nAgGrid allow you to apply transformers based on the column of your grid. This allow you to perform operations on the data before displaying it on the grid, without having to pre-process the data on the backend, reducing the load on your application.\n\nTOC:\n- Value Getter\n- Value Formatter\n\nValue Getter\n\n is a property of the column definition that allows you to define a function that will be called to get the value of the cell. This function will receive the row data as a parameter and should return the value to be displayed on the cell.\n\nIf you have two columns  and  and you want to display the sum of these two columns in a third column , you can define the  of  as follows:\n\nValue Formatter\n\n is a property of the column definition that allows you to define a function that will be called to format the value of the cell. This function will receive the value of the cell as a parameter and should return the formatted value to be displayed on the cell.\n\nIf you have a column  and you want to display the price with a currency symbol, you can define the  of  as follows:"
  },
  {
    "name": "Index",
    "parts": [
      "Enterprise",
      "Map",
      "Index"
    ],
    "url": "docs/enterprise/map/index",
    "description": "---\ntitle: Interactive Maps\n---\n\nInteractive Maps\n\nThe map components in Reflex Enterprise provide interactive mapping capabilities built on top of **Leaflet**, one of the most popular open-source JavaScript mapping libraries. These components enable you to create rich, interactive maps with markers, layers, controls, and event handling.\n\n🌍 **View Live Demo** - See the map components in action with interactive examples.\n\nInstallation & Setup\n\nMap components are included with . No additional installation is required.\n\nBasic Usage\n\nHere's a simple example of creating a map with a marker:\n\nCore Components\n\nMap Container\n\nThe  component is the primary container that holds all other map elements:\n\n**Key Properties:**\n- : Initial map center coordinates\n- : Initial zoom level (0-18+ depending on tile provider)\n- : Alternative to center/zoom, fits map to bounds\n- /: Map container dimensions\n\nTile Layers\n\nTile layers provide the base map imagery. The most common is OpenStreetMap:\n\nMarkers\n\nAdd point markers to specific locations:\n\nVector Layers\n\nDraw shapes and areas on the map:\n\nInteractive Features\n\nEvent Handling\n\nMaps support comprehensive event handling for user interactions:\n\nMap Controls\n\nAdd UI controls for enhanced user interaction:\n\nHelper Functions\n\nCoordinate Creation\n\nMap API\n\nThe Map API provides programmatic control over your maps, allowing you to manipulate the map programmatically from your Reflex state methods.\n\nGetting the API Reference\n\nTo access the Map API, you need to get a reference to your map using its ID:\n\nInteractive Demo\n\nHere are some commonly used API methods demonstrated in action:\n\nCommon API Methods\n\n**View Control:**\n-  - Smooth animated movement to location\n-  - Instant movement to location\n-  - Change zoom level\n-  /  - Zoom by one level\n-  - Fit map to specific bounds\n\n**Location Services:**\n-  - Get user's current location\n-  - Stop location tracking\n\n**Information Retrieval:**\n-  - Get current map center\n-  - Get current zoom level\n-  - Get current map bounds\n-  - Get map container size\n\n**Layer Management:**\n-  - Add a layer to the map\n-  - Remove a layer from the map\n-  - Check if layer exists on map\n\nFull Leaflet API Access\n\nThis means you can use any method from the Leaflet Map documentation. For example:\n\n**Python (snake_case) → JavaScript (camelCase):**\n-  → \n-  → \n-  → \n-  → \n\nAdvanced Example\n\nCallback Handling\n\nMany API methods that retrieve information require callbacks to handle the results:\n\nAvailable Events\n\nThe map components support a comprehensive set of events:\n\n**Map Events:**\n- ,  - Mouse click events\n- , ,  - Zoom events\n- , ,  - Pan events\n-  - Map container resize\n- ,  - Map lifecycle\n\n**Location Events:**\n- ,  - Geolocation\n\n**Layer Events:**\n- ,  - Layer management\n\n**Popup Events:**\n- ,  - Popup lifecycle\n- ,  - Tooltip lifecycle\n\nCommon Patterns\n\nDynamic Markers\n\nBest Practices\n\n1. **Always include attribution** for tile providers\n2. **Set reasonable zoom levels** (typically 1-18)\n3. **Use bounds for multiple markers** instead of arbitrary center/zoom\n4. **Handle loading states** for dynamic map content\n5. **Optimize marker rendering** for large datasets using clustering\n6. **Test on mobile devices** for touch interactions\n\n---\n\n← Back to main documentation"
  },
  {
    "name": "Model Wrapper",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Model Wrapper"
    ],
    "url": "docs/enterprise/ag-grid/model-wrapper",
    "description": "---\norder: 6\n---\n\nModel Wrapper\n\nA model wrapper is an utility used to wrap a database model and provide a consistent interface over it. It allows automatically adding new rows to the database, updating existing rows, and deleting rows.\n\nDefault Model Wrapper\n\nYou can use the basic functionality of the model wrapper by using the  function. This function takes a database model and returns a wrapper object that can be used to interact with the model.\n\nBy default the model_wrapper use the infinite rows model from AgGrid.\n\nCustom Model Wrapper\n\nIf the default model wrapper does not fit your needs, you can create a custom model wrapper by subclassing the  class. This allows you to customize the behavior of the model wrapper to fit your specific use case.\n\nIn the custom model wrapper, you can override the following methods:\n- \n- \n- \n- \n\nto modify how the model wrapper will behave.\n\nSSRM Model Wrapper\n\nThe SSRM model wrapper, used with , is a version of the model wrapper that allows you to use the ServerSideRowModel of AgGrid.\n\nSSRM Custom Model Wrapper\n\nIn the same way you can extend the default model wrapper, you can extend the SSRM custom model wrapper by subclassing the  class. This allows you to customize the behavior of the model wrapper to fit your specific use case.\n\nThe overridable methods are the same as the standard model wrapper."
  },
  {
    "name": "Aligned Grids",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Aligned Grids"
    ],
    "url": "docs/enterprise/ag-grid/aligned-grids",
    "description": "---\ntitle: Aligned Grids\n---\n\nAgGrid provides a way to align multiple grids together. This is useful when you want to display related data in a synchronized manner.\n\nYou can do so through the  prop. This prop takes a list of grid IDs that you want to align."
  },
  {
    "name": "Index",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Index"
    ],
    "url": "docs/enterprise/ag-grid/index",
    "description": "---\ntitle: \"AgGrid Overview\"\norder: 3\n---\n\nAG Grid\n\nAG Grid Features\n\nYour First Reflex AG Grid\n\nA basic Reflex AG Grid contains column definitions , which define the columns to be displayed in the grid, and , which contains the data to be displayed in the grid.\n\nEach grid also requires a unique , which is needed to uniquely identify the Ag-Grid instance on the page. If you have multiple grids on the same page, each grid must have a unique  so that it can be correctly rendered and managed.\n\nThe format of the data passed to the  prop is a list of dictionaries. Each dictionary represents a row in the grid as seen below.\n\nThe previous example showed the  written out in full. You can also extract the required information from the dataframe's column names:\n\nHeaders\n\nIn the above example, the first letter of the field names provided are capitalized when displaying the header name. You can customize the header names by providing a  key in the column definition. In this example, the  is customized for the second and third columns.\n\nColumn Filtering\n\nAllow a user to filter a column by setting the  key to  in the column definition. In this example we enable filtering for the first and last columns.\n\nFilter Types\n\nYou can set  to enable the default filter for a column.\n\nYou can also set the filter type using the  key. The following filter types are available: ,  and . These ensure that the input you enter to the filter is of the correct type.\n\n( and  are available with AG Grid Enterprise)\n\nRow Sorting\n\nBy default, the rows can be sorted by any column by clicking on the column header. You can disable sorting of the rows for a column by setting the  key to  in the column definition.\n\nIn this example, we disable sorting for the first column.\n\nRow Selection\n\nRow Selection is enabled using the  attribute. Setting it to  allows users to select multiple rows at a time. You can use the  column definition attribute to render checkboxes for selection.\n\nEditing\n\nEnable Editing by setting the  attribute to . The cell editor is inferred from the cell data type. Set the cell editor type using the  attribute.\n\nThere are 7 provided cell editors in AG Grid:\n\n1. \n2. \n3. \n4. \n5. \n6. \n7. \n\nIn this example, we enable editing for the second and third columns. The second column uses the  cell editor, and the third column uses the  cell editor.\n\nThe  event trigger is linked to the  event handler in the state. This event handler is called whenever a cell value is changed and changes the value of the backend var  and the state var .\n\nPagination\n\nBy default, the grid uses a vertical scroll. You can reduce the amount of scrolling required by adding pagination. To add pagination, set . You can set the  to the number of rows per page and  to a list of options for the user to select from.\n\nAG Grid with State\n\nPutting Data in State\n\nAssuming you want to make any edit to your data, you can put the data in State. This allows you to update the grid based on user input. Whenever the  var is updated, the grid will be re-rendered with the new data.\n\nUpdating the Grid with State\n\nYou can use State to update the grid based on a users input. In this example, we update the  of the grid when a user clicks a button.\n\nAG Grid with Data from a Database\n\nIn this example, we will use a database to store the data. The data is loaded from a csv file and inserted into the database when the page is loaded using the  event handler.\n\nThe data is then fetched from the database and displayed in the grid using the  computed var.\n\nWhen a cell value is changed, the data is updated in the database using the  event handler.\n\nUsing AG Grid Enterprise\n\nAG Grid offers both community and enterprise versions. See the AG Grid docs for details on purchasing a license key.\n\nTo use an AG Grid Enterprise license key with Reflex AG Grid set the environment variable :\n\ncolumn_def props\n\nThe following props are available for  as well as many others that can be found here: AG Grid Column Def Docs. (it is necessary to use snake_case for the keys in Reflex, unlike in the AG Grid docs where camelCase is used)\n\n- : : The field of the row object to get the cell's data from.\n- : : The unique ID to give the column. This is optional. If missing, the ID will default to the field.\n- : : The type of the column.\n- : : The data type of the cell values for this column. Can either infer the data type from the row data (true - the default behaviour), define a specific data type (string), or have no data type (false).\n- : : Set to true for this column to be hidden.\n- : : Set to true if this column is editable, otherwise false.\n- : : Filter component to use for this column. Set to true to use the default filter. Set to the name of a provided filter to use that filter. (Check out the Filter Types section of this page for more information)\n- : : Whether to display a floating filter for this column.\n- : : The name to render in the column header. If not specified and field is specified, the field name will be used as the header name.\n- : : Tooltip for the column header.\n- : : Set to true to render a checkbox for row selection.\n- : : Provide your own cell editor component for this column's cells. (Check out the Editing section of this page for more information)\n- : : Params to be passed to the cellEditor component.\n\nFunctionality you need is not available/working in Reflex\n\nAll AGGrid options found in this documentation are mapped in rxe.ag_grid, but some features might not have been fully tested, due to the sheer number of existing features in the underlying AG Grid library.\n\nIf one of the ag_grid props does not import the expected module, you can pass it manually via the props  or , which expect a  of the module names. You will get a warning in the browser console if a module is missing, so you can check there if a feature is not working as expected.\n\nYou can also report the missing module on our discord or GitHub issues page of the main Reflex repository.\n\nBest practice is to create a single instance of  with the same  as the  of the  component that is to be referenced,  in this first example.\n\nThe example below uses the  and  methods of the AG Grid API to select and deselect all rows in the grid. This method is not available in Reflex directly. Check out this documentation to see what the methods look like in the AG Grid docs.\n\nThe react code for the  event handler is . \n\nTo use this in Reflex as you can see, it should be called in snake case rather than camel case. The  means it doesn't return anything. The  indicates that it takes an optional  argument.\n\npython\nrx.button(\"Select all\", on_click=rxe.ag_grid.api(id=\"ag_grid_basic_row_selection\").select_all()),\npython demo exec toggle\nimport reflex as rx\nimport reflex_enterprise as rxe\nimport pandas as pd\n\ndf = pd.read_csv(\n    \"https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv\"\n)\n\ncolumn_defs = [\n    {\"field\": \"country\", \"checkboxSelection\": True},\n    {\"field\": \"pop\"},\n    {\"field\": \"continent\"},\n]\n\ndef ag_grid_api_simple2():\n    my_api = rxe.ag_grid.api(id=\"ag_grid_export_and_resize\")\n    return rx.vstack(\n            rxe.ag_grid(\n            id=\"ag_grid_export_and_resize\",\n            row_data=df.to_dict(\"records\"),\n            column_defs=column_defs,\n            width=\"100%\",\n            height=\"40vh\",\n        ),\n        rx.button(\"Export\", on_click=my_api.export_data_as_csv()),\n        rx.button(\"Resize Columns\", on_click=my_api.size_columns_to_fit()),\n        spacing=\"4\",\n        width=\"100%\",\n    )\npython\nimport reflex as rx\nimport reflex_enterprise as rxe\nimport pandas as pd\n\nclass AGGridStateAPI(rx.State):\n    def handle_get_data(self, data: str):\n        yield rx.toast(f\"Got CSV data: {data}\")\n\ndf = pd.read_csv(\n    \"https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv\"\n)\n\ncolumn_defs = [\n    \\{\"field\": \"country\", \"checkboxSelection\": True\\},\n    \\{\"field\": \"pop\"\\},\n    \\{\"field\": \"continent\"\\},\n]\n\ndef ag_grid_api_argument():\n    my_api = rxe.ag_grid.api(id=\"ag_grid_get_data_as_csv\")\n    return rx.vstack(\n        rxe.ag_grid(\n            id=\"ag_grid_get_data_as_csv\",\n            row_data=df.to_dict(\"records\"),\n            column_defs=column_defs,\n            width=\"100%\",\n            height=\"40vh\",\n        ),\n        rx.button(\"Get CSV data on backend\", on_click=my_api.get_data_as_csv(callback=AGGridStateAPI.handle_get_data)),\n        spacing=\"4\",\n        width=\"100%\",\n    )\n``get_data_as_csvgetDataAsCsv = (params?: CsvExportParams) => string  |  undefined;stringcallbackget_data_as_csvhandle_get_dataget_data_as_csv` method."
  },
  {
    "name": "Pivot Mode",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Pivot Mode"
    ],
    "url": "docs/enterprise/ag-grid/pivot-mode",
    "description": "Pivot Mode\n\nPivot mode allows you to visualize your data in a different way than how they are originally structured in the data source. When pivoting on a column, the values in that column will be used as column headers. This allows you to see the data in a more compact way, and can be useful when you have a lot of data to display.\n\nTo enable pivot mode, set the  property to  in the grid props. Once pivot mode is enabled, you can define which column to pivot on by setting the  property in a column definition. In addition to the pivot column, at least one column definition must have  property set to  to define the row grouping.\n\nYou can also define how rows are aggregated by passing the  property in the column definition. The  property should be set to a string that represents the aggregation function to use. The built-in aggregation functions are , , , , , , and .\n\nYou can find a live example here: Pivot Mode Example.\n\nPivot using State"
  },
  {
    "name": "Theme",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Theme"
    ],
    "url": "docs/enterprise/ag-grid/theme",
    "description": "---\norder: 3\n---\n\nThemes\n\nYou can style your grid with a theme. AG Grid includes the following themes:\n\n1. \n2. \n3. \n4. \n\nThe grid uses  by default. To use any other theme, set it using the  prop, i.e. .\n\nAG Grid"
  },
  {
    "name": "Column Defs",
    "parts": [
      "Enterprise",
      "Ag Grid",
      "Column Defs"
    ],
    "url": "docs/enterprise/ag-grid/column-defs",
    "description": "---\norder: 1\n---\n\nColumn Definitions\n\nBasic Columns\n\nAgGrid allows you to define the columns of your grid, passed to the prop . Each dictionary represents a column.\n\nHere we define a grid with 3 columns:\n\nTo set default properties for all your columns, you can define  in your grid:"
  },
  {
    "name": "Browser Storage",
    "parts": [
      "API Reference",
      "Browser Storage"
    ],
    "url": "docs/api-reference/browser-storage",
    "description": "Browser Storage\n\nrx.Cookie\n\nRepresents a state Var that is stored as a cookie in the browser. Currently only supports string values.\n\nParameters\n\n-  : The name of the cookie on the client side.\n- : The cookie path. Use  to make the cookie accessible on all pages.\n-  : Relative max age of the cookie in seconds from when the client receives it.\n- : Domain for the cookie (e.g.,  or ).\n- : If the cookie is only accessible through HTTPS.\n- : Whether the cookie is sent with third-party requests. Can be one of (, , , , ).\n\nAccessing Cookies\n\nCookies are accessed like any other Var in the state. If another state needs access\nto the value of a cookie, the state should be a substate of the state that defines\nthe cookie. Alternatively the  API can be used to access the other state.\n\nFor rendering cookies in the frontend, import the state that defines the cookie and\nreference it directly.\n\nrx.remove_cookies\n\nRemove a cookie from the client's browser.\n\nParameters:\n\n- : The name of cookie to remove.\n\nThis event can also be returned from an event handler:\n\nrx.LocalStorage\n\nRepresents a state Var that is stored in localStorage in the browser. Currently only supports string values.\n\nParameters\n\n- : The name of the storage key on the client side.\n- : Boolean indicates if the state should be kept in sync across tabs of the same browser.\n\nSyncing Vars\n\nBecause LocalStorage applies to the entire browser, all LocalStorage Vars are\nautomatically shared across tabs.\n\nThe  parameter controls whether an update in one tab should be actively\npropagated to other tabs without requiring a navigation or page refresh event.\n\nrx.remove_local_storage\n\nRemove a local storage item from the client's browser.\n\nParameters\n\n- : The key to remove from local storage.\n\nThis event can also be returned from an event handler:\n\nrx.clear_local_storage()\n\nClear all local storage items from the client's browser. This may affect other\napps running in the same domain or libraries within your app that use local\nstorage.\n\nrx.SessionStorage\n\nRepresents a state Var that is stored in sessionStorage in the browser. Similar to localStorage, but the data is cleared when the page session ends (when the browser/tab is closed). Currently only supports string values.\n\nParameters\n\n- : The name of the storage key on the client side.\n\nSession Persistence\n\nSessionStorage data is cleared when the page session ends. A page session lasts as long as the browser is open and survives page refreshes and restores, but is cleared when the tab or browser is closed.\n\nUnlike LocalStorage, SessionStorage is isolated to the tab/window in which it was created, so it's not shared with other tabs/windows of the same origin.\n\nrx.remove_session_storage\n\nRemove a session storage item from the client's browser.\n\nParameters\n\n- : The key to remove from session storage.\n\nThis event can also be returned from an event handler:\n\nrx.clear_session_storage()\n\nClear all session storage items from the client's browser. This may affect other\napps running in the same domain or libraries within your app that use session\nstorage.\n\nSerialization Strategies\n\nIf a non-trivial data structure should be stored in a , , or  var it needs to be serialized before and after storing it. It is recommended to use a pydantic class for the data which provides simple serialization helpers and works recursively in complex object structures.\n\nComparison of Storage Types\n\nHere's a comparison of the different client-side storage options in Reflex:\n\n| Feature | rx.Cookie | rx.LocalStorage | rx.SessionStorage |\n|---------|-----------|----------------|------------------|\n| Persistence | Until cookie expires | Until explicitly deleted | Until browser/tab is closed |\n| Storage Limit | ~4KB | ~5MB | ~5MB |\n| Sent with Requests | Yes | No | No |\n| Accessibility | Server & Client | Client Only | Client Only |\n| Expiration | Configurable | Never | End of session |\n| Scope | Configurable (domain, path) | Origin (domain) | Tab/Window |\n| Syncing Across Tabs | No | Yes (with sync=True) | No |\n| Use Case | Authentication, Server-side state | User preferences, App state | Temporary session data |\n\nWhen to Use Each Storage Type\n\nUse rx.Cookie When:\n- You need the data to be accessible on the server side (cookies are sent with HTTP requests)\n- You're handling user authentication\n- You need fine-grained control over expiration and scope\n- You need to limit the data to specific paths in your app\n\nUse rx.LocalStorage When:\n- You need to store larger amounts of data (up to ~5MB)\n- You want the data to persist indefinitely (until explicitly deleted)\n- You need to share data between different tabs/windows of your app\n- You want to store user preferences that should be remembered across browser sessions\n\nUse rx.SessionStorage When:\n- You need temporary data that should be cleared when the browser/tab is closed\n- You want to isolate data to a specific tab/window\n- You're storing sensitive information that shouldn't persist after the session ends\n- You're implementing per-session features like form data, shopping carts, or multi-step processes\n- You want to persist data for a state after Redis expiration (for server-side state that needs to survive longer than Redis TTL)"
  },
  {
    "name": "Var System",
    "parts": [
      "API Reference",
      "Var System"
    ],
    "url": "docs/api-reference/var-system",
    "description": "Reflex's Var System\n\nMotivation\n\nReflex supports some basic operations in state variables on the frontend.\nReflex automatically converts variable operations from Python into a JavaScript equivalent.\n\nHere's an example of a Reflex conditional in Python that returns \"Pass\" if the threshold is equal to or greater than 50 and \"Fail\" otherwise:\n\n The conditional to roughly the following in Javascript:\n\nOverview\n\nSimply put, a  in Reflex represents a Javascript expression.\nIf the type is known, it can be any of the following:\n\n-  represents an expression that evaluates to a Javascript .  can support both integers and floating point values\n-  represents a boolean expression. For example: , .\n-  represents an expression that evaluates to a string. For example: , .\n-  represents an expression that evaluates to an array object. For example: , .\n-  represents an expression that evaluates to an object. For example: , .\n-  represent null values. These can be either  or .\n\nCreating Vars\n\nState fields are converted to  by default. Additionally, you can create a  from Python values using :\n\nIf you want to explicitly create a  from a raw Javascript string, you can instantiate  directly:\n\nIn the example above,  will attempt to downcast from a generic  type into .\nFor this example, calling the function  can also be used in place of .\n\nOperations\n\nThe  system also supports some other basic operations.\nFor example,  supports basic arithmetic operations like  and , as in Python.\nIt also supports comparisons that return a .\n\nCustom  operations can also be defined:\n\nUse  to pass explicit JavaScript expressions; in the  example, we pass in a JavaScript expression that calculates the product of all elements in an array called  by using the reduce method to multiply each element with the accumulated result, starting from an initial value of 1.\nLater, we leverage  in the' factorial' function, we instantiate an array using the  function, and pass this array to ."
  },
  {
    "name": "CLI",
    "parts": [
      "API Reference",
      "CLI"
    ],
    "url": "docs/api-reference/cli",
    "description": "CLI\n\nThe  command line interface (CLI) is a tool for creating and managing Reflex apps.\n\nTo see a list of all available commands, run .\n\nInit\n\nThe  command creates a new Reflex app in the current directory.\nIf an  file already exists already, it will re-initialize the app with the latest template.\n\nRun\n\nThe  command runs the app in the current directory.\n\nBy default it runs your app in development mode.\nThis means that the app will automatically reload when you make changes to the code.\nYou can also run in production mode which will create an optimized build of your app.\n\nYou can configure the mode, as well as other options through flags.\n\nExport\n\nYou can export your app's frontend and backend to zip files using the  command.\n\nThe frontend is a compiled NextJS app, which can be deployed to a static hosting service like Github Pages or Vercel.\nHowever this is just a static build, so you will need to deploy the backend separately.\nSee the self-hosting guide for more information.\n\nRename\n\nThe  command allows you to rename your Reflex app. This updates the app name in the configuration files.\n\nCloud\n\nThe  command provides access to the Reflex Cloud hosting service. It includes subcommands for managing apps, projects, secrets, and more.\n\nFor detailed documentation on Reflex Cloud and deployment, see the Cloud Quick Start Guide.\n\nScript\n\nThe  command provides access to helper scripts for Reflex development."
  },
  {
    "name": "Plugins",
    "parts": [
      "API Reference",
      "Plugins"
    ],
    "url": "docs/api-reference/plugins",
    "description": "Plugins\n\nReflex supports a plugin system that allows you to extend the framework's functionality during the compilation process. Plugins can add frontend dependencies, modify build configurations, generate static assets, and perform custom tasks before compilation.\n\nConfiguring Plugins\n\nPlugins are configured in your  file using the  parameter:\n\nBuilt-in Plugins\n\nReflex comes with several built-in plugins that provide common functionality.\n\nSitemapPlugin\n\nThe  automatically generates a sitemap.xml file for your application, which helps search engines discover and index your pages.\n\nThe sitemap plugin automatically includes all your app's routes. For dynamic routes or custom configuration, you can add sitemap metadata to individual pages:\n\nThe sitemap configuration supports the following options:\n- : Custom URL for the page (required for dynamic routes)\n- : Last modification date (datetime object)\n- : How frequently the page changes (, , , , , , )\n- : Priority of this URL relative to other URLs (0.0 to 1.0)\n\nTailwindV4Plugin\n\nThe  provides support for Tailwind CSS v4, which is the recommended version for new projects and includes performance improvements and new features.\n\nYou can customize the Tailwind configuration by passing a config dictionary:\n\nTailwindV3Plugin\n\nThe  integrates Tailwind CSS v3 into your Reflex application. While still supported, TailwindV4Plugin is recommended for new projects.\n\nYou can customize the Tailwind configuration by passing a config dictionary:\n\nPlugin Management\n\nDefault Plugins\n\nSome plugins are enabled by default. Currently, the  is enabled automatically. If you want to disable a default plugin, use the  parameter:\n\nPlugin Order\n\nPlugins are executed in the order they appear in the  list. This can be important if plugins have dependencies on each other or modify the same files.\n\nPlugin Architecture\n\nAll plugins inherit from the base  class and can implement several lifecycle methods:\n\nCreating Custom Plugins\n\nYou can create custom plugins by inheriting from the base  class:\n\nThen use it in your configuration:"
  },
  {
    "name": "Utils",
    "parts": [
      "API Reference",
      "Utils"
    ],
    "url": "docs/api-reference/utils",
    "description": "Utility Functions\n\nReflex provides utility functions to help with common tasks in your applications.\n\nrun_in_thread\n\nThe  function allows you to run a **non-async** function in a separate thread, which is useful for preventing long-running operations from blocking the UI event queue.\n\nParameters\n\n- : The non-async function to run in a separate thread.\n\nReturns\n\n- The return value of the function.\n\nRaises\n\n- : If the function is an async function.\n\nUsage\n\nWhen to Use run_in_thread\n\nUse  when you need to:\n\n1. Execute CPU-bound operations that would otherwise block the event loop\n2. Call synchronous libraries that don't have async equivalents\n3. Prevent long-running operations from blocking UI responsiveness\n\nExample: Processing a Large File"
  },
  {
    "name": "Special Events",
    "parts": [
      "API Reference",
      "Special Events"
    ],
    "url": "docs/api-reference/special-events",
    "description": "Special Events\n\nReflex includes a set of built-in special events that can be utilized as event triggers\nor returned from event handlers in your applications. These events enhance interactivity and user experience.\nBelow are the special events available in Reflex, along with explanations of their functionality:\n\nrx.console_log\n\nPerform a console.log in the browser's console.\n\nWhen triggered, this event logs a specified message to the browser's developer console.\nIt's useful for debugging and monitoring the behavior of your application.\n\nrx.scroll_to\n\nscroll to an element in the page\n\nWhen this is triggered, it scrolls to an element passed by id as parameter. Click on button to scroll to download button (rx.download section) at the bottom of the page\n\nrx.redirect\n\nRedirect the user to a new path within the application.\n\nParameters\n\n- : The destination path or URL to which the user should be redirected.\n- : If set to True, the redirection will open in a new tab. Defaults to .\n\nWhen this event is triggered, it navigates the user to a different page or location within your Reflex application.\nBy default, the redirection occurs in the same tab. However, if you set the external parameter to True, the redirection\nwill open in a new tab or window, providing a seamless user experience.\n\nThis event can also be run from an event handler in State. It is necessary to  the .\n\nrx.set_clipboard\n\nSet the specified text content to the clipboard.\n\nThis event allows you to copy a given text or content to the user's clipboard.\nIt's handy when you want to provide a \"Copy to Clipboard\" feature in your application,\nallowing users to easily copy information to paste elsewhere.\n\nrx.set_value\n\nSet the value of a specified reference element.\n\nWith this event, you can modify the value of a particular HTML element, typically an input field or another form element.\n\nrx.window_alert\n\nCreate a window alert in the browser.\n\nrx.download\n\nDownload a file at a given path.\n\nParameters:\n\n- : The URL of the file to be downloaded.\n- : The data to be downloaded. Should be  or ,  URI, , or any state Var (to be converted to JSON).\n- : The desired filename of the downloaded file."
  },
  {
    "name": "Event Triggers",
    "parts": [
      "API Reference",
      "Event Triggers"
    ],
    "url": "docs/api-reference/event-triggers",
    "description": "Event Triggers\n\nComponents can modify the state based on user events such as clicking a button or entering text in a field.\nThese events are triggered by event triggers.\n\nEvent triggers are component specific and are listed in the documentation for each component.\n\nComponent Lifecycle Events\n\nReflex components have lifecycle events like  and  that allow you to execute code at specific points in a component's existence. These events are crucial for initializing data, cleaning up resources, and creating dynamic user interfaces.\n\nWhen Lifecycle Events Are Activated\n\n- **on_mount**: This event is triggered immediately after a component is rendered and attached to the DOM. It fires:\n  - When a page containing the component is first loaded\n  - When a component is conditionally rendered (appears after being hidden)\n  - When navigating to a page containing the component using internal navigation\n  - It does NOT fire when the page is refreshed or when following external links\n\n- **on_unmount**: This event is triggered just before a component is removed from the DOM. It fires:\n  - When navigating away from a page containing the component using internal navigation\n  - When a component is conditionally removed from the DOM (e.g., via a condition that hides it)\n  - It does NOT fire when refreshing the page, closing the browser tab, or following external links\n\nPage Load Events\n\nIn addition to component lifecycle events, Reflex also provides page-level events like  that are triggered when a page loads. The  event is useful for:\n\n- Fetching data when a page first loads\n- Checking authentication status\n- Initializing page-specific state\n- Setting default values for cookies or browser storage\n\nYou can specify an event handler to run when the page loads using the  parameter in the  decorator or  method:\n\nThis is particularly useful for authentication checks:\n\nFor more details on page load events, see the page load events documentation.\n\nEvent Reference"
  },
  {
    "name": "Browser Javascript",
    "parts": [
      "API Reference",
      "Browser Javascript"
    ],
    "url": "docs/api-reference/browser-javascript",
    "description": "Browser Javascript\n\nReflex compiles your frontend code, defined as python functions, into a Javascript web application\nthat runs in the user's browser. There are instances where you may need to supply custom javascript\ncode to interop with Web APIs, use certain third-party libraries, or wrap low-level functionality\nthat is not exposed via Reflex's Python API.\n\nExecuting Script\n\nThere are four ways to execute custom Javascript code into your Reflex app:\n\n-  - Injects the script via  for efficient loading of inline and external Javascript code. Described further in the component library.\n  - These components can be directly included in the body of a page, or they may\n    be passed to  to be included in\n    the  tag of all pages.\n-  - An event handler that evaluates arbitrary Javascript code,\n  and optionally returns the result to another event handler.\n\nThese previous two methods can work in tandem to load external scripts and then\ncall functions defined within them in response to user events.\n\nThe following two methods are geared towards wrapping components and are\ndescribed with examples in the Wrapping React\nsection.\n\n-  and  in an  subclass\n-  with \n\nInline Scripts\n\nThe  component is the recommended way to load inline Javascript for greater control over\nfrontend behavior.\n\nThe functions and variables in the script can be accessed from backend event\nhandlers or frontend event triggers via the  interface.\n\nExternal Scripts\n\nExternal scripts can be loaded either from the  directory, or from CDN URL, and then controlled\nvia .\n\nAccessing Client Side Values\n\nThe  function accepts a  parameter that expects an\nEvent Handler with one argument which will receive the result of evaluating the\nJavascript code. This can be used to access client-side values such as the\n or current scroll location, or any previously defined value.\n\nUsing React Hooks\n\nTo use React Hooks directly in a Reflex app, you must subclass ,\ntypically  is used when the hook functionality has no visual\nelement. The hook code is returned by the  method, which is expected\nto return a  containing Javascript code which will be inserted into the\npage component (i.e the render function itself).\n\nFor supporting code that must be defined outside of the component render\nfunction, use .\n\nThe following example uses  to register global hotkeys on the\n object, and then triggers an event when a specific key is pressed.\n\nThis snippet can also be imported through pip: reflex-global-hotkey."
  },
  {
    "name": "Command Reference",
    "parts": [
      "Custom Components",
      "Command Reference"
    ],
    "url": "docs/custom-components/command-reference",
    "description": "Command Reference\n\nThe custom component commands are under  subcommand. To see the list of available commands, run . To see the manual on a specific command, run , for example, .\n\nreflex component init\n\nBelow is an example of running the  command.\n\nThe  command uses the current enclosing folder name to construct a python package name, typically in the kebab case. For example, if running init in folder , the package name will be . The added prefix reduces the chance of name collision on PyPI (the Python Package Index), and it indicates that the package is a Reflex custom component. The user can override the package name by providing the  option.\n\nThe  command creates a set of files and folders prefilled with the package name and other details. During the init, the  folder is installed locally in editable mode, so a developer can incrementally develop and test with ease. The changes in component implementation is automatically reflected where it is used. Below is the folder structure after the  command.\n\npyproject.toml\n\nThe  is required for the package to build and be published. It is prefilled with information such as the package name, version (), author name and email, homepage URL. By default the **Apache-2.0** license is used, the same as Reflex. If any of this information requires update, the user can edit the file by hand.\n\nREADME\n\nThe  file is created with installation instructions, e.g. , and a brief description of the package. Typically the  contains usage examples. On PyPI, the  is rendered as part of the package page.\n\nCustom Components Folder\n\nThe  folder is where the actual implementation is. Do not worry about this folder name: there is no need to change it. It is where  specifies the source of the python package is. The published package contains the contents inside it, excluding this folder.\n\n is the top folder for importable code. The  imports everything from the . For the user of the package, the import looks like .\n\n is prefilled with code example and instructions from the wrapping react guide.\n\nDemo App Folder\n\nA demo app is generated inside  folder with import statements and example usage of the component. This is a regular Reflex app. Go into this directory and start using any reflex commands for testing. The user is encouraged to deploy the demo app, so it can later be included as part of the Gallery.\n\nHelp Manual\n\nThe help manual is shown when adding the  option to the command.\n\nreflex component publish\n\nTo publish to a package index, a user is required to already have an account with them. As of **0.7.5**, Reflex does not handle the publishing process for you. You can do so manually by first running  followed by  or  or your choice of a publishing utility.\n\nYou can then share your build on our website with .\n\nreflex component build\n\nIt is not required to run the  command separately before publishing. The  command will build the package if it is not already built. The  command is provided for the user's convenience.\n\nThe  command generates the  and  distribution files to be uploaded to the desired package index, for example, PyPI. This command must be run at the top level of the project where the  file is. As a result of a successful build, there is a new  folder with the distribution files."
  },
  {
    "name": "Overview",
    "parts": [
      "Custom Components",
      "Overview"
    ],
    "url": "docs/custom-components/overview",
    "description": "Custom Components Overview\n\nReflex users create many components of their own: ready to use high level components, or nicely wrapped React components. With **Custom Components**, the community can easily share these components now.\n\nRelease **0.4.3** introduces a series of  commands that help developers wrap react components, test, and publish them as python packages. As shown in the image below, there are already a few custom components published on PyPI, such as , .\n\nCheck out the custom components gallery here.\n\nPrerequisites for Publishing\n\nIn order to publish a Python package, an account is required with a python package index, for example, PyPI. The documentation to create accounts and generate API tokens can be found on their websites. For a quick reference, check out our Prerequisites for Publishing page.\n\nSteps to Publishing\n\nFollow these steps to publish the custom component as a python package:\n\n1. : creates a new custom component project from templates.\n2. dev and test: developer implements and tests the custom component.\n3. : builds the package.\n4.  or : uploads the package to a python package index.\n\nInitialization\n\nFirst create a new folder for your custom component project, for example . The package name will be . The prefix  is intentionally added for all custom components for easy search on PyPI. If you prefer a particular name for the package, you can either change it manually in the  file or add the  option in the  command initially.\n\nRun , and a set of files and folders will be created in the  folder. The  file is the configuration file for the project. The  folder is where the custom component implementation is. The  folder is a demo Reflex app that uses the custom component. If this is the first time of creating python packages, it is encouraged to browse through all the files (there are not that many) to understand the structure of the project.\n\nDevelop and Test\n\nAfter finishing the custom component implementation, the user is encouraged to fully test it before publishing. The generated Reflex demo app  is a good place to start. It is a regular Reflex app prefilled with imports and usage of this component. During the init, the  folder is installed locally in editable mode, so a developer can incrementally develop and test with ease. The changes in component implementation are automatically reflected in the demo app.\n\nPublish\n\nOnce you're ready to publish your package, run  to build the package. The command builds the distribution files if they are not already built. The end result is a  folder containing the distribution files. The user does not need to do anything manually with these distribution files.\n\nIn order to publish these files as a Python package, you need to use a publishing utility. Any would work, but we recommend either Twine or (uv)[https://docs.astral.sh/uv/guides/package/#publishing-your-package]. Make sure to keep your package version in pyproject.toml updated.\n\nYou can also share your components with the rest of the community at our website using the command . See you there!"
  },
  {
    "name": "Prerequisites For Publishing",
    "parts": [
      "Custom Components",
      "Prerequisites For Publishing"
    ],
    "url": "docs/custom-components/prerequisites-for-publishing",
    "description": "Python Package Index\n\nIn order to publish a Python package, you need to use a publishing utility. Any would work, but we recommend either Twine or (uv)[https://docs.astral.sh/uv/guides/package/#publishing-your-package].\n\nPyPI\n\nIt is straightforward to create accounts and API tokens with PyPI. There is official help on the PyPI website. For a quick reference here, go to the top right corner of the PyPI website and look for the button to register and fill out personal information.\n\nA user can use username and password to authenticate with PyPI when publishing.\n\nScroll down to the API tokens section and click on the \"Add API token\" button. Fill out the form and click \"Generate API token\"."
  },
  {
    "name": "Accordion",
    "parts": [
      "Library",
      "Disclosure",
      "Accordion"
    ],
    "url": "docs/library/disclosure/accordion",
    "description": "---\ncomponents:\n  - rx.accordion.root\n  - rx.accordion.item\n\nAccordionRoot: |\n  lambda **props: rx.accordion.root(\n      rx.accordion.item(header=\"First Item\", content=\"The first accordion item's content\"),\n      rx.accordion.item(\n          header=\"Second Item\", content=\"The second accordion item's content\",\n      ),\n      rx.accordion.item(header=\"Third item\", content=\"The third accordion item's content\"),\n      width=\"300px\",\n      **props,\n  )\n\nAccordionItem: |\n  lambda **props: rx.accordion.root(\n      rx.accordion.item(header=\"First Item\", content=\"The first accordion item's content\", **props),\n      rx.accordion.item(\n          header=\"Second Item\", content=\"The second accordion item's content\", **props,\n      ),\n      rx.accordion.item(header=\"Third item\", content=\"The third accordion item's content\", **props),\n      width=\"300px\",\n  )\n---\n\nAccordion\n\nAn accordion is a vertically stacked set of interactive headings that each reveal an associated section of content.\nThe accordion component is made up of , which is the root of the component and takes in an ,\nwhich contains all the contents of the collapsible section.\n\nBasic Example\n\nStyling\n\nType\n\nWe use the  prop to determine whether multiple items can be opened at once. The allowed values for this prop are\n and  where  will only open one item at a time. The default value for this prop is .\n\nDefault Value\n\nWe use the  prop to specify which item should open by default. The value for this prop should be any of the\nunique values set by an .\n\nCollapsible\n\nWe use the  prop to allow all items to close. If set to , an opened item cannot be closed.\n\nDisable\n\nWe use the  prop to prevent interaction with the accordion and all its items.\n\nOrientation\n\nWe use  prop to set the orientation of the accordion to  or . By default, the orientation\nwill be set to . Note that, the orientation prop won't change the visual orientation but the\nfunctional orientation of the accordion. This means that for vertical orientation, the up and down arrow keys moves focus between the next or previous item,\nwhile for horizontal orientation, the left or right arrow keys moves focus between items.\n\nVariant\n\nColor Scheme\n\nWe use the  prop to assign a specific color to the accordion background, ignoring the global theme.\n\nValue\n\nWe use the  prop to specify the controlled value of the accordion item that we want to activate.\nThis property should be used in conjunction with the  event argument.\n\nAccordionItem\n\nThe accordion item contains all the parts of a collapsible section.\n\nStyling\n\nValue\n\nDisable"
  },
  {
    "name": "Segmented Control",
    "parts": [
      "Library",
      "Disclosure",
      "Segmented Control"
    ],
    "url": "docs/library/disclosure/segmented-control",
    "description": "---\ncomponents:\n    - rx.segmented_control.root\n    - rx.segmented_control.item\n---\n\nSegmented Control\n\nSegmented Control offers a clear and accessible way to switch between predefined values and views, e.g., \"Inbox,\" \"Drafts,\" and \"Sent.\"\n\nWith Segmented Control, you can make mutually exclusive choices, where only one option can be active at a time, clear and accessible. Without Segmented Control, end users might have to deal with controls like dropdowns or multiple buttons that don't clearly convey state or group options together visually.\n\nBasic Example\n\nThe  component is made up of a  which groups .\n\nThe  components define the individual segments of the control, each with a label and a unique value.\n\n**In the example above:**\n\n is used to specify a callback function that will be called when the user selects a different segment. In this case, the  function is used to update the  state variable when the user changes the selected segment.\n\n prop is used to specify the currently selected segment, which is bound to the  state variable."
  },
  {
    "name": "Tabs",
    "parts": [
      "Library",
      "Disclosure",
      "Tabs"
    ],
    "url": "docs/library/disclosure/tabs",
    "description": "---\ncomponents:\n  - rx.tabs.root\n  - rx.tabs.list\n  - rx.tabs.trigger\n  - rx.tabs.content\n\nonly_low_level:\n  - True\n\nTabsRoot: |\n  lambda **props: rx.tabs.root(\n      rx.tabs.list(\n          rx.tabs.trigger(\"Account\", value=\"account\"),\n          rx.tabs.trigger(\"Documents\", value=\"documents\"),\n          rx.tabs.trigger(\"Settings\", value=\"settings\"),\n      ),\n      rx.box(\n          rx.tabs.content(\n              rx.text(\"Make changes to your account\"),\n              value=\"account\",\n          ),\n          rx.tabs.content(\n              rx.text(\"Update your documents\"),\n              value=\"documents\",\n          ),\n          rx.tabs.content(\n              rx.text(\"Edit your personal profile\"),\n              value=\"settings\",\n          ),\n      ),\n      **props,\n  )\n\nTabsList: |\n  lambda **props: rx.tabs.root(\n      rx.tabs.list(\n          rx.tabs.trigger(\"Account\", value=\"account\"),\n          rx.tabs.trigger(\"Documents\", value=\"documents\"),\n          rx.tabs.trigger(\"Settings\", value=\"settings\"),\n          **props,\n      ),\n      rx.box(\n          rx.tabs.content(\n              rx.text(\"Make changes to your account\"),\n              value=\"account\",\n          ),\n          rx.tabs.content(\n              rx.text(\"Update your documents\"),\n              value=\"documents\",\n          ),\n          rx.tabs.content(\n              rx.text(\"Edit your personal profile\"),\n              value=\"settings\",\n          ),\n      ),\n  )\n\nTabsTrigger: |\n  lambda **props: rx.tabs.root(\n      rx.tabs.list(\n          rx.tabs.trigger(\"Account\", value=\"account\", **props,),\n          rx.tabs.trigger(\"Documents\", value=\"documents\"),\n          rx.tabs.trigger(\"Settings\", value=\"settings\"),\n      ),\n      rx.box(\n          rx.tabs.content(\n              rx.text(\"Make changes to your account\"),\n              value=\"account\",\n          ),\n          rx.tabs.content(\n              rx.text(\"Update your documents\"),\n              value=\"documents\",\n          ),\n          rx.tabs.content(\n              rx.text(\"Edit your personal profile\"),\n              value=\"settings\",\n          ),\n      ),\n  )\n\nTabsContent: |\n  lambda **props: rx.tabs.root(\n      rx.tabs.list(\n          rx.tabs.trigger(\"Account\", value=\"account\"),\n          rx.tabs.trigger(\"Documents\", value=\"documents\"),\n          rx.tabs.trigger(\"Settings\", value=\"settings\"),\n      ),\n      rx.box(\n          rx.tabs.content(\n              rx.text(\"Make changes to your account\"),\n              value=\"account\",\n              **props,\n          ),\n          rx.tabs.content(\n              rx.text(\"Update your documents\"),\n              value=\"documents\",\n              **props,\n          ),\n          rx.tabs.content(\n              rx.text(\"Edit your personal profile\"),\n              value=\"settings\",\n              **props,\n          ),\n      ),\n  )\n---\n\nTabs\n\nTabs are a set of layered sections of content—known as tab panels that are displayed one at a time.\nThey facilitate the organization and navigation between sets of content that share a connection and exist at a similar level of hierarchy.\n\nBasic Example\n\nThe  component is made up of a  which groups  and  parts.\n\nStyling\n\nDefault value\n\nWe use the  prop to set a default active tab, this will select the specified tab by default.\n\nOrientation\n\nWe use  prop to set the orientation of the tabs component to  or . By default, the orientation\nwill be set to . Setting this value will change both the visual orientation and the functional orientation.\n\nValue\n\nWe use the  prop to specify the controlled value of the tab that we want to activate. This property should be used in conjunction with the  event argument.\n\nTablist\n\nThe Tablist is used to list the respective tabs to the tab component\n\nTab Trigger\n\nThis is the button that activates the tab's associated content. It is typically used in the \n\nStyling\n\nValue\n\nWe use the  prop to assign a unique value that associates the trigger with content.\n\nDisable\n\nWe use the  prop to disable the tab.\n\nTabs Content\n\nContains the content associated with each trigger.\n\nStyling\n\nValue\n\nWe use the  prop to assign a unique value that associates the content with a trigger."
  },
  {
    "name": "Input",
    "parts": [
      "Library",
      "Forms",
      "Input"
    ],
    "url": "docs/library/forms/input",
    "description": "---\ncomponents:\n  - rx.input\n  - rx.input.slot\n\nInput: |\n  lambda **props: rx.input(placeholder=\"Search the docs\", **props)\n\nTextFieldSlot: |\n  lambda **props: rx.input(\n      rx.input.slot(\n          rx.icon(tag=\"search\", height=\"16\", width=\"16\"),\n          **props,\n      ),\n      placeholder=\"Search the docs\",\n  )\n---\n\nInput\n\nThe  component is an input field that users can type into.\n\nBasic Example\n\nThe  event handler is called when focus has left the  for example, it’s called when the user clicks outside of a focused text input.\n\nThe  event handler is called when the  of  has changed.\n\nBehind the scenes, the input component is implemented as a debounced input to avoid sending individual state updates per character to the backend while the user is still typing. This allows a state variable to directly control the  prop from the backend without the user experiencing input lag.\n\nSubmitting a form using input\n\nThe  prop is needed to submit with its owning form as part of a name/value pair.\n\nWhen the  prop is , it indicates that the user must input text before the owning form can be submitted.\n\nThe  is set here to . The element is presented as a one-line plain text editor control in which the text is obscured so that it cannot be read. The  prop can take any value of , , ,  and several others. Learn more here.\n\nTo learn more about how to use forms in the Form docs.\n\nSetting a value without using a State var\n\nSet the value of the specified reference element, without needing to link it up to a State var. This is an alternate way to modify the value of the ."
  },
  {
    "name": "Checkbox",
    "parts": [
      "Library",
      "Forms",
      "Checkbox"
    ],
    "url": "docs/library/forms/checkbox",
    "description": "---\ncomponents:\n  - rx.checkbox\n\nHighLevelCheckbox: |\n  lambda **props: rx.checkbox(\"Basic Checkbox\", **props)\n---\n\nCheckbox\n\nBasic Example\n\nThe  trigger is called when the  is clicked.\n\nThe  prop is used to set the  as a controlled component."
  },
  {
    "name": "Form",
    "parts": [
      "Library",
      "Forms",
      "Form"
    ],
    "url": "docs/library/forms/form",
    "description": "---\ncomponents:\n  - rx.form\n  - rx.form.root\n  - rx.form.field\n  - rx.form.control\n  - rx.form.label\n  - rx.form.message\n  - rx.form.submit\n\nFormRoot: |\n  lambda **props: rx.form.root(\n      rx.form.field(\n          rx.flex(\n              rx.form.label(\"Email\"),\n              rx.form.control(\n                  rx.input(\n                      placeholder=\"Email Address\",\n                      # type attribute is required for \"typeMismatch\" validation\n                      type=\"email\",\n                  ),\n                  as_child=True,\n              ),\n              rx.form.message(\"Please enter a valid email\"),\n              rx.form.submit(\n                  rx.button(\"Submit\"),\n                  as_child=True,\n              ),\n              direction=\"column\",\n              spacing=\"2\",\n              align=\"stretch\",\n          ),\n          name=\"email\",\n      ),\n      **props,\n  )\n\nFormField: |\n  lambda **props: rx.form.root(\n      rx.form.field(\n          rx.flex(\n              rx.form.label(\"Email\"),\n              rx.form.control(\n                  rx.input(\n                      placeholder=\"Email Address\",\n                      # type attribute is required for \"typeMismatch\" validation\n                      type=\"email\",\n                  ),\n                  as_child=True,\n              ),\n              rx.form.message(\"Please enter a valid email\", match=\"typeMismatch\"),\n              rx.form.submit(\n                  rx.button(\"Submit\"),\n                  as_child=True,\n              ),\n              direction=\"column\",\n              spacing=\"2\",\n              align=\"stretch\",\n          ),\n          **props,\n      ),\n      reset_on_submit=True,\n  )\n\nFormLabel: |\n  lambda **props: rx.form.root(\n      rx.form.field(\n          rx.flex(\n              rx.form.label(\"Email\", **props,),\n              rx.form.control(\n                  rx.input(\n                      placeholder=\"Email Address\",\n                      # type attribute is required for \"typeMismatch\" validation\n                      type=\"email\",\n                  ),\n                  as_child=True,\n              ),\n              rx.form.message(\"Please enter a valid email\", match=\"typeMismatch\"),\n              rx.form.submit(\n                  rx.button(\"Submit\"),\n                  as_child=True,\n              ),\n              direction=\"column\",\n              spacing=\"2\",\n              align=\"stretch\",\n          ),\n      ),\n      reset_on_submit=True,\n  )\n\nFormMessage: |\n  lambda **props: rx.form.root(\n              rx.form.field(\n                  rx.flex(\n                      rx.form.label(\"Email\"),\n                      rx.form.control(\n                          rx.input(\n                              placeholder=\"Email Address\",\n                              # type attribute is required for \"typeMismatch\" validation\n                              type=\"email\",\n                          ),\n                          as_child=True,\n                      ),\n                      rx.form.message(\"Please enter a valid email\", **props,),\n                      rx.form.submit(\n                          rx.button(\"Submit\"),\n                          as_child=True,\n                      ),\n                      direction=\"column\",\n                      spacing=\"2\",\n                      align=\"stretch\",\n                  ),\n                  name=\"email\",\n              ),\n              on_submit=lambda form_data: rx.window_alert(form_data.to_string()),\n              reset_on_submit=True,\n          )\n---\n\nForm\n\nForms are used to collect user input. The  component is used to group inputs and submit them together.\n\nThe form component's children can be form controls such as , , , , ,  or . The controls should have a  attribute that is used to identify the control in the form data. The  event trigger submits the form data as a dictionary to the  event handler.\n\nThe form is submitted when the user clicks the submit button or presses enter on the form controls.\n\nDynamic Forms\n\nForms can be dynamically created by iterating through state vars using .\n\nThis example allows the user to add new fields to the form prior to submit, and all\nfields will be included in the form data passed to the  function."
  },
  {
    "name": "Slider",
    "parts": [
      "Library",
      "Forms",
      "Slider"
    ],
    "url": "docs/library/forms/slider",
    "description": "---\ncomponents:\n  - rx.slider\n\nSlider: |\n  lambda **props: rx.center(rx.slider(default_value=40, height=\"100%\", **props), height=\"4em\", width=\"100%\")\n---\n\nSlider\n\nProvides user selection from a range of values. The\n\nBasic Example\n\nThe slider can be controlled by a single value or a range of values. Slider can be hooked to state to control its value. Passing a list of two values creates a range slider.\n\nRange Slider\n\nRange slider is created by passing a list of two values to the  prop. The list should contain two values that are in the range of the slider.\n\nLive Updating Slider\n\nYou can use the  prop to update the slider value as you interact with it. The  prop takes a function that will be called with the new value of the slider.\n\nHere we use the  method to limit the rate at which the function is called, which is useful to prevent excessive updates. In this example, the slider value is updated every 100ms.\n\nSlider in forms\n\nHere we show how to use a slider in a form. We use the  prop to identify the slider in the form data. The form data is then passed to the  method to be processed."
  },
  {
    "name": "Button",
    "parts": [
      "Library",
      "Forms",
      "Button"
    ],
    "url": "docs/library/forms/button",
    "description": "---\ncomponents:\n  - rx.button\n\nButton: |\n  lambda **props: rx.button(\"Basic Button\", **props)\n---\n\nButton\n\nButtons are essential elements in your application's user interface that users can click to trigger events.\n\nBasic Example\n\nThe  trigger is called when the button is clicked.\n\nLoading and Disabled\n\nThe  prop is used to indicate that the action triggered by the button is currently in progress. When set to , the button displays a loading spinner, providing visual feedback to the user that the action is being processed. This also prevents multiple clicks while the button is in the loading state. By default,  is set to .\n\nThe  prop also prevents the button from being but does not provide a spinner."
  },
  {
    "name": "Select",
    "parts": [
      "Library",
      "Forms",
      "Select"
    ],
    "url": "docs/library/forms/select",
    "description": "---\ncomponents:\n  - rx.select\n  - rx.select.root\n  - rx.select.trigger\n  - rx.select.content\n  - rx.select.group\n  - rx.select.item\n  - rx.select.label\n  - rx.select.separator\n\nHighLevelSelect: |\n  lambda **props: rx.select([\"apple\", \"grape\", \"pear\"], default_value=\"pear\", **props)\n\nSelectRoot: |\n  lambda **props: rx.select.root(\n      rx.select.trigger(),\n      rx.select.content(\n          rx.select.group(\n              rx.select.item(\"apple\", value=\"apple\"),\n              rx.select.item(\"grape\", value=\"grape\"),\n              rx.select.item(\"pear\", value=\"pear\"),\n          ),\n      ),\n      default_value=\"pear\",\n      **props\n  )\n\nSelectTrigger: |\n  lambda **props: rx.select.root(\n      rx.select.trigger(**props),\n      rx.select.content(\n          rx.select.group(\n              rx.select.item(\"apple\", value=\"apple\"),\n              rx.select.item(\"grape\", value=\"grape\"),\n              rx.select.item(\"pear\", value=\"pear\"),\n          ),\n      ),\n      default_value=\"pear\",\n  )\n\nSelectContent: |\n  lambda **props: rx.select.root(\n      rx.select.trigger(),\n      rx.select.content(\n          rx.select.group(\n              rx.select.item(\"apple\", value=\"apple\"),\n              rx.select.item(\"grape\", value=\"grape\"),\n              rx.select.item(\"pear\", value=\"pear\"),\n          ),\n          **props,\n      ),\n      default_value=\"pear\",\n  )\n\nSelectItem: |\n  lambda **props: rx.select.root(\n      rx.select.trigger(),\n      rx.select.content(\n          rx.select.group(\n              rx.select.item(\"apple\", value=\"apple\", **props),\n              rx.select.item(\"grape\", value=\"grape\"),\n              rx.select.item(\"pear\", value=\"pear\"),\n          ),\n      ),\n      default_value=\"pear\",\n  )\n---\n\nSelect\n\nDisplays a list of options for the user to pick from—triggered by a button.\n\nThe  event handler acts in a similar way to the  and is called when the open state of the select changes.\n\nSubmitting a form using select\n\nThe  prop is needed to submit with its owning form as part of a name/value pair.\n\nWhen the  prop is , it indicates that the user must select a value before the owning form can be submitted.\n\nUsing Select within a Drawer component\n\nIf using within a Drawer component, set the  prop to  to ensure the select menu is displayed correctly."
  },
  {
    "name": "Text Area",
    "parts": [
      "Library",
      "Forms",
      "Text Area"
    ],
    "url": "docs/library/forms/text-area",
    "description": "---\ncomponents:\n  - rx.text_area\n\nTextArea: |\n  lambda **props: rx.text_area(**props)\n---\n\nText Area\n\nA text area is a multi-line text input field.\n\nBasic Example\n\nThe text area component can be controlled by a single value. The  prop can be used to update the value when the text area loses focus.\n\nText Area in forms\n\nHere we show how to use a text area in a form. We use the  prop to identify the text area in the form data. The form data is then passed to the  method to be processed."
  },
  {
    "name": "Radio Group",
    "parts": [
      "Library",
      "Forms",
      "Radio Group"
    ],
    "url": "docs/library/forms/radio-group",
    "description": "---\ncomponents:\n  - rx.radio_group\n  - rx.radio_group.root\n  - rx.radio_group.item\n\nHighLevelRadioGroup: |\n  lambda **props: rx.radio_group([\"1\", \"2\", \"3\", \"4\", \"5\"], **props)\n\nRadioGroupRoot: |\n  lambda **props: rx.radio_group.root(\n      rx.radio_group.item(value=\"1\"),\n      rx.radio_group.item(value=\"2\"),\n      rx.radio_group.item(value=\"3\"),\n      rx.radio_group.item(value=\"4\"),\n      rx.radio_group.item(value=\"5\"),\n      **props\n  )\n\nRadioGroupItem: |\n  lambda **props: rx.radio_group.root(\n      rx.radio_group.item(value=\"1\", **props),\n      rx.radio_group.item(value=\"2\", **props),\n      rx.radio_group.item(value=\"3\",),\n      rx.radio_group.item(value=\"4\",),\n      rx.radio_group.item(value=\"5\",),\n  )\n---\n\nRadio Group\n\nA set of interactive radio buttons where only one can be selected at a time.\n\nBasic example\n\nSubmitting a form using Radio Group\n\nThe  prop is used to name the group. It is submitted with its owning form as part of a name/value pair.\n\nWhen the  prop is , it indicates that the user must check a radio item before the owning form can be submitted."
  },
  {
    "name": "Upload",
    "parts": [
      "Library",
      "Forms",
      "Upload"
    ],
    "url": "docs/library/forms/upload",
    "description": "---\ncomponents:\n  - rx.upload\n  - rx.upload.root\n\nUpload: |\n  lambda **props: rx.center(rx.upload(id=\"my_upload\", **props))\n---\n\nFile Upload\n\nReflex makes it simple to add file upload functionality to your app. You can let users select files, store them on your server, and display or process them as needed. Below is a minimal example that demonstrates how to upload files, save them to disk, and display uploaded images using application state.\n\nBasic File Upload Example\n\nYou can let users upload files and keep track of them in your app’s state. The example below allows users to upload files, saves them using the backend, and then displays the uploaded files as images.\n\nHow File Upload Works\n\nSelecting a file will add it to the browser file list, which can be rendered\non the frontend using the  special Var. To clear the\nselected files, you can use another special Var  as\nan event handler.\n\nTo upload the file(s), you need to bind an event handler and pass the special\n event arg to it.\n\nFile Storage Functions\n\nReflex provides two key functions for handling uploaded files:\n\nrx.get_upload_dir()\n- **Purpose**: Returns a  object pointing to the server-side directory where uploaded files should be saved\n- **Usage**: Used in backend event handlers to determine where to save uploaded files\n- **Default Location**:  (can be customized via  environment variable)\n- **Type**: Returns \n\nrx.get_upload_url(filename)\n- **Purpose**: Returns the URL string that can be used in frontend components to access uploaded files\n- **Usage**: Used in frontend components (like , ) to display uploaded files\n- **URL Format**: \n- **Type**: Returns \n\nKey Differences\n- **rx.get_upload_dir()** -> Backend file path for saving files\n- **rx.get_upload_url()** -> Frontend URL for displaying files\n\nBasic Upload Pattern\n\nHere is the standard pattern for handling file uploads:\n\nMultiple File Upload\n\nBelow is an example of how to allow multiple file uploads (in this case images).\n\nUploading a Single File (Video)\n\nBelow is an example of how to allow only a single file upload and render (in this case a video).\n\nCustomizing the Upload\n\nIn the example below, the upload component accepts a maximum number of 5 files of specific types.\nIt also disables the use of the space or enter key in uploading files.\n\nTo use a one-step upload, bind the event handler to the  component's\n trigger.\n\nUnstyled Upload Component\n\nTo use a completely unstyled upload component and apply your own customization, use  instead:\n\nHandling the Upload\n\nYour event handler should be an async function that accepts a single argument,\n, which will contain FastAPI UploadFile instances.\nYou can read the files and save them anywhere as shown in the example.\n\nIn your UI, you can bind the event handler to a trigger, such as a button\n event or upload  event, and pass in the files using\n.\n\nSaving the File\n\nBy convention, Reflex provides the function  to get the directory where uploaded files may be saved. The upload dir comes from the environment variable , or  if not specified.\n\nThe backend of your app will mount this uploaded files directory on  without restriction. Any files uploaded via this mechanism will automatically be publicly accessible. To get the URL for a file inside the upload dir, use the  function in a frontend component.\n\nDirectory Structure and URLs\n\nBy default, Reflex creates the following structure:\n\nThe files are automatically served at:\n-  ← \n-  ← \n-  ← \n\nCancellation\n\nThe  provided to the  component can be passed to the special event handler  to stop uploading on demand. Cancellation can be triggered directly by a frontend event trigger, or it can be returned from a backend event handler.\n\nProgress\n\nThe  special event arg also accepts an  event trigger which will be fired about every second during the upload operation to report the progress of the upload. This can be used to update a progress bar or other UI elements to show the user the progress of the upload.\n\nThe  dictionary contains the following keys:"
  },
  {
    "name": "Switch",
    "parts": [
      "Library",
      "Forms",
      "Switch"
    ],
    "url": "docs/library/forms/switch",
    "description": "---\ncomponents:\n  - rx.switch\n\nSwitch: |\n  lambda **props: rx.switch(**props)\n---\n\nSwitch\n\nA toggle switch alternative to the checkbox.\n\nBasic Example\n\nHere is a basic example of a switch. We use the  trigger to toggle the value in the state.\n\nControl the value\n\nThe  prop is used to control the state of the switch. The event  is called when the state of the switch changes, when the  event handler is called.\n\nThe  prop when , prevents the user from interacting with the switch. In our example below, even though the second switch is  we are still able to change whether it is checked or not using the  prop.\n\nSwitch in forms\n\nThe  of the switch is needed to submit with its owning form as part of a name/value pair. When the  prop is , it indicates that the user must check the switch before the owning form can be submitted.\n\nThe  prop is only used for form submission, use the  prop to control state of the ."
  },
  {
    "name": "Form Ll",
    "parts": [
      "Library",
      "Forms",
      "Form Ll"
    ],
    "url": "docs/library/forms/form-ll",
    "description": "---\ncomponents:\n  - rx.form.root\n  - rx.form.field\n  - rx.form.control\n  - rx.form.label\n  - rx.form.message\n  - rx.form.submit\n\nFormRoot: |\n  lambda **props: rx.form.root(\n      rx.form.field(\n          rx.flex(\n              rx.form.label(\"Email\"),\n              rx.form.control(\n                  rx.input(\n                      placeholder=\"Email Address\",\n                      # type attribute is required for \"typeMismatch\" validation\n                      type=\"email\",\n                  ),\n                  as_child=True,\n              ),\n              rx.form.message(\"Please enter a valid email\"),\n              rx.form.submit(\n                  rx.button(\"Submit\"),\n                  as_child=True,\n              ),\n              direction=\"column\",\n              spacing=\"2\",\n              align=\"stretch\",\n          ),\n          name=\"email\",\n      ),\n      **props,\n  )\n\nFormField: |\n  lambda **props: rx.form.root(\n      rx.form.field(\n          rx.flex(\n              rx.form.label(\"Email\"),\n              rx.form.control(\n                  rx.input(\n                      placeholder=\"Email Address\",\n                      # type attribute is required for \"typeMismatch\" validation\n                      type=\"email\",\n                  ),\n                  as_child=True,\n              ),\n              rx.form.message(\"Please enter a valid email\", match=\"typeMismatch\"),\n              rx.form.submit(\n                  rx.button(\"Submit\"),\n                  as_child=True,\n              ),\n              direction=\"column\",\n              spacing=\"2\",\n              align=\"stretch\",\n          ),\n          **props,\n      ),\n      reset_on_submit=True,\n  )\n\nFormMessage: |\n  lambda **props: rx.form.root(\n              rx.form.field(\n                  rx.flex(\n                      rx.form.label(\"Email\"),\n                      rx.form.control(\n                          rx.input(\n                              placeholder=\"Email Address\",\n                              # type attribute is required for \"typeMismatch\" validation\n                              type=\"email\",\n                          ),\n                          as_child=True,\n                      ),\n                      rx.form.message(\"Please enter a valid email\", **props,),\n                      rx.form.submit(\n                          rx.button(\"Submit\"),\n                          as_child=True,\n                      ),\n                      direction=\"column\",\n                      spacing=\"2\",\n                      align=\"stretch\",\n                  ),\n                  name=\"email\",\n              ),\n              on_submit=lambda form_data: rx.window_alert(form_data.to_string()),\n              reset_on_submit=True,\n          )\n---\n\nForm\n\nForms are used to collect information from your users. Forms group the inputs and submit them together.\n\nBasic Example\n\nHere is an example of a form collecting an email address, with built-in validation on the email. If email entered is invalid, the form cannot be submitted. Note that the  button is not automatically disabled. It is still clickable, but does not submit the form data. After successful submission, an alert window shows up and the form is cleared. There are a few  containers used in the example to control the layout of the form components.\n\nIn this example, the  has an attribute  and the  has the attribute . Those are required for the form to validate the input by its type. The prop  is required when using other components to construct a Form component. This example has used  to construct the Form Control and  the Form Submit.\n\nForm Anatomy\n\nA Form Root () contains all the parts of a form. The Form Field (), Form Submit (), etc should all be inside a Form Root. A Form Field can contain a Form Label (), a Form Control (), and a Form Message (). A Form Label is a label element. A Form Control is where the user enters the input or makes selections. By default, the Form Control is a input. Using other form components to construct the Form Control is supported. To do that, set the prop  on the Form Control.\n\nThe Form Message is a validation message which is automatically wired (functionality and accessibility). When the Form Control determines the input is invalid, the Form Message is shown. The  prop is to enable client side validation. To perform server side validation, **both** the  prop of the Form Control and the  prop of the Form Field are set together.\n\nThe Form Submit is by default a button that submits the form. To use another button component as a Form Submit, include that button as a child inside  and set the prop .\n\nThe  prop of the Form Root accepts an event handler. It is called with the submitted form data dictionary. To clear the form after submission, set the  prop.\n\nData Submission\n\nAs previously mentioned, the various pieces of data in the form are submitted together as a dictionary. The form control or the input components must have the  attribute. This  is the key to get the value from the form data dictionary. If no validation is needed, the form type components such as Checkbox, Radio Groups, TextArea can be included directly under the Form Root instead of inside a Form Control.\n\nValidation\n\nServer side validation is done through **Computed Vars** on the State. The **Var** should return a boolean flag indicating when input is invalid. Set that **Var** on both the  prop of  and the  prop of . There is an example how to do that in the Final Example.\n\nFinal Example\n\nThe final example shows a form that collects username and email during sign-up and validates them using server side validation. When server side validation fails, messages are displayed in red to show what is not accepted in the form, and the submit button is disabled. After submission, the collected form data is displayed in texts below the form and the form is cleared."
  },
  {
    "name": "Select Ll",
    "parts": [
      "Library",
      "Forms",
      "Select Ll"
    ],
    "url": "docs/library/forms/select-ll",
    "description": "---\ncomponents:\n  - rx.select\n  - rx.select.root\n  - rx.select.trigger\n  - rx.select.content\n  - rx.select.group\n  - rx.select.item\n  - rx.select.label\n  - rx.select.separator\n---\n\nSelect\n\nDisplays a list of options for the user to pick from, triggered by a button.\n\nBasic Example\n\nUsage\n\nDisabling\n\nIt is possible to disable individual items in a  using the  prop associated with the .\n\nTo prevent the user from interacting with select entirely, set the  prop to  on the  component.\n\nSetting Defaults\n\nIt is possible to set several default values when constructing a .\n\nThe  prop in the  specifies the content that will be rendered when  or  is empty or not set.\n\nThe  in the  specifies the value of the  when initially rendered.\nThe  should correspond to the  of a child .\n\nFully controlled\n\nThe  event trigger is fired when the value of the select changes.\nIn this example the   prop specifies which item is selected, and this\ncan also be controlled using state and a button without direct interaction with the select component.\n\nThe  prop and  event trigger work similarly to  and  to control the open state of the select.\nIf  handler does not alter the  prop, the select will not be able to be opened or closed by clicking on the\n.\n\nSubmitting a Form with Select\n\nWhen a select is part of a form, the  prop of the  sets the key that will be submitted with the form data.\n\nThe  prop of  provides the value to be associated with the  key when the form is submitted with that item selected.\n\nWhen the  prop of the  is , it indicates that the user must select a value before the form may be submitted.\n\nReal World Example"
  },
  {
    "name": "Input Ll",
    "parts": [
      "Library",
      "Forms",
      "Input Ll"
    ],
    "url": "docs/library/forms/input-ll",
    "description": "---\ncomponents:\n    - rx.input\n    - rx.input.slot\n---\n\nInput\n\nA text field is an input field that users can type into. This component uses Radix's text field component.\n\nOverview\n\nThe TextField component is used to capture user input and can include an optional slot for buttons and icons. It is based on the <div> element and supports common margin props.\n\nBasic Example\n\nStateful Example with Blur Event\n\nControlled Example\n\nReal World Example"
  },
  {
    "name": "Data Table",
    "parts": [
      "Library",
      "Tables And Data Grids",
      "Data Table"
    ],
    "url": "docs/library/tables-and-data-grids/data-table",
    "description": "---\ncomponents:\n    - rx.data_table\n---\n\nData Table\n\nThe data table component is a great way to display static data in a table format.\nYou can pass in a pandas dataframe to the data prop to create the table.\n\nIn this example we will read data from a csv file, convert it to a pandas dataframe and display it in a data_table.\n\nWe will also add a search, pagination, sorting to the data_table to make it more accessible.\n\nIf you want to add, edit or remove data in your app or deal with anything but static data then the []({library.tables_and_data_grids.table.path}) might be a better fit for your use case.\n\nThe example below shows how to create a data table from from a list."
  },
  {
    "name": "Table",
    "parts": [
      "Library",
      "Tables And Data Grids",
      "Table"
    ],
    "url": "docs/library/tables-and-data-grids/table",
    "description": "---\ncomponents:\n  - rx.table.root\n  - rx.table.header\n  - rx.table.row\n  - rx.table.column_header_cell\n  - rx.table.body\n  - rx.table.cell\n  - rx.table.row_header_cell\n\nonly_low_level:\n  - True\n\nTableRoot: |\n  lambda **props: rx.table.root(\n          rx.table.header(\n              rx.table.row(\n                  rx.table.column_header_cell(\"Full Name\"),\n                  rx.table.column_header_cell(\"Email\"),\n                  rx.table.column_header_cell(\"Group\"),\n              ),\n          ),\n          rx.table.body(\n              rx.table.row(\n                  rx.table.row_header_cell(\"Danilo Rosa\"),\n                  rx.table.cell(\"danilo@example.com\"),\n                  rx.table.cell(\"Developer\"),\n              ),\n              rx.table.row(\n                  rx.table.row_header_cell(\"Zahra Ambessa\"),\n                  rx.table.cell(\"zahra@example.com\"),\n                  rx.table.cell(\"Admin\"),\n              ),\n          ),\n          width=\"80%\",\n          **props,\n      )\n\nTableRow: |\n  lambda **props: rx.table.root(\n          rx.table.header(\n              rx.table.row(\n                  rx.table.column_header_cell(\"Full Name\"),\n                  rx.table.column_header_cell(\"Email\"),\n                  rx.table.column_header_cell(\"Group\"),\n                  **props,\n              ),\n          ),\n          rx.table.body(\n              rx.table.row(\n                  rx.table.row_header_cell(\"Danilo Rosa\"),\n                  rx.table.cell(rx.text(\"danilo@example.com\", as_=\"p\"), rx.text(\"danilo@yahoo.com\", as_=\"p\"), rx.text(\"danilo@gmail.com\", as_=\"p\"),),\n                  rx.table.cell(\"Developer\"),\n                  **props,\n              ),\n              rx.table.row(\n                  rx.table.row_header_cell(\"Zahra Ambessa\"),\n                  rx.table.cell(\"zahra@example.com\"),\n                  rx.table.cell(\"Admin\"),\n                  **props,\n              ),\n          ),\n          width=\"80%\",\n      )\n\nTableColumnHeaderCell: |\n  lambda **props: rx.table.root(\n          rx.table.header(\n              rx.table.row(\n                  rx.table.column_header_cell(\"Full Name\", **props,),\n                  rx.table.column_header_cell(\"Email\", **props,),\n                  rx.table.column_header_cell(\"Group\", **props,),\n              ),\n          ),\n          rx.table.body(\n              rx.table.row(\n                  rx.table.row_header_cell(\"Danilo Rosa\"),\n                  rx.table.cell(\"danilo@example.com\"),\n                  rx.table.cell(\"Developer\"),\n              ),\n              rx.table.row(\n                  rx.table.row_header_cell(\"Zahra Ambessa\"),\n                  rx.table.cell(\"zahra@example.com\"),\n                  rx.table.cell(\"Admin\"),\n              ),\n          ),\n          width=\"80%\",\n      )\n\nTableCell: |\n  lambda **props: rx.table.root(\n          rx.table.header(\n              rx.table.row(\n                  rx.table.column_header_cell(\"Full Name\"),\n                  rx.table.column_header_cell(\"Email\"),\n                  rx.table.column_header_cell(\"Group\"),\n              ),\n          ),\n          rx.table.body(\n              rx.table.row(\n                  rx.table.row_header_cell(\"Danilo Rosa\"),\n                  rx.table.cell(\"danilo@example.com\", **props,),\n                  rx.table.cell(\"Developer\", **props,),\n              ),\n              rx.table.row(\n                  rx.table.row_header_cell(\"Zahra Ambessa\"),\n                  rx.table.cell(\"zahra@example.com\", **props,),\n                  rx.table.cell(\"Admin\", **props,),\n              ),\n          ),\n          width=\"80%\",\n      )\n\nTableRowHeaderCell: |\n  lambda **props: rx.table.root(\n          rx.table.header(\n              rx.table.row(\n                  rx.table.column_header_cell(\"Full Name\"),\n                  rx.table.column_header_cell(\"Email\"),\n                  rx.table.column_header_cell(\"Group\"),\n              ),\n          ),\n          rx.table.body(\n              rx.table.row(\n                  rx.table.row_header_cell(\"Danilo Rosa\", **props,),\n                  rx.table.cell(\"danilo@example.com\"),\n                  rx.table.cell(\"Developer\"),\n              ),\n              rx.table.row(\n                  rx.table.row_header_cell(\"Zahra Ambessa\", **props,),\n                  rx.table.cell(\"zahra@example.com\"),\n                  rx.table.cell(\"Admin\"),\n              ),\n          ),\n          width=\"80%\",\n      )\n---\n\nTable\n\nA semantic table for presenting tabular data.\n\nIf you just want to represent static data then the []({library.tables_and_data_grids.data_table.path}) might be a better fit for your use case as it comes with in-built pagination, search and sorting.\n\nBasic Example\n\nShowing State data (using foreach)\n\nMany times there is a need for the data we represent in our table to be dynamic. Dynamic data must be in . Later we will show an example of how to access data from a database and how to load data from a source file.\n\nIn this example there is a  data structure in  that is iterated through using .\n\nIt is also possible to define a  such as  below and then iterate through this data structure, as a .\n\nSorting and Filtering (Searching)\n\nIn this example we show two approaches to sort and filter data:\n1. Using SQL-like operations for database-backed models (simulated)\n2. Using Python operations for in-memory data\n\nBoth approaches use the same UI components:  for sorting and  for filtering.\n\nApproach 1: Database Filtering and Sorting\n\nFor database-backed models, we typically use SQL queries with , , and . In this example, we'll simulate this behavior with mock data.\n\nApproach 2: In-Memory Filtering and Sorting\n\nFor in-memory data, we use Python operations like  and list comprehensions.\n\nThe state variable  is set to be a backend-only variable. This is done in case the variable is very large in order to reduce network traffic and improve performance.\n\nWhen a  item is selected, the  event trigger is hooked up to the  event handler. Every base var has a built-in event handler to set its value for convenience, called .\n\n is an . It is a var that is only recomputed when the other state vars it depends on change. This ensures that the  shown in the table are always up to date whenever they are searched or sorted.\n\nWhen to Use Each Approach\n\n- **Database Approach**: Best for large datasets or when the data already exists in a database\n- **In-Memory Approach**: Best for smaller datasets, prototyping, or when the data is static or loaded from an API\n\nBoth approaches provide the same user experience with filtering and sorting functionality.\n\nDatabase\n\nThe more common use case for building an  is to use data from a database.\n\nThe code below shows how to load data from a database and place it in an .\n\nLoading data into table\n\nA  model is defined that inherits from .\n\nThe  event handler executes a query that is used to request information from a database table. This  event handler is called on the  event trigger of the .\n\nIf you want to load the data when the page in the app loads you can set  in  to equal this event handler, like .\n\nFiltering (Searching) and Sorting\n\nIn this example we sort and filter the data.\n\nFor sorting the  component is used. The data is sorted based on the attributes of the  class. When a select item is selected, as the  event trigger is hooked up to the  event handler, the data is sorted based on the state variable  attribute selected.\n\nThe sorting query gets the  based on the state variable , it gets the order using the  function from sql and finally uses the  function.\n\nFor filtering the  component is used. The data is filtered based on the search query entered into the  component. When a search query is entered, as the  event trigger is hooked up to the  event handler, the data is filtered based on if the state variable  is present in any of the data in that specific .\n\nThe  character before and after  makes it a wildcard pattern that matches any sequence of characters before or after the .  modifies the existing query to include a filtering condition. The  operator is a logical OR operator that combines multiple conditions. The query will return results that match any of these conditions.  checks if the  column of the  table matches the  pattern in a case-insensitive manner ( stands for \"case-insensitive like\").\n\nPagination\n\nPagination is an important part of database management, especially when working with large datasets. It helps in enabling efficient data retrieval by breaking down results into manageable loads.\n\nThe purpose of this code is to retrieve a specific subset of rows from the  table based on the specified pagination parameters  and .\n\n modifies the query to skip a certain number of rows before returning the results. The number of rows to skip is specified by .\n\n modifies the query to limit the number of rows returned. The maximum number of rows to return is specified by .\n\nMore advanced examples\n\nThe real power of the  comes where you are able to visualise, add and edit data live in your app. Check out these apps and code to see how this is done: app: https://customer-data-app.reflex.run code: https://github.com/reflex-dev/reflex-examples/tree/main/customer_data_app and code: https://github.com/reflex-dev/data-viewer.\n\nDownload\n\nMost users will want to download their data after they have got the subset that they would like in their table.\n\nIn this example there are buttons to download the data as a  and as a .\n\nFor the  download the  is in the frontend code attached to the  event trigger for the button. This works because if the  is not already a string, it will be converted to a string using .\n\nFor the  download the  is in the backend code as an event_handler . There is also a helper function  that converts the data in  to  format.\n\nReal World Example UI"
  },
  {
    "name": "Data Editor",
    "parts": [
      "Library",
      "Tables And Data Grids",
      "Data Editor"
    ],
    "url": "docs/library/tables-and-data-grids/data-editor",
    "description": "---\ncomponents:\n    - rx.data_editor\n---\n\nData Editor\n\nA datagrid editor based on Glide Data Grid\n\nThis component is introduced as an alternative to the datatable to support editing the displayed data.\n\nColumns\n\nThe columns definition should be a  of , each  describing the associated columns.\nProperty of a column dict:\n\n- : The text to display in the header of the column.\n- : An id for the column, if not defined, will default to a lower case of \n- : The width of the column.\n- : The type of the columns, default to .\n\nData\n\nThe  props of  accept a  of , where each  represent a row of data to display in the table.\n\nSimple Example\n\nHere is a basic example of using the data_editor representing data with no interaction and no styling. Below we define the  and the  which are taken in by the  component. When we define the  we must define a  and a  for each column we create. The columns in the  must then match the defined  or errors will be thrown.\n\nInteractive Example\n\nHere we define a State, as shown below, that allows us to print the location of the cell as a heading when we click on it, using the  . Check out all the other  that you can use with datatable at the bottom of this page. We also define a  with a label . This groups all the columns with this  label under a larger group  as seen in the table below.\n\nStyling Example\n\nNow let's style our datatable to make it look more aesthetic and easier to use. We must first import  and then we can start setting our style props as seen below in .\n\nWe then set these themes using . On top of the styling we can also set some  to make some other aesthetic changes to our datatable. We have set the  to equal  so that the content is easier to read. We have also made the  and  equal  so that we can smoothly scroll along the columns and rows. Finally, we added , where column select can take any of the following values ,  or ."
  },
  {
    "name": "Stack",
    "parts": [
      "Library",
      "Layout",
      "Stack"
    ],
    "url": "docs/library/layout/stack",
    "description": "---\ncomponents:\n    - rx.stack\n    - rx.hstack\n    - rx.vstack\nStack: |\n    lambda **props: rx.stack(\n        rx.card(\"Card 1\", size=\"2\"), rx.card(\"Card 2\", size=\"2\"), rx.card(\"Card 3\", size=\"2\"),\n        width=\"100%\",\n        height=\"20vh\",\n        **props,\n    )\n---\n\nStack\n\n is a layout component used to group elements together and apply a space between them.\n\n is used to stack elements in the vertical direction.\n\n is used to stack elements in the horizontal direction.\n\n is used to stack elements in the vertical or horizontal direction.\n\nThese components are based on the  component and therefore inherit all of its props.\n\nThe  component can be used with the  prop to set to either  or  to set the direction.\n\nHstack\n\nVstack\n\nReal World Example"
  },
  {
    "name": "Card",
    "parts": [
      "Library",
      "Layout",
      "Card"
    ],
    "url": "docs/library/layout/card",
    "description": "---\ncomponents:\n  - rx.card\n\nCard: |\n    lambda **props: rx.card(\"Basic Card \", **props)\n---\n\nCard\n\nA Card component is used for grouping related components. It is similar to the Box, except it has a\nborder, uses the theme colors and border radius, and provides a  prop to control spacing\nand margin according to the Radix  -  scale.\n\nThe Card requires less styling than a Box to achieve consistent visual results when used with\nthemes.\n\nBasic Example\n\nRendering as a Different Element\n\nThe  prop may be used to render the Card as a different element. Link and Button are\ncommonly used to make a Card clickable.\n\nUsing Inset Content"
  },
  {
    "name": "Container",
    "parts": [
      "Library",
      "Layout",
      "Container"
    ],
    "url": "docs/library/layout/container",
    "description": "---\ncomponents:\n  - rx.container\n---\n\nContainer\n\nConstrains the maximum width of page content, while keeping flexible margins\nfor responsive layouts.\n\nA Container is generally used to wrap the main content for a page.\n\nBasic Example"
  },
  {
    "name": "Fragment",
    "parts": [
      "Library",
      "Layout",
      "Fragment"
    ],
    "url": "docs/library/layout/fragment",
    "description": "---\ncomponents:\n    - rx.fragment\n---\n\nFragment\n\nA Fragment is a Component that allow you to group multiple Components without a wrapper node.\n\nRefer to the React docs at React/Fragment for more information on its use-case."
  },
  {
    "name": "Aspect Ratio",
    "parts": [
      "Library",
      "Layout",
      "Aspect Ratio"
    ],
    "url": "docs/library/layout/aspect-ratio",
    "description": "---\ncomponents:\n  - rx.aspect_ratio\n---\n\nAspect Ratio\n\nDisplays content with a desired ratio.\n\nBasic Example\n\nSetting the  prop will adjust the width or height\nof the content such that the  divided by the  equals the .\nFor responsive scaling, set the  or  of the content to ."
  },
  {
    "name": "Grid",
    "parts": [
      "Library",
      "Layout",
      "Grid"
    ],
    "url": "docs/library/layout/grid",
    "description": "---\ncomponents:\n  - rx.grid\n---\n\nGrid\n\nComponent for creating grid layouts. Either  or  may be specified.\n\nBasic Example"
  },
  {
    "name": "Flex",
    "parts": [
      "Library",
      "Layout",
      "Flex"
    ],
    "url": "docs/library/layout/flex",
    "description": "---\ncomponents:\n  - rx.flex\n---\n\nFlex\n\nThe Flex component is used to make flexbox layouts.\nIt makes it simple to arrange  child components in horizontal or vertical directions, apply wrapping,\njustify and align  content, and automatically size components based on available space, making it\nideal for building responsive layouts.\n\nBy default, children are arranged horizontally () without wrapping.\n\nBasic Example\n\nWrapping\n\nWith , the children will wrap to the next line instead of being resized.\n\nDirection\n\nWith , the children will be arranged vertically.\n\nAlignment\n\nTwo props control how children are aligned within the Flex component:\n\n*  controls how children are aligned along the cross axis (vertical for  and horizontal for ).\n*  controls how children are aligned along the main axis (horizontal for  and vertical for ).\n\nThe following example visually demonstrates the effect of these props with different  and  values.\n\nSize Hinting\n\nWhen a child component is included in a flex container,\nthe  (default ) and  (default ) props control\nhow the box is sized relative to other components in the same container.\n\nThe resizing always applies to the main axis of the flex container. If the direction is\n, then the sizing applies to the . If the direction is , then the sizing\napplies to the . To set the optimal size along the main axis, the  prop\nis used and may be either a percentage or CSS size units. When unspecified, the\ncorresponding  or  value is used if set, otherwise the content size is used.\n\nWhen , the box will not grow beyond the .\n\nWhen , the box will not shrink to less than the .\n\nThese props are used when creating flexible responsive layouts.\n\nMove the slider below and see how adjusting the width of the flex container\naffects the computed  sizes of the flex items based on the props that are set."
  },
  {
    "name": "Separator",
    "parts": [
      "Library",
      "Layout",
      "Separator"
    ],
    "url": "docs/library/layout/separator",
    "description": "---\ncomponents:\n    - rx.separator\nSeparator: |\n    lambda **props: rx.separator(**props)\n\n---\n\nSeparator\n\nVisually or semantically separates content.\n\nBasic Example\n\nSize\n\nThe  prop controls how long the separator is. Using  will make\nthe separator fill the parent container. Setting CSS  or  prop to \ncan also achieve this effect, but  works the same regardless of the orientation.\n\nOrientation\n\nSetting the orientation prop to  will make the separator appear vertically."
  },
  {
    "name": "Box",
    "parts": [
      "Library",
      "Layout",
      "Box"
    ],
    "url": "docs/library/layout/box",
    "description": "---\ncomponents:\n  - rx.box\n---\n\nBox\n\nBox is a generic container component that can be used to group other components.\n\nBy default, the Box component is based on the  and rendered as a block element. It's primary use is for applying styles.\n\nBasic Example\n\nBackground\n\nTo set a background image or\ngradient,\nuse the  CSS prop."
  },
  {
    "name": "Section",
    "parts": [
      "Library",
      "Layout",
      "Section"
    ],
    "url": "docs/library/layout/section",
    "description": "---\ncomponents:\n  - rx.section\n---\n\nSection\n\nDenotes a section of page content, providing vertical padding by default.\n\nPrimarily this is a semantic component that is used to group related textual content.\n\nBasic Example"
  },
  {
    "name": "Center",
    "parts": [
      "Library",
      "Layout",
      "Center"
    ],
    "url": "docs/library/layout/center",
    "description": "---\ncomponents:\n    - rx.center\n---\n\nCenter\n\n is a component that centers its children within itself. It is based on the  component and therefore inherits all of its props."
  },
  {
    "name": "Inset",
    "parts": [
      "Library",
      "Layout",
      "Inset"
    ],
    "url": "docs/library/layout/inset",
    "description": "---\ncomponents:\n    - rx.inset\n\nInset: |\n    lambda **props: rx.card(\n        rx.inset(\n            rx.image(src=\"/reflex_banner.png\", height=\"auto\"),\n            **props,\n        ),\n        width=\"500px\",\n    )\n\n---\n\nInset\n\nApplies a negative margin to allow content to bleed into the surrounding container.\n\nBasic Example\n\nNesting an Inset component inside a Card will render the content from edge to edge of the card.\n\nOther Directions\n\nThe  prop controls which side the negative margin is applied to. When using a specific side,\nit is helpful to set the padding for the opposite side to  to retain the same padding the\ncontent would have had if it went to the edge of the parent component."
  },
  {
    "name": "Spacer",
    "parts": [
      "Library",
      "Layout",
      "Spacer"
    ],
    "url": "docs/library/layout/spacer",
    "description": "---\ncomponents:\n    - rx.spacer\n---\n\nSpacer\n\nCreates an adjustable, empty space that can be used to tune the spacing between child elements within .\n\nAs ,  and  are all built from , it is possible to also use  inside of these components."
  },
  {
    "name": "Html Embed",
    "parts": [
      "Library",
      "Other",
      "Html Embed"
    ],
    "url": "docs/library/other/html-embed",
    "description": "---\ncomponents:\n    - rx.html\n---\n\nHTML Embed\n\nThe HTML component can be used to render raw HTML code.\n\nBefore you reach for this component, consider using Reflex's raw HTML element support instead.\n\nIn this example, we render an image."
  },
  {
    "name": "Script",
    "parts": [
      "Library",
      "Other",
      "Script"
    ],
    "url": "docs/library/other/script",
    "description": "---\ncomponents:\n    - rx.script\n---\n\nScript\n\nThe Script component can be used to include inline javascript or javascript files by URL.\n\nIt uses the  component to inject the script and can be safely used with conditional rendering to allow script side effects to be controlled by the state.\n\nComplex inline scripting should be avoided.\nIf the code to be included is more than a couple lines, it is more maintainable to implement it in a separate javascript file in the  directory and include it via the  prop.\n\nThis component is particularly helpful for including tracking and social scripts.\nAny additional attrs needed for the script tag can be supplied via  prop.\n\nThis code renders to something like the following to enable stat counting with a third party service."
  },
  {
    "name": "Theme",
    "parts": [
      "Library",
      "Other",
      "Theme"
    ],
    "url": "docs/library/other/theme",
    "description": "---\n components:\n     - rx.theme\n     - rx.theme_panel\n---\n\nTheme\n\n The  component is used to change the theme of the application. The  can be set directly in the rx.App.\n\n # Theme Panel\n\n The  component is a container for the  component. It provides a way to change the theme of the application.\n\n The theme panel is closed by default. You can set it open ."
  },
  {
    "name": "Clipboard",
    "parts": [
      "Library",
      "Other",
      "Clipboard"
    ],
    "url": "docs/library/other/clipboard",
    "description": "---\ncomponents:\n  - rx.clipboard\n---\n\nClipboard\n\n_New in 0.5.6_\n\nThe Clipboard component can be used to respond to paste events with complex data.\n\nIf the Clipboard component is included in a page without children,\n, then it will attach to the document's  event handler\nand will be triggered when data is pasted anywhere into the page.\n\nThe  argument passed to the  method is a list of tuples, where\neach tuple contains the MIME type of the pasted data and the data itself. Binary\ndata will be base64 encoded as a data URI, and can be decoded using python's\n or used directly as the  prop of an image.\n\nScoped Paste Events\n\nIf you want to limit the scope of the paste event to a specific element, wrap\nthe  component around the elements that should trigger the paste\nevent.\n\nTo avoid having outer paste handlers also trigger the event, you can use the\nevent action  to prevent the paste from bubbling up through\nthe DOM.\n\nIf you need to also prevent the default action of pasting the data into a text\nbox, you can also attach the  action."
  },
  {
    "name": "Memo",
    "parts": [
      "Library",
      "Other",
      "Memo"
    ],
    "url": "docs/library/other/memo",
    "description": "Memo\n\nThe  decorator is used to optimize component rendering by memoizing components that don't need to be re-rendered. This is particularly useful for expensive components that depend on specific props and don't need to be re-rendered when other state changes in your application.\n\nRequirements\n\nWhen using , you must follow these requirements:\n\n1. **Type all arguments**: All arguments to a memoized component must have type annotations.\n2. **Use keyword arguments**: When calling a memoized component, you must use keyword arguments (not positional arguments).\n\nBasic Usage\n\nWhen you wrap a component function with , the component will only re-render when its props change. This helps improve performance by preventing unnecessary re-renders.\n\nIn this example, the  will only re-render when the  prop changes, not when the  state changes.\n\nWith Event Handlers\n\nYou can also use  with components that have event handlers:\n\nWith State Variables\n\nWhen used with state variables, memoized components will only re-render when the specific state variables they depend on change:\n\nAdvanced Event Handler Example\n\nYou can also pass arguments to event handlers in memoized components:\n\nPerformance Considerations\n\nUse  for:\n- Components with expensive rendering logic\n- Components that render the same result given the same props\n- Components that re-render too often due to parent component updates\n\nAvoid using  for:\n- Simple components where the memoization overhead might exceed the performance gain\n- Components that almost always receive different props on re-render"
  },
  {
    "name": "Skeleton",
    "parts": [
      "Library",
      "Other",
      "Skeleton"
    ],
    "url": "docs/library/other/skeleton",
    "description": "---\ndescription: Skeleton, a loading placeholder component for content that is not yet available.\ncomponents:\n    - rx.skeleton\n---\n\nSkeleton (loading placeholder)\n\n is a loading placeholder component that serves as a visual placeholder while content is loading.\nIt is useful for maintaining the layout's structure and providing users with a sense of progression while awaiting the final content.\n\nWhen using  with text, wrap the text itself instead of the parent element to have a placeholder of the same size.\n\nUse the loading prop to control whether the skeleton or its children are displayed. Skeleton preserves the dimensions of children when they are hidden and disables interactive elements."
  },
  {
    "name": "Html",
    "parts": [
      "Library",
      "Other",
      "Html"
    ],
    "url": "docs/library/other/html",
    "description": "---\ncomponents:\n    - rx.el.A\n    - rx.el.Abbr\n    - rx.el.Address\n    - rx.el.Area\n    - rx.el.Article\n    - rx.el.Aside\n    - rx.el.Audio\n    - rx.el.B\n    - rx.el.Bdi\n    - rx.el.Bdo\n    - rx.el.Blockquote\n    - rx.el.Body\n    - rx.el.Br\n    - rx.el.Button\n    - rx.el.Canvas\n    - rx.el.Caption\n    - rx.el.Cite\n    - rx.el.Code\n    - rx.el.Col\n    - rx.el.Colgroup\n    - rx.el.Data\n    - rx.el.Dd\n    - rx.el.Del\n    - rx.el.Details\n    - rx.el.Dfn\n    - rx.el.Dialog\n    - rx.el.Div\n    - rx.el.Dl\n    - rx.el.Dt\n    - rx.el.Em\n    - rx.el.Embed\n    - rx.el.Fieldset\n    - rx.el.Figcaption\n    - rx.el.Footer\n    - rx.el.Form\n    - rx.el.H1\n    - rx.el.H2\n    - rx.el.H3\n    - rx.el.H4\n    - rx.el.H5\n    - rx.el.H6\n    - rx.el.Head\n    - rx.el.Header\n    - rx.el.Hr\n    - rx.el.Html\n    - rx.el.I\n    - rx.el.Iframe\n    - rx.el.Img\n    - rx.el.Input\n    - rx.el.Ins\n    - rx.el.Kbd\n    - rx.el.Label\n    - rx.el.Legend\n    - rx.el.Li\n    - rx.el.Link\n    - rx.el.Main\n    - rx.el.Mark\n    - rx.el.Math\n    - rx.el.Meta\n    - rx.el.Meter\n    - rx.el.Nav\n    - rx.el.Noscript\n    - rx.el.Object\n    - rx.el.Ol\n    - rx.el.Optgroup\n    - rx.el.Option\n    - rx.el.Output\n    - rx.el.P\n    - rx.el.Picture\n    - rx.el.Portal\n    - rx.el.Pre\n    - rx.el.Progress\n    - rx.el.Q\n    - rx.el.Rp\n    - rx.el.Rt\n    - rx.el.Ruby\n    - rx.el.S\n    - rx.el.Samp\n    - rx.el.Script\n    - rx.el.Section\n    - rx.el.Select\n    - rx.el.Small\n    - rx.el.Source\n    - rx.el.Span\n    - rx.el.Strong\n    - rx.el.Sub\n    - rx.el.Sup\n    - rx.el.svg.circle\n    - rx.el.svg.defs\n    - rx.el.svg.linear_gradient\n    - rx.el.svg.polygon\n    - rx.el.svg.path\n    - rx.el.svg.rect\n    - rx.el.svg.stop\n    - rx.el.Table\n    - rx.el.Tbody\n    - rx.el.Td\n    - rx.el.Template\n    - rx.el.Textarea\n    - rx.el.Tfoot\n    - rx.el.Th\n    - rx.el.Thead\n    - rx.el.Time\n    - rx.el.Title\n    - rx.el.Tr\n    - rx.el.Track\n    - rx.el.U\n    - rx.el.Ul\n    - rx.el.Video\n    - rx.el.Wbr\n---\n\nHTML\n\nReflex also provides a set of HTML elements that can be used to create web pages. These elements are the same as the HTML elements that are used in web development. These elements come unstyled bhy default. You can style them using style props or tailwindcss classes.\n\nThe following is a list of the HTML elements that are available in Reflex:"
  },
  {
    "name": "Foreach",
    "parts": [
      "Library",
      "Dynamic Rendering",
      "Foreach"
    ],
    "url": "docs/library/dynamic-rendering/foreach",
    "description": "Foreach\n\nThe  component takes an iterable(list, tuple or dict) and a function that renders each item in the list.\nThis is useful for dynamically rendering a list of items defined in a state.\n\nThe function can also take an index as a second argument.\n\nNested foreach components can be used to render nested lists.\n\nWhen indexing into a nested list, it's important to declare the list's type as Reflex requires it for type checking.\nThis ensures that any potential frontend JS errors are caught before the user can encounter them.\n\nBelow is a more complex example of foreach within a todo list.\n\nDictionaries\n\nItems in a dictionary can be accessed as list of key-value pairs.\nUsing the color example, we can slightly modify the code to use dicts as shown below.\n\nNow let's show a more complex example with dicts using the color example.\nAssuming we want to display a dictionary of secondary colors as keys and their constituent primary colors as values, we can modify the code as below:"
  },
  {
    "name": "Match",
    "parts": [
      "Library",
      "Dynamic Rendering",
      "Match"
    ],
    "url": "docs/library/dynamic-rendering/match",
    "description": "Match\n\nThe  feature in Reflex serves as a powerful alternative to  for handling conditional statements.\nWhile  excels at conditionally rendering two components based on a single condition,\n extends this functionality by allowing developers to handle multiple conditions and their associated components.\nThis feature is especially valuable when dealing with intricate conditional logic or nested scenarios,\nwhere the limitations of  might lead to less readable and more complex code.\n\nWith , developers can not only handle multiple conditions but also perform structural pattern matching,\nmaking it a versatile tool for managing various scenarios in Reflex applications.\n\nBasic Usage\n\nThe  function provides a clear and expressive syntax for handling multiple\nconditions and their corresponding components:\n\n- : The value to match against.\n- : A Tuple of matching cases and their corresponding return components.\n- : A special case for the default component when the condition isn't matched by any of the match cases.\n\nExample\n\nDefault Case\n\nThe default case in  serves as a universal handler for scenarios where none of\nthe specified match cases aligns with the given match condition. Here are key considerations\nwhen working with the default case:\n\n- **Placement in the Match Function**: The default case must be the last non-tuple argument in the  component.\n  All match cases should be enclosed in tuples; any non-tuple value is automatically treated as the default case. For example:\n\nThe above code snippet will result in an error due to the misplaced default case.\n\n- **Single Default Case**: Only one default case is allowed in the  component.\n  Attempting to specify multiple default cases will lead to an error. For instance:\n\n- **Optional Default Case for Component Return Values**: If the match cases in a  component\n  return components, the default case can be optional. In this scenario, if a default case is\n  not provided,  will be implicitly assigned as the default. For example:\n\nIn this case,  is the default case. However, not providing a default case for non-component\nreturn values will result in an error:\n\nThe above code snippet will result in an error as a default case must be explicitly\nprovided in this scenario.\n\nHandling Multiple Conditions\n\n excels in efficiently managing multiple conditions and their corresponding components,\nproviding a cleaner and more readable alternative compared to nested  structures.\n\nConsider the following example:\n\nIn a match case tuple, you can specify multiple conditions. The last value of the match case\ntuple is automatically considered as the return value. It's important to note that a match case\ntuple should contain a minimum of two elements: a match case and a return value.\nThe following code snippet will result in an error:\n\nUsage as Props\n\nSimilar to ,  can be used as prop values, allowing dynamic behavior for UI components:\n\nIn the example above, the background color property of the box component containing  changes to red when\n is 1, blue when its 5, green when its 5, orange when its 15 and black for any other value.\n\nThe example below also shows handling multiple conditions with the match component as props."
  },
  {
    "name": "Cond",
    "parts": [
      "Library",
      "Dynamic Rendering",
      "Cond"
    ],
    "url": "docs/library/dynamic-rendering/cond",
    "description": "Cond\n\nThis component is used to conditionally render components.\n\nThe cond component takes a condition and two components.\nIf the condition is , the first component is rendered, otherwise the second component is rendered.\n\nThe second component is optional and can be omitted.\nIf it is omitted, nothing is rendered if the condition is .\n\nNegation\n\nYou can use the logical operator  to negate a condition.\n\nMultiple Conditions\n\nIt is also possible to make up complex conditions using the  (|) and  (&) operators.\n\nHere we have an example using the var operators , , . We define a condition that if a person has an age between 18 and 65, including those ages, they are able to work, otherwise they cannot.\n\nWe could equally use the operator  to represent a  in one of our conditions.\n\nNested Conditional\n\nWe can also nest  components within each other to create more complex logic. In python we can have an  statement that then has several  statements before finishing with an . This is also possible in reflex using nested  components. In this example we check whether a number is positive, negative or zero.\n\nHere is the python logic using  statements:\n\nThis reflex code that is logically identical:\n\nHere is a more advanced example where we have three numbers and we are checking which of the three is the largest. If any two of them are equal then we return that .\n\nThe reflex code that follows is logically identical to doing the following in python:"
  },
  {
    "name": "Callout Ll",
    "parts": [
      "Library",
      "Data Display",
      "Callout Ll"
    ],
    "url": "docs/library/data-display/callout-ll",
    "description": "---\ncomponents:\n    - rx.callout.root\n    - rx.callout.icon\n    - rx.callout.text\n---\n\nCallout\n\nA  is a short message to attract user's attention.\n\nThe  component is made up of a , which groups  and  parts. This component is based on the  element and supports common margin props.\n\nThe  provides width and height for the  associated with the . This component is based on the  element. See the **icon** component for all icons that are available.\n\nThe  renders the callout text. This component is based on the  element.\n\nAs alert\n\nStyle\n\nSize\n\nUse the  prop to control the size.\n\nVariant\n\nUse the  prop to control the visual style. It is set to  by default.\n\nColor\n\nUse the  prop to assign a specific color, ignoring the global theme.\n\nHigh Contrast\n\nUse the  prop to add additional contrast."
  },
  {
    "name": "Scroll Area",
    "parts": [
      "Library",
      "Data Display",
      "Scroll Area"
    ],
    "url": "docs/library/data-display/scroll-area",
    "description": "---\ncomponents:\n    - rx.scroll_area\n\nScrollArea: |\n    lambda **props: rx.scroll_area(\n        rx.flex(\n            rx.text(\n                \"\"\"Three fundamental aspects of typography are legibility, readability, and aesthetics. Although in a non-technical sense \"legible\" and \"readable\"are often used synonymously, typographically they are separate but related concepts.\"\"\",\n                size=\"5\",\n            ),\n            rx.text(\n                \"\"\"Legibility describes how easily individual characters can be distinguished from one another. It is described by Walter Tracy as \"the quality of being decipherable and recognisable\". For instance, if a \"b\" and an \"h\", or a \"3\" and an \"8\", are difficult to distinguish at small sizes, this is a problem of legibility.\"\"\",\n                size=\"5\",\n            ),\n            direction=\"column\",\n            spacing=\"4\",\n            height=\"100px\",\n            width=\"50%\",\n        ),\n        **props\n    )\n\n---\n\nScroll Area\n\nCustom styled, cross-browser scrollable area using native functionality.\n\nBasic Example\n\nControl the scrollable axes\n\nUse the  prop to limit scrollable axes. This prop can take values .\n\nSetting the type of the Scrollbars\n\nThe  prop describes the nature of scrollbar visibility.\n\n means that scrollbars are visible when content is overflowing on the corresponding orientation.\n\n means that scrollbars are always visible regardless of whether the content is overflowing.\n\n means that scrollbars are visible when the user is scrolling along its corresponding orientation.\n\n when the user is scrolling along its corresponding orientation and when the user is hovering over the scroll area."
  },
  {
    "name": "Auto Scroll",
    "parts": [
      "Library",
      "Dynamic Rendering",
      "Auto Scroll"
    ],
    "url": "docs/library/dynamic-rendering/auto-scroll",
    "description": "Auto Scroll\n\nThe  component is a div that automatically scrolls to the bottom when new content is added. This is useful for chat interfaces, logs, or any container where new content is dynamically added and you want to ensure the most recent content is visible.\n\nBasic Usage\n\nThe  component automatically scrolls to show the newest content when it's added. In this example, each time you click \"Add Message\", a new message is added to the list and the container automatically scrolls to display it.\n\nWhen to Use Auto Scroll\n\n- **Chat applications**: Keep the chat window scrolled to the most recent messages.\n- **Log viewers**: Automatically follow new log entries as they appear.\n- **Feed interfaces**: Keep the newest content visible in dynamically updating feeds.\n\nProps\n\n is based on the  component and inherits all of its props. By default, it sets  to enable scrolling.\n\nSome common props you might use with :\n\n- : Set the height of the scrollable container.\n- : Set the width of the scrollable container.\n- : Add padding inside the container.\n- : Add a border around the container.\n- : Round the corners of the container.\n\nHow It Works\n\nThe component tracks when new content is added and maintains the scroll position in two scenarios:\n\n1. When the user is already near the bottom of the content (within 50 pixels), it will scroll to the bottom when new content is added.\n2. When the container didn't have a scrollbar before but does now (due to new content), it will automatically scroll to the bottom.\n\nThis behavior ensures that users can scroll up to view older content without being forced back to the bottom, while still automatically following new content in most cases."
  },
  {
    "name": "Code Block",
    "parts": [
      "Library",
      "Data Display",
      "Code Block"
    ],
    "url": "docs/library/data-display/code-block",
    "description": "---\ncomponents:\n    - rx.code_block\n---\n\nCode Block\n\nThe Code Block component can be used to display code easily within a website.\nPut in a multiline string with the correct spacing and specify and language to show the desired code."
  },
  {
    "name": "Spinner",
    "parts": [
      "Library",
      "Data Display",
      "Spinner"
    ],
    "url": "docs/library/data-display/spinner",
    "description": "---\ncomponents:\n    - rx.spinner\n---\n\nSpinner\n\nSpinner is used to display an animated loading indicator when a task is in progress.\n\nBasic Examples\n\nSpinner can have different sizes.\n\nDemo with buttons\n\nButtons have their own loading prop that automatically composes a spinner.\n\nSpinner inside a button\n\nIf you have an icon inside the button, you can use the button's disabled state and wrap the icon in a standalone rx.spinner to achieve a more sophisticated design."
  },
  {
    "name": "List",
    "parts": [
      "Library",
      "Data Display",
      "List"
    ],
    "url": "docs/library/data-display/list",
    "description": "---\ncomponents:\n    - rx.list.item\n    - rx.list.ordered\n    - rx.list.unordered\n---\n\nList\n\nA  is a component that is used to display a list of items, stacked vertically by default. A  can be either  or . It is based on the  component and therefore inherits all of its props.\n\n has bullet points to display the list items.\n\n  has numbers to display the list items.\n\n and  can have no bullet points or numbers by setting the  prop to .\nThis is effectively the same as using the  component.\n\nLists can also be used with icons."
  },
  {
    "name": "Callout",
    "parts": [
      "Library",
      "Data Display",
      "Callout"
    ],
    "url": "docs/library/data-display/callout",
    "description": "---\ncomponents:\n    - rx.callout\n    - rx.callout.root\n    - rx.callout.icon\n    - rx.callout.text\n\nCallout: |\n    lambda **props: rx.callout(\"Basic Callout\", icon=\"search\", **props)\n\nCalloutRoot: |\n    lambda **props: rx.callout.root(\n        rx.callout.icon(rx.icon(tag=\"info\")),\n        rx.callout.text(\"You will need admin privileges to install and access this application.\"),\n        **props\n    )\n---\n\nCallout\n\nA  is a short message to attract user's attention.\n\nThe  prop allows an icon to be passed to the  component. See the **icon** component for all icons that are available.\n\nAs alert\n\nStyle\n\nSize\n\nUse the  prop to control the size.\n\nVariant\n\nUse the  prop to control the visual style. It is set to  by default.\n\nColor\n\nUse the  prop to assign a specific color, ignoring the global theme.\n\nHigh Contrast\n\nUse the  prop to add additional contrast."
  },
  {
    "name": "Progress",
    "parts": [
      "Library",
      "Data Display",
      "Progress"
    ],
    "url": "docs/library/data-display/progress",
    "description": "---\ncomponents:\n    - rx.progress\n\nProgress: |\n    lambda **props: rx.progress(value=50, **props)\n---\n\nProgress\n\nProgress is used to display the progress status for a task that takes a long time or consists of several steps.\n\nBasic Example\n\n expects the  prop to set the progress value.\n is default to 100%, the width of its parent component.\n\nFor a dynamic progress, you can assign a state variable to the  prop instead of a constant value."
  },
  {
    "name": "Icon",
    "parts": [
      "Library",
      "Data Display",
      "Icon"
    ],
    "url": "docs/library/data-display/icon",
    "description": "---\ncomponents:\n    - rx.lucide.Icon\n---\n\nIcon\n\nThe Icon component is used to display an icon from a library of icons. This implementation is based on the Lucide Icons where you can find a list of all available icons.\n\nIcons List\n\nBasic Example\n\nTo display an icon, specify the  prop from the list of available icons.\nPassing the tag as the first children is also supported and will be assigned to the  prop.\n\nThe  is expected to be in  format, but  is also supported to allow copy-paste from https://lucide.dev/icons.\n\nDynamic Icons\n\nThere are two ways to use dynamic icons in Reflex:\n\nUsing rx.match\n\nIf you have a specific subset of icons you want to use dynamically, you can define an  with them:\n\nUsing Dynamic Icon Tags\n\nReflex also supports using dynamic values directly as the  prop in . This allows you to use any icon from the Lucide library dynamically at runtime.\n\nUnder the hood, when a dynamic value is passed as the  prop to , Reflex automatically uses a special  component that can load icons at runtime.\n\nStyling\n\nIcon from Lucide can be customized with the following props ,  and .\n\nStroke Width\n\nSize\n\nColor\n\nHere is an example using basic colors in icons.\n\nA radix color with a scale may also be specified using  as seen below.\n\nHere is another example using the  color with scales. The  is the most dominant color in your theme.\n\nFinal Example\n\nIcons can be used as child components of many other components. For example, adding a magnifying glass icon to a search bar."
  },
  {
    "name": "Data List",
    "parts": [
      "Library",
      "Data Display",
      "Data List"
    ],
    "url": "docs/library/data-display/data-list",
    "description": "---\ncomponents:\n    - rx.data_list.root\n    - rx.data_list.item\n    - rx.data_list.label\n    - rx.data_list.value\nDataListRoot: |\n    lambda **props: rx.data_list.root(\n        rx.foreach(\n            [[\"Status\", \"Authorized\"], [\"ID\", \"U-474747\"], [\"Name\", \"Developer Success\"], [\"Email\", \"foo@reflex.dev\"]],\n            lambda item: rx.data_list.item(rx.data_list.label(item[0]), rx.data_list.value(item[1])),\n        ),\n        **props,\n    )\nDataListItem: |\n    lambda **props: rx.data_list.root(\n        rx.foreach(\n            [[\"Status\", \"Authorized\"], [\"ID\", \"U-474747\"], [\"Name\", \"Developer Success\"], [\"Email\", \"foo@reflex.dev\"]],\n            lambda item: rx.data_list.item(rx.data_list.label(item[0]), rx.data_list.value(item[1]), **props),\n        ),\n    )\nDataListLabel: |\n    lambda **props: rx.data_list.root(\n        rx.foreach(\n            [[\"Status\", \"Authorized\"], [\"ID\", \"U-474747\"], [\"Name\", \"Developer Success\"], [\"Email\", \"foo@reflex.dev\"]],\n            lambda item: rx.data_list.item(rx.data_list.label(item[0], **props), rx.data_list.value(item[1])),\n        ),\n    )\nDataListValue: |\n    lambda **props: rx.data_list.root(\n        rx.foreach(\n            [[\"Status\", \"Authorized\"], [\"ID\", \"U-474747\"], [\"Name\", \"Developer Success\"], [\"Email\", \"foo@reflex.dev\"]],\n            lambda item: rx.data_list.item(rx.data_list.label(item[0]), rx.data_list.value(item[1], **props)),\n        ),\n    )\n---\n\nData List\n\nThe  component displays key-value pairs and is particularly helpful for showing metadata.\n\nA  needs to be initialized using  and currently takes in data list items:"
  },
  {
    "name": "Avatar",
    "parts": [
      "Library",
      "Data Display",
      "Avatar"
    ],
    "url": "docs/library/data-display/avatar",
    "description": "---\ncomponents:\n    - rx.avatar\nAvatar: |\n    lambda **props: rx.hstack(rx.avatar(src=\"/logo.jpg\", **props), rx.avatar(fallback=\"RX\", **props), spacing=\"3\")\n---\nAvatar\n\nThe Avatar component is used to represent a user, and display their profile pictures or fallback texts such as initials.\n\nBasic Example\n\nTo create an avatar component with an image, pass the image URL as the  prop.\n\nTo display a text such as initials, set the  prop without passing the  prop.\n\nStyling\n\nSize\n\nThe  prop controls the size and spacing of the avatar. The acceptable size is from  to , with  being the default.\n\nVariant\n\nThe  prop controls the visual style of the avatar fallback text. The variant can be  or . The default is .\n\nColor Scheme\n\nThe  prop sets a specific color to the fallback text, ignoring the global theme.\n\nHigh Contrast\n\nThe  prop increases color contrast of the fallback text with the background.\n\nRadius\n\nThe  prop sets specific radius value, ignoring the global theme. It can take values .\n\nFallback\n\nThe  prop indicates the rendered text when the  cannot be loaded.\n\nFinal Example\n\nAs part of a user profile page, the Avatar component is used to display the user's profile picture, with the fallback text showing the user's initials. Text components displays the user's full name and username handle and a Button component shows the edit profile button."
  },
  {
    "name": "Badge",
    "parts": [
      "Library",
      "Data Display",
      "Badge"
    ],
    "url": "docs/library/data-display/badge",
    "description": "---\ncomponents:\n    - rx.badge\n\nBadge: |\n    lambda **props: rx.badge(\"Basic Badge\", **props)\n---\nBadge\n\nBadges are used to highlight an item's status for quick recognition.\n\nBasic Example\n\nTo create a badge component with only text inside, pass the text as an argument.\n\nStyling\n\nSize\n\nThe  prop controls the size and padding of a badge. It can take values of , with default being .\n\nVariant\n\nThe  prop controls the visual style of the badge. The supported variant types are . The variant default is .\n\nColor Scheme\n\nThe  prop sets a specific color, ignoring the global theme.\n\nHigh Contrast\n\nThe  prop increases color contrast of the fallback text with the background.\n\nRadius\n\nThe  prop sets specific radius value, ignoring the global theme. It can take values .\n\nFinal Example\n\nA badge may contain more complex elements within it. This example uses a  component to align an icon and the text correctly, using the  prop to\nensure a comfortable spacing between the two."
  },
  {
    "name": "Moment",
    "parts": [
      "Library",
      "Data Display",
      "Moment"
    ],
    "url": "docs/library/data-display/moment",
    "description": "---\ncomponents:\n    - rx.moment\n\n---\n\nMoment\n\nDisplaying date and relative time to now sometimes can be more complicated than necessary.\n\nTo make it easy, Reflex is wrapping react-moment  under .\n\nExamples\n\nUsing a date from a state var as a value, we will display it in a few different\nway using . \n\nThe  state var is initialized when the site was deployed. The\nbutton below can be used to update the var to the current datetime, which will\nbe reflected in the subsequent examples.\n\nDisplay the date as-is:\n\nHumanized interval\n\nSometimes we don't want to display just a raw date, but we want something more instinctive to read. That's when we can use  and .\n\nYou can also set a duration (in milliseconds) with  where the date will display as relative, then after that, it will be displayed as defined in .\n\nFormatting dates\n\nOffset Date\n\nWith the props  and , you can pass an  object to modify the displayed date without affecting the stored date in your state.\n\nTimezones\n\nYou can also set dates to display in a specific timezone:\n\nClient-side periodic update\n\nIf a date is not passed to , it will use the client's current time.\n\nIf you want to update the date every second, you can use the  prop.\n\nEven better, you can actually link an event handler to the  prop that will be called every time the date is updated:"
  },
  {
    "name": "Label",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Label"
    ],
    "url": "docs/library/graphing/general/label",
    "description": "---\ncomponents:\n    - rx.recharts.Label\n    - rx.recharts.LabelList\n---\n\nLabel\n\nLabel is a component used to display a single label at a specific position within a chart or axis, while LabelList is a component that automatically renders a list of labels for each data point in a chart series, providing a convenient way to display multiple labels without manually positioning each one.\n\nSimple Example\n\nHere's a simple example that demonstrates how you can customize the label of your axis using . The  prop represents the actual text of the label, the  prop specifies where the label is positioned within the axis component, and the  prop is used to fine-tune the label's position.\n\nLabel List Example\n\n takes in a  where we define the data column to plot."
  },
  {
    "name": "Reference",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Reference"
    ],
    "url": "docs/library/graphing/general/reference",
    "description": "---\ncomponents:\n    - rx.recharts.ReferenceLine\n    - rx.recharts.ReferenceDot\n    - rx.recharts.ReferenceArea\n---\n\nReference\n\nThe Reference components in Recharts, including ReferenceLine, ReferenceArea, and ReferenceDot, are used to add visual aids and annotations to the chart, helping to highlight specific data points, ranges, or thresholds for better data interpretation and analysis.\n\nReference Area\n\nThe  component in Recharts is used to highlight a specific area or range on the chart by drawing a rectangular region. It is defined by specifying the coordinates (x1, x2, y1, y2) and can be used to emphasize important data ranges or intervals on the chart.\n\nReference Line\n\nThe  component in rx.recharts is used to draw a horizontal or vertical line on the chart at a specified position. It helps to highlight important values, thresholds, or ranges on the axis, providing visual reference points for better data interpretation.\n\nReference Dot\n\nThe  component in Recharts is used to mark a specific data point on the chart with a customizable dot. It allows you to highlight important values, outliers, or thresholds by providing a visual reference marker at the specified coordinates (x, y) on the chart."
  },
  {
    "name": "Brush",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Brush"
    ],
    "url": "docs/library/graphing/general/brush",
    "description": "---\ncomponents:\n    - rx.recharts.Brush\n---\n\nBrush\n\nSimple Example\n\nThe brush component allows us to view charts that have a large number of data points. To view and analyze them efficiently, the brush provides a slider with two handles that helps the viewer to select some range of data points to be displayed.\n\nPosition, Size, and Range\n\nThis example showcases ways to set the Position, Size, and Range. The  prop provides the spacing between stops on the brush when the graph will refresh. The  and  props defines the default range of the brush.  prop specifies the width of each handle (\"traveller\" in recharts lingo)."
  },
  {
    "name": "Cartesiangrid",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Cartesiangrid"
    ],
    "url": "docs/library/graphing/general/cartesiangrid",
    "description": "---\ncomponents:\n    - rx.recharts.CartesianGrid\n    # - rx.recharts.CartesianAxis\n---\n\nCartesian Grid\n\nThe Cartesian Grid is a component in Recharts that provides a visual reference for data points in charts. It helps users to better interpret the data by adding horizontal and vertical lines across the chart area.\n\nSimple Example\n\nThe  prop in Recharts is used to create dashed or dotted lines for various chart elements like lines, axes, or grids. It's based on the SVG stroke-dasharray attribute. The  prop accepts a comma-separated string of numbers that define a repeating pattern of dashes and gaps along the length of the stroke.\n\n- :  creates a line with 5-pixel dashes and 5-pixel gaps\n- :  creates a more complex pattern with 10-pixel dashes, 5-pixel gaps, 5-pixel dashes, and 5-pixel gaps\n\nHere's a simple example using it on a Line component:\n\nHidden Axes\n\nA  component can be used to hide the horizontal and vertical grid lines in a chart by setting the  and  props to . This can be useful when you want to show the grid lines only on one axis or when you want to create a cleaner look for the chart.\n\nCustom Grid Lines\n\nThe  and  props allow you to specify custom grid lines on the chart, offering fine-grained control over the grid's appearance.\n\nThese props accept arrays of numbers, where each number represents a pixel offset:\n- For , the offset is measured from the top edge of the chart\n- For , the offset is measured from the left edge of the chart\n\nHere's an example demonstrating custom grid lines in a scatter chart:\n\nUse these props judiciously to enhance data visualization without cluttering the chart. They're particularly useful for highlighting specific data ranges or creating visual reference points."
  },
  {
    "name": "Axis",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Axis"
    ],
    "url": "docs/library/graphing/general/axis",
    "description": "---\ncomponents:\n  - rx.recharts.XAxis\n  - rx.recharts.YAxis\n  - rx.recharts.ZAxis\n---\n\nAxis\n\nThe Axis component in Recharts is a powerful tool for customizing and configuring the axes of your charts. It provides a wide range of props that allow you to control the appearance, behavior, and formatting of the axis. Whether you're working with an AreaChart, LineChart, or any other chart type, the Axis component enables you to create precise and informative visualizations.\n\nBasic Example\n\nMultiple Axes\n\nMultiple axes can be used for displaying different data series with varying scales or units on the same chart. This allows for a more comprehensive comparison and analysis of the data.\n\nChoosing Location of Labels for Axes\n\nThe axes  can take several positions. The example below allows you to try out different locations for the x and y axis labels."
  },
  {
    "name": "Legend",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Legend"
    ],
    "url": "docs/library/graphing/general/legend",
    "description": "---\ncomponents:\n    - rx.recharts.Legend\n---\n\nLegend\n\nA legend tells what each plot represents. Just like on a map, the legend helps the reader understand what they are looking at. For a line graph for example it tells us what each line represents.\n\nSimple Example\n\nExample with Props\n\nThe style and layout of the legend can be customized using a set of props.  and  set the dimensions of the container that wraps the legend, and  can set the legend to display vertically or horizontally.  and  set the position relative to the chart container. The type and size of icons can be set using  and ."
  },
  {
    "name": "Radarchart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Radarchart"
    ],
    "url": "docs/library/graphing/charts/radarchart",
    "description": "---\ncomponents:\n  - rx.recharts.RadarChart\n  - rx.recharts.Radar\n---\n\nRadar Chart\n\nA radar chart shows multivariate data of three or more quantitative variables mapped onto an axis.\n\nSimple Example\n\nFor a radar chart we must define an  component for each set of values we wish to plot. Each  component has a  which clearly states which variable in our data we are plotting. In this simple example we plot the  column of our data against the  column which we set as the  in .\n\nMultiple Radars\n\nWe can also add two radars on one chart by using two  components.\n\nIn this plot an  and an  are set which determine the chart's size and shape. The  sets the distance from the center to the innermost part of the chart (creating a hollow center if greater than zero), while the  defines the chart's overall size by setting the distance from the center to the outermost edge of the radar plot.\n\nUsing More Props\n\nThe  prop shows points at each data vertex when true.  displays a line in the chart legend.  starts the animation immediately,  sets an 8-second animation, and  makes the animation start slowly and speed up. These props control the chart's appearance and animation behavior.\n\nDynamic Data\n\nChart data tied to a State var causes the chart to automatically update when the\nstate changes, providing a nice way to visualize data in response to user\ninterface elements. View the \"Data\" tab to see the substate driving this\nradar chart of character traits."
  },
  {
    "name": "Tooltip",
    "parts": [
      "Library",
      "Graphing",
      "General",
      "Tooltip"
    ],
    "url": "docs/library/graphing/general/tooltip",
    "description": "---\ncomponents:\n    - rx.recharts.GraphingTooltip\n---\n\nTooltip\n\nTooltips are the little boxes that pop up when you hover over something. Tooltips are always attached to something, like a dot on a scatter chart, or a bar on a bar chart.\n\nCustom Styling\n\nThe  component allows for customization of the tooltip's style, position, and layout.  sets the separator between the data key and value.  prop defines the dimensions of the chart's viewbox while  determines whether the tooltip can extend beyond the viewBox horizontally (x) or vertically (y).  prop allows you to style the outer container or wrapper of the tooltip.  prop allows you to style the inner content area of the tooltip.  prop determines if the tooltip animation is active or not."
  },
  {
    "name": "Barchart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Barchart"
    ],
    "url": "docs/library/graphing/charts/barchart",
    "description": "---\ncomponents:\n  - rx.recharts.BarChart\n  - rx.recharts.Bar\n---\n\nBar Chart\n\nA bar chart presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.\n\nFor a bar chart we must define an  component for each set of values we wish to plot. Each  component has a  which clearly states which variable in our data we are tracking. In this simple example we plot  as a bar against the  column which we set as the  in .\n\nSimple Example\n\nMultiple Bars\n\nMultiple bars can be placed on the same , using multiple  components.\n\nRanged Charts\n\nYou can also assign a range in the bar by assigning the data_key in the  to a list with two elements, i.e. here a range of two temperatures for each date.\n\nStateful Charts\n\nHere is an example of a bar graph with a . Here we have defined a function , which randomly changes the data for both graphs when the first defined  is clicked on using .\n\nExample with Props\n\nHere's an example demonstrates how to customize the appearance and layout of bars using the , , , and  props. These props accept values in pixels to control the spacing and size of the bars.\n\nVertical Example\n\nThe  prop allows you to set the orientation of the graph to be vertical or horizontal, it is set horizontally by default.\n\nTo learn how to use the , , and  props check out the of the area chart documentation, where these props are all described with examples."
  },
  {
    "name": "Composedchart",
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
    "name": "Errorbar",
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
    "name": "Piechart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Piechart"
    ],
    "url": "docs/library/graphing/charts/piechart",
    "description": "---\ncomponents:\n  - rx.recharts.PieChart\n  - rx.recharts.Pie\n---\n\nPie Chart\n\nA pie chart is a circular statistical graphic which is divided into slices to illustrate numerical proportion.\n\nFor a pie chart we must define an  component for each set of values we wish to plot. Each  component has a , a  and a  which clearly states which data and which variables in our data we are tracking. In this simple example we plot  column as our  against the  column which we set as our .\nWe also use the  prop to set the color of the pie slices.\n\nWe can also add two pies on one chart by using two  components.\n\nIn this example  and  props are used. They define the doughnut shape of a pie chart:  creates the hollow center (use \"0%\" for a full pie), while  sets the overall size. The  prop, used on the green pie below, adds space between pie slices, enhancing visibility of individual segments.\n\nDynamic Data\n\nChart data tied to a State var causes the chart to automatically update when the\nstate changes, providing a nice way to visualize data in response to user\ninterface elements. View the \"Data\" tab to see the substate driving this\nhalf-pie chart."
  },
  {
    "name": "Funnelchart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Funnelchart"
    ],
    "url": "docs/library/graphing/charts/funnelchart",
    "description": "---\ncomponents:\n  - rx.recharts.FunnelChart\n  - rx.recharts.Funnel\n---\n\nFunnel Chart\n\nA funnel chart is a graphical representation used to visualize how data moves through a process. In a funnel chart, the dependent variable’s value diminishes in the subsequent stages of the process. It can be used to demonstrate the flow of users through a business or sales process.\n\nSimple Example\n\nEvent Triggers\n\nFunnel chart supports , ,  and  event triggers, allows you to interact with the funnel chart and perform specific actions based on user interactions.\n\nDynamic Data\n\nHere is an example of a funnel chart with a . Here we have defined a function , which randomly changes the data when the graph is clicked on using .\n\nChanging the Chart Animation\n\nThe  prop can be used to turn off the animation, but defaults to .  sets the delay before animation starts,  determines how long the animation lasts, and  defines the speed curve of the animation for smooth transitions."
  },
  {
    "name": "Scatterchart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Scatterchart"
    ],
    "url": "docs/library/graphing/charts/scatterchart",
    "description": "---\ncomponents:\n  - rx.recharts.ScatterChart\n  - rx.recharts.Scatter\n---\n\nScatter Chart\n\nA scatter chart always has two value axes to show one set of numerical data along a horizontal (value) axis and another set of numerical values along a vertical (value) axis. The chart displays points at the intersection of an x and y numerical value, combining these values into single data points.\n\nSimple Example\n\nFor a scatter chart we must define an  component for each set of values we wish to plot. Each  component has a  prop which clearly states which data source we plot. We also must define  and  so that the graph knows what data to plot on each axis.\n\nMultiple Scatters\n\nWe can also add two scatters on one chart by using two  components, and we can define an  which represents a third column of data and is represented by the size of the dots in the scatter plot.\n\nTo learn how to use the  and  props, check out the Multiple Axis section of the area chart documentation.\n\nDynamic Data\n\nChart data tied to a State var causes the chart to automatically update when the\nstate changes, providing a nice way to visualize data in response to user\ninterface elements. View the \"Data\" tab to see the substate driving this\ncalculation of iterations in the Collatz Conjecture for a given starting number.\nEnter a starting number in the box below the chart to recalculate.\n\nLegend Type and Shape"
  },
  {
    "name": "Areachart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Areachart"
    ],
    "url": "docs/library/graphing/charts/areachart",
    "description": "---\ncomponents:\n  - rx.recharts.AreaChart\n  - rx.recharts.Area\n---\n\nArea Chart\n\nA Recharts area chart displays quantitative data using filled areas between a line connecting data points and the axis.\n\nBasic Example\n\nSyncing Charts\n\nThe  prop allows you to sync two graphs. In the example, it is set to \"1\" for both charts, indicating that they should be synchronized. This means that any interactions (such as brushing) performed on one chart will be reflected in the other chart.\n\nStacking Charts\n\nThe  prop allows you to stack multiple graphs on top of each other. In the example, it is set to \"1\" for both charts, indicating that they should be stacked together. This means that the bars or areas of the charts will be vertically stacked, with the values of each chart contributing to the total height of the stacked areas or bars.\n\nThis is similar to the  prop, but instead of synchronizing the interaction between the charts, it just stacks the charts on top of each other.\n\nMultiple Axis\n\nMultiple axes can be used for displaying different data series with varying scales or units on the same chart. This allows for a more comprehensive comparison and analysis of the data.\n\nLayout\n\nUse the  prop to set the orientation to either  (default) or .\n\nStateful Example\n\nHere is an example of an area graph with a . Here we have defined a function , which randomly changes the data for both graphs when the first defined  is clicked on using ."
  },
  {
    "name": "Linechart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Linechart"
    ],
    "url": "docs/library/graphing/charts/linechart",
    "description": "---\ncomponents:\n  - rx.recharts.LineChart\n  - rx.recharts.Line\n---\n\nLine Chart\n\nA line chart is a type of chart used to show information that changes over time. Line charts are created by plotting a series of several points and connecting them with a straight line.\n\nSimple Example\n\nFor a line chart we must define an  component for each set of values we wish to plot. Each  component has a  which clearly states which variable in our data we are tracking. In this simple example we plot  and  as separate lines against the  column which we set as the  in .\n\nExample with Props\n\nOur second example uses exactly the same data as our first example, except now we add some extra features to our line graphs. We add a  prop to  to style the lines differently. In addition, we add an  to get a grid in the background, an  to give us a legend for our graphs and an  to add a box with text that appears when you pause the mouse pointer on an element in the graph.\n\nLayout\n\nThe  prop allows you to set the orientation of the graph to be vertical or horizontal. The  prop defines the spacing around the graph,\n\nDynamic Data\n\nChart data can be modified by tying the  prop to a State var. Most other\nprops, such as , can be controlled dynamically as well. In the following\nexample the \"Munge Data\" button can be used to randomly modify the data, and the\ntwo  elements change the line . Since the data and style is saved\nin the per-browser-tab State, the changes will not be visible to other visitors.\n\nTo learn how to use the ,  and  props check out the of the area chart documentation, where these props are all described with examples."
  },
  {
    "name": "Radialbarchart",
    "parts": [
      "Library",
      "Graphing",
      "Charts",
      "Radialbarchart"
    ],
    "url": "docs/library/graphing/charts/radialbarchart",
    "description": "---\ncomponents:\n    - rx.recharts.RadialBarChart\n---\n\nRadial Bar Chart\n\nSimple Example\n\nThis example demonstrates how to use a  with a . The  takes in  and then the  takes in a . A radial bar chart is a circular visualization where data categories are represented by bars extending outward from a central point, with the length of each bar proportional to its value.\n\nAdvanced Example\n\nThe  and  define the circular arc over which the bars are distributed, while  and  determine the radial extent of the bars from the center."
  },
  {
    "name": "Plotly",
    "parts": [
      "Library",
      "Graphing",
      "Other Charts",
      "Plotly"
    ],
    "url": "docs/library/graphing/other-charts/plotly",
    "description": "---\ncomponents:\n  - rx.plotly\n---\n\nPlotly\n\nPlotly is a graphing library that can be used to create interactive graphs. Use the rx.plotly component to wrap Plotly as a component for use in your web page. Checkout Plotly for more information.\n\nBasic Example\n\nLet's create a line graph of life expectancy in Canada.\n\n3D graphing example\n\nLet's create a 3D surface plot of Mount Bruno. This is a slightly more complicated example, but it wraps in Reflex using the same method. In fact, you can wrap any figure using the same approach.\n\nPlot as State Var\n\nIf the figure is set as a state var, it can be updated during run time.\n\nAdding Styles and Layouts\n\nUse  method to update the layout of your chart. Checkout Plotly Layouts for all layouts props."
  },
  {
    "name": "Pyplot",
    "parts": [
      "Library",
      "Graphing",
      "Other Charts",
      "Pyplot"
    ],
    "url": "docs/library/graphing/other-charts/pyplot",
    "description": "---\ncomponents:\n  - pyplot\n---\n\nPyplot\n\nPyplot () is a graphing library that wraps Matplotlib. Use the  component to display any Matplotlib plot in your app. Check out Matplotlib for more information.\n\nInstallation\n\nInstall the  package using pip.\n\nBasic Example\n\nTo display a Matplotlib plot in your app, you can use the  component. Pass in the figure you created with Matplotlib to the  component as a child.\n\nStateful Example\n\nLets create a scatter plot of random data. We'll also allow the user to randomize the data and change the number of points.\n\nIn this example, we'll use a  to display the plot in both light and dark mode. We need to do this manually here because the colors are determined by the matplotlib chart and not the theme."
  },
  {
    "name": "Text",
    "parts": [
      "Library",
      "Typography",
      "Text"
    ],
    "url": "docs/library/typography/text",
    "description": "---\ncomponents:\n    - rx.text\n    - rx.text.em\n\n---\n\nText\n\nAs another element\n\nUse the  prop to render text as a , ,  or . This prop is purely semantic and does not alter visual appearance.\n\nSize\n\nUse the  prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.\n\nSizes 2–4 are designed to work well for long-form content. Sizes 1–3 are designed to work well for UI labels.\n\nWeight\n\nUse the  prop to set the text weight.\n\nAlign\n\nUse the  prop to set text alignment.\n\nTrim\n\nUse the  prop to trim the leading space at the start, end, or both sides of the text box.\n\nTrimming the leading is useful when dialing in vertical spacing in cards or other “boxy” components. Otherwise, padding looks larger on top and bottom than on the sides.\n\nColor\n\nUse the  prop to assign a specific color, ignoring the global theme.\n\nHigh Contrast\n\nUse the  prop to increase color contrast with the background.\n\nWith formatting\n\nCompose  with formatting components to add emphasis and structure to content.\n\nPreformmatting\nBy Default, the browser renders multiple white spaces into one. To preserve whitespace, use the  css prop.\n\nWith form controls\n\nComposing  with a form control like , , or  automatically centers the control with the first line of text, even when the text is multi-line."
  },
  {
    "name": "Strong",
    "parts": [
      "Library",
      "Typography",
      "Strong"
    ],
    "url": "docs/library/typography/strong",
    "description": "---\ncomponents:\n    - rx.text.strong\n---\n\nStrong\n\nMarks text to signify strong importance."
  },
  {
    "name": "Markdown",
    "parts": [
      "Library",
      "Typography",
      "Markdown"
    ],
    "url": "docs/library/typography/markdown",
    "description": "---\ncomponents:\n    - rx.markdown\n---\n\nMarkdown\n\nThe  component can be used to render markdown text.\nIt is based on Github Flavored Markdown.\n\nMath Equations\n\nYou can render math equations using LaTeX.\nFor inline equations, surround the equation with :\n\nSyntax Highlighting\n\nYou can render code blocks with syntax highlighting using the \\\\|component_mapcomponent_map` prop is a markdown element, and the value is\na function that takes the text of the element as input and returns a Reflex component.\n\npython\nimport reflex as rx\n\ncomponent = rx.text(\"Hello World!\")\n\\"
  },
  {
    "name": "Link",
    "parts": [
      "Library",
      "Typography",
      "Link"
    ],
    "url": "docs/library/typography/link",
    "description": "---\ncomponents:\n    - rx.link\n---\n\nLink\n\nLinks are accessible elements used primarily for navigation. Use the  prop to specify the location for the link to navigate to.\n\nYou can also provide local links to other pages in your project without writing the full url.\n\nThe  component can be used to wrap other components to make them link to other pages.\n\nYou can also create anchors to link to specific parts of a page using the  prop.\n\nTo reference an anchor, you can use the  prop of the  component. The  should be in the format of the page you want to link to followed by a # and the id of the anchor.\n\nStyle\n\nSize\n\nUse the  prop to control the size of the link. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.\n\nWeight\n\nUse the  prop to set the text weight.\n\nTrim\n\nUse the  prop to trim the leading space at the start, end, or both sides of the rendered text.\n\nUnderline\n\nUse the  prop to manage the visibility of the underline affordance. It defaults to .\n\nColor\n\nUse the  prop to assign a specific color, ignoring the global theme.\n\nHigh Contrast\n\nUse the  prop to increase color contrast with the background."
  },
  {
    "name": "Blockquote",
    "parts": [
      "Library",
      "Typography",
      "Blockquote"
    ],
    "url": "docs/library/typography/blockquote",
    "description": "---\ncomponents:\n    - rx.blockquote\n---\n\nBlockquote\n\nSize\n\nUse the  prop to control the size of the blockquote. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.\n\nWeight\n\nUse the  prop to set the blockquote weight.\n\nColor\n\nUse the  prop to assign a specific color, ignoring the global theme.\n\nHigh Contrast\n\nUse the  prop to increase color contrast with the background."
  },
  {
    "name": "Em",
    "parts": [
      "Library",
      "Typography",
      "Em"
    ],
    "url": "docs/library/typography/em",
    "description": "---\ncomponents:\n    - rx.text.em\n---\n\nEm (Emphasis)\n\nMarks text to stress emphasis."
  },
  {
    "name": "Quote",
    "parts": [
      "Library",
      "Typography",
      "Quote"
    ],
    "url": "docs/library/typography/quote",
    "description": "---\ncomponents:\n    - rx.text.quote\n---\n\nQuote\n\nA short inline quotation."
  },
  {
    "name": "Heading",
    "parts": [
      "Library",
      "Typography",
      "Heading"
    ],
    "url": "docs/library/typography/heading",
    "description": "---\ncomponents:\n    - rx.heading\n---\n\nHeading\n\nAs another element\n\nUse the  prop to change the heading level. This prop is purely semantic and does not change the visual appearance.\n\nSize\n\nUse the  prop to control the size of the heading. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease\n\nWeight\n\nUse the  prop to set the text weight.\n\nAlign\n\nUse the  prop to set text alignment.\n\nTrim\n\nUse the  prop to trim the leading space at the start, end, or both sides of the text.\n\nTrimming the leading is useful when dialing in vertical spacing in cards or other “boxy” components. Otherwise, padding looks larger on top and bottom than on the sides.\n\nColor\n\nUse the  prop to assign a specific color, ignoring the global theme.\n\nHigh Contrast\n\nUse the  prop to increase color contrast with the background."
  },
  {
    "name": "Kbd",
    "parts": [
      "Library",
      "Typography",
      "Kbd"
    ],
    "url": "docs/library/typography/kbd",
    "description": "---\ncomponents:\n    - rx.text.kbd\n---\n\nrx.text.kbd (Keyboard)\n\nRepresents keyboard input or a hotkey.\n\nSize\n\nUse the  prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease."
  },
  {
    "name": "Code",
    "parts": [
      "Library",
      "Typography",
      "Code"
    ],
    "url": "docs/library/typography/code",
    "description": "---\ncomponents:\n    - rx.code\n---\n\nCode\n\nSize\n\nUse the  prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.\n\nWeight\n\nUse the  prop to set the text weight.\n\nVariant\n\nUse the  prop to control the visual style.\n\nColor\n\nUse the  prop to assign a specific color, ignoring the global theme.\n\nHigh Contrast\n\nUse the  prop to increase color contrast with the background."
  },
  {
    "name": "Toast",
    "parts": [
      "Library",
      "Overlay",
      "Toast"
    ],
    "url": "docs/library/overlay/toast",
    "description": "---\ncomponents:\n  - rx.toast.provider\n---\n\nToast\n\nA  is a non-blocking notification that disappears after a certain amount of time. It is often used to show a message to the user without interrupting their workflow.\n\nUsage\n\nYou can use  as an event handler for any component that triggers an action.\n\nUsage in State\n\nYou can also use  in a state to show a toast when a specific action is triggered, using .\n\nInteraction\n\nIf you want to interact with a toast, a few props are available to customize the behavior.\n\nBy passing a  to the  or  prop, you can trigger an action when the toast is clicked or when it is closed.\n\nPresets\n\n has some presets that you can use to show different types of toasts.\n\nCustomization\n\nIf the presets don't fit your needs, you can customize the toasts by passing to  or to  some kwargs.\n\nThe following props are available for customization:\n\n- : : Toast's description, renders underneath the title.\n- : : Whether to show the close button.\n- : : Dark toast in light mode and vice versa.\n- : : Control the sensitivity of the toast for screen readers.\n- : : Time in milliseconds that should elapse before automatically closing the toast.\n- : : Position of the toast.\n- : : If false, it'll prevent the user from dismissing the toast.\n- : : Renders a primary button, clicking it will close the toast.\n- : : Renders a secondary button, clicking it will close the toast.\n- : : Custom id for the toast.\n- : : Removes the default styling, which allows for easier customization.\n- : : Custom style for the toast.\n- : : The function gets called when either the close button is clicked, or the toast is swiped.\n- : : Function that gets called when the toast disappears automatically after it's timeout ( prop).\n\nToast Provider\n\nUsing the  function require to have a toast provider in your app.\n\n is a component that provides a context for displaying toasts. It should be placed at the root of your app."
  },
  {
    "name": "Popover",
    "parts": [
      "Library",
      "Overlay",
      "Popover"
    ],
    "url": "docs/library/overlay/popover",
    "description": "---\ncomponents:\n  - rx.popover.root\n  - rx.popover.content\n  - rx.popover.trigger\n  - rx.popover.close\n\nonly_low_level:\n  - True\n\nPopoverRoot: |\n  lambda **props: rx.popover.root(\n      rx.popover.trigger(\n          rx.button(\"Popover\"),\n      ),\n      rx.popover.content(\n          rx.flex(\n              rx.text(\"Simple Example\"),\n              rx.popover.close(\n                  rx.button(\"Close\"),\n              ),\n              direction=\"column\",\n              spacing=\"3\",\n          ),\n      ),\n      **props\n  )\n\nPopoverContent: |\n  lambda **props: rx.popover.root(\n      rx.popover.trigger(\n          rx.button(\"Popover\"),\n      ),\n      rx.popover.content(\n          rx.flex(\n              rx.text(\"Simple Example\"),\n              rx.popover.close(\n                  rx.button(\"Close\"),\n              ),\n              direction=\"column\",\n              spacing=\"3\",\n          ),\n          **props\n      ),\n  )\n---\n\nPopover\n\nA popover displays content, triggered by a button.\n\nThe  contains all the parts of a popover.\n\nThe  contains the button that toggles the popover.\n\nThe  is the component that pops out when the popover is open.\n\nThe  is the button that closes an open popover.\n\nBasic Example\n\nExamples in Context\n\nPopover with dynamic title\n\nCode like below will not work as expected and it is necessary to place the dynamic title () inside of an  component.\n\nThis code will work:\n\nEvents when the Popover opens or closes\n\nThe  event is called when the  state of the popover changes. It is used in conjunction with the  prop, which is passed to the event handler."
  },
  {
    "name": "Hover Card",
    "parts": [
      "Library",
      "Overlay",
      "Hover Card"
    ],
    "url": "docs/library/overlay/hover-card",
    "description": "---\ncomponents:\n  - rx.hover_card.root\n  - rx.hover_card.content\n  - rx.hover_card.trigger\n\nonly_low_level:\n  - True\n\nHoverCardRoot: |\n  lambda **props: rx.hover_card.root(\n      rx.hover_card.trigger(\n          rx.link(\"Hover over me\"),\n      ),\n      rx.hover_card.content(\n          rx.text(\"This is the tooltip content.\"),\n      ),\n      **props\n  )\n\nHoverCardContent: |\n  lambda **props: rx.hover_card.root(\n      rx.hover_card.trigger(\n          rx.link(\"Hover over me\"),\n      ),\n      rx.hover_card.content(\n          rx.text(\"This is the tooltip content.\"),\n          **props\n      ),\n  )\n---\n\nHovercard\n\nThe  contains all the parts of a hover card.\n\nThe  wraps the link that will open the hover card.\n\nThe  contains the content of the open hover card.\n\nEvents when the Hovercard opens or closes\n\nThe  event is called when the  state of the hovercard changes. It is used in conjunction with the  prop, which is passed to the event handler."
  },
  {
    "name": "Drawer",
    "parts": [
      "Library",
      "Overlay",
      "Drawer"
    ],
    "url": "docs/library/overlay/drawer",
    "description": "---\ncomponents:\n  - rx.drawer.root\n  - rx.drawer.trigger\n  - rx.drawer.overlay\n  - rx.drawer.portal\n  - rx.drawer.content\n  - rx.drawer.close\n\nonly_low_level:\n  - True\n\nDrawerRoot: |\n  lambda **props: rx.drawer.root(\n      rx.drawer.trigger(rx.button(\"Open Drawer\")),\n      rx.drawer.overlay(z_index=\"5\"),\n      rx.drawer.portal(\n          rx.drawer.content(\n              rx.flex(\n                  rx.drawer.close(rx.button(\"Close\")),\n              ),\n              height=\"100%\",\n              width=\"20em\",\n              background_color=\"#FFF\"\n          ),\n      ),\n      **props,\n  )\n---\n\nDrawer\n\nSidebar Menu with a Drawer and State\n\nThis example shows how to create a sidebar menu with a drawer. The drawer is opened by clicking a button. The drawer contains links to different sections of the page. When a link is clicked the drawer closes and the page scrolls to the section.\n\nThe  component has an  prop that is set by the state variable . Setting the  prop to  allows the user to interact with the rest of the page while the drawer is open and allows the page to be scrolled when a user clicks one of the links."
  },
  {
    "name": "Dialog",
    "parts": [
      "Library",
      "Overlay",
      "Dialog"
    ],
    "url": "docs/library/overlay/dialog",
    "description": "---\ncomponents:\n  - rx.dialog.root\n  - rx.dialog.trigger\n  - rx.dialog.title\n  - rx.dialog.content\n  - rx.dialog.description\n  - rx.dialog.close\n\nonly_low_level:\n  - True\n\nDialogRoot: |\n  lambda **props: rx.dialog.root(\n      rx.dialog.trigger(rx.button(\"Open Dialog\")),\n      rx.dialog.content(\n          rx.dialog.title(\"Welcome to Reflex!\"),\n          rx.dialog.description(\n              \"This is a dialog component. You can render anything you want in here.\",\n          ),\n          rx.dialog.close(\n              rx.button(\"Close Dialog\"),\n          ),\n      ),\n      **props,\n  )\n\nDialogContent: |\n  lambda **props: rx.dialog.root(\n      rx.dialog.trigger(rx.button(\"Open Dialog\")),\n      rx.dialog.content(\n          rx.dialog.title(\"Welcome to Reflex!\"),\n          rx.dialog.description(\n              \"This is a dialog component. You can render anything you want in here.\",\n          ),\n          rx.dialog.close(\n              rx.button(\"Close Dialog\"),\n          ),\n          **props,\n      ),\n  )\n---\n\nDialog\n\nThe  contains all the parts of a dialog.\n\nThe  wraps the control that will open the dialog.\n\nThe  contains the content of the dialog.\n\nThe  is a title that is announced when the dialog is opened.\n\nThe  is a description that is announced when the dialog is opened.\n\nThe  wraps the control that will close the dialog.\n\nIn context examples\n\nEvents when the Dialog opens or closes\n\nThe  event is called when the  state of the dialog changes. It is used in conjunction with the  prop, which is passed to the event handler.\n\nCheck out the menu docs for an example of opening a dialog from within a dropdown menu.\n\nForm Submission to a Database from a Dialog\n\nThis example adds new users to a database from a dialog using a form.\n\n1. It defines a User model with name and email fields.\n2. The  method adds a new user to the database, checking for existing emails.\n3. On form submission, it calls the  method.\n4. The UI component has:\n\n- A button to open a dialog\n- A dialog containing a form to add a new user\n- Input fields for name and email\n- Submit and Cancel buttons"
  },
  {
    "name": "Dropdown Menu",
    "parts": [
      "Library",
      "Overlay",
      "Dropdown Menu"
    ],
    "url": "docs/library/overlay/dropdown-menu",
    "description": "---\ncomponents:\n  - rx.dropdown_menu.root\n  - rx.dropdown_menu.content\n  - rx.dropdown_menu.trigger\n  - rx.dropdown_menu.item\n  - rx.dropdown_menu.separator\n  - rx.dropdown_menu.sub_content\n\nonly_low_level:\n  - True\n\nDropdownMenuRoot: |\n  lambda **props: rx.menu.root(\n      rx.menu.trigger(rx.button(\"drop down menu\")),\n      rx.menu.content(\n          rx.menu.item(\"Edit\", shortcut=\"⌘ E\"),\n          rx.menu.item(\"Share\"),\n          rx.menu.item(\"Delete\", shortcut=\"⌘ ⌫\", color=\"red\"),\n          rx.menu.sub(\n              rx.menu.sub_trigger(\"More\"),\n              rx.menu.sub_content(\n                  rx.menu.item(\"Eradicate\"),\n                  rx.menu.item(\"Duplicate\"),\n                  rx.menu.item(\"Archive\"),\n              ),\n          ),\n      ),\n      **props\n  )\n\nDropdownMenuContent: |\n  lambda **props: rx.menu.root(\n      rx.menu.trigger(rx.button(\"drop down menu\")),\n      rx.menu.content(\n          rx.menu.item(\"Edit\", shortcut=\"⌘ E\"),\n          rx.menu.item(\"Share\"),\n          rx.menu.item(\"Delete\", shortcut=\"⌘ ⌫\", color=\"red\"),\n          rx.menu.sub(\n              rx.menu.sub_trigger(\"More\"),\n              rx.menu.sub_content(\n                  rx.menu.item(\"Eradicate\"),\n                  rx.menu.item(\"Duplicate\"),\n                  rx.menu.item(\"Archive\"),\n              ),\n          ),\n          **props,\n      ),\n  )\n\nDropdownMenuItem: |\n  lambda **props: rx.menu.root(\n      rx.menu.trigger(rx.button(\"drop down menu\")),\n      rx.menu.content(\n          rx.menu.item(\"Edit\", shortcut=\"⌘ E\", **props),\n          rx.menu.item(\"Share\", **props),\n          rx.menu.item(\"Delete\", shortcut=\"⌘ ⌫\", color=\"red\", **props),\n          rx.menu.sub(\n              rx.menu.sub_trigger(\"More\"),\n              rx.menu.sub_content(\n                  rx.menu.item(\"Eradicate\", **props),\n                  rx.menu.item(\"Duplicate\", **props),\n                  rx.menu.item(\"Archive\", **props),\n              ),\n          ),\n      ),\n  )\n\nDropdownMenuSub: |\n  lambda **props: rx.menu.root(\n      rx.menu.trigger(rx.button(\"drop down menu\")),\n      rx.menu.content(\n          rx.menu.item(\"Edit\", shortcut=\"⌘ E\"),\n          rx.menu.item(\"Share\"),\n          rx.menu.item(\"Delete\", shortcut=\"⌘ ⌫\", color=\"red\"),\n          rx.menu.sub(\n              rx.menu.sub_trigger(\"More\"),\n              rx.menu.sub_content(\n                  rx.menu.item(\"Eradicate\"),\n                  rx.menu.item(\"Duplicate\"),\n                  rx.menu.item(\"Archive\"),\n              ),\n              **props,\n          ),\n      ),\n  )\n\nDropdownMenuSubTrigger: |\n  lambda **props: rx.menu.root(\n      rx.menu.trigger(rx.button(\"drop down menu\")),\n      rx.menu.content(\n          rx.menu.item(\"Edit\", shortcut=\"⌘ E\"),\n          rx.menu.item(\"Share\"),\n          rx.menu.item(\"Delete\", shortcut=\"⌘ ⌫\", color=\"red\"),\n          rx.menu.sub(\n              rx.menu.sub_trigger(\"More\", **props),\n              rx.menu.sub_content(\n                  rx.menu.item(\"Eradicate\"),\n                  rx.menu.item(\"Duplicate\"),\n                  rx.menu.item(\"Archive\"),\n              ),\n          ),\n      ),\n  )\n\nDropdownMenuSubContent: |\n  lambda **props: rx.menu.root(\n      rx.menu.trigger(rx.button(\"drop down menu\")),\n      rx.menu.content(\n          rx.menu.item(\"Edit\", shortcut=\"⌘ E\"),\n          rx.menu.item(\"Share\"),\n          rx.menu.item(\"Delete\", shortcut=\"⌘ ⌫\", color=\"red\"),\n          rx.menu.sub(\n              rx.menu.sub_trigger(\"More\"),\n              rx.menu.sub_content(\n                  rx.menu.item(\"Eradicate\"),\n                  rx.menu.item(\"Duplicate\"),\n                  rx.menu.item(\"Archive\"),\n                  **props,\n              ),\n          ),\n      ),\n  )\n---\n\nDropdown Menu\n\nA Dropdown Menu is a menu that offers a list of options that a user can select from. They are typically positioned near a button that will control their appearance and disappearance.\n\nA Dropdown Menu is composed of a , a  and a . The  is the element that the user interacts with to open the menu. It wraps the element that will open the dropdown menu. The  is the component that pops out when the dropdown menu is open.\n\nThe  contains the actual dropdown menu items and sits under the . The  prop is an optional shortcut command displayed next to the item text.\n\nThe  contains all the parts of a submenu. There is a , which is an item that opens a submenu. It must be rendered inside a  component. The  is the component that pops out when a submenu is open. It must also be rendered inside a  component.\n\nThe  is used to visually separate items in a dropdown menu.\n\nEvents when the Dropdown Menu opens or closes\n\nThe  event, from the , is called when the  state of the dropdown menu changes. It is used in conjunction with the  prop, which is passed to the event handler.\n\nOpening a Dialog from Menu using State\n\nAccessing an overlay component from within another overlay component is a common use case but does not always work exactly as expected.\n\nThe code below will not work as expected as because the dialog is within the menu and the dialog will only be open when the menu is open, rendering the dialog unusable.\n\nIn this example, we will show how to open a dialog box from a dropdown menu, where the menu will close and the dialog will open and be functional."
  },
  {
    "name": "Context Menu",
    "parts": [
      "Library",
      "Overlay",
      "Context Menu"
    ],
    "url": "docs/library/overlay/context-menu",
    "description": "---\ncomponents:\n  - rx.context_menu.root\n  - rx.context_menu.item\n  - rx.context_menu.separator\n  - rx.context_menu.trigger\n  - rx.context_menu.content\n  - rx.context_menu.sub\n  - rx.context_menu.sub_trigger\n  - rx.context_menu.sub_content\n\nonly_low_level:\n  - True\n\nContextMenuRoot: |\n  lambda **props: rx.context_menu.root(\n          rx.context_menu.trigger(\n              rx.text(\"Context Menu (right click)\")\n          ),\n          rx.context_menu.content(\n              rx.context_menu.item(\"Copy\", shortcut=\"⌘ C\"),\n              rx.context_menu.item(\"Share\"),\n              rx.context_menu.item(\"Delete\", shortcut=\"⌘ ⌫\", color=\"red\"),\n              rx.context_menu.sub(\n                  rx.context_menu.sub_trigger(\"More\"),\n                  rx.context_menu.sub_content(\n                      rx.context_menu.item(\"Eradicate\"),\n                      rx.context_menu.item(\"Duplicate\"),\n                      rx.context_menu.item(\"Archive\"),\n                  ),\n              ),\n          ),\n          **props\n      )\n\nContextMenuTrigger: |\n  lambda **props: rx.context_menu.root(\n          rx.context_menu.trigger(\n              rx.text(\"Context Menu (right click)\"),\n              **props\n          ),\n          rx.context_menu.content(\n              rx.context_menu.item(\"Copy\", shortcut=\"⌘ C\"),\n              rx.context_menu.item(\"Share\"),\n              rx.context_menu.item(\"Delete\", shortcut=\"⌘ ⌫\", color=\"red\"),\n              rx.context_menu.sub(\n                  rx.context_menu.sub_trigger(\"More\"),\n                  rx.context_menu.sub_content(\n                      rx.context_menu.item(\"Eradicate\"),\n                      rx.context_menu.item(\"Duplicate\"),\n                      rx.context_menu.item(\"Archive\"),\n                  ),\n              ),\n          ),\n      )\n\nContextMenuContent: |\n  lambda **props: rx.context_menu.root(\n          rx.context_menu.trigger(\n              rx.text(\"Context Menu (right click)\")\n          ),\n          rx.context_menu.content(\n              rx.context_menu.item(\"Copy\", shortcut=\"⌘ C\"),\n              rx.context_menu.item(\"Share\"),\n              rx.context_menu.item(\"Delete\", shortcut=\"⌘ ⌫\", color=\"red\"),\n              rx.context_menu.sub(\n                  rx.context_menu.sub_trigger(\"More\"),\n                  rx.context_menu.sub_content(\n                      rx.context_menu.item(\"Eradicate\"),\n                      rx.context_menu.item(\"Duplicate\"),\n                      rx.context_menu.item(\"Archive\"),\n                  ),\n              ),\n              **props\n          ),\n      )\n\nContextMenuSub: |\n  lambda **props: rx.context_menu.root(\n          rx.context_menu.trigger(\n              rx.text(\"Context Menu (right click)\")\n          ),\n          rx.context_menu.content(\n              rx.context_menu.item(\"Copy\", shortcut=\"⌘ C\"),\n              rx.context_menu.item(\"Share\"),\n              rx.context_menu.item(\"Delete\", shortcut=\"⌘ ⌫\", color=\"red\"),\n              rx.context_menu.sub(\n                  rx.context_menu.sub_trigger(\"More\"),\n                  rx.context_menu.sub_content(\n                      rx.context_menu.item(\"Eradicate\"),\n                      rx.context_menu.item(\"Duplicate\"),\n                      rx.context_menu.item(\"Archive\"),\n                  ),\n              **props\n              ),\n          ),\n      )\n\nContextMenuSubTrigger: |\n  lambda **props: rx.context_menu.root(\n          rx.context_menu.trigger(\n              rx.text(\"Context Menu (right click)\")\n          ),\n          rx.context_menu.content(\n              rx.context_menu.item(\"Copy\", shortcut=\"⌘ C\"),\n              rx.context_menu.item(\"Share\"),\n              rx.context_menu.item(\"Delete\", shortcut=\"⌘ ⌫\", color=\"red\"),\n              rx.context_menu.sub(\n                  rx.context_menu.sub_trigger(\"More\", **props),\n                  rx.context_menu.sub_content(\n                      rx.context_menu.item(\"Eradicate\"),\n                      rx.context_menu.item(\"Duplicate\"),\n                      rx.context_menu.item(\"Archive\"),\n                  ),\n              ),\n          ),\n      )\n\nContextMenuSubContent: |\n  lambda **props: rx.context_menu.root(\n          rx.context_menu.trigger(\n              rx.text(\"Context Menu (right click)\")\n          ),\n          rx.context_menu.content(\n              rx.context_menu.item(\"Copy\", shortcut=\"⌘ C\"),\n              rx.context_menu.item(\"Share\"),\n              rx.context_menu.item(\"Delete\", shortcut=\"⌘ ⌫\", color=\"red\"),\n              rx.context_menu.sub(\n                  rx.context_menu.sub_trigger(\"More\"),\n                  rx.context_menu.sub_content(\n                      rx.context_menu.item(\"Eradicate\"),\n                      rx.context_menu.item(\"Duplicate\"),\n                      rx.context_menu.item(\"Archive\"),\n                      **props\n                  ),\n              ),\n          ),\n      )\n\nContextMenuItem: |\n  lambda **props: rx.context_menu.root(\n          rx.context_menu.trigger(\n              rx.text(\"Context Menu (right click)\")\n          ),\n          rx.context_menu.content(\n              rx.context_menu.item(\"Copy\", shortcut=\"⌘ C\", **props),\n              rx.context_menu.item(\"Share\", **props),\n              rx.context_menu.item(\"Delete\", shortcut=\"⌘ ⌫\", color=\"red\", **props),\n              rx.context_menu.sub(\n                  rx.context_menu.sub_trigger(\"More\"),\n                  rx.context_menu.sub_content(\n                      rx.context_menu.item(\"Eradicate\", **props),\n                      rx.context_menu.item(\"Duplicate\", **props),\n                      rx.context_menu.item(\"Archive\", **props),\n                  ),\n              ),\n          ),\n      )\n---\n\nContext Menu\n\nA Context Menu is a popup menu that appears upon user interaction, such as a right-click or a hover.\n\nBasic Usage\n\nA Context Menu is composed of a , a  and a . The  contains all the parts of a context menu. The  is the element that the user interacts with to open the menu. It wraps the element that will open the context menu. The  is the component that pops out when the context menu is open.\n\nThe  contains the actual context menu items and sits under the .\n\nThe  contains all the parts of a submenu. There is a , which is an item that opens a submenu. It must be rendered inside a  component. The  is the component that pops out when a submenu is open. It must also be rendered inside a  component.\n\nThe  is used to visually separate items in a context menu.\n\npython\nrx.context_menu.root(\n    rx.context_menu.trigger(\n       rx.button(\"Right click me\"),\n    ),\n    rx.context_menu.content(\n        rx.cond(\n            State.count % 2 == 0,\n            rx.vstack(\n                rx.context_menu.item(\"Even Option 1\", on_click=State.set_selected_option(\"Even Option 1\")),\n                rx.context_menu.item(\"Even Option 2\", on_click=State.set_selected_option(\"Even Option 2\")),\n                rx.context_menu.item(\"Even Option 3\", on_click=State.set_selected_option(\"Even Option 3\")),\n            ),\n            rx.vstack(\n                rx.context_menu.item(\"Odd Option A\", on_click=State.set_selected_option(\"Odd Option A\")),\n                rx.context_menu.item(\"Odd Option B\", on_click=State.set_selected_option(\"Odd Option B\")),\n                rx.context_menu.item(\"Odd Option C\", on_click=State.set_selected_option(\"Odd Option C\")),\n            )\n        )\n    ),\n)\n`\n\nOpening a Dialog from Context Menu using State\n\nAccessing an overlay component from within another overlay component is a common use case but does not always work exactly as expected.\n\nThe code below will not work as expected as because the dialog is within the menu and the dialog will only be open when the menu is open, rendering the dialog unusable.\n\nIn this example, we will show how to open a dialog box from a context menu, where the menu will close and the dialog will open and be functional."
  },
  {
    "name": "Alert Dialog",
    "parts": [
      "Library",
      "Overlay",
      "Alert Dialog"
    ],
    "url": "docs/library/overlay/alert-dialog",
    "description": "---\ncomponents:\n  - rx.alert_dialog.root\n  - rx.alert_dialog.content\n  - rx.alert_dialog.trigger\n  - rx.alert_dialog.title\n  - rx.alert_dialog.description\n  - rx.alert_dialog.action\n  - rx.alert_dialog.cancel\n\nonly_low_level:\n  - True\n\nAlertDialogRoot: |\n  lambda **props: rx.alert_dialog.root(\n      rx.alert_dialog.trigger(\n          rx.button(\"Revoke access\"),\n      ),\n      rx.alert_dialog.content(\n          rx.alert_dialog.title(\"Revoke access\"),\n          rx.alert_dialog.description(\n              \"Are you sure? This application will no longer be accessible and any existing sessions will be expired.\",\n          ),\n          rx.flex(\n              rx.alert_dialog.cancel(\n                  rx.button(\"Cancel\"),\n              ),\n              rx.alert_dialog.action(\n                  rx.button(\"Revoke access\"),\n              ),\n              spacing=\"3\",\n          ),\n      ),\n      **props\n  )\n\nAlertDialogContent: |\n  lambda **props: rx.alert_dialog.root(\n      rx.alert_dialog.trigger(\n          rx.button(\"Revoke access\"),\n      ),\n      rx.alert_dialog.content(\n          rx.alert_dialog.title(\"Revoke access\"),\n          rx.alert_dialog.description(\n              \"Are you sure? This application will no longer be accessible and any existing sessions will be expired.\",\n          ),\n          rx.flex(\n              rx.alert_dialog.cancel(\n                  rx.button(\"Cancel\"),\n              ),\n              rx.alert_dialog.action(\n                  rx.button(\"Revoke access\"),\n              ),\n              spacing=\"3\",\n          ),\n          **props\n      ),\n  )\n---\n\nAlert Dialog\n\nAn alert dialog is a modal confirmation dialog that interrupts the user and expects a response.\n\nThe  contains all the parts of the dialog.\n\nThe  wraps the control that will open the dialog.\n\nThe  contains the content of the dialog.\n\nThe  is the title that is announced when the dialog is opened.\n\nThe  is an optional description that is announced when the dialog is opened.\n\nThe  wraps the control that will close the dialog. This should be distinguished visually from the  control.\n\nThe  wraps the control that will close the dialog. This should be distinguished visually from the  control.\n\nBasic Example\n\nThis example has a different color scheme and the  and  buttons are right aligned.\n\nUse the  component to align content flush with the sides of the dialog.\n\nEvents when the Alert Dialog opens or closes\n\nThe  event is called when the  state of the dialog changes. It is used in conjunction with the  prop.\n\nControlling Alert Dialog with State\n\nThis example shows how to control whether the dialog is open or not with state. This is an easy way to show the dialog without needing to use the .\n\n has a prop  that can be set to a boolean value to control whether the dialog is open or not.\n\nWe toggle this  prop with a button outside of the dialog and the  and  buttons inside the dialog.\n\nForm Submission to a Database from an Alert Dialog\n\nThis example adds new users to a database from an alert dialog using a form.\n\n1. It defines a User1 model with name and email fields.\n2. The  method adds a new user to the database, checking for existing emails.\n3. On form submission, it calls the  method.\n4. The UI component has:\n- A button to open an alert dialog\n- An alert dialog containing a form to add a new user\n- Input fields for name and email\n- Submit and Cancel buttons"
  },
  {
    "name": "Tooltip",
    "parts": [
      "Library",
      "Overlay",
      "Tooltip"
    ],
    "url": "docs/library/overlay/tooltip",
    "description": "---\ncomponents:\n  - rx.tooltip\n\nTooltip: |\n  lambda **props: rx.tooltip(\n      rx.button(\"Hover over me\"),\n      content=\"This is the tooltip content.\",\n      **props,\n  )\n---\n\nTooltip\n\nA  displays informative information when users hover over or focus on an element.\n\nIt takes a  prop, which is the content associated with the tooltip.\n\nEvents when the Tooltip opens or closes\n\nThe  event is called when the  state of the tooltip changes. It is used in conjunction with the  prop, which is passed to the event handler."
  },
  {
    "name": "Audio",
    "parts": [
      "Library",
      "Media",
      "Audio"
    ],
    "url": "docs/library/media/audio",
    "description": "---\ncomponents:\n    - rx.audio\n---\n\nAudio\n\nThe audio component can display an audio given an src path as an argument. This could either be a local path from the assets folder or an external link.\n\nIf we had a local file in the  folder named  we could set  to view the audio file."
  },
  {
    "name": "Intro",
    "parts": [
      "AI Builder",
      "Intro"
    ],
    "url": "docs/ai-builder/intro",
    "description": "Overview"
  },
  {
    "name": "Image",
    "parts": [
      "Library",
      "Media",
      "Image"
    ],
    "url": "docs/library/media/image",
    "description": "---\ncomponents:\n    - rx.image\n---\n\nImage\n\nThe Image component can display an image given a  path as an argument.\nThis could either be a local path from the assets folder or an external link.\n\nImage composes a box and can be styled similarly.\n\nYou can also pass a  image object as the ."
  },
  {
    "name": "Faq",
    "parts": [
      "AI Builder",
      "Faq"
    ],
    "url": "docs/ai-builder/faq",
    "description": ""
  },
  {
    "name": "Overview",
    "parts": [
      "AI Builder",
      "Overview"
    ],
    "url": "docs/ai-builder/overview",
    "description": "Overview"
  },
  {
    "name": "Video",
    "parts": [
      "Library",
      "Media",
      "Video"
    ],
    "url": "docs/library/media/video",
    "description": "---\ncomponents:\n    - rx.video\n---\n\nVideo\n\nThe video component can display a video given an src path as an argument. This could either be a local path from the assets folder or an external link.\n\nIf we had a local file in the  folder named  we could set  to view the video."
  },
  {
    "name": "Fixing Errors",
    "parts": [
      "AI Builder",
      "Prompting",
      "Fixing Errors"
    ],
    "url": "docs/ai-builder/prompting/fixing-errors",
    "description": "Fixing Errors\n\nStill to come!"
  },
  {
    "name": "Breaking Up Complex Prompts",
    "parts": [
      "AI Builder",
      "Prompting",
      "Breaking Up Complex Prompts"
    ],
    "url": "docs/ai-builder/prompting/breaking-up-complex-prompts",
    "description": "Breaking up complex prompts\n\nIncremental Prompting\n\nAsking for incremental, smaller changes leads to better results, rather than asking for everything all in a single huge prompt. It's better to take it step-by-step rather than give the AI complex tasks all at once.\n\nExample 1                      \nToo Complex:\n\nBetter Approach:\n\nPrompt 1: \n\nPrompt 2: \n\nPrompt 3: \n\nPrompt 4: \n\nPrompt 5: \n\nPrompt 6: \n\nExample 2                 \nToo Complex:\n\nBetter Approach:\n\nPrompt 1: \n\nPrompt 2: \n\nPrompt 3: \n\nPrompt 4: \n\nPrompt 5:"
  },
  {
    "name": "Download App",
    "parts": [
      "AI Builder",
      "Features",
      "Download App"
    ],
    "url": "docs/ai-builder/features/download-app",
    "description": "Download your App\n\nIt is easy to download your app to work on locally or self-host. (It is recommended to use the GitHub integration, but if this is not possible, you can download your app to work on locally.) \n\nSimply click the  button in the bottom right corner of Reflex Build, as shown below:"
  },
  {
    "name": "Image As Prompt",
    "parts": [
      "AI Builder",
      "Features",
      "Image As Prompt"
    ],
    "url": "docs/ai-builder/features/image-as-prompt",
    "description": "Use Images as a prompt\n\nUploading an image (screenshot) of a website (web) app of what you are looking to build gives the AI really good context. \n\n*This is the recommended way to start an app generation.*\n\nBelow is a GIF showing how to upload an image to the AI Builder:\n\nThe advised prompt to use is:"
  },
  {
    "name": "Ide",
    "parts": [
      "AI Builder",
      "Features",
      "Ide"
    ],
    "url": "docs/ai-builder/features/ide",
    "description": "Reflex Build's IDE\n\nReflex Build includes a powerful, in-browser IDE designed to streamline the entire development process—from writing code\nto deploying your app. With an intuitive layout, real-time editing, and seamless integration with the rest of the\nplatform, the IDE empowers users to stay focused and productive without ever leaving the browser.\n\n<div class=\"p-1 my-4 rounded-lg bg-slate-5\">\n  <iframe\n    width=\"100%\"\n    height=\"400\"\n    src=\"https://www.youtube.com/embed/aW0ZefEC3SU \"\n    title=\"Reflex Build - IDE\"\n    frameborder=\"0\"\n    allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\"\n    allowfullscreen>\n  </iframe>\n</div>\n\nIDE Features\n\nReal-Time Editing\n\nChanges you make in the editor are immediately reflected across your project—no manual saves or rebuilds required. Stay in flow and iterate faster.\n\nFile & Folder Management\n\nEasily create, rename, or delete files and folders directly in the workspace. The file tree gives you full visibility into your application structure at all times.\n\nDrag-and-Drop File Upload\n\nSeamlessly import files into your project by dragging them straight into the editor. Whether you're adding assets, scripts, or config files, it's fast and intuitive—no extra clicks required.\n\nContext-Aware Code Editor\n\nThe built-in code editor supports syntax highlighting, inline error detection, and AI-assisted suggestions to help you write clean, efficient code with confidence.\n\nOne-Click Deployment\n\nFrom the IDE, you can deploy your app with a single click. No terminal, no external tools—just build and ship straight from your browser."
  },
  {
    "name": "Templates",
    "parts": [
      "AI Builder",
      "Features",
      "Templates"
    ],
    "url": "docs/ai-builder/features/templates",
    "description": "Templates\n\nReflex has many certified templates, seen on the  tab of the Reflex Build, that can be used to kickstart your app. You can also use any app created by the community as a template. \n\nUsing a Template\n\nTo use a template, simply click the template and then in the bottom right corner of the app click the  button. This will create a copy of the template in your own account. You can then edit the app as you like with further prompting.\n\nBelow is an example of how to use a template:\n\nTemplates are great to get started if they have similar UI to what you are looking to build. You can then add your own data to the app."
  },
  {
    "name": "Deploy App",
    "parts": [
      "AI Builder",
      "Features",
      "Deploy App"
    ],
    "url": "docs/ai-builder/features/deploy-app",
    "description": "Deploy your App\n\nIt is easy to deploy your app into production from Reflex Build to Reflex Cloud. \n\nSimply click the  button in the bottom right corner of Reflex Build, as shown below:\n\nWhen deploying you can set the following options:\n- **App Name**: The name of your app\n- **Hostname**: Set your url by setting your hostname, i.e. if you set  as your hostname, your app will be available at \n- **Region**: The regions where your app will be deployed\n- **VM Size**: The size of the VM where your app will be deployed\n- **Secrets**: The environment variables that will be set for your app, you can load the variables currently being used by your app by clicking the  button"
  },
  {
    "name": "Environment Variables",
    "parts": [
      "AI Builder",
      "Features",
      "Environment Variables"
    ],
    "url": "docs/ai-builder/features/environment-variables",
    "description": "Environment Variables (Secrets)\n\nIt is possible to add environment variables to your app. This is useful for storing secrets such as API keys, and other sensitive information.\n\nAdding Environment Variables\n\nYou can add environment variables to your app by clicking the  button at the bottom of the chat input box, as seen below:\n\nAfter you add the environment variables the AI now has context of these and you can prompt it to use them in your code.\n\nYou can also add environment variables after your app is built, by again clicking the  button at the bottom of the chat input box on the generation page."
  },
  {
    "name": "Installing External Packages",
    "parts": [
      "AI Builder",
      "Features",
      "Installing External Packages"
    ],
    "url": "docs/ai-builder/features/installing-external-packages",
    "description": "Installing External Packages\n\nReflex Build allows you to install external python packages to use in your app. This is useful if you want to use a package that is not included in the default Reflex Build environment. Examples might include , , , etc.\n\nThere are two ways to install external packages:\n\n1. **Through the Chat Interface**: You can ask the AI to install a package for you.\n2. **Add to the  file**: You can add the package to the  file and then save the app. This will install the package in your app's environment.\n\nInstalling through the Chat Interface\n\nEnter the name of the package you want to install in the chat interface. The AI will then install the package for you.\n\nInstalling through the requirements.txt file\n\nAdd the package to the  file and then save the app. This will install the package in your app's environment and recompile your app."
  },
  {
    "name": "Github",
    "parts": [
      "AI Builder",
      "Integrations",
      "Github"
    ],
    "url": "docs/ai-builder/integrations/github",
    "description": "Connecting to Github\n\nThe Github integration is important to make sure that you don't lose your progress. It also allows you to revert to previous versions of your app. \n\nThe GitHub integration allows you to:\n\n- Save your app progress\n- Work on your code locally and push your local changes back to Reflex.Build\n\nGithub Commit History\n\nThe commit history is a great way to see the changes that you have made to your app. You can also revert to previous versions of your app from here."
  },
  {
    "name": "Frequently Asked Questions",
    "parts": [
      "AI Builder",
      "Overview",
      "Frequently Asked Questions"
    ],
    "url": "docs/ai-builder/overview/frequently-asked-questions",
    "description": "FAQs\n\nStill to come!"
  },
  {
    "name": "What Is Reflex Build",
    "parts": [
      "AI Builder",
      "Overview",
      "What Is Reflex Build"
    ],
    "url": "docs/ai-builder/overview/what-is-reflex-build",
    "description": "What Is Reflex Build\n\n<div class=\"p-1 my-4 rounded-lg bg-slate-5\">\n  <iframe\n    width=\"100%\"\n    height=\"400\"\n    src=\"https://www.youtube.com/embed/s-kr8v7827g \"\n    title=\"Reflex Build\"\n    frameborder=\"0\"\n    allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\"\n    allowfullscreen>\n  </iframe>\n</div>\n\nReflex Build is an AI-powered platform that empowers users of all skill levels to create full-stack web applications\nwithout writing any code—just by describing their ideas in plain English. Instead of hiring developers, users can\ninstantly generate web apps or websites, turning ideas into functional apps as quickly as possible.\n\nReflex Build provides everything you need to create stunning websites, front-end interfaces, and full-stack web\napplications—all from a single browser tab, with no installation required. It includes AI-powered coding tools,\nreal-time collaboration (currently in beta), and easy project sharing to give you a head start on your app development\njourney.\n\nFeature Overview\n\nReflex Build provides a streamlined interface for building AI applications. The **Project Menu Bar** helps you manage sessions and stored variables, while the **Chat Area** displays real-time prompts, edits, and file generations. The **Application Workspace** organizes your project structure, and the **Code Editor** allows direct, instant code editing. Key actions like deploy and share are accessible via the **Bottom Menu Bar**, and the **Preview Tab** lets you view and interact with your live app at any time.\n\nInterface Highlights\n\nReflex Build’s interface is designed for clarity and efficiency. The **Project Menu Bar** helps you manage sessions, apps, and variables. The **Chat Area** shows prompts in action with visual feedback and file generation. In the **Application Workspace**, you can view and organize your project files. The **Code Editor** allows quick, direct edits with instant saving. Use the **Bottom Menu Bar** for key actions like deploy and download. The **Preview Tab** lets you interact with a live version of your app, including refresh and full-screen options."
  },
  {
    "name": "Database",
    "parts": [
      "AI Builder",
      "Integrations",
      "Database"
    ],
    "url": "docs/ai-builder/integrations/database",
    "description": "Connecting to a Database\n\nConnecting to a database is critical to give your app access to real data. This section will cover how to connect to a database using the AI Builder. \n\nTo connect to a database you will need a . Reflex.build currently supports  and  databases.\n\nThis is what it looks like for a Postgres database:\n\nYou can also use a MySQL database. The connection string looks like this:\n\nConnecting your Database before the app is generated\n\nYou can add your  at the start of your generation as shown below. \n\nHere if you wanted to build a dashboard for example we recommend a prompt as follows: \n\nConnecting your Database after the app is generated\n\nYou can add your  after you've already generated an app or directly from a template that you have forked as shown below.\n\nHere if you wanted to hook up your data correctly we recommend a prompt as follows:"
  },
  {
    "name": "Quickstart",
    "parts": [
      "AI Builder",
      "Overview",
      "Quickstart"
    ],
    "url": "docs/ai-builder/overview/quickstart",
    "description": "Quickstart\n\nStill to come!"
  },
  {
    "name": "Overview",
    "parts": [
      "State",
      "Overview"
    ],
    "url": "docs/state/overview",
    "description": "State\n\nState allows us to create interactive apps that can respond to user input.\nIt defines the variables that can change over time, and the functions that can modify them.\n\nState Basics\n\nYou can define state by creating a class that inherits from :\n\nA state class is made up of two parts: vars and event handlers.\n\n**Vars** are variables in your app that can change over time.\n\n**Event handlers** are functions that modify these vars in response to events.\n\nThese are the main concepts to understand how state works in Reflex:\n\nExample\n\nHere is a example of how to use state within a Reflex app.\nClick the text to change its color.\n\nThe base vars are  and . They are the only vars in the app that\nmay be directly modified within event handlers.\n\nThere is a single computed var, , that is a function of the base vars. It\nwill be computed automatically whenever the base vars change.\n\nThe heading component links its  event to the\n event handler, which increments the color index.\n\nClient States\n\nEach user who opens your app has a unique ID and their own copy of the state.\nThis means that each user can interact with the app and modify the state\nindependently of other users.\n\nBecause Reflex internally creates a new instance of the state for each user, your code should\nnever directly initialize a state class.\n\nAll user state is stored on the server, and all event handlers are executed on\nthe server. Reflex uses websockets to send events to the server, and to send\nstate updates back to the client.\n\nHelper Methods\n\nSimilar to backend vars, any method defined in a State class that begins with an\nunderscore  is considered a helper method. Such methods are not usable as\nevent triggers, but may be called from other event handler methods within the\nstate.\n\nFunctionality that should only be available on the backend, such as an\nauthenticated action, should use helper methods to ensure it is not accidentally\nor maliciously triggered by the client."
  },
  {
    "name": "Component State",
    "parts": [
      "State Structure",
      "Component State"
    ],
    "url": "docs/state-structure/component-state",
    "description": "Component State\n\n_New in version 0.4.6_.\n\nDefining a subclass of  creates a special type of state that is tied to an\ninstance of a component, rather than existing globally in the app. A Component State combines\nUI code with state Vars and\nEvent Handlers,\nand is useful for creating reusable components which operate independently of each other.\n\nUsing ComponentState\n\nThe vars and event handlers defined on the \nclass are treated similarly to a normal State class, but will be scoped to the component instance. Each time a\n is created, a new state class for that instance of the component is also created.\n\nThe  classmethod is used to define the UI for the component and link it up to the State, which\nis accessed via the  argument. Other states may also be referenced by the returned component, but\n will always be the instance of the  that is unique to the component being returned.\n\nPassing Props\n\nSimilar to a normal Component, the  classmethod accepts the arbitrary\n and  arguments, and by default passes them to your  classmethod.\nThese arguments may be used to customize the component, either by applying defaults or\npassing props to certain subcomponents.\n\nIn the following example, we implement an editable text component that allows the user to click on\nthe text to turn it into an input field. If the user does not provide their own  or \nprops, then the defaults defined in the  class will be used.\n\nBecause this  component is designed to be reusable, it can handle the case\nwhere the  and  are linked to a normal global state.\n\nAccessing the State\n\nThe underlying state class of a  is accessible via the  attribute. To use it,\nassign an instance of the component to a local variable, then include that instance in the page.\n\nOther components can also affect a  by referencing its event handlers or vars\nvia the  attribute."
  },
  {
    "name": "Html To Reflex",
    "parts": [
      "Components",
      "Html To Reflex"
    ],
    "url": "docs/components/html-to-reflex",
    "description": "Convert HTML to Reflex\n\nTo convert HTML, CSS, or any design into Reflex code, use our AI-powered build tool at Reflex Build.\n\nSimply paste your HTML, CSS, or describe what you want to build, and our AI will generate the corresponding Reflex code for you.\n\nHow to use Reflex Build\n\n1. Go to Reflex Build\n2. Paste your HTML/CSS code or describe your design\n3. The AI will automatically generate Reflex code\n4. Copy the generated code into your Reflex application\n\nConvert Figma file to Reflex\n\nCheck out this Notion doc for a walk through on how to convert a Figma file into Reflex code."
  },
  {
    "name": "Overview",
    "parts": [
      "State Structure",
      "Overview"
    ],
    "url": "docs/state-structure/overview",
    "description": "Substates\n\nSubstates allow you to break up your state into multiple classes to make it more manageable. This is useful as your app\ngrows, as it allows you to think about each page as a separate entity. Substates also allow you to share common state\nresources, such as variables or event handlers.\n\nWhen a particular state class becomes too large, breaking it up into several substates can bring performance\nbenefits by only loading parts of the state that are used to handle a certain event.\n\nMultiple States\n\nOne common pattern is to create a substate for each page in your app.\nThis allows you to think about each page as a separate entity, and makes it easier to manage your code as your app grows.\n\nTo create a substate, simply inherit from  multiple times:\n\nSeparating the states is purely a matter of organization. You can still access the state from other pages by importing the state class.\n\nAccessing Arbitrary States\n\nAn event handler in a particular state can access and modify vars in another state instance by calling\nthe  async method and passing the desired state class. If the requested state is not already loaded,\nit will be loaded and deserialized on demand.\n\nIn the following example, the  accesses the  to get the  and uses it\nto update the  var.\n\nNotably, the widget that sets the salutation does NOT have to load the  when handling the\ninput  event, which improves performance.\n\nAccessing Individual Var Values\n\nIn addition to accessing entire state instances with , you can retrieve individual variable values using the  method:\n\nThis async method is particularly useful when you only need a specific value rather than loading the entire state. Using  can be more efficient than  when:\n\n1. You only need to access a single variable from another state\n2. The other state contains a large amount of data\n3. You want to avoid loading unnecessary data into memory\n\nHere's an example that demonstrates how to use  to access data between states:\n\nIn this example:\n1. We have two separate states:  which manages a counter, and  which displays information\n2. When you click \"Increment\", it calls  to increase the counter value\n3. When you click \"Show Count\", it calls  which uses  to retrieve just the count value from  without loading the entire state\n4. The current count is then displayed in the message\n\nThis pattern is useful when you have multiple states that need to interact with each other but don't need to access all of each other's data.\n\nIf the var is not retrievable,  will raise an .\n\nPerformance Implications\n\nWhen an event handler is called, Reflex will load the data not only for the substate containing\nthe event handler, but also all of its substates and parent states as well.\nIf a state has a large number of substates or contains a large amount of data, it can slow down processing\nof events associated with that state.\n\nFor optimal performance, keep a flat structure with most substate classes directly inheriting from .\nOnly inherit from another state when the parent holds data that is commonly used by the substate.\nImplementing different parts of the app with separate, unconnected states ensures that only the necessary\ndata is loaded for processing events for a particular page or component.\n\nAvoid defining computed vars inside a state that contains a large amount of data, as\nstates with computed vars are always loaded to ensure the values are recalculated.\nWhen using computed vars, it better to define them in a state that directly inherits from  and\ndoes not have other states inheriting from it, to avoid loading unnecessary data."
  },
  {
    "name": "Props",
    "parts": [
      "Components",
      "Props"
    ],
    "url": "docs/components/props",
    "description": "Props\n\nProps modify the behavior and appearance of a component. They are passed in as keyword arguments to a component.\n\nComponent Props\n\nThere are props that are shared between all components, but each component can also define its own props.\n\nFor example, the  component has a  prop that specifies the URL of the image to display and an  prop that specifies the alternate text for the image.\n\nCheck the docs for the component you are using to see what props are available and how they affect the component (see the  reference page for example).\n\nCommon Props\n\nComponents support many standard HTML properties as props. For example: the HTML id property is exposed directly as the prop . The HTML className property is exposed as the prop  (note the Pythonic snake_casing!).\n\nIn the example above, the  prop of the  component is assigned a list of class names. This means the  component will be styled with the CSS classes  and .\n\nStyle Props\n\nIn addition to component-specific props, most built-in components support a full range of style props. You can use any CSS property to style a component.\n\nSee the styling docs to learn more about customizing the appearance of your app.\n\nBinding Props to State\n\nReflex apps define State classes that hold variables that can change over time.\n\nState may be modified in response to things like user input like clicking a button, or in response to events like loading a page.\n\nState vars can be bound to component props, so that the UI always reflects the current state of the app.\n\nTry clicking the badge below to change its color.\n\nIn this example, the  prop is bound to the  state var.\n\nWhen the  event handler is called, the  var is updated, and the  prop is updated to match."
  },
  {
    "name": "Rendering Iterables",
    "parts": [
      "Components",
      "Rendering Iterables"
    ],
    "url": "docs/components/rendering-iterables",
    "description": "Rendering Iterables\n\nRecall again from the basics that we cannot use Python  loops when referencing state vars in Reflex. Instead, use the  component to render components from a collection of data.\n\nFor dynamic content that should automatically scroll to show the newest items, consider using the auto scroll component together with .\n\nHere's the same example using a lambda function.\n\nYou can also use lambda functions directly with components without defining a separate function.\n\nIn this first simple example we iterate through a  of colors and render a dynamic number of buttons.\n\nThe first argument of the  function is the state var that you want to iterate through. The second argument is a function that takes in an item from the data and returns a component. In this case, the  function takes in a color and returns a button with that color.\n\nFor vs Foreach\n\nThe above example could have been written using a regular Python  loop, since the data is constant.\n\nHowever, as soon as you need the data to be dynamic, you must use .\n\nRender Function\n\nThe function to render each item can be defined either as a separate function or as a lambda function. In the example below, we define the function  separately and pass it to the  function. \n\nNotice that the type annotation for the  parameter in the  function is  (rather than just ). This is because the  function passes the item as a  object, which is a wrapper around the actual value. This is what allows us to compile the frontend without knowing the actual value of the state var (which is only known at runtime).\n\nEnumerating Iterables\n\nThe function can also take an index as a second argument, meaning that we can enumerate through data as shown in the example below.\n\nHere's the same example using a lambda function.\n\nIterating Dictionaries\n\nWe can iterate through a  using a . When the dict is passed through to the function that renders each item, it is presented as a list of key-value pairs .\n\nNested examples\n\n can be used with nested state vars. Here we use nested  components to render the nested state vars. The  inside of the  function, renders the  values which are of type . The  inside of the  function renders each  inside of the overall state var .\n\nIf you want an example where not all of the values in the dict are the same type then check out the example on var operations using foreach.\n\nHere is a further example of how to use  with a nested data structure.\n\nForeach with Cond\n\nWe can also use  with the  component.\n\nIn this example we define the function . This function takes in an , uses the  to check if the item . If it is packed it returns the  with a  next to it, and if not then it just returns the . We use the  to iterate over all of the items in the  using the  function."
  },
  {
    "name": "Overview",
    "parts": [
      "API Routes",
      "Overview"
    ],
    "url": "docs/api-routes/overview",
    "description": "API Transformer\n\nIn addition to your frontend app, Reflex uses a FastAPI backend to serve your app. The API transformer feature allows you to transform or extend the ASGI app that serves your Reflex application.\n\nOverview\n\nThe API transformer provides a way to:\n\n1. Integrate existing FastAPI or Starlette applications with your Reflex app\n2. Apply middleware or transformations to the ASGI app\n3. Extend your Reflex app with additional API endpoints\n\nThis is useful for creating a backend API that can be used for purposes beyond your Reflex app, or for integrating Reflex with existing backend services.\n\nUsing API Transformer\n\nYou can set the  parameter when initializing your Reflex app:\n\nTypes of API Transformers\n\nThe  parameter can accept:\n\n1. A Starlette or FastAPI instance\n2. A callable that takes an ASGIApp and returns an ASGIApp\n3. A sequence of the above\n\nUsing a FastAPI or Starlette Instance\n\nWhen you provide a FastAPI or Starlette instance as the API transformer, Reflex will mount its internal API to your app, allowing you to define additional routes:\n\nUsing a Callable Transformer\n\nYou can also provide a callable that transforms the ASGI app:\n\nUsing Multiple Transformers\n\nYou can apply multiple transformers by providing a sequence:\n\nReserved Routes\n\nSome routes on the backend are reserved for the runtime of Reflex, and should not be overridden unless you know what you are doing.\n\nPing\n\n: You can use this route to check the health of the backend.\n\nThe expected return is .\n\nEvent\n\n: the frontend will use this route to notify the backend that an event occurred.\n\nUpload\n\n: This route is used for the upload of file when using ."
  },
  {
    "name": "Conditional Rendering",
    "parts": [
      "Components",
      "Conditional Rendering"
    ],
    "url": "docs/components/conditional-rendering",
    "description": "Conditional Rendering\n\nRecall from the basics that we cannot use Python  statements when referencing state vars in Reflex. Instead, use the  component to conditionally render components or set props based on the value of a state var.\n\nBelow is a simple example showing how to toggle between two text components by checking the value of the state var .\n\nIf  is  then the first component is rendered (in this case the blue text). Otherwise the second component is rendered (in this case the red text).\n\nConditional Props\n\nYou can also set props conditionally using . In this example, we set the  prop of a text component based on the value of the state var .\n\nVar Operations\n\nYou can use var operations with the  component for more complex conditions. See the full cond reference for more details.\n\nMultiple Conditional Statements\n\nThe []({library.dynamic_rendering.match.path}) component in Reflex provides a powerful alternative to for handling multiple conditional statements and structural pattern matching. This component allows you to handle multiple conditions and their associated components in a cleaner and more readable way compared to nested  structures."
  },
  {
    "name": "More Wrapping Examples",
    "parts": [
      "Wrapping React",
      "More Wrapping Examples"
    ],
    "url": "docs/wrapping-react/more-wrapping-examples",
    "description": "More React Libraries \n\nAG Charts\n\nHere we wrap the AG Charts library from the NPM package ag-charts-react. \n\nIn the react code below we can see the first  lines are importing React and ReactDOM, and this can be ignored when wrapping your component.\n\nWe import the  component from the  library on line 5. In Reflex this is wrapped by  and .\n\nLine  defines a functional React component, which on line  returns  which is similar in the Reflex code to using the  component.\n\nLine  uses the  hook to create a state variable  and its setter function  (equivalent to the event handler  in reflex). The initial state variable is of type dict and has two key value pairs  and . \n\nWhen we see  in React code, it correlates to state variables in your State. As you can see in our Reflex code we have a state variable  which is a dictionary, like in our React code.\n\nMoving to line  we see that the  has a prop . In order to use this in Reflex we must wrap this prop. We do this with  in the  component. \n\nLines  and  are rendering the component inside the root element. This can be ignored when we are wrapping a component as it is done in Reflex by creating an  function and adding it to the app.\n\n---md tabs\n\n--tab React Code    \n\n--\n--tab Reflex Code\n\n--\n\n---\n\nReact Leaflet\n\nIn this example we are wrapping the React Leaflet library from the NPM package react-leaflet.\n\nOn line  we import the  function from Next.js and on line  we set . Lines  and  use the  function to import the  and  components from the  library. This is used to dynamically import the  and  components from the  library. This is done in Reflex by using the  class when defining the component. There is more information of when this is needed on the  section of this page.\n\nIt mentions in the documentation that it is necessary to include the Leaflet CSS file, which is added on line  in the React code below. This can be done in Reflex by using the  method in the  component. We can add a relative path from within the React library or a full URL to the CSS file.\n\nLine  defines a functional React component, which on line  returns the  which is done in the Reflex code using the  component.\n\nThe  component has props , , , which we wrap in the  component in the Reflex code. We ignore the  prop as it is a reserved name in Reflex. We can use the  method to change the name of the prop, as we will see in the React PDF Renderer example, but in this case we just ignore it and add the  and  props as css in Reflex.\n\nThe  component has a prop  which we wrap in the  component in the Reflex code.\n\nLines  and  defines and exports a React functional component named  which returns the  component. This can be ignored in the Reflex code when wrapping the component as we return the  component in the  function.\n\n---md tabs\n\n--tab React Code \n\n--\n--tab Reflex Code\n\n--\n\n---\n\nReact PDF Renderer\n\nIn this example we are wrapping the React renderer for creating PDF files on the browser and server from the NPM package @react-pdf/renderer.\n\nThis example is similar to the previous examples, and again Dynamic Imports are required for this library. This is done in Reflex by using the  class when defining the component. There is more information on why this is needed on the  section of this page.\n\nThe main difference with this example is that the  prop, used on lines ,  and  in React code, is a reserved name in Reflex so can not be wrapped. A different name must be used when wrapping this prop and then this name must be changed back to the original with the  method. In this example we name the prop  in our Reflex code and then change it back to  with the  method in both the  and  components.\n\n---md tabs\n\n--tab React Code    \n\n--\n--tab Reflex Code\n\n--\n\n---"
  },
  {
    "name": "Local Packages",
    "parts": [
      "Wrapping React",
      "Local Packages"
    ],
    "url": "docs/wrapping-react/local-packages",
    "description": "---\ntitle: Wrapping Local Packages\n---\n\nAssets\n\nIf a wrapped component depends on assets such as images, scripts, or\nstylesheets, these can be kept adjacent to the component code and\nincluded in the final build using the  function.\n\n returns a relative path that references the asset in the compiled\noutput. The target files are copied into a subdirectory of \nbased on the module where they are initially used. This allows third-party\ncomponents to have external assets with the same name without conflicting\nwith each other.\n\nFor example, if there is an SVG file named  in the same directory as\nthis component, it can be rendered using  and .\n\nLocal Components\n\nYou can also wrap components that you have written yourself. For local components (when the code source is directly in the project), we recommend putting it beside the files that is wrapping it.\n\nYou can then use the path obtained via  to reference the component path.\n\nSo if you create a file called  in the same directory as the component with this content:\n\nYou can specify the library as follow (note: we use the  directory here instead of  as this is the directory that is served by the web server):\n\nLocal Packages\n\nIf the component is part of a local package, available on Github, or\ndownloadable via a web URL, it can also be wrapped in Reflex. Specify the path\nor URL after an  following the package name.\n\nAny local paths are relative to the  folder, so you can use  prefix\nto reference the Reflex project root.\n\nSome examples of valid specifiers for a package called \n[](https://github.com/masenf/hello-react) are:\n\n* GitHub: \n* URL: \n* Local Archive: \n* Local Directory: \n\nIt is important that the package name matches the name in  so\nReflex can generate the correct import statement in the generated javascript\ncode.\n\nThese package specifiers can be used for  or .\n\nAlthough more complicated, this approach is useful when the local components\nhave additional dependencies or build steps required to prepare the component\nfor use.\n\nSome important notes regarding this approach:\n\n* The repo or archive must contain a  file.\n*  or  scripts will NOT be executed. The distribution archive,\n  directory, or repo must already contain the built javascript files (this is common).\n\njson\n{\n  // ...,\n  \"exports\": {\n    \".\": {\n      \"import\": \"./dist/index.js\",\n      \"require\": \"./dist/index.umd.cjs\"\n    },\n    \"./dist/style.css\": {\n      \"import\": \"./dist/style.css\",\n      \"require\": \"./dist/style.css\"\n    }\n  },\n  // ...\n}\n```"
  },
  {
    "name": "Overview",
    "parts": [
      "Wrapping React",
      "Overview"
    ],
    "url": "docs/wrapping-react/overview",
    "description": "Wrapping React\n\nOne of Reflex's most powerful features is the ability to wrap React components and take advantage of the vast ecosystem of React libraries.\n\nIf you want a specific component for your app but Reflex doesn't provide it, there's a good chance it's available as a React component. Search for it on npm, and if it's there, you can use it in your Reflex app. You can also create your own local React components and wrap them in Reflex.\n\nOnce you wrap your component, you publish it to the Reflex library so that others can use it.\n\nSimple Example\n\nSimple components that don't have any interaction can be wrapped with just a few lines of code. \n\nBelow we show how to wrap the Spline library can be used to create 3D scenes and animations.\n\nColorPicker Example\n\nSimilar to the Spline example we start with defining the library and tag. In this case the library is  and the tag is .\n\nWe also have a var  which is the current color of the color picker.\n\nSince this component has interaction we must specify any event triggers that the component takes. The color picker has a single trigger  to specify when the color changes. This trigger takes in a single argument  which is the new color.\n\nWhat Not To Wrap\n\nThere are some libraries on npm that are not do not expose React components and therefore are very hard to wrap with Reflex. \n\nA library like spline below is going to be difficult to wrap with Reflex because it does not expose a React component.\n\nYou should look out for JSX, a syntax extension to JavaScript, which has angle brackets . If you see JSX, it's likely that the library is a React component and can be wrapped with Reflex. \n\nIf the library does not expose a react component you need to try and find a JS React wrapper for the library, such as react-spline.\n\nIn the next page, we will go step by step through a more complex example of wrapping a React component."
  },
  {
    "name": "Step By Step",
    "parts": [
      "Wrapping React",
      "Step By Step"
    ],
    "url": "docs/wrapping-react/step-by-step",
    "description": ""
  },
  {
    "name": "Example",
    "parts": [
      "Wrapping React",
      "Example"
    ],
    "url": "docs/wrapping-react/example",
    "description": "Complex Example\n\nIn this more complex example we will be wrapping  a library for building node based applications like flow charts, diagrams, graphs, etc.\n\nImport\n\nLets start by importing the library reactflow. Lets make a separate file called  and add the following code:\n\nNotice we also use the  method to import the css file that is needed for the styling of the library.\n\nComponents\n\nFor this tutorial we will wrap three components from Reactflow: , , and . Lets start with the  component.\n\nHere we will define the  and the  that we will need to use the component.\n\nFor this tutorial we will define  props  and , but you can find all the events that the component triggers in the reactflow docs.\n\nNow lets add the  and  components. We will also create the components using the  method so that we can use them in our app.\n\nBuilding the App\n\nNow that we have our components lets build the app.\n\nLets start by defining the initial nodes and edges that we will use in our app.\n\nNext we will define the state of our app. We have four event handlers: , ,  and .\n\nThe  event handler is triggered when a node is selected and dragged. This function is used to update the position of a node during dragging. It takes a single argument , which is a list of dictionaries containing various types of metadata. For updating positions, the function specifically processes changes of type .\n\nNow lets define the UI of our app. We will use the  component and pass in the  and  from our state. We will also add the  event handler to the  component to handle when an edge is connected.\n\nHere is an example of the app running:"
  },
  {
    "name": "Library And Tags",
    "parts": [
      "Wrapping React",
      "Library And Tags"
    ],
    "url": "docs/wrapping-react/library-and-tags",
    "description": "---\ntitle: Library and Tags\n---\n\nFind The Component\n\nThere are two ways to find a component to wrap:\n1. Write the component yourself locally.\n2. Find a well-maintained React library on npm that contains the component you need.\n\nIn both cases, the process of wrapping the component is the same except for the  field.\n\nWrapping the Component\n\nTo start wrapping your React component, the first step is to create a new component in your Reflex app. This is done by creating a new class that inherits from  or . \n\nSee the API Reference for more details on the  class.\n\nThis is when we will define the most important attributes of the component:\n1. **library**: The name of the npm package that contains the component.\n2. **tag**: The name of the component to import from the package.\n3. **alias**: (Optional) The name of the alias to use for the component. This is useful if multiple component from different package have a name in common. If  is not specified,  will be used.\n4. **lib_dependencies**: Any additional libraries needed to use the component.\n5. **is_default**: (Optional) If the component is a default export from the module, set this to . Default is .\n\nOptionally, you can override the default component creation behavior by implementing the  class method. Most components won't need this when props are straightforward conversions from Python to JavaScript. However, this is useful when you need to add custom initialization logic, transform props, or handle special cases when the component is created.\n\nWrapping a Dynamic Component \n\nWhen wrapping some libraries, you may want to use dynamic imports. This is because they may not be compatible with Server-Side Rendering (SSR).\n\nTo handle this in Reflex, subclass  when defining your component. It works the same as , but it will automatically add the correct custom code for a dynamic import.\n\nOften times when you see an import something like this:\n\nYou can wrap it in Reflex like this:\n\nIt may not always be clear when a library requires dynamic imports. A few things to keep in mind are if the component is very client side heavy i.e. the view and structure depends on things that are fetched at run time, or if it uses  or  objects directly it will need to be wrapped as a . \n\nSome examples are:\n\n1. Video and Audio Players\n2. Maps\n3. Drawing Canvas\n4. 3D Graphics\n5. QR Scanners\n6. Reactflow\n\nThe reason for this is that it does not make sense for your server to render these components as the server does not have access to your camera, it cannot draw on your canvas or render a video from a file. \n\nIn addition, if in the component documentation it mentions nextJS compatibility or server side rendering compatibility, it is a good sign that it requires dynamic imports.\n\nAdvanced - Parsing a state Var with a JS Function\nWhen wrapping a component, you may need to parse a state var by applying a JS function to it. \n\nDefine the parsing function\n\nFirst you need to define the parsing function by writing it in .\n\nApply the parsing function to your props\n\nThen, you can apply the parsing function to your props in the  method."
  },
  {
    "name": "Props",
    "parts": [
      "Wrapping React",
      "Props"
    ],
    "url": "docs/wrapping-react/props",
    "description": "---\ntitle: Props - Wrapping React \n---\n\nProps\n\nWhen wrapping a React component, you want to define the props that will be accepted by the component.\nThis is done by defining the props and annotating them with a .\n\nBroadly, there are three kinds of props you can encounter when wrapping a React component:\n1. **Simple Props**: These are props that are passed directly to the component. They can be of any type, including strings, numbers, booleans, and even lists or dictionaries.\n2. **Callback Props**: These are props that expect to receive a function. That function will usually be called by the component as a callback. (This is different from event handlers.)\n3. **Component Props**: These are props that expect to receive a components themselves. They can be used to create more complex components by composing them together.\n4. **Event Handlers**: These are props that expect to receive a function that will be called when an event occurs. They are defined as  with a signature function to define the spec of the event.\n\nSimple Props\n\nSimple props are the most common type of props you will encounter when wrapping a React component. They are passed directly to the component and can be of any type (but most commonly strings, numbers, booleans, and structures).\n\nFor custom types, you can use  to define the structure of the custom types. However, if you need the attributes to be automatically converted to camelCase once compiled in JS, you can use  instead of .\n\nCallback Props\n\nCallback props are used to handle events or to pass data back to the parent component. They are defined as  with a type of  or .\n\nComponent Props\nSome components will occasionally accept other components as props, usually annotated as . In Reflex, these are defined as .\n\nEvent Handlers\nEvent handlers are props that expect to receive a function that will be called when an event occurs. They are defined as  with a signature function to define the spec of the event."
  },
  {
    "name": "Custom Code And Hooks",
    "parts": [
      "Wrapping React",
      "Custom Code And Hooks"
    ],
    "url": "docs/wrapping-react/custom-code-and-hooks",
    "description": "When wrapping a React component, you may need to define custom code or hooks that are specific to the component. This is done by defining the or  methods in your component class.\n\nCustom Code\n\nCustom code is any JS code that need to be included in your page, but not necessarily in the component itself. This can include things like CSS styles, JS libraries, or any other code that needs to be included in the page.\n\nThe above example will render the following JS code in the page:\n\nCustom Hooks\nCustom hooks are any hooks that need to be included in your component. This can include things like , , or any other hooks from the library you are wrapping.\n\n- Simple hooks can be added as strings.\n- More complex hooks that need to have special import or be written in a specific order can be added as  with a  object to specify the position of the hook.\n    - The  attribute of the  object can be used to specify any imports that need to be included in the component.\n    - The  attribute of the  object can be set to  or  to specify the position of the hook in the component.\n\nThe  will be rendered in the component in the following way:"
  },
  {
    "name": "Imports And Styles",
    "parts": [
      "Wrapping React",
      "Imports And Styles"
    ],
    "url": "docs/wrapping-react/imports-and-styles",
    "description": "Styles and Imports\n\nWhen wrapping a React component, you may need to define styles and imports that are specific to the component. This is done by defining the  and  methods in your component class.\n\nImports\n\nSometimes, the component you are wrapping will need to import other components or libraries. This is done by defining the  method in your component class.\nThat method should return a dictionary of imports, where the keys are the names of the packages to import and the values are the names of the components or libraries to import.\n\nValues can be either a string or a list of strings. If the import needs to be aliased, you can use the  object to specify the alias and whether the import should be installed as a dependency.\n\nStyles\n\nStyles are any CSS styles that need to be included in the component. The style will be added inline to the component, so you can use any CSS styles that are valid in React."
  },
  {
    "name": "Login Form",
    "parts": [
      "Recipes",
      "Auth",
      "Login Form"
    ],
    "url": "docs/recipes/auth/login-form",
    "description": "Login Form\n\nThe login form is a common component in web applications. It allows users to authenticate themselves and access their accounts. This recipe provides examples of login forms with different elements, such as third-party authentication providers.\n\nDefault\n\nIcons\n\nThird-party auth\n\nMultiple third-party auth"
  },
  {
    "name": "Serializers",
    "parts": [
      "Wrapping React",
      "Serializers"
    ],
    "url": "docs/wrapping-react/serializers",
    "description": "---\ntitle: Serializers\n---\n\nSerializers\n\nVars can be any type that can be serialized to JSON. This includes primitive types like strings, numbers, and booleans, as well as more complex types like lists, dictionaries, and dataframes.\n\nIn case you need to serialize a more complex type, you can use the  decorator to convert the type to a primitive type that can be stored in the state. Just define a method that takes the complex type as an argument and returns a primitive type. We use type annotations to determine the type that you want to serialize.\n\nFor example, the Plotly component serializes a plotly figure into a JSON string that can be stored in the state.\n\nWe can then define a var of this type as a prop in our component."
  },
  {
    "name": "Signup Form",
    "parts": [
      "Recipes",
      "Auth",
      "Signup Form"
    ],
    "url": "docs/recipes/auth/signup-form",
    "description": "Sign up Form\n\nThe sign up form is a common component in web applications. It allows users to create an account and access the application's features. This page provides a few examples of sign up forms that you can use in your application.\nDefault\n\nIcons\n\nThird-party auth\n\nMultiple third-party auth"
  },
  {
    "name": "Footer",
    "parts": [
      "Recipes",
      "Layout",
      "Footer"
    ],
    "url": "docs/recipes/layout/footer",
    "description": "Footer Bar\n\nA footer bar is a common UI element located at the bottom of a webpage. It typically contains information about the website, such as contact details and links to other pages or sections of the site.\n\nBasic\n\nNewsletter form\n\nThree columns"
  },
  {
    "name": "Dark Mode Toggle",
    "parts": [
      "Recipes",
      "Others",
      "Dark Mode Toggle"
    ],
    "url": "docs/recipes/others/dark-mode-toggle",
    "description": "Dark Mode Toggle\n\nThe Dark Mode Toggle component lets users switch between light and dark themes."
  },
  {
    "name": "Checkboxes",
    "parts": [
      "Recipes",
      "Others",
      "Checkboxes"
    ],
    "url": "docs/recipes/others/checkboxes",
    "description": "Smart Checkboxes Group\n\nA smart checkboxes group where you can track all checked boxes, as well as place a limit on how many checks are possible.\n\nRecipe\n\nThis recipe use a  for the checkboxes state tracking.\nAdditionally, the limit that prevent the user from checking more boxes than allowed with a computed var."
  },
  {
    "name": "Sidebar",
    "parts": [
      "Recipes",
      "Layout",
      "Sidebar"
    ],
    "url": "docs/recipes/layout/sidebar",
    "description": "Sidebar\n\nSimilar to a navigation bar, a sidebar is a common UI element found on the side of a webpage or application. It typically contains links to different sections of the site or app.\n\nBasic\n\nBottom user profile\n\nTop user profile"
  },
  {
    "name": "Speed Dial",
    "parts": [
      "Recipes",
      "Others",
      "Speed Dial"
    ],
    "url": "docs/recipes/others/speed-dial",
    "description": "Speed Dial\n\nA speed dial is a component that allows users to quickly access frequently used actions or pages. It is often used in the bottom right corner of the screen.\n\nVertical\n\nHorizontal\n\nVertical with text\n\nReveal animation\n\nMenu"
  },
  {
    "name": "Chips",
    "parts": [
      "Recipes",
      "Others",
      "Chips"
    ],
    "url": "docs/recipes/others/chips",
    "description": "Chips\n\nChips are compact elements that represent small pieces of information, such as tags or categories. They are commonly used to select multiple items from a list or to filter content.\n\nStatus\n\nSingle selection\n\nMultiple selection\n\nThis example demonstrates selecting multiple skills from a list. It includes buttons to add all skills, clear selected skills, and select a random number of skills."
  },
  {
    "name": "Pricing Cards",
    "parts": [
      "Recipes",
      "Others",
      "Pricing Cards"
    ],
    "url": "docs/recipes/others/pricing-cards",
    "description": "Pricing Cards\n\nA pricing card shows the price of a product or service. It typically includes a title, description, price, features, and a purchase button.\n\nBasic\n\nComparison cards"
  },
  {
    "name": "Forms",
    "parts": [
      "Recipes",
      "Content",
      "Forms"
    ],
    "url": "docs/recipes/content/forms",
    "description": "Forms\n\nForms are a common way to gather information from users. Below are some examples.\n\nFor more details, see the form docs page.\n\nEvent creation\n\nContact"
  },
  {
    "name": "Navbar",
    "parts": [
      "Recipes",
      "Layout",
      "Navbar"
    ],
    "url": "docs/recipes/layout/navbar",
    "description": "Navigation Bar\n\nA navigation bar, also known as a navbar, is a common UI element found at the top of a webpage or application.\nIt typically provides links or buttons to the main sections of a website or application, allowing users to easily navigate and access the different pages.\n\nNavigation bars are useful for web apps because they provide a consistent and intuitive way for users to navigate through the app.\nHaving a clear and consistent navigation structure can greatly improve the user experience by making it easy for users to find the information they need and access the different features of the app.\n\nBasic\n\nDropdown\n\nSearch bar\n\nIcons\n\nButtons\n\nUser profile"
  },
  {
    "name": "Top Banner",
    "parts": [
      "Recipes",
      "Content",
      "Top Banner"
    ],
    "url": "docs/recipes/content/top-banner",
    "description": "Top Banner\n\nTop banners are used to highlight important information or features at the top of a page. They are typically designed to grab the user's attention and can be used for announcements, navigation, or key messages.\n\nBasic\n\nSign up\n\nGradient\n\nNewsletter"
  },
  {
    "name": "Stats",
    "parts": [
      "Recipes",
      "Content",
      "Stats"
    ],
    "url": "docs/recipes/content/stats",
    "description": "Stats\n\nStats cards are used to display key metrics or data points. They are typically used in dashboards or admin panels.\n\nVariant 1\n\nVariant 2"
  },
  {
    "name": "Multi Column Row",
    "parts": [
      "Recipes",
      "Content",
      "Multi Column Row"
    ],
    "url": "docs/recipes/content/multi-column-row",
    "description": "Multi-column and row layout\n\nA simple responsive multi-column and row layout. We specify the number of columns/rows to the  property as a list. The layout will automatically adjust the number of columns/rows based on the screen size.\n\nFor details, see the responsive docs page.\n\nColumn\n\nRow"
  },
  {
    "name": "Grid",
    "parts": [
      "Recipes",
      "Content",
      "Grid"
    ],
    "url": "docs/recipes/content/grid",
    "description": "Grid\n\nA simple responsive grid layout. We specify the number of columns to the  property as a list. The grid will automatically adjust the number of columns based on the screen size.\n\nFor details, see the responsive docs page.\n\nCards\n\nInset cards"
  },
  {
    "name": "Overview",
    "parts": [
      "Styling",
      "Overview"
    ],
    "url": "docs/styling/overview",
    "description": "Styling\n\nReflex components can be styled using the full power of CSS.\n\nThere are three main ways to add style to your app and they take precedence in the following order:\n\n1. **Inline:** Styles applied to a single component instance.\n2. **Component:** Styles applied to components of a specific type.\n3. **Global:** Styles applied to all components.\n\nGlobal Styles\n\nYou can pass a style dictionary to your app to apply base styles to all components.\n\nFor example, you can set the default font family and font size for your app here just once rather than having to set it on every component.\n\nComponent Styles\n\nIn your style dictionary, you can also specify default styles for specific component types or arbitrary CSS classes and IDs.\n\nUsing style dictionaries like this, you can easily create a consistent theme for your app.\n\nInline Styles\n\nInline styles apply to a single component instance. They are passed in as regular props to the component.\n\nChildren components inherit inline styles unless they are overridden by their own inline styles.\n\nStyle Prop\n\nInline styles can also be set with a  prop. This is useful for reusing styles between multiple components.\n\nThe style dictionaries are applied in the order they are passed in. This means that styles defined later will override styles defined earlier.\n\nTheming\n\nAs of Reflex 'v0.4.0', you can now theme your Reflex web apps. To learn more checkout the Theme docs.\n\nThe  component is used to change the theme of the application. The  can be set directly in your rx.App.\n\nAdditionally you can modify the theme of your app through using the  component which can be found in the Theme Panel docs.\n\nSpecial Styles\n\nWe support all of Chakra UI's pseudo styles.\n\nBelow is an example of text that changes color when you hover over it."
  },
  {
    "name": "Tailwind",
    "parts": [
      "Styling",
      "Tailwind"
    ],
    "url": "docs/styling/tailwind",
    "description": "Tailwind\n\nReflex supports Tailwind CSS through a plugin system that provides better control and supports multiple Tailwind versions.\n\nPlugin-Based Configuration\n\nThe recommended way to use Tailwind CSS is through the plugin system:\n\nYou can customize the Tailwind configuration by passing a config dictionary to the plugin:\n\nChoosing Between Tailwind Versions\n\nReflex supports both Tailwind CSS v3 and v4:\n\n- **TailwindV4Plugin**: The recommended choice for new projects. Includes the latest features and performance improvements and is used by default in new Reflex templates.\n- **TailwindV3Plugin**: Still supported for existing projects. Use this if you need compatibility with older Tailwind configurations.\n\nAll Tailwind configuration options are supported.\n\nYou can use any of the utility classes under the  prop:\n\nDisabling Tailwind\n\nTo disable Tailwind in your project, simply don't include any Tailwind plugins in your configuration. This will prevent Tailwind styles from being applied to your application.\n\nCustom theme\n\nYou can integrate custom Tailwind themes within your Reflex app as well. The setup process is similar to the CSS Styling method mentioned above, with only a few minor variations.\n\nBegin by creating a CSS file inside your  folder. Inside the CSS file, include the following Tailwind directives:\n\nWe define a couple of custom CSS variables ( and ) that will be used throughout your app for styling. These variables can be dynamically updated based on the theme.\n\nTailwind defaults to light mode, but to handle dark mode, you can define a separate set of CSS variables under the  class. \n\nTailwind Directives (, , ): These are essential Tailwind CSS imports that enable the default base styles, components, and utility classes.\n\nNext, you'll need to configure Tailwind in your  file to ensure that the Reflex app uses your custom Tailwind setup.\n\nIn the theme section, we're extending the default Tailwind theme to include custom colors. Specifically, we're referencing the CSS variables ( and ) that were defined earlier in your CSS file.\n\nThe  object is used to initialize and configure your Reflex app. Here, we're passing the  dictionary to ensure Tailwind's custom setup is applied to the app.\n\nFinally, to apply your custom styles and Tailwind configuration, you need to reference the CSS file you created in your  folder inside the  setup. This will allow you to use the custom properties (variables) directly within your Tailwind classes.\n\nIn your  (or main application file), make the following changes:\n\nThe  class uses the  variable (defined in the CSS file), which will be applied as the background color.\n\nDynamic Styling\n\nYou can style a component based of a condition using  or .\n\nUsing Tailwind Classes from the State\n\nWhen using Tailwind with Reflex, it's important to understand that class names must be statically defined in your code for Tailwind to properly compile them. If you dynamically generate class names from state variables or functions at runtime, Tailwind won't be able to detect these classes during the build process, resulting in missing styles in your application.\n\nFor example, this won't work correctly because the class names are defined in the state:\n\nUsing Tailwind with Reflex Core Components\n\nReflex core components are built on Radix Themes, which means they come with pre-defined styling. When you apply Tailwind classes to these components, you may encounter styling conflicts or unexpected behavior as the Tailwind styles compete with the built-in Radix styles.\n\nFor the best experience when using Tailwind CSS in your Reflex application, we recommend using the lower-level  components. These components don't have pre-applied styles, giving you complete control over styling with Tailwind classes without any conflicts. Check the list of HTML components here."
  },
  {
    "name": "Theming",
    "parts": [
      "Styling",
      "Theming"
    ],
    "url": "docs/styling/theming",
    "description": "Theming\n\nAs of Reflex , you can now theme your Reflex applications. The core of our theming system is directly based on the Radix Themes library. This allows you to easily change the theme of your application along with providing a default light and dark theme. Themes cause all the components to have a unified color appearance.\n\nOverview\n\nThe  component is used to change the theme of the application. The  can be set directly in your rx.App.\n\nHere are the props that can be passed to the  component:\n\nAdditionally you can modify the theme of your app through using the  component which can be found in the Theme Panel docs.\n\nColors\n\nColor Scheme\n\nOn a high-level, component  inherits from the color specified in the theme. This means that if you change the theme, the color of the component will also change. Available colors can be found here.\n\nYou can also specify the  prop.\n\nShades\n\nSometime you may want to use a specific shade of a color from the theme. This is recommended vs using a hex color directly as it will automatically change when the theme changes appearance change from light/dark.\n\nTo access a specific shade of color from the theme, you can use the . When switching to light and dark themes, the color will automatically change. Shades can be accessed by using the color name and the shade number. The shade number ranges from 1 to 12. Additionally, they can have their alpha value set by using the  parameter it defaults to . A full list of colors can be found here.\n\nRegular Colors\n\nYou can also use standard hex, rgb, and rgba colors.\n\nToggle Appearance\n\nTo toggle between the light and dark mode manually, you can use the  with the desired event trigger of your choice.\n\nAppearance Conditional Rendering\n\nTo render a different component depending on whether the app is in  mode or  mode, you can use the  component. The first component will be rendered if the app is in  mode and the second component will be rendered if the app is in  mode.\n\nThis can also be applied to props."
  },
  {
    "name": "Responsive",
    "parts": [
      "Styling",
      "Responsive"
    ],
    "url": "docs/styling/responsive",
    "description": "Responsive\n\nReflex apps can be made responsive to look good on mobile, tablet, and desktop.\n\nYou can pass a list of values to any style property to specify its value on different screen sizes.\n\nThe text will change color based on your screen size. If you are on desktop, try changing the size of your browser window to see the color change.\n\n_New in 0.5.6_\n\nResponsive values can also be specified using . Each size maps to a corresponding key, the value of which will be applied when the screen size is greater than or equal to the named breakpoint.\n\nCustom breakpoints in CSS units can be mapped to values per component using a dictionary instead of named parameters.\n\nFor the Radix UI components' fields that supports responsive value, you can also use  (note that custom breakpoints and list syntax aren't supported).\n\nSetting Defaults\n\nThe default breakpoints are shown below.\n\nYou can customize them using the style property.\n\nShowing Components Based on Display\n\nA common use case for responsive is to show different components based on the screen size.\n\nReflex provides useful helper components for this.\n\nSpecifying Display Breakpoints\n\nYou can specify the breakpoints to use for the responsive components by using the  style property."
  },
  {
    "name": "Common Props",
    "parts": [
      "Styling",
      "Common Props"
    ],
    "url": "docs/styling/common-props",
    "description": "Style and Layout Props\n\nAny CSS prop can be used in a component in Reflex. This is a short list of the most commonly used props. To see all CSS props that can be used check out this documentation. \n\nHyphens in CSS property names may be replaced by underscores to use as valid python identifiers, i.e. the CSS prop  would be used as  in Reflex."
  },
  {
    "name": "Custom Stylesheets",
    "parts": [
      "Styling",
      "Custom Stylesheets"
    ],
    "url": "docs/styling/custom-stylesheets",
    "description": "Custom Stylesheets\n\nReflex allows you to add custom stylesheets. Simply pass the URLs of the stylesheets to :\n\nLocal Stylesheets\n\nYou can also add local stylesheets. Just put the stylesheet under []({assets.upload_and_download_files.path}) and pass the path to the stylesheet to :\n\nStyling with CSS\n\nYou can use CSS variables directly in your Reflex app by passing them alongside the appropriae props. Create a  file inside the  folder with the following lines:\n\nThen, after referencing the CSS file within the  props of , you can access the CSS props directly like this\n\nSASS/SCSS Support\n\nReflex supports SASS/SCSS stylesheets alongside regular CSS. This allows you to use more advanced styling features like variables, nesting, mixins, and more.\n\nUsing SASS/SCSS Files\n\nTo use SASS/SCSS files in your Reflex app:\n\n1. Create a  or  file in your  directory\n2. Reference the file in your  configuration just like you would with CSS files\n\nReflex automatically detects the file extension and compiles these files to CSS using the  package.\n\nExample SASS/SCSS File\n\nHere's an example of a SASS file () that demonstrates some of the features:\n\nDependency Requirement\n\nThe  package is required for SASS/SCSS compilation. If it's not installed, Reflex will show an error message. You can install it with:\n\nThis package is included in the default Reflex installation, so you typically don't need to install it separately.\n\nFonts\n\nYou can take advantage of Reflex's support for custom stylesheets to add custom fonts to your app.\n\nIn this example, we will use the IBM Plex Mono font from Google Fonts. First, add the stylesheet with the font to your app. You can get this link from the \"Get embed code\" section of the Google font page.\n\nThen you can use the font in your component by setting the  prop.\n\nLocal Fonts\n\nBy making use of the two previous points, we can also make a stylesheet that allow you to use a font hosted on your server.\n\nIf your font is called , copy it in .\n\nNow we have the font ready, let's create the stylesheet .\n\nAdd the reference to your new Stylesheet in your App.\n\nAnd that's it! You can now use  like any other FontFamily to style your components."
  },
  {
    "name": "Layout",
    "parts": [
      "Styling",
      "Layout"
    ],
    "url": "docs/styling/layout",
    "description": "Layout Components\n\nLayout components such as , , , etc. are used to organize and structure the visual presentation of your application. This page gives a breakdown of when and how each of these components might be used.\n\nBox\n\n is a generic component that can apply any CSS style to its children. It's a building block that can be used to apply a specific layout or style property.\n\n**When to use:** Use  when you need to apply specific styles or constraints to a part of your interface.\n\nStack\n\n is a layout component that arranges its children in a single column or row, depending on the direction. It’s useful for consistent spacing between elements.\n\n**When to use:** Use  when you need to lay out a series of components either vertically or horizontally with equal spacing.\n\nFlex\n\nThe  component is used to create a flexible box layout, inspired by CSS Flexbox. It's ideal for designing a layout where the size of the items can grow and shrink dynamically based on the available space.\n\n**When to use:** Use  when you need a responsive layout that adjusts the size and position of child components dynamically.\n\nGrid\n\n components are used to create complex responsive layouts based on a grid system, similar to CSS Grid Layout.\n\n**When to use:** Use  when dealing with complex layouts that require rows and columns, especially when alignment and spacing among multiple axes are needed.\n\nContainer\n\nThe  component typically provides padding and fixes the maximum width of the content inside it, often used to center content on large screens.\n\n**When to use:** Use  for wrapping your application’s content in a centered block with some padding."
  },
  {
    "name": "Secrets Environment Vars",
    "parts": [
      "Hosting",
      "Secrets Environment Vars"
    ],
    "url": "docs/hosting/secrets-environment-vars",
    "description": "Secrets (Environment Variables)\n\nAdding Secrets through the CLI\n\nBelow is an example of how to use an environment variable file. You can pass the  flag with the path to the env file. For example:\n\nIn this example the path to the file is .\n\nIf you prefer to pass the environment variables manually below is deployment command example:\n\nThey are passed after the  flag as key value pairs. \n\nTo pass multiple environment variables, you can repeat the  tag. i.e. . The  flag will override any envs set manually.\n\nAdding Secrets through the Cloud UI\n\nTo find the secrets tab, click on the  tab in the Cloud UI on the app page.\n\nThen click on the  tab as shown below.\n\nFrom here you can add or edit your environment variables. You will need to restart your app for these changes to take effect.\n\nThis functionality in the UI can be disabled by an admin of the project."
  },
  {
    "name": "Self Hosting",
    "parts": [
      "Hosting",
      "Self Hosting"
    ],
    "url": "docs/hosting/self-hosting",
    "description": "Self Hosting\n\nWe recommend using , but if this does not fit your use case then you can also host your apps yourself.\n\nClone your code to a server and install the requirements.\n\nAPI URL\n\nEdit your  file and set  to the publicly accessible IP\naddress or hostname of your server, with the port  at the end. Setting\nthis correctly is essential for the frontend to interact with the backend state.\n\nFor example if your server is at , your config would look like this:\n\nIt is also possible to set the environment variable  at run time or\nexport time to retain the default for local development.\n\nProduction Mode\n\nThen run your app in production mode:\n\nProduction mode creates an optimized build of your app.  By default, the static\nfrontend of the app (HTML, Javascript, CSS) will be exposed on port  and\nthe backend (event handlers) will be listening on port .\n\nExporting a Static Build\n\nExporting a static build of the frontend allows the app to be served using a\nstatic hosting provider, like Netlify or Github Pages. Be sure  is set\nto an accessible backend URL when the frontend is exported.\n\nThis will create a  file with your app's minified HTML,\nJavascript, and CSS build that can be uploaded to your static hosting service.\n\nIt also creates a  file with your app's backend python code to\nupload to your server and run.\n\nYou can export only the frontend or backend by passing in the \nor  flags.\n\nIt is also possible to export the components without zipping. To do\nthis, use the  parameter. This provides the frontend in the\n directory and the backend can be found in the root directory of\nthe project.\n\nReflex Container Service\n\nAnother option is to run your Reflex service in a container. For this\npurpose, a  and additional documentation is available in the Reflex\nproject in the directory .\n\nFor the build of the container image it is necessary to edit the \nand the add the \nto your project folder. The following changes are necessary in :\n\nNotice that the  should be set to the externally accessible hostname or\nIP, as the client browser must be able to connect to it directly to establish\ninteractivity.\n\nYou can find the  in the  folder of the\nproject too.\n\nThe project structure should looks like this:\n\nAfter all changes have been made, the container image can now be created as follows.\n\nFinally, you can start your Reflex container service as follows."
  },
  {
    "name": "Custom Domains",
    "parts": [
      "Hosting",
      "Custom Domains"
    ],
    "url": "docs/hosting/custom-domains",
    "description": "Custom Domains\n\nWith the Pro tier of Reflex Cloud you can use your own custom domain to host your app. \n\nPrerequisites\n\nYou must purchase a domain from a domain registrar such as GoDaddy, Cloudflare, Namecheap, or AWS. \n\nFor this tutorial we will use GoDaddy and the example domain .\n\nSteps\n\nOnce you have purchased your domain, you can add it to your Reflex Cloud app by following these steps:\n\n1 - Ensure you have deployed your app to Reflex Cloud.\n\n2 - Once your app is deployed click the  tab and add your custom domain to the input field and press the Add domain button. You should now see a page like below:\n\n3 - On the domain registrar's website, navigate to the DNS settings for your domain. It should look something like the image below:\n\n4 - Add all four of the DNS records provided by Reflex Cloud to your domain registrar's DNS settings. If there is already an A name record, delete it and replace it with the one provided by Reflex Cloud. Your DNS settings should look like the image below:\n\n5 - Once you have added the DNS records, refresh the page on the Reflex Cloud page (it may take a few minutes to a few hours to update successfully). If the records are correct, you should see a success message like the one below:\n\n6 - Now redeploy your app using the  command and your app should now be live on your custom domain!"
  },
  {
    "name": "Logs",
    "parts": [
      "Hosting",
      "Logs"
    ],
    "url": "docs/hosting/logs",
    "description": "View Logs\n\nTo view the app logs follow the arrow in the image below and press on the  dropdown.\n\nView Deployment Logs and Deployment History\n\nTo view the deployment history follow the arrow in the image below and press on the .\n\nThis brings you to the page below where you can see the deployment history of your app. Click on deployment you wish to explore further.\n\nThis brings you to the page below where you can view the deployment logs of your app by clicking the  dropdown."
  },
  {
    "name": "Deploy Quick Start",
    "parts": [
      "Hosting",
      "Deploy Quick Start"
    ],
    "url": "docs/hosting/deploy-quick-start",
    "description": "Reflex Cloud - Quick Start\n\nSo far, we have been running our apps locally on our own machines.\nBut what if we want to share our apps with the world? This is where\nthe hosting service comes in.\n\nQuick Start\n\nReflex’s hosting service makes it easy to deploy your apps without worrying about configuring the infrastructure.\n\nPrerequisites\n\n1. Hosting service requires .\n2. This tutorial assumes you have successfully  and  your app.\n3. Also make sure you have a  file at the top level app directory that contains all your python dependencies! (To create a  file, run .)\n\nAuthentication\n\nFirst run the command below to login / signup to your Reflex Cloud account: (command line)\n\nYou will be redirected to your browser where you can authenticate through Github or Gmail.\n\nWeb UI\n\nOnce you are at this URL and you have successfully authenticated, click on the one project you have in your workspace. You should get a screen like this:\n\nThis screen shows the login command and the deploy command. As we are already logged in, we can skip the login command.\n\nDeployment\n\nNow you can start deploying your app.\n\nIn your cloud UI copy the  command similar to the one shown below.\n\nIn your project directory (where you would normally run ) paste this command.\n\nThe command is by default interactive. It asks you a few questions for information required for the deployment.\n\n1. The first question will compare your  to your python environment and if they are different then it will ask you if you want to update your  or to continue with the current one. If they are identical this question will not appear. To create a  file, run .\n2. The second question will search for a deployed app with the name of your current app, if it does not find one then it will ask if you wish to proceed in deploying your new app.\n3. The third question is optional and will ask you for an app description.\n\nThat’s it! You should receive some feedback on the progress of your deployment and in a few minutes your app should be up. 🎉\n\nFor detailed information about the deploy command and its options, see the Deploy API Reference and the CLI Reference.\n\nIf you go back to the Cloud UI you should be able to see your deployed app and other useful app information."
  },
  {
    "name": "Machine Types",
    "parts": [
      "Hosting",
      "Machine Types"
    ],
    "url": "docs/hosting/machine-types",
    "description": "Machine Types\n\nTo scale your app you can choose different VMTypes. VMTypes are different configurations of CPU and RAM.\n\nTo scale your VM in the Cloud UI, click on the  tab in the Cloud UI on the app page, and then click on the  tab as shown below. Clicking on the  button will allow you to scale your app.\n\nVMTypes in the CLI\n\nTo get all the possible VMTypes you can run the following command:\n\nTo set which VMType to use when deploying your app you can pass the  flag with the id of the VMType. For example:\n\nThis will deploy your app with the  VMType, giving your app 2 CPU cores and 4 GB of RAM."
  },
  {
    "name": "Databricks",
    "parts": [
      "Hosting",
      "Databricks"
    ],
    "url": "docs/hosting/databricks",
    "description": "Deploy Reflex to Databricks\n\nThis guide walks you through deploying a Reflex web application on Databricks using the Apps platform.\n\nPrerequisites\n\n- Databricks workspace with Unity Catalog enabled\n- GitHub repository containing your Reflex application\n- Reflex Enterprise license (for single-port deployment)\n\nStep 1: Connect Your Repository\n\n1. **Link GitHub Repository**\n   - Navigate to your Databricks workspace\n   - Go to your user directory\n   - Click **Create** → **Git folder**\n   - Paste the URL of your GitHub repository containing the Reflex application\n\nStep 2: Configure Application Settings\n\nCreate Configuration File\n\nCreate a new file called  directly in Databricks (not in GitHub):\n\nObtain Required Tokens\n\n1. **Reflex Access Token**\n   - Visit Reflex Cloud Tokens\n   - Navigate to Account Settings → Tokens\n   - Create a new token and copy the value\n   - Replace  in the configuration\n2. **Databricks Resources**\n   - Update  with your target catalog name\n   - Update  with your target schema name\n\nStep 3: Enable Single-Port Deployment\n\nUpdate your Reflex application for Databricks compatibility:\n\nUpdate rxconfig.py\n\nUpdate Application Entry Point\n\nModify your main application file where you define :\n\nStep 4: Create Databricks App\n\n1. **Navigate to Apps**\n   - Go to **Compute** → **Apps**\n   - Click **Create App**\n2. **Configure Application**\n   - Select **Custom App**\n   - Configure SQL warehouse for your application\n\nStep 5: Set Permissions\n\nCatalog Permissions\n\n1. Navigate to **Catalog** → Select your target catalog\n2. Go to **Permissions**\n3. Add the app's service principal user\n4. Grant the following permissions:\n   - **USE CATALOG**\n   - **USE SCHEMA**\n\nSchema Permissions\n\n1. Navigate to the specific schema\n2. Go to **Permissions**\n3. Grant the following permissions:\n   - **USE SCHEMA**\n   - **EXECUTE**\n   - **SELECT**\n   - **READ VOLUME** (if required)\n\nStep 6: Deploy Application\n\n1. **Initiate Deployment**\n   - Click **Deploy** in the Apps interface\n   - When prompted for the code path, provide your Git folder path or select your repository folder\n2. **Monitor Deployment**\n   - The deployment process will begin automatically\n   - Monitor logs for any configuration issues\n\nUpdating Your Application\n\nTo deploy updates from your GitHub repository:\n\n1. **Pull Latest Changes**\n   - In the deployment interface, click **Deployment Source**\n   - Select **main** branch\n   - Click **Pull** to fetch the latest changes from GitHub\n2. **Redeploy**\n   - Click **Deploy** again to apply the updates\n\nConfiguration Reference\n\nTroubleshooting\n\n- **Permission Errors**: Verify that all catalog and schema permissions are correctly set\n- **Port Issues**: Ensure you're using  and single-port configuration\n- **Token Issues**: Verify your Reflex access token is valid and properly configured\n- **Deployment Failures**: Check the deployment logs for specific error messages\n\nNotes\n\n- Single-port deployment requires Reflex Enterprise\n- Configuration must be created directly in Databricks, not pushed from GitHub\n- Updates require manual pulling from the deployment interface"
  },
  {
    "name": "Billing",
    "parts": [
      "Hosting",
      "Billing"
    ],
    "url": "docs/hosting/billing",
    "description": "Overview \n\nBilling for Reflex Cloud is monthly per project. Project owners and admins are able to view and manage the billing page. \n\nThe billing for a project is comprised of two parts - number of  and . \n\nSeats\n\nProjects on a paid plan can invite collaborators to join their project. \n\nEach additional collaborator is considered a  and is charged on a flat monthly rate. Project owners and admins can manage permissions and roles for each seat in the settings tab on the project page. \n\nCompute\n\nReflex Cloud is billed on a per second basis so you only pay for when your app is being used by your end users. When your app is idle, you are not charged. \n\nFor more information on compute pricing, please see the compute page.\n\nManage Billing\n\nTo manage your billing, you can go to the  tab in the Cloud UI on the project page.\n\nSetting Billing Limits\n\nIf you want to set a billing limit for your project, you can do so by going to the  tab in the Cloud UI on the project page."
  },
  {
    "name": "Compute",
    "parts": [
      "Hosting",
      "Compute"
    ],
    "url": "docs/hosting/compute",
    "description": "Compute Usage\n\nReflex Cloud is billed on a per second basis so you only pay for when your app is being used by your end users. When your app is idle, you are not charged. \n\nThis allows you to deploy your app on larger sizes and multiple regions without worrying about paying for idle compute. We bill on a per second basis so you only pay for the compute you use.\n\nBy default your app stays alive for 5 minutes after the no users are connected. After this time your app will be considered idle and you will not be charged. Start up times usually take less than 1 second for you apps to come back online.\n\nWarm vs Cold Start\n- Apps below  are considered warm starts and are usually less than 1 second.\n- If your app is larger than  it will be a cold start which takes around 15 seconds. If you want to avoid this you can reserve a machine.\n\nCompute Pricing Table\n\nReserved Machines (Coming Soon)\n\nIf you expect your apps to be continuously receiving users, you may want to reserve a machine instead of having us manage your compute. \n\nThis will be a flat monthly rate for the machine.\n\nMonitoring Usage\n\nTo monitor your projects usage, you can go to the billing tab in the Reflex Cloud UI on the project page.\n\nHere you can see the current billing and usage for your project.\n\nReal Life Examples of compute charges on the Pro tier\n\nOne thing that is important to note is that in the hypothetical example where you have  using your app  or if you have  using your app , you  as the charge is based on the amount of time your app up and not the number of users using your app. In  your  and therefore you will be ."
  },
  {
    "name": "App Management",
    "parts": [
      "Hosting",
      "App Management"
    ],
    "url": "docs/hosting/app-management",
    "description": "App\n\nIn Reflex Cloud an \"app\" (or \"application\" or \"website\") refers to a web application built using the Reflex framework, which can be deployed and managed within the Cloud platform. \n\nYou can deploy an app using the  command.\n\nThere are many actions you can take in the Cloud UI to manage your app. Below are some of the most common actions you may want to take.\n\nStopping an App\n\nTo stop an app follow the arrow in the image below and press on the  button. Pausing an app will stop it from running and will not be accessible to users until you resume it. In addition, this will stop you being billed for your app.\n\nDeleting an App\n\nTo delete an app click on the  tab in the Cloud UI on the app page.\n\nThen click on the  tab as shown below.\n\nHere there is a  button. Pressing this button will delete the app and all of its data. This action is irreversible.\n\nOther app settings\n\nClicking on the  tab in the Cloud UI on the app page also allows a user to change the , change the  and check the .\n\nThe other app settings also allows users to edit and add secrets (environment variables) to the app. For more information on secrets, see the Secrets (Environment Variables) page."
  },
  {
    "name": "Adding Members",
    "parts": [
      "Hosting",
      "Adding Members"
    ],
    "url": "docs/hosting/adding-members",
    "description": "Project\n\nA project is a collection of applications (apps / websites).\n\nEvery project has its own billing page that are accessible to Admins.\n\nAdding Team Members\n\nTo see the team members of a project click on the  tab in the Cloud UI on the project page. \n\nIf you are a User you have the ability to create, deploy and delete apps, but you do not have the power to add or delete users from that project. You must be an Admin for that.\n\nAs an Admin you will see the an  button in the top right of the screen, as shown in the image below. Clicking on this will allow you to add a user to the project. You will need to enter the email address of the user you wish to add.\n\nOther project settings\n\nClicking on the  tab in the Cloud UI on the project page allows a user to change the , check the  and, if the project is not your default project, delete the project."
  },
  {
    "name": "Config File",
    "parts": [
      "Hosting",
      "Config File"
    ],
    "url": "docs/hosting/config-file",
    "description": "What is reflex cloud config?\n\nThe following command:\n\ngenerates a  configuration file used to deploy your Reflex app to the Reflex cloud platform. This file tells Reflex how and where to run your app in the cloud.\n\nConfiguration File Structure\n\nThe  file uses YAML format and supports the following structure. **All fields are optional** and will use sensible defaults if not specified:\n\nConfiguration Options Reference\n\nConfiguration Options\n\nFor details of specific sections click the links in the table.\n\nProjects\n\nOrganize deployments using projects:\n\nYou can also specify a project uuid instead of name:\n\nYou can go to the homepage of the project in the reflex cloud dashboard to find your project uuid in the url \n\nApt Packages\n\nInstall additional system packages your application requires. Package names are based on the apt package manager:\n\nInclude SQLite\n\nInclude local sqlite database:\n\nThis is not persistent and will be lost on restart. It is recommended to use a database service instead.\n\nStrategy\n\nDeployment strategy:\nAvailable strategies:\n- : [Default] Deploy immediately\n- : Deploy in a rolling manner\n- : Deploy in a blue-green manner\n- : Deploy in a canary manner, boot as single machine verify its health and then restart the rest.\n\nMulti-Environment Setup\n\n**Development ():**\n\n**Staging ():**\n\n**Production ():**\n\nDeploy with specific configuration files:"
  },
  {
    "name": "Deploy With Github Actions",
    "parts": [
      "Hosting",
      "Deploy With Github Actions"
    ],
    "url": "docs/hosting/deploy-with-github-actions",
    "description": "Deploy with Github Actions\n\nThis GitHub Action simplifies the deployment of Reflex applications to Reflex Cloud. It handles setting up the environment, installing the Reflex CLI, and deploying your app with minimal configuration.\n\n**Features:**\n- Deploy Reflex apps directly from your GitHub repository to Reflex Cloud.\n- Supports subdirectory-based app structures.\n- Securely uses authentication tokens via GitHub Secrets.\n\nUsage\nAdd the Action to Your Workflow\nCreate a  file in your repository and add the following:\n\nSet Up Your Secrets\nStore your Reflex authentication token securely in your repository's secrets:\n\n1. Go to your GitHub repository.\n2. Navigate to Settings > Secrets and variables > Actions > New repository secret.\n3. Create new secrets for  and . \n\n(Create a  in the tokens tab of your UI, check out these docs. \n\nThe  can be found in the UI when you click on the How to deploy button on the top right when inside a project and copy the ID after the  flag.)\n\nInputs"
  },
  {
    "name": "Regions",
    "parts": [
      "Hosting",
      "Regions"
    ],
    "url": "docs/hosting/regions",
    "description": "Regions\n\nTo scale your app you can choose different regions. Regions are different locations around the world where your app can be deployed. \n\nTo scale your app to multiple regions in the Cloud UI, click on the  tab in the Cloud UI on the app page, and then click on the  tab as shown below. Clicking on the  button will allow you to scale your app to multiple regions.\n\nThe images below show all the regions that can be deployed in.\n\nSelecting Regions to Deploy in the CLI\n\nBelow is an example of how to deploy your app in several regions:\n\nBy default all apps are deloyed in  if no other regions are given. If you wish to deploy in another region or several regions you can pass the  flag ( also works) with the region code. Check out all the regions that we can deploy to below:\n\nConfig File\n\nTo create a  file for your app run the command below:\n\nThis will create a yaml file similar to the one below where you can edit the app configuration:"
  },
  {
    "name": "Reflex Branding",
    "parts": [
      "Hosting",
      "Reflex Branding"
    ],
    "url": "docs/hosting/reflex-branding",
    "description": "Reflex Branding\n\nRemove Reflex branding from your exported or deployed sites. \n\nBy default, Reflex branding, such as the \"Built with Reflex\" badge, will appear on all your published sites.\n\nHow to remove the Reflex branding from your app\n\nYou can turn off the Reflex branding, when deploying to Reflex Cloud, by adding  to the  in the  file. \n\nIn order for this to work a user hosting with Reflex Cloud must be logged in and on a paid plan (at least pro tier). \n\nIf you are self-hosting check out these instructions on how to remove the Reflex branding from your self-hosted app."
  },
  {
    "name": "Other Methods",
    "parts": [
      "Utility Methods",
      "Other Methods"
    ],
    "url": "docs/utility-methods/other-methods",
    "description": "Other Methods\n\n* : set all Vars to their default value for the given state (including substates).\n* : returns the value of a Var **without tracking changes to it**. This is useful\n   for serialization where the tracking wrapper is considered unserializable.\n* : returns all state Vars (and substates) as a dictionary. This is\n  used internally when a page is first loaded and needs to be \"hydrated\" and\n  sent to the client.\n\nSpecial Attributes\n\n* : a set of all Var names that have been modified since the last\n  time the state was sent to the client. This is used internally to determine\n  which Vars need to be sent to the client after processing an event."
  },
  {
    "name": "Tokens",
    "parts": [
      "Hosting",
      "Tokens"
    ],
    "url": "docs/hosting/tokens",
    "description": "Tokens\n\nA token gives someone else all the permissions you have as a User or an Admin. They can run any Reflex Cloud command from the CLI as if they are you using the  flag. A good use case would be for GitHub actions (you store this token in the secrets).\n\nTokens are found on the Project List page under the tab . If you cannot find it click the Reflex Logo in the top left side of the page until it appears as in the image below."
  },
  {
    "name": "Router Attributes",
    "parts": [
      "Utility Methods",
      "Router Attributes"
    ],
    "url": "docs/utility-methods/router-attributes",
    "description": "State Utility Methods\n\nThe state object has several methods and attributes that return information\nabout the current page, session, or state.\n\nRouter Attributes\n\nThe  attribute has several sub-attributes that provide various information:\n\n* : data about the current page and route\n  * : The hostname and port serving the current page (frontend).\n  * : The path of the current page (for dynamic pages, this will contain the slug)\n  * : The path of the page displayed in the browser (including params and dynamic values)\n  * :  with  prefixed\n  * :  with  prefixed\n  * : Dictionary of query params associated with the request\n\n* : data about the current session\n  * : UUID associated with the current tab's token. Each tab has a unique token.\n  * : The ID associated with the client's websocket connection. Each tab has a unique session ID.\n  * : The IP address of the client. Many users may share the same IP address.\n\n* : headers associated with the websocket connection. These values can only change when the websocket is re-established (for example, during page refresh).\n  * : The hostname and port serving the websocket (backend).\n  * : The origin of the request.\n  * : The upgrade header for websocket connections.\n  * : The connection header.\n  * : The cookie header.\n  * : The pragma header.\n  * : The cache control header.\n  * : The user agent string of the client.\n  * : The websocket version.\n  * : The websocket key.\n  * : The websocket extensions.\n  * : The accepted encodings.\n  * : The accepted languages.\n  * : A mapping of all HTTP headers as a frozen dictionary. This provides access to any header that was sent with the request, not just the common ones listed above.\n\nExample Values on this Page\n\nAccessing Raw Headers\n\nThe  attribute provides access to all HTTP headers as a frozen dictionary. This is useful when you need to access headers that are not explicitly defined in the  class:\n\nThis is particularly useful for accessing custom headers or when working with specific HTTP headers that are not part of the standard set exposed as direct attributes."
  },
  {
    "name": "Lifespan Tasks",
    "parts": [
      "Utility Methods",
      "Lifespan Tasks"
    ],
    "url": "docs/utility-methods/lifespan-tasks",
    "description": "Lifespan Tasks\n\n_Added in v0.5.2_\n\nLifespan tasks are coroutines that run when the backend server is running. They\nare useful for setting up the initial global state of the app, running periodic\ntasks, and cleaning up resources when the server is shut down.\n\nLifespan tasks are defined as async coroutines or async contextmanagers. To avoid\nblocking the event thread, never use  or perform non-async I/O within\na lifespan task.\n\nIn dev mode, lifespan tasks will stop and restart when a hot-reload occurs.\n\nTasks\n\nAny async coroutine can be used as a lifespan task. It will be started when the\nbackend comes up and will run until it returns or is cancelled due to server\nshutdown. Long-running tasks should catch  to perform\nany necessary clean up.\n\nRegister the Task\n\nTo register a lifespan task, use .\nAny keyword arguments specified during registration will be passed to the task.\n\nIf the task accepts the special argument, , it will be an instance of the  object\nassociated with the app.\n\nContext Managers\n\nLifespan tasks can also be defined as async contextmanagers. This is useful for\nsetting up and tearing down resources and behaves similarly to the ASGI lifespan\nprotocol.\n\nCode up to the first  will run when the backend comes up. As the backend\nis shutting down, the code after the  will run to clean up.\n\nHere is an example borrowed from the FastAPI docs and modified to work with this\ninterface."
  },
  {
    "name": "Exception Handlers",
    "parts": [
      "Utility Methods",
      "Exception Handlers"
    ],
    "url": "docs/utility-methods/exception-handlers",
    "description": "Exception handlers\n\n_Added in v0.5.7_\n\nExceptions handlers are functions that can be assigned to your app to handle exceptions that occur during the application runtime.\nThey are useful for customizing the response when an error occurs, logging errors, and performing cleanup tasks.\n\nTypes\n\nReflex support two type of exception handlers  and .\n\nThey are used to handle exceptions that occur in the  and  respectively.\n\nThe  errors are coming from the JavaScript side of the application, while  errors are coming from the the event handlers on the Python side.\n\nRegister an Exception Handler\n\nTo register an exception handler, assign it to  or  to assign a function that will handle the exception.\n\nThe expected signature for an error handler is .\n\nExamples"
  },
  {
    "name": "Decentralized Event Handlers",
    "parts": [
      "Events",
      "Decentralized Event Handlers"
    ],
    "url": "docs/events/decentralized-event-handlers",
    "description": "Decentralized Event Handlers\n\nOverview\n\nDecentralized event handlers allow you to define event handlers outside of state classes, providing more flexible code organization. This feature was introduced in Reflex v0.7.10 and enables a more modular approach to event handling.\n\nWith decentralized event handlers, you can:\n- Organize event handlers by feature rather than by state class\n- Separate UI logic from state management\n- Create more maintainable and scalable applications\n\nBasic Usage\n\nTo create a decentralized event handler, use the  decorator on a function that takes a state instance as its first parameter:\n\nIn this example:\n1. We define a  class with a  variable\n2. We create a decentralized event handler  that takes a  instance as its first parameter\n3. We use the event handler in buttons, passing different amounts to increment by\n\nCompared to Traditional Event Handlers\n\nHere's a comparison between traditional event handlers defined within state classes and decentralized event handlers:\n\nKey differences:\n- Traditional event handlers use  to reference the state instance\n- Decentralized event handlers explicitly take a state instance as the first parameter\n- Both approaches use the same syntax for triggering events in components\n- Both can be decorated with  respectively\n\nBest Practices\n\nWhen to Use Decentralized Event Handlers\n\nDecentralized event handlers are particularly useful in these scenarios:\n\n1. **Large applications** with many event handlers that benefit from better organization\n2. **Feature-based organization** where you want to group related event handlers together\n3. **Separation of concerns** when you want to keep state definitions clean and focused\n\nType Annotations\n\nAlways use proper type annotations for your state parameter and any additional parameters:\n\nNaming Conventions\n\nFollow these naming conventions for clarity:\n\n1. Use descriptive names that indicate the action being performed\n2. Use the state class name as the type annotation for the first parameter\n3. Name the state parameter consistently across your codebase (e.g., always use  or the first letter of the state class)\n\nOrganization\n\nConsider these approaches for organizing decentralized event handlers:\n\n1. Group related event handlers in the same file\n2. Place event handlers near the state classes they modify\n3. For larger applications, create a dedicated  directory with files organized by feature\n\nCombining with Other Event Features\n\nDecentralized event handlers work seamlessly with other Reflex event features:"
  },
  {
    "name": "Background Events",
    "parts": [
      "Events",
      "Background Events"
    ],
    "url": "docs/events/background-events",
    "description": "Background Tasks\n\nA background task is a special type of  that may run\nconcurrently with other  functions. This enables long-running\ntasks to execute without blocking UI interactivity.\n\nA background task is defined by decorating an async  method with\n.\n\nWhenever a background task needs to interact with the state, **it must enter an\n context block** which refreshes the state and takes an\nexclusive lock to prevent other tasks or event handlers from modifying it\nconcurrently. Because other  functions may modify state while the\ntask is running, **outside of the context block, Vars accessed by the background\ntask may be _stale_**. Attempting to modify the state from a background task\noutside of the context block will raise an  exception.\n\nIn the following example, the  event handler is decorated with\n and increments the  variable every half second, as\nlong as certain conditions are met. While it is running, the UI remains\ninteractive and continues to process events normally.\n\nTerminating Background Tasks on Page Close or Navigation\n\nSometimes, background tasks may continue running even after the user navigates away from the page or closes the browser tab. To handle such cases, you can check if the websocket associated with the state is disconnected and terminate the background task when necessary.\n\nThe solution involves checking if the client_token is still valid in the app.event_namespace.token_to_sid mapping. If the session is lost (e.g., the user navigates away or closes the page), the background task will stop.\n\nTask Lifecycle\n\nWhen a background task is triggered, it starts immediately, saving a reference to\nthe task in . When the task completes, it is removed from\nthe set.\n\nMultiple instances of the same background task may run concurrently, and the\nframework makes no attempt to avoid duplicate tasks from starting.\n\nIt is up to the developer to ensure that duplicate tasks are not created under\nthe circumstances that are undesirable. In the example above, the \nbackend var is used to control whether  will enter the increment loop,\nor exit early.\n\nBackground Task Limitations\n\nBackground tasks mostly work like normal  methods, with certain exceptions:\n\n- Background tasks must be  functions.\n- Background tasks cannot modify the state outside of an  context block.\n- Background tasks may read the state outside of an  context block, but the value may be stale.\n- Background tasks may not be directly called from other event handlers or background tasks. Instead use  or  to trigger the background task."
  },
  {
    "name": "Setters",
    "parts": [
      "Events",
      "Setters"
    ],
    "url": "docs/events/setters",
    "description": "Setters\n\nEvery base var has a built-in event handler to set it's value for convenience, called .\n\nSay you wanted to change the value of the select component. You could write your own event handler to do this:\n\nOr you could could use a built-in setter for conciseness.\n\nIn this example, the setter for  is . Both of these examples are equivalent.\n\nSetters are a great way to make your code more concise. But if you want to do something more complicated, you can always write your own function in the state."
  },
  {
    "name": "Event Actions",
    "parts": [
      "Events",
      "Event Actions"
    ],
    "url": "docs/events/event-actions",
    "description": "Event Actions\n\nIn Reflex, an event action is a special behavior that occurs during or after\nprocessing an event on the frontend.\n\nEvent actions can modify how the browser handles DOM events or throttle and\ndebounce events before they are processed by the backend.\n\nAn event action is specified by accessing attributes and methods present on all\nEventHandlers and EventSpecs.\n\nDOM Event Propagation\n\n_Added in v0.3.2_\n\nprevent_default\n\nThe  action prevents the default behavior of the browser for\nthe action. This action can be added to any existing event, or it can be used on its own by\nspecifying  as an event handler.\n\nA common use case for this is to prevent navigation when clicking a link.\n\nstop_propagation\n\nThe  action stops the event from propagating to parent elements.\n\nThis action is often used when a clickable element contains nested buttons that\nshould not trigger the parent element's click event.\n\nIn the following example, the first button uses  to prevent\nthe click event from propagating to the outer vstack. The second button does not\nuse , so the click event will also be handled by the on_click\nattached to the outer vstack.\n\nThrottling and Debounce\n\n_Added in v0.5.0_\n\nFor events that are fired frequently, it can be useful to throttle or debounce\nthem to avoid network latency and improve performance. These actions both take a\nsingle argument which specifies the delay time in milliseconds.\n\nthrottle\n\nThe  action limits the number of times an event is processed within a\na given time period. It is useful for  and  events which are\nfired very frequently, causing lag when handling them in the backend.\n\nIn the following example, the  event is throttled to only fire every half second.\n\ndebounce\n\nThe  action delays the processing of an event until the specified\ntimeout occurs. If another event is triggered during the timeout, the timer is\nreset and the original event is discarded.\n\nDebounce is useful for handling the final result of a series of events, such as\nmoving a slider.\n\nIn the following example, the slider's  handler, , is\nonly triggered on the backend when the slider value has not changed for half a\nsecond.\n\nTemporal Events\n\n_Added in v0.6.6_\n\ntemporal\n\nThe  action prevents events from being queued when the backend is down.\nThis is useful for non-critical events where you do not want them to pile up if there is\na temporary connection issue.\n\nIn the following example, the  component with  and  uses  to\nprevent periodic updates from being queued when the backend is down:"
  },
  {
    "name": "Event Arguments",
    "parts": [
      "Events",
      "Event Arguments"
    ],
    "url": "docs/events/event-arguments",
    "description": "Event Arguments\n\nThe event handler signature needs to match the event trigger definition argument count. If the event handler takes two arguments, the event trigger must be able to provide two arguments.\n\nHere is a simple example:\n\nThe event trigger here is  and it is called when the value changes at the end of an interaction. This event trigger passes one argument, which is the value of the slider. The event handler which is triggered by the event trigger must therefore take one argument, which is  here.\n\nHere is a form example:\n\nIn this example the event trigger is the  event of the form. The event handler is . The  event trigger passes one argument, the form data as a dictionary, to the  event handler. The  event handler must take one argument because the  event trigger passes one argument.\n\nWhen the number of args accepted by an EventHandler differs from that provided by the event trigger, an  error will be raised.\n\nPass Additional Arguments to Event Handlers\n\nIn some use cases, you want to pass additional arguments to your event handlers. To do this you can bind an event trigger to a lambda, which can call your event handler with the arguments you want.\n\nTry typing a color in an input below and clicking away from it to change the color of the input.\n\nIn this case, in we want to pass two arguments to the event handler , the color and the index of the color to change.\n\nThe  event trigger passes the text of the input as an argument to the lambda, and the lambda calls the  event handler with the text and the index of the input.\n\nWhen the number of args accepted by a lambda differs from that provided by the event trigger, an  error will be raised.\n\nEvents with Partial Arguments (Advanced)\n\n_Added in v0.5.0_\n\nEvent arguments in Reflex are passed positionally. Any additional arguments not\npassed to an EventHandler will be filled in by the event trigger when it is\nfired.\n\nThe following two code samples are equivalent:"
  },
  {
    "name": "Special Events",
    "parts": [
      "Events",
      "Special Events"
    ],
    "url": "docs/events/special-events",
    "description": "Special Events\n\nReflex also has built-in special events can be found in the reference.\n\nFor example, an event handler can trigger an alert on the browser.\n\nSpecial events can also be triggered directly in the UI by attaching them to an event trigger."
  },
  {
    "name": "Chaining Events",
    "parts": [
      "Events",
      "Chaining Events"
    ],
    "url": "docs/events/chaining-events",
    "description": "Chaining events\n\nCalling Event Handlers From Event Handlers\n\nYou can call other event handlers from event handlers to keep your code modular. Just use the  syntax to run another event handler. As always, you can yield within your function to send incremental updates to the frontend.\n\nReturning Events From Event Handlers\n\nSo far, we have only seen events that are triggered by components. However, an event handler can also return events.\n\nIn Reflex, event handlers run synchronously, so only one event handler can run at a time, and the events in the queue will be blocked until the current event handler finishes.The difference between returning an event and calling an event handler is that returning an event will send the event to the frontend and unblock the queue.\n\nTry entering an integer in the input below then clicking out.\n\nIn this example, we run the Collatz Conjecture on a number entered by the user.\n\nWhen the  event is triggered, the event handler  is called. It sets the initial count, then calls  which runs until the count reaches ."
  },
  {
    "name": "Events Overview",
    "parts": [
      "Events",
      "Events Overview"
    ],
    "url": "docs/events/events-overview",
    "description": "Events Overview\n\nEvents are composed of two parts: Event Triggers and Event Handlers.\n\n- **Events Handlers** are how the State of a Reflex application is updated. They are triggered by user interactions with the UI, such as clicking a button or hovering over an element. Events can also be triggered by the page loading or by other events.\n\n- **Event triggers** are component props that create an event to be sent to an event handler.\nEach component supports a set of events triggers. They are described in each component's documentation in the event trigger section.\n\nExample \nLets take a look at an example below. Try mousing over the heading to change the word.\n\nIn this example, the heading component has the **event trigger**, .\nWhenever the user hovers over the heading, the  **event handler** will be called to cycle the word. Once the handler returns, the UI will be updated to reflect the new state.\n\nAdding the  decorator above the event handler is strongly recommended. This decorator enables proper static type checking, which ensures event handlers receive the correct number and types of arguments.\n\nWhat's in this section?\n\nIn the event section of the documentation, you will explore the different types of events supported by Reflex, along with the different ways to call them."
  },
  {
    "name": "Yield Events",
    "parts": [
      "Events",
      "Yield Events"
    ],
    "url": "docs/events/yield-events",
    "description": "Yielding Updates\n\nA regular event handler will send a  when it has finished running. This works fine for basic event, but sometimes we need more complex logic. To update the UI multiple times in an event handler, we can  when we want to send an update.\n\nTo do so, we can use the Python keyword . For every yield inside the function, a  will be sent to the frontend with the changes up to this point in the execution of the event handler.\n\nThis example below shows how to yield 100 updates to the UI.\n\nHere is another example of yielding multiple updates with a loading icon.\n\nYielding Other Events\n\nEvents can also yield other events. This is useful when you want to chain events together. To do this, you can yield the event handler function itself."
  },
  {
    "name": "Page Load Events",
    "parts": [
      "Events",
      "Page Load Events"
    ],
    "url": "docs/events/page-load-events",
    "description": "Page Load Events\n\nYou can also specify a function to run when the page loads. This can be useful for fetching data once vs on every render or state change.\nIn this example, we fetch data when the page loads:\n\nAnother example would be checking if the user is authenticated when the page loads. If the user is not authenticated, we redirect them to the login page. If they are authenticated, we don't do anything, letting them access the page. This  event would be placed on every page that requires authentication to access."
  },
  {
    "name": "Overview",
    "parts": [
      "Assets",
      "Overview"
    ],
    "url": "docs/assets/overview",
    "description": "Assets\n\nStatic files such as images and stylesheets can be placed in  folder of the project. These files can be referenced within your app.\n\nReferencing Assets\n\nThere are two ways to reference assets in your Reflex app:\n\n1. Direct Path Reference\n\nTo reference an image in the  folder, pass the relative path as a prop.\n\nFor example, you can store your logo in your assets folder:\n\nThen you can display it using a  component:\n\n2. Using rx.asset Function\n\nThe  function provides a more flexible way to reference assets in your app. It supports both local assets (in the app's  directory) and shared assets (placed next to your Python files).\n\nLocal Assets\n\nLocal assets are stored in the app's  directory and are referenced using :\n\nShared Assets\n\nShared assets are placed next to your Python file and are linked to the app's external assets directory. This is useful for creating reusable components with their own assets:\n\nYou can also specify a subfolder for shared assets:\n\nFavicon\n\nThe favicon is the small icon that appears in the browser tab.\n\nYou can add a  file to the  folder to change the favicon."
  },
  {
    "name": "Upload And Download Files",
    "parts": [
      "Assets",
      "Upload And Download Files"
    ],
    "url": "docs/assets/upload-and-download-files",
    "description": "Files\n\nIn addition to any assets you ship with your app, many web app will often need to receive or send files, whether you want to share media, allow user to import their data, or export some backend data.\n\nIn this section, we will cover all you need to know for manipulating files in Reflex.\n\nAssets vs Upload Directory\n\nBefore diving into file uploads and downloads, it's important to understand the difference between assets and the upload directory in Reflex:\n\nFor more information about assets, see the Assets Overview.\n\nDownload\n\nIf you want to let the users of your app download files from your server to their computer, Reflex offer you two way.\n\nWith a regular link\n\nFor some basic usage, simply providing the path to your resource in a  will work, and clicking the link will download or display the resource.\n\nWith  event\n\nUsing the  event will always prompt the browser to download the file, even if it could be displayed in the browser.\n\nThe  event also allows the download to be triggered from another backend event handler.\n\n lets you specify a name for the file that will be downloaded, if you want it to be different from the name on the server side.\n\nIf the data to download is not already available at a known URL, pass the  directly to the  event from the backend.\n\nThe  arg accepts  or  data, a  URI, , or any state Var. If the Var is not already a string, it will be converted to a string using . This allows complex state structures to be offered as JSON downloads.\n\nReference page for  here.\n\nUpload\n\nUploading files to your server let your users interact with your app in a different way than just filling forms to provide data.\n\nThe component  let your users upload files on the server.\n\nHere is a basic example of how it is used:\n\nFor detailed information, see the reference page of the component here."
  },
  {
    "name": "Overview",
    "parts": [
      "Pages",
      "Overview"
    ],
    "url": "docs/pages/overview",
    "description": "Pages\n\nPages map components to different URLs in your app. This section covers creating pages, handling URL arguments, accessing query parameters, managing page metadata, and handling page load events.\n\nAdding a Page\n\nYou can create a page by defining a function that returns a component.\nBy default, the function name will be used as the route, but you can also specify a route.\n\nIn this example we create three pages:\n\n-  - The root route, available at \n-  - available at \n-  - available at \n\nPage Decorator\n\nYou can also use the  decorator to add a page.\n\nThis is equivalent to calling  with the same arguments.\n\nNavigating Between Pages\n\nLinks\n\nLinks are accessible elements used primarily for navigation. Use the  prop to specify the location for the link to navigate to.\n\nYou can also provide local links to other pages in your project without writing the full url.\n\nTo open the link in a new tab, set the  prop to .\n\nCheck out the link docs to learn more.\n\nRedirect\n\nRedirect the user to a new path within the application using .\n\n- : The destination path or URL to which the user should be redirected.\n- : If set to True, the redirection will open in a new tab. Defaults to .\n\nRedirect can also be run from an event handler in State, meaning logic can be added behind it. It is necessary to  the .\n\nNested Routes\n\nPages can also have nested routes.\n\nThis component will be available at .\n\nPage Metadata\n\nYou can add page metadata such as:\n\n- The title to be shown in the browser tab\n- The description as shown in search results\n- The preview image to be shown when the page is shared on social media\n- Any additional metadata\n\nGetting the Current Page\n\nYou can access the current page from the  attribute in any state. See the router docs for all available attributes.\n\nThe  attribute allows you to obtain the path of the current page from the router data,\nfor dynamic pages this will contain the slug rather than the actual value used to load the page.\n\nTo get the actual URL displayed in the browser, use . This\nwill contain all query parameters and dynamic path segments.\n\nIn the above example,  will contain the route pattern (e.g., ), while \nwill contain the actual URL (e.g., ).\n\nTo get the full URL, access the same attributes with  prefix.\n\nExample:\n\nIn this example, running on  should display"
  },
  {
    "name": "Dynamic Routing",
    "parts": [
      "Pages",
      "Dynamic Routing"
    ],
    "url": "docs/pages/dynamic-routing",
    "description": "Dynamic Routes\n\nDynamic routes in Reflex allow you to handle varying URL structures, enabling you to create flexible\nand adaptable web applications. This section covers regular dynamic routes, catch-all routes,\nand optional catch-all routes, each with detailed examples.\n\nRegular Dynamic Routes\n\nRegular dynamic routes in Reflex allow you to match specific segments in a URL dynamically. A regular dynamic route is defined by square brackets in a route string / url pattern. For example  or . These dynamic route arguments can be accessed through a state var. For the examples above they would be  and  respectively.\n\nExample:\n\nThe [pid] part in the route is a dynamic segment, meaning it can match any value provided in the URL. For instance, , , or  would all match this route.\n\nIf a user navigates to ,  will return , and the page will display  as the heading. If the URL is , it will display . If the URL is  without any additional parameter, it will display .\n\nAdding Dynamic Routes\n\nAdding dynamic routes uses the  method like any other page. The only difference is that the route string contains dynamic segments enclosed in square brackets.\n\nIf you are using the  method to define pages, it is necessary to add the dynamic routes first, especially if they use the same function as a non dynamic route.\n\nFor example the code snippet below will:\n\nBut if we switch the order of adding the pages, like in the example below, it will not work:\n\nCatch-All Routes\n\nCatch-all routes in Reflex allow you to match any number of segments in a URL dynamically.\n\nExample:\n\nIn this case, the  catch-all pattern captures any number of segments after\n, allowing URLs like  and  to match the route.\n\nRoutes Validation Table\n\n| Route Pattern                                    | Example URl                                     |   valid |\n| :----------------------------------------------- | :---------------------------------------------- | ------: |\n|                                    |                                   |   valid |\n|                            |                          |   valid |\n|                    |                            |   valid |\n|                       |                              | invalid |\n|                                                  |                          | invalid |\n|                             |                                   |   valid |\n|                                                  |                                |   valid |\n|               |                  |   valid |\n|                                                  |           |   valid |\n|               |                          |   valid |\n|                                                  |                  |   valid |\n|                                                  |           |   valid |\n|                                                  |  |   valid |\n|  |                  | invalid |\n|                                                  |           | invalid |\n|                                                  |  | invalid |"
  },
  {
    "name": "Authentication Overview",
    "parts": [
      "Authentication",
      "Authentication Overview"
    ],
    "url": "docs/authentication/authentication-overview",
    "description": "Authentication Overview\n\nMany apps require authentication to manage users. There are a few different ways to accomplish this in Reflex:\n\nWe have solutions that currently exist outside of the core framework:\n\n1. Local Auth: Uses your own database: https://github.com/masenf/reflex-local-auth\n2. Google Auth: Uses sign in with Google: https://github.com/masenf/reflex-google-auth\n3. Captcha: Generates tests that humans can pass but automated systems cannot: https://github.com/masenf/reflex-google-recaptcha-v2\n4. Magic Link Auth: A passwordless login method that sends a unique, one-time-use URL to a user's email: https://github.com/masenf/reflex-magic-link-auth\n5. Clerk Auth: A community member wrapped this component and hooked it up in this app: https://github.com/TimChild/reflex-clerk-api\n\nGuidance for Implementing Authentication\n\n- Store sensitive user tokens and information in backend-only vars.\n- Validate user session and permissions for each event handler that performs an authenticated action and all computed vars or loader events that access private data.\n- All content that is statically rendered in the frontend (for example, data hardcoded or loaded at compile time in the UI) will be publicly available, even if the page redirects to a login or uses  to hide content.\n- Only data that originates from state can be truly private and protected.\n- When using cookies or local storage, a signed JWT can detect and invalidate any local tampering.\n\nMore auth documentation on the way. Check back soon!"
  },
  {
    "name": "Overview",
    "parts": [
      "Client Storage",
      "Overview"
    ],
    "url": "docs/client-storage/overview",
    "description": "Client-storage\n\nYou can use the browser's local storage to persist state between sessions.\nThis allows user preferences, authentication cookies, other bits of information\nto be stored on the client and accessed from different browser tabs.\n\nA client-side storage var looks and acts like a normal  var, except the\ndefault value is either  or  depending on where the\nvalue should be stored. The key name will be based on the var name, but this\ncan be overridden by passing  as a keyword argument.\n\nFor more information see Browser Storage.\n\nTry entering some values in the text boxes below and then load the page in a separate\ntab or check the storage section of browser devtools to see the values saved in the browser."
  },
  {
    "name": "Chatapp Tutorial",
    "parts": [
      "Getting Started",
      "Chatapp Tutorial"
    ],
    "url": "docs/getting-started/chatapp-tutorial",
    "description": "Interactive Tutorial: AI Chat App\n\nThis tutorial will walk you through building an AI chat app with Reflex. This app is fairly complex, but don't worry - we'll break it down into small steps.\n\nYou can find the full source code for this app here.\n\nWhat You'll Learn\n\nIn this tutorial you'll learn how to:\n\n1. Install  and set up your development environment.\n2. Create components to define and style your UI.\n3. Use state to add interactivity to your app.\n4. Deploy your app to share with others.\n\nSetting up Your Project\n\nWe will start by creating a new project and setting up our development environment. First, create a new directory for your project and navigate to it.\n\nNext, we will create a virtual environment for our project. This is optional, but recommended. In this example, we will use venv to create our virtual environment.\n\nNow, we will install Reflex and create a new project. This will create a new directory structure in our project directory.\n\n> **Note:** When prompted to select a template, choose option 0 for a blank project.\n\nYou can run the template app to make sure everything is working.\n\nYou should see your app running at http://localhost:3000.\n\nReflex also starts the backend server which handles all the state management and communication with the frontend. You can test the backend server is running by navigating to http://localhost:8000/ping.\n\nNow that we have our project set up, in the next section we will start building our app!\n\nBasic Frontend\n\nLet's start with defining the frontend for our chat app. In Reflex, the frontend can be broken down into independent, reusable components. See the components docs for more information.\n\nDisplay A Question And Answer\n\nWe will modify the  function in  file to return a component that displays a single question and answer.\n\nComponents can be nested inside each other to create complex layouts. Here we create a parent container that contains two boxes for the question and answer.\n\nWe also add some basic styling to the components. Components take in keyword arguments, called props, that modify the appearance and functionality of the component. We use the  prop to align the text to the left and right.\n\nReusing Components\n\nNow that we have a component that displays a single question and answer, we can reuse it to display multiple questions and answers. We will move the component to a separate function  and call it from the  function.\n\nChat Input\n\nNow we want a way for the user to input a question. For this, we will use the input component to have the user add text and a button component to submit the question.\n\nStyling\n\nLet's add some styling to the app. More information on styling can be found in the styling docs. To keep our code clean, we will move the styling to a separate file .\n\nWe will import the styles in  and use them in the components. At this point, the app should look like this:\n\nThe app is looking good, but it's not very useful yet! In the next section, we will add some functionality to the app.\n\nState\n\nNow let’s make the chat app interactive by adding state. The state is where we define all the variables that can change in the app and all the functions that can modify them. You can learn more about state in the state docs.\n\nDefining State\n\nWe will create a new file called  in the  directory. Our state will keep track of the current question being asked and the chat history. We will also define an event handler  which will process the current question and add the answer to the chat history.\n\nBinding State to Components\n\nNow we can import the state in  and reference it in our frontend components. We will modify the  component to use the state instead of the current fixed questions and answers.\n\nNormal Python  loops don't work for iterating over state vars because these values can change and aren't known at compile time. Instead, we use the foreach component to iterate over the chat history.\n\nWe also bind the input's  event to the  event handler, which will update the  state var while the user types in the input. We bind the button's  event to the  event handler, which will process the question and add the answer to the chat history. The  event handler is a built-in implicitly defined event handler. Every base var has one. Learn more in the events docs under the Setters section.\n\nClearing the Input\n\nCurrently the input doesn't clear after the user clicks the button. We can fix this by binding the value of the input to , with , and clear it when we run the event handler for , with .\n\nStreaming Text\n\nNormally state updates are sent to the frontend when an event handler returns. However, we want to stream the text from the chatbot as it is generated. We can do this by yielding from the event handler. See the yield events docs for more info.\n\nIn the next section, we will finish our chatbot by adding AI!\n\nFinal App\n\nWe will use OpenAI's API to give our chatbot some intelligence.\n\nConfigure the OpenAI API Key\n\nFirst, ensure you have an active OpenAI subscription.\nNext, install the latest openai package:\n\nDirect Configuration of API in Code\n\nUpdate the state.py file to include your API key directly:\n\nUsing the API\n\nMaking your chatbot intelligent requires connecting to a language model API. This section explains how to integrate with OpenAI's API to power your chatbot's responses.\n\n1. First, the user types a prompt that is updated via the  event handler.\n2. Next, when a prompt is ready, the user can choose to submit it by clicking the  button which in turn triggers the  method inside our  file.\n3. Finally, if the method is triggered, the  is sent via a request to OpenAI client and returns an answer that we can trim and use to update the chat history! \n\nFinally, we have our chatbot!\n\nFinal Code\n\nThis application is a simple, interactive chatbot built with Reflex that leverages OpenAI's API for intelligent responses. The chatbot features a clean interface with streaming responses for a natural conversation experience.\n\nKey Features\n\n1. Real-time streaming responses\n2. Clean, visually distinct chat bubbles for questions and answers\n3. Simple input interface with question field and submit button\n\nProject Structure\n\nBelow is the full chatbot code with a commented title that corresponds to the filename.\n\nThe  file:\n\nThe  file:\n\nThe  file:\n\nNext Steps\n\nCongratulations! You have built your first chatbot. From here, you can read through the rest of the documentations to learn about Reflex in more detail. The best way to learn is to build something, so try to build your own app using this as a starting point!\n\nOne More Thing\n\nWith our hosting service, you can deploy this app with a single command within minutes. Check out our Hosting Quick Start."
  },
  {
    "name": "Basics",
    "parts": [
      "Getting Started",
      "Basics"
    ],
    "url": "docs/getting-started/basics",
    "description": "Reflex Basics\n\nThis page gives an introduction to the most common concepts that you will use to build Reflex apps.\n\nInstall  using pip.\n\nImport the  library to get started.\n\nCreating and nesting components\n\nComponents are the building blocks for your app's user interface (UI). They are the visual elements that make up your app, like buttons, text, and images. Reflex has a wide selection of built-in components to get you started quickly.\n\nComponents are created using functions that return a component object.\n\nComponents can be nested inside each other to create complex UIs.\n\nTo nest components as children, pass them as positional arguments to the parent component. In the example below, the  and  components are children of the  component.\n\nYou can also use any base HTML element through the []({docs.library.other.html.path}) namespace. This allows you to use standard HTML elements directly in your Reflex app when you need more control or when a specific component isn't available in the Reflex component library.\n\nIf you need a component not provided by Reflex, you can check the 3rd party ecosystem or wrap your own React component.\n\nCustomizing and styling components\n\nComponents can be customized using props, which are passed in as keyword arguments to the component function.\n\nEach component has props that are specific to that component. Check the docs for the component you are using to see what props are available.\n\nIn addition to component-specific props, components can also be styled using CSS properties passed as props.\n\nSee the styling guide for more information on how to style components\n\nIn summary, components are made up of children and props.\n\nDisplaying data that changes over time\n\nApps need to store and display data that changes over time. Reflex handles this through State, which is a Python class that stores variables that can change when the app is running, as well as the functions that can change those variables.\n\nTo define a state class, subclass  and define fields that store the state of your app. The state variables (vars) should have a type annotation, and can be initialized with a default value.\n\nReferencing state vars in components\n\nTo reference a state var in a component, you can pass it as a child or prop. The component will automatically update when the state changes.\n\nVars are referenced through class attributes on your state class. For example, to reference the  var in a component, use .\n\nVars can be referenced in multiple components, and will automatically update when the state changes.\n\nResponding to events and updating the screen\n\nSo far, we've defined state vars but we haven't shown how to change them. All state changes are handled through functions in the state class, called event handlers.\n\nComponents have special props, such as , called event triggers that can be used to make components interactive. Event triggers connect components to event handlers, which update the state.\n\nWhen an event trigger is activated, the event handler is called, which updates the state. The UI is automatically re-rendered to reflect the new state. \n\nEvent handlers with arguments\n\nEvent handlers can also take in arguments. For example, the  event handler can take an argument to increment the count by a specific amount.\n\nThe  event trigger doesn't pass any arguments here, but some event triggers do. For example, the  event trigger passes the text of an input as an argument to the event handler.\n\nCompile-time vs. runtime (IMPORTANT)\n\nBefore we dive deeper into state, it's important to understand the difference between compile-time and runtime in Reflex.\n\nWhen you run your app, the frontend gets compiled to Javascript code that runs in the browser (compile-time). The backend stays in Python and runs on the server during the lifetime of the app (runtime).\n\nWhen can you not use pure Python?\n\nWe cannot compile arbitrary Python code, only the components that you define. What this means importantly is that you cannot use arbitrary Python operations and functions on state vars in components.\n\nHowever, since any event handlers in your state are on the backend, you **can use any Python code or library** within your state.\n\nExamples that work\n\nWithin an event handler, use any Python code or library.\n\nUse any Python function within components, as long as it is defined at compile time (i.e. does not reference any state var)\n\nExamples that don't work\n\nYou cannot do an  statement on vars in components, since the value is not known at compile time.\n\nYou cannot do a  loop over a list of vars.\n\nYou cannot do arbitrary Python operations on state vars in components.\n\nIn the next sections, we will show how to handle these cases.\n\nConditional rendering\n\nAs mentioned above, you cannot use Python  statements with state vars in components. Instead, use the []({docs.components.conditional_rendering.path}) function to conditionally render components.\n\nRendering lists\n\nTo iterate over a var that is a list, use the []({docs.components.rendering_iterables.path}) function to render a list of components.\n\nPass the list var and a function that returns a component as arguments to .\n\nThe function that renders each item takes in a , since this will get compiled up front.\n\nVar Operations\n\nYou can't use arbitrary Python operations on state vars in components, but Reflex has var operations that you can use to manipulate state vars.\n\nFor example, to check if a var is even, you can use the  and  var operations.\n\nApp and Pages\n\nReflex apps are created by instantiating the  class. Pages are linked to specific URL routes, and are created by defining a function that returns a component.\n\nNext Steps\n\nNow that you have a basic understanding of how Reflex works, the next step is to start coding your own apps. Try one of the following tutorials:\n\n- Dashboard Tutorial\n- Chatapp Tutorial"
  },
  {
    "name": "Introduction",
    "parts": [
      "Getting Started",
      "Introduction"
    ],
    "url": "docs/getting-started/introduction",
    "description": "Introduction\n\n**Reflex** is an open-source framework for quickly building beautiful, interactive web applications in **pure Python**.\n\nGoals\n\nAn example: Make it count\n\nHere, we go over a simple counter app that lets the user count up or down.\n\nHere is the full code for this example:\n\nThe Structure of a Reflex App\n\nLet's break this example down.\n\nImport\n\nWe begin by importing the  package (aliased to ). We reference Reflex objects as  by convention.\n\nState\n\nThe state defines all the variables (called **vars**) in an app that can change, as well as the functions (called **event_handlers**) that change them.\n\nHere our state has a single var, , which holds the current value of the counter. We initialize it to .\n\nEvent Handlers\n\nWithin the state, we define functions, called **event handlers**, that change the state vars.\n\nEvent handlers are the only way that we can modify the state in Reflex.\nThey can be called in response to user actions, such as clicking a button or typing in a text box.\nThese actions are called **events**.\n\nOur counter app has two event handlers,  and .\n\nUser Interface (UI)\n\nThis function defines the app's user interface.\n\nWe use different components such as , , and  to build the frontend. Components can be nested to create complex layouts, and can be styled using the full power of CSS.\n\nReflex comes with 50+ built-in components to help you get started.\nWe are actively adding more components. Also, it's easy to wrap your own React components.\n\nComponents can reference the app's state vars.\nThe  component displays the current value of the counter by referencing .\nAll components that reference state will reactively update whenever the state changes.\n\nComponents interact with the state by binding events triggers to event handlers.\nFor example,  is an event that is triggered when a user clicks a component.\n\nThe first button in our app binds its  event to the  event handler. Similarly the second button binds  to .\n\nIn other words, the sequence goes like this:\n\n- User clicks \"increment\" on the UI.\n-  event is triggered.\n- Event handler  is called.\n-  is incremented.\n- UI updates to reflect the new value of .\n\nAdd pages\n\nNext we define our app and add the counter component to the base route.\n\nNext Steps\n\n🎉 And that's it!\n\nWe've created a simple, yet fully interactive web app in pure Python.\n\nBy continuing with our documentation, you will learn how to building awesome apps with Reflex.\n\nFor a glimpse of the possibilities, check out these resources:\n\n* For a more real-world example, check out either the dashboard tutorial or the chatapp tutorial.\n* We have bots that can answer questions and generate Reflex code for you. Check them out in #ask-ai in our Discord!"
  },
  {
    "name": "Dashboard Tutorial",
    "parts": [
      "Getting Started",
      "Dashboard Tutorial"
    ],
    "url": "docs/getting-started/dashboard-tutorial",
    "description": "Tutorial: Data Dashboard\n\nDuring this tutorial you will build a small data dashboard, where you can input data and it will be rendered in table and a graph. This tutorial does not assume any existing Reflex knowledge, but we do recommend checking out the quick Basics Guide first. \n\nThe techniques you’ll learn in the tutorial are fundamental to building any Reflex app, and fully understanding it will give you a deep understanding of Reflex.\n\nThis tutorial is divided into several sections:\n\n- **Setup for the Tutorial**: A starting point to follow the tutorial\n- **Overview**: The fundamentals of Reflex UI (components and props)\n- **Showing Dynamic Data**: How to use State to render data that will change in your app.\n- **Add Data to your App**: Using a Form to let a user add data to your app and introduce event handlers.\n- **Plotting Data in a Graph**: How to use Reflex's graphing components.\n- **Final Cleanup and Conclusion**: How to further customize your app and add some extra styling to it.\n\nWhat are you building?\n\nIn this tutorial, you are building an interactive data dashboard with Reflex.\n\nYou can see what the finished app and code will look like here:\n\nDon't worry if you don't understand the code above, in this tutorial we are going to walk you through the whole thing step by step.\n\nSetup for the tutorial\n\nCheck out the installation docs to get Reflex set up on your machine. Follow these to create a folder called , which you will  into and .\n\nWe will choose template  when we run  to get the blank template. Finally run  to start the app and confirm everything is set up correctly.\n\nOverview\n\nNow that you’re set up, let’s get an overview of Reflex!\n\nInspecting the starter code\n\nWithin our  folder we just 'd into, there is a  file that contains the configuration for our Reflex app. (Check out the config docs for more information)\n\nThere is also an  folder where static files such as images and stylesheets can be placed to be referenced within your app. (asset docs for more information)\n\nMost importantly there is a folder also called  which contains all the code for your app. Inside of this folder there is a file named . To begin this tutorial we will delete all the code in this file so that we can start from scratch and explain every step as we go.\n\nThe first thing we need to do is import . Once we have done this we can create a component, which is a reusable piece of user interface code. Components are used to render, manage, and update the UI elements in your application. \n\nLet's look at the example below. Here we have a function called  that returns a  component (an in-built Reflex UI component) that displays the text \"Hello World!\".\n\nNext we define our app using  and add the component we just defined () to a page using . The function name (in this example ) which defines the component, must be what we pass into the . The definition of the app and adding a component to a page are required for every Reflex app.\n\nThis code will render a page with the text \"Hello World!\" when you run your app like below:\n\nCreating a table\n\nLet's create a new component that will render a table. We will use the  component to do this. The  component has a , which takes in a  and a , which in turn take in  components. The  component takes in  components which are the actual data that will be displayed in the table.\n\nComponents in Reflex have , which can be used to customize the component and are passed in as keyword arguments to the component function. \n\nThe  component has for example the  and  props, which customize the table as seen below.\n\nShowing dynamic data (State)\n\nUp until this point all the data we are showing in the app is static. This is not very useful for a data dashboard. We need to be able to show dynamic data that can be added to and updated.\n\nThis is where  comes in.  is a Python class that stores variables that can change when the app is running, as well as the functions that can change those variables.\n\nTo define a state class, subclass  and define fields that store the state of your app. The state variables (vars) should have a type annotation, and can be initialized with a default value. Check out the basics section for a simple example of how state works.\n\nIn the example below we define a  class called  that has a variable called  that is a list of lists of strings. Each list in the  list represents a user and contains their name, email and gender.\n\nTo iterate over a state var that is a list, we use the []({docs.components.rendering_iterables.path}) function to render a list of components. The  component takes an  (list, tuple or dict) and a  that renders each item in the .\n\nHere the render function is  which takes in a single user and returns a  component that displays the users name, email and gender.\n\nAs you can see the output above looks the same as before, except now the data is no longer static and can change with user input to the app.\n\nUsing a proper class structure for our data\n\nSo far our data has been defined in a list of lists, where the data is accessed by index i.e. , . This is not very maintainable as our app gets bigger. \n\nA better way to structure our data in Reflex is to use a class to represent a user. This way we can access the data using attributes i.e. , .\n\nIn Reflex when we create these classes to showcase our data, the class must inherit from .\n\n is also necessary if we want to have a state var that is an iterable with different types. For example if we wanted to have  as an  we would have to use  as we could not do this with a state var defined as . \n\nThe  render function is also updated to access the data by named attributes, instead of indexing.\n\nNext let's add a form to the app so we can add new users to the table.\n\nUsing a Form to Add Data \n\nWe build a form using , which takes several components such as  and , which represent the form fields that allow you to add information to submit with the form. Check out the form docs for more information on form components.\n\nThe  component takes in several props. The  prop is the text that is displayed in the input field when it is empty. The  prop is the name of the input field, which gets passed through in the dictionary when the form is submitted. The  prop is a boolean that determines if the input field is required.\n\nThe  component takes in a list of options that are displayed in the dropdown. The other props used here are identical to the  component.\n\nThis form is all very compact as you can see from the example, so we need to add some styling to make it look better. We can do this by adding a  component around the form fields. The  component stacks the form fields vertically. Check out the layout docs for more information on how to layout your app.\n\nNow you have probably realised that we have all the form fields, but we have no way to submit the form. We can add a submit button to the form by adding a  component to the  component. The  component takes in the text that is displayed on the button and the  prop which is the type of button. The  prop is set to  so that the form is submitted when the button is clicked. \n\nIn addition to this we need a way to update the  state variable when the form is submitted. All state changes are handled through functions in the state class, called event handlers.\n\nComponents have special props called event triggers, such as , that can be used to make components interactive. Event triggers connect components to event handlers, which update the state. Different event triggers expect the event handler that you hook them up to, to take in different arguments (and some do not take in any arguments).\n\nThe  event trigger of  is hooked up to the  event handler that is defined in the  class. This event trigger expects to pass a , containing the form data, to the event handler that it is hooked up to. The  event handler takes in the form data as a dictionary and appends it to the  state variable. \n\nFinally we must add the new  component we have defined to the  function so that the form is rendered on the page.\n\nBelow is the full code for the app so far. If you try this form out you will see that you can add new users to the table by filling out the form and clicking the submit button. The form data will also appear as a toast (a small window in the corner of the page) on the screen when submitted.\n\nPutting the Form in an Overlay\n\nIn Reflex, we like to make the user interaction as intuitive as possible. Placing the form we just constructed in an overlay creates a focused interaction by dimming the background, and ensures a cleaner layout when you have multiple action points such as editing and deleting as well.\n\nWe will place the form inside of a  component (also called a modal). The  contains all the parts of a dialog, and the  wraps the control that will open the dialog. In our case the trigger will be an  that says \"Add User\" as shown below.\n\nAfter the trigger we have the  which contains everything within our dialog, including a title, a description and our form. The first way to close the dialog is without submitting the form and the second way is to close the dialog by submitting the form as shown below. This requires two  components within the dialog.\n\nThe total code for the dialog with the form in it is below.\n\nAt this point we have an app that allows you to add users to a table by filling out a form. The form is placed in a dialog that can be opened by clicking the \"Add User\" button. We change the name of the component from  to  and update this in our  component. The full app so far and code are below.\n\nPlotting Data in a Graph\n\nThe last part of this tutorial is to plot the user data in a graph. We will use Reflex's built-in graphing library recharts to plot the number of users of each gender. \n\nTransforming the data for the graph\n\nThe graphing components in Reflex expect to take in a list of dictionaries. Each dictionary represents a data point on the graph and contains the x and y values. We will create a new event handler in the state called  to transform the user data into the format that the graphing components expect. We must also create a new state variable called  to store the transformed data, which will be used to render the graph.\n\nAs we can see above the  event handler uses the  class from the  module to count the number of users of each gender. We then create a list of dictionaries from this which we set to the state var . \n\nFinally we can see that whenever we add a new user through submitting the form and running the  event handler, we call the  event handler to update the  state variable.\n\nRendering the graph\n\nWe use the  component to render the graph. We pass through the state variable for our graphing data as . We also pass in a  component which represents the bars on the graph. The  component takes in the  prop which is the key in the data dictionary that represents the y value of the bar. The  and  props are used to set the color of the bars.\n\nThe  component also takes in  and  components which represent the x and y axes of the graph. The  prop of the  component is set to the key in the data dictionary that represents the x value of the bar. Finally we add  and  props to set the size of the graph.\n\nFinally we add this  component to our  component so that the graph is rendered on the page. The code for the full app with the graph included is below. If you try this out you will see that the graph updates whenever you add a new user to the table.\n\nOne thing you may have noticed about your app is that the graph does not appear initially when you run the app, and that you must add a user to the table for it to first appear. This occurs because the  event handler is only called when a user is added to the table. In the next section we will explore a solution to this.\n\nFinal Cleanup\n\nRevisiting app.add_page\n\nAt the beginning of this tutorial we mentioned that the  function is required for every Reflex app. This function is used to add a component to a page. \n\nThe  currently looks like this . We could change the route that the page renders on by setting the  prop such as , this would change the route to  for this page.\n\nWe can also set a  to be shown in the browser tab and a  as shown in search results. \n\nTo solve the problem we had above about our graph not loading when the page loads, we can use  inside of  to call the  event handler when the page loads. This would look like . Below see what our  would look like with some of the changes above added.\n\nRevisiting app=rx.App()\n\nAt the beginning of the tutorial we also mentioned that we defined our app using . We can also pass in some props to the  component to customize the app.\n\nThe most important one is  which allows you to customize the look and feel of the app. The  prop takes in an  component which has several props that can be set. \n\nThe  prop sets the global radius value for the app that is inherited by all components that have a  prop. It can be overwritten locally for a specific component by manually setting the  prop.\n\nThe  prop sets the accent color of the app. Check out other options for the accent color here.\n\nTo see other props that can be set at the app level check out this documentation\n\nUnfortunately in this tutorial here we cannot actually apply this to the live example on the page, but if you copy and paste the code below into a reflex app locally you can see it in action.\n\nConclusion\n\nFinally let's make some final styling updates to our app. We will add some hover styling to the table rows and center the table inside the  with .\n\nIn addition, we will add some  and  to the  component to center the items on the page and ensure they stretch the full width of the page.\n\nCheck out the full code and interactive app below:\n\nAnd that is it for your first dashboard tutorial. In this tutorial we have created \n\n- a table to display user data\n- a form to add new users to the table\n- a dialog to showcase the form\n- a graph to visualize the user data\n\nIn addition to the above we have we have \n\n- explored state to allow you to show dynamic data that changes over time\n- explored events to allow you to make your app interactive and respond to user actions\n- added styling to the app to make it look better\n\nAdvanced Section (Hooking this up to a Database)\n\nComing Soon!"
  },
  {
    "name": "Installation",
    "parts": [
      "Getting Started",
      "Installation"
    ],
    "url": "docs/getting-started/installation",
    "description": "Installation\n\nReflex requires Python 3.10+.\n\nVirtual Environment\n\nWe **highly recommend** creating a virtual environment for your project.\n\nvenv is the standard option. conda and poetry are some alternatives.\n\nInstall Reflex on your system\n\n---md tabs\n\n--tab macOS/Linux\nInstall on macOS/Linux\n\nWe will go with venv here.\n\nPrerequisites\nmacOS (Apple Silicon) users should install Rosetta 2. Run this command:\n\nCreate the project directory \n\nReplace  with your project name. Switch to the new directory.\n\nSetup virtual environment\n\nInstall Reflex package\n\nReflex is available as a pip package.\n\nInitialize the project\n\n--\n--tab Windows\nInstall on Windows\n\nPrerequisites\nFor Windows users, we recommend using Windows Subsystem for Linux (WSL) for optimal performance.\n\nWSL users should refer to instructions for Linux above.\n\nFor the rest of this section we will work with native Windows (non-WSL).\n\nWe will go with venv here, for virtual environments.\n\nCreate the project directory \n\nReplace  with your project name. Switch to the new directory.\n\nSetup virtual environment\n\nInstall Reflex package\n\nReflex is available as a pip package.\n\nInitialize the project\n\n--\n\n---\n\nThe command will return four template options to choose from as shown below.\n\nFrom here select a template. \n\nRun the App\n\nRun it in development mode:\n\nYour app runs at http://localhost:3000.\n\nReflex prints logs to the terminal. To increase log verbosity to help with debugging, use the  flag:\n\nReflex will *hot reload* any code changes in real time when running in development mode. Your code edits will show up on http://localhost:3000 automatically."
  },
  {
    "name": "Project Structure",
    "parts": [
      "Getting Started",
      "Project Structure"
    ],
    "url": "docs/getting-started/project-structure",
    "description": "Project Structure\n\nDirectory Structure\n\nLet's create a new app called \n\nThis will create a directory structure like this:\n\nLet's go over each of these directories and files.\n\n.web\n\nThis is where the compiled Javascript files will be stored. You will never need to touch this directory, but it can be useful for debugging.\n\nEach Reflex page will compile to a corresponding  file in the  directory.\n\nAssets\n\nThe  directory is where you can store any static assets you want to be publicly available. This includes images, fonts, and other files.\n\nFor example, if you save an image to  you can display it from your app like this:\n\nj\nMain Project\n\nInitializing your project creates a directory with the same name as your app. This is where you will write your app's logic.\n\nReflex generates a default app within the  file. You can modify this file to customize your app.\n\nConfiguration\n\nThe  file can be used to configure your app. By default it looks something like this:\n\nWe will discuss project structure and configuration in more detail in the advanced project structure documentation."
  }
]
