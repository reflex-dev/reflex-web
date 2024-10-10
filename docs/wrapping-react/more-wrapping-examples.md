# Wrapping More React Libraries 


## Wrapping AG Charts


from NPM package: https://www.npmjs.com/package/ag-charts-react

```javascript
import React, \{ useState } from 'react';
import ReactDOM from 'react-dom/client';

// React Chart Component
import \{ AgCharts } from 'ag-charts-react';

const ChartExample = () => {
    // Chart Options: Control & configure the chart
    const [chartOptions, setChartOptions] = useState({
        // Data: Data to be displayed in the chart
        data: [
            \{ month: 'Jan', avgTemp: 2.3, iceCreamSales: 162000 },
            \{ month: 'Mar', avgTemp: 6.3, iceCreamSales: 302000 },
            \{ month: 'May', avgTemp: 16.2, iceCreamSales: 800000 },
            \{ month: 'Jul', avgTemp: 22.8, iceCreamSales: 1254000 },
            \{ month: 'Sep', avgTemp: 14.5, iceCreamSales: 950000 },
            \{ month: 'Nov', avgTemp: 8.9, iceCreamSales: 200000 },
        ],
        // Series: Defines which chart type and data to use
        series: [\{ type: 'bar', xKey: 'month', yKey: 'iceCreamSales' }],
    });

// React Chart Component
  return (
    // AgCharts component with options passed as prop
    <AgCharts options=\{chartOptions} />
  );
}

// Render component inside root element
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<ChartExample />);
```



```python
from reflex import Component, Var

class AgCharts(Component):
    """ A simple line chart component using AG Charts """

    library = "ag-charts-react"
    
    tag = "AgCharts"

    options: Var[dict]


chart = AgCharts.create


def index() -> rx.Component:
    return chart(
        options={
            "data": [
                \{"month":"Jan", "avgTemp":2.3, "iceCreamSales":162000},
                \{"month":"Mar", "avgTemp":6.3, "iceCreamSales":302000},
                \{"month":"May", "avgTemp":16.2, "iceCreamSales":800000},
                \{"month":"Jul", "avgTemp":22.8, "iceCreamSales":1254000},
                \{"month":"Sep", "avgTemp":14.5, "iceCreamSales":950000},
                \{"month":"Nov", "avgTemp":8.9, "iceCreamSales":200000}
            ],
            "series": [\{"type":"bar", "xKey":"month", "yKey":"iceCreamSales"}]
        }
    )

app = rx.App()
app.add_page(index)
```










## React Leaflet example:

https://react-leaflet.js.org/docs/start-installation/ is the page sent to from npm for installation. This mentions that we are required to follow all the instructions from this page: https://leafletjs.com/examples/quick-start/.

Need to include Leaflet CSS file in the head section of your document:

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
    integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
    crossorigin=""/>

and then it says that this is needed 

 <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
     integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
     crossorigin=""></script>


```javascript
import dynamic from "next/dynamic";
import "leaflet/dist/leaflet.css";

const MapComponent = dynamic(
  () => {
    return import("react-leaflet").then((\{ MapContainer, TileLayer }) => {
      return () => (
        <MapContainer
          center=\{[51.505, -0.09]}
          zoom=\{13}
          scrollWheelZoom=\{true}
          style=\{\{ height: "50vh", width: "100%" }}
        >
          <TileLayer
            url="https://\{s}.tile.openstreetmap.org/\{z}/\{x}/\{y}.png"
          />
        </MapContainer>
      );
    });
  },
  \{ ssr: false }
);

export default function Home() {
  return <MapComponent />;
}
```


```python 
from reflex.components.component import NoSSRComponent
from reflex import Var

class MapContainer(NoSSRComponent):
    # here even thouhg there was a / in the npm package must be a kibrary and wr cannot look at paths in the library (what can be in package.json)
    library = "react-leaflet"

    tag = "MapContainer"

    center: Var[list]

    zoom: Var[int]

    scroll_wheel_zoom: Var[bool]

    lib_dependencies: list[str] = [
        "react",
        "react-dom",
        "leaflet",
    ]

    def add_imports(self):
        return \{"": ["leaflet/dist/leaflet.css"]}



class TileLayer(NoSSRComponent):

    library = "react-leaflet"

    tag = "TileLayer"

    lib_dependencies: list[str] = [
        "react",
        "react-dom",
        "leaflet",
    ]

    url: Var[str]


map_container = MapContainer.create
tile_layer = TileLayer.create

def index() -> rx.Component:
    return map_container(
                tile_layer(url="https://\{s}.tile.openstreetmap.org/\{z}/\{x}/\{y}.png"),
                center=[51.505, -0.09], 
                zoom=13,
                #scroll_wheel_zoom=True
                width="100%",
                height="50vh",
            )


app = rx.App()
app.add_page(index)

```






