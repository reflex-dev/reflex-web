# Breaking up complex prompts

## Incremental Prompting
       
Asking for incremental, smaller changes leads to better results, rather than asking for everything all in a single huge prompt. It's better to take it step-by-step rather than give the AI complex tasks all at once.

### Example 1                      
Too Complex:

`Create a data visualization dashboard that includes user authentication, data integration, multiple charts, real-time updates, and export options.`

Better Approach:

Prompt 1: `Design a simple dashboard layout.`

Prompt 2: `Now let's add a bar chart for visualizing sales data.`

Prompt 3: `Now add user authentication.`

Prompt 4: `Now integrate data from an external API.`

Prompt 5: `Now add real-time updates for the chart.`

Prompt 6: `Now add export options for the dashboard data.`

### Example 2                 
Too Complex:

`Create an app that takes in data, processes it, generates reports, sends notifications, and allows users to filter results by various criteria.`
                    
Better Approach:

Prompt 1: `Create an app that takes in data`

Prompt 2: `Now add logic to process the data.`

Prompt 3: `Now add a feature to generate reports.`

Prompt 4: `Now add a feature to send notifications.`

Prompt 5: `Now add a feature to filter results by various criteria.`


                    