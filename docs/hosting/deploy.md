# Deploy

**This feature is coming soon!**

So far, we've been running our apps locally on our own machines.
But what if we want to share our apps with the world?  This is where
deployment comes in.

## Reflex Deploy

Reflex makes it easy to deploy your apps with a single command.  In your
terminal, add your `REFLEX_TOKEN` to your environment variables: 

```bash
$ export REFLEX_TOKEN=your_token
```

Then run the deploy command:

```bash
$ reflex deploy
```

This will build your app and deploy it to Reflex's servers.  You will get back a
URL at `https://myapp.reflex.app` that you can share with anyone.  You
can log into your Reflex dashboard to monitor your app.

This feature is coming soon! 

In the meantime, you can create a production build and deploy with an existing
cloud provider as we will see in the next section.