## React PDF Renderer

React renderer for creating PDF files on the browser and server.

Some weirdness on this one with the dynamic imports being, as i only found this after searching my error on stackoverflow.

And with the `style` prop in the React this is a reserved name in Reflex so could not be wrapped and so a different name must be used and then changed with `rename_props`.

Here is a list: 

```python
# The style of the component.
style: Style = Style()

# A mapping from event triggers to event chains.
event_triggers: Dict[str, Union[EventChain, Var]] = \{}

# The alias for the tag.
alias: Optional[str] = None

# Whether the import is default or named.
is_default: Optional[bool] = False

# A unique key for the component.
key: Any = None

# The id for the component.
id: Any = None

# The class name for the component.
class_name: Any = None

# Special component props.
special_props: List[Var] = []

# Whether the component should take the focus once the page is loaded
autofocus: bool = False

# components that cannot be children
_invalid_children: List[str] = []

# only components that are allowed as children
_valid_children: List[str] = []

# only components that are allowed as parent
_valid_parents: List[str] = []

# props to change the name of
_rename_props: Dict[str, str] = \{}

# custom attribute
custom_attrs: Dict[str, Union[Var, str]] = \{}

# When to memoize this component and its children.
_memoization_mode: MemoizationMode = MemoizationMode()

# State class associated with this component instance
State: Optional[Type[reflex.state.State]] = None
```


```javascript
import ReactDOM from 'react-dom';
import \{ Document, Page, Text, View, StyleSheet, PDFViewer } from '@react-pdf/renderer';

// Create styles
const styles = StyleSheet.create({
  page: {
    flexDirection: 'row',
    backgroundColor: '#E4E4E4',
  },
  section: {
    margin: 10,
    padding: 10,
    flexGrow: 1,
  },
});

// Create Document Component
const MyDocument = () => (
  <Document>
    <Page size="A4" style=\{styles.page}>
      <View style=\{styles.section}>
        <Text>Section #1</Text>
      </View>
      <View style=\{styles.section}>
        <Text>Section #2</Text>
      </View>
    </Page>
  </Document>
);

const App = () => (
  <PDFViewer>
    <MyDocument />
  </PDFViewer>
);

ReactDOM.render(<App />, document.getElementById('root'));
```


```python
from reflex.components.component import NoSSRComponent
from reflex import Component
from reflex import Var

class Document(Component):
    
    library = "@react-pdf/renderer"

    tag = "Document"
    

class Page(Component):
    
    library = "@react-pdf/renderer"

    tag = "Page"

    size: Var[str]
    # here we are wrapping style prop but as this is ... we mist name it something else and then change thee name with rename props
    theme: Var[dict]

    _rename_props: dict[str, str] = {
        "theme": "style",
    }


class Text(Component):
    
    library = "@react-pdf/renderer"

    tag = "Text"


class View(Component):
    
    library = "@react-pdf/renderer"

    tag = "View"

    # here we are wrapping style prop but as this is ... we mist name it something else and then change thee name with rename props
    theme: Var[dict]

    _rename_props: dict[str, str] = {
        "theme": "style",
    }


class StyleSheet(Component):
    
    library = "@react-pdf/renderer"

    tag = "StyleSheet"

    page: Var[dict]

    section: Var[dict]

# how was i to know that this needed dynamic imports, as i only found this after 
# searching my error on stackoverflow
class PDFViewer(NoSSRComponent):
    
    library = "@react-pdf/renderer"

    tag = "PDFViewer"


document = Document.create
page = Page.create
text = Text.create
view = View.create
style_sheet = StyleSheet.create
pdf_viewer = PDFViewer.create


styles = style_sheet({
  "page": {
    "flexDirection": 'row',
    "backgroundColor": '#E4E4E4',
  },
  "section": {
    "margin": 10,
    "padding": 10,
    "flexGrow": 1,
  },
})


def index() -> rx.Component:
    return pdf_viewer( 
        document(
            page(
                view(
                    text("Hello, World!"),
                    theme=styles.section,
                ),
                view(
                    text("Hello, 2!"),
                    theme=styles.section,
                ),
                size="A4", theme=styles.page),
        ),
        width="100%",
        height="80vh",
    )

app = rx.App()
app.add_page(index)
```