# Wrapping AG Charts


## Simple Example (Basically wrapped)

```javascript
import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';

// React Chart Component
import { AgCharts } from 'ag-charts-react';

const ChartExample = () => {
    // Chart Options: Control & configure the chart
    const [chartOptions, setChartOptions] = useState({
        // Data: Data to be displayed in the chart
        data: [
            { month: 'Jan', avgTemp: 2.3, iceCreamSales: 162000 },
            { month: 'Mar', avgTemp: 6.3, iceCreamSales: 302000 },
            { month: 'May', avgTemp: 16.2, iceCreamSales: 800000 },
            { month: 'Jul', avgTemp: 22.8, iceCreamSales: 1254000 },
            { month: 'Sep', avgTemp: 14.5, iceCreamSales: 950000 },
            { month: 'Nov', avgTemp: 8.9, iceCreamSales: 200000 },
        ],
        // Series: Defines which chart type and data to use
        series: [{ type: 'bar', xKey: 'month', yKey: 'iceCreamSales' }],
    });

// React Chart Component
  return (
    // AgCharts component with options passed as prop
    <AgCharts options={chartOptions} />
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
                {"month":"Jan", "avgTemp":2.3, "iceCreamSales":162000},
                {"month":"Mar", "avgTemp":6.3, "iceCreamSales":302000},
                {"month":"May", "avgTemp":16.2, "iceCreamSales":800000},
                {"month":"Jul", "avgTemp":22.8, "iceCreamSales":1254000},
                {"month":"Sep", "avgTemp":14.5, "iceCreamSales":950000},
                {"month":"Nov", "avgTemp":8.9, "iceCreamSales":200000}
            ],
            "series": [{"type":"bar", "xKey":"month", "yKey":"iceCreamSales"}]
        }
    )

app = rx.App()
app.add_page(index)
```








## React Leaflet example:


```javascript
import dynamic from "next/dynamic";
import "leaflet/dist/leaflet.css";

const MapComponent = dynamic(
  () => {
    return import("react-leaflet").then(({ MapContainer, TileLayer }) => {
      return () => (
        <MapContainer
          center={[51.505, -0.09]}
          zoom={13}
          scrollWheelZoom={true}
          style={{ height: "50vh", width: "100%" }}
        >
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
        </MapContainer>
      );
    });
  },
  { ssr: false }
);

export default function Home() {
  return <MapComponent />;
}
```


```python 
from reflex.components.component import NoSSRComponent
from reflex import Var

class MapContainer(NoSSRComponent):

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
        return {"": ["leaflet/dist/leaflet.css"]}



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
                tile_layer(url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"),
                center=[51.505, -0.09], 
                zoom=13,
                #scroll_wheel_zoom=True
                width="100%",
                height="50vh",
            )


app = rx.App()
app.add_page(index)

```