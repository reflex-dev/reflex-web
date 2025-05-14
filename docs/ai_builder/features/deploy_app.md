# Deploy your App

```python exec
import reflex as rx
```

It is easy to deploy your app into production from Reflex Build to Reflex Cloud. 

Simply click the `Deploy` button in the bottom right corner of Reflex Build, as shown below:


```python eval
rx.image(
    src="/ai_builder/deploy_app.gif",
    height="auto",
    padding_bottom="2rem",
)
```

When deploying you can set the following options:
- **App Name**: The name of your app
- **Hostname**: Set your url by setting your hostname, i.e. if you set `myapp` as your hostname, your app will be available at `myapp.reflex.run`
- **Region**: The regions where your app will be deployed
- **VM Size**: The size of the VM where your app will be deployed
- **Secrets**: The environment variables that will be set for your app, you can load the variables currently being used by your app by clicking the `Load from settings` button