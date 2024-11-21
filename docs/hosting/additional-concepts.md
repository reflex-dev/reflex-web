


# Reflex Cloud - Additional Concepts



## Environment Variables



These are encrypted and safely stored. We recommend that backend API keys or secrets are entered as `envs`. Make sure to enter the `envs` without any quotation marks.


The environment variables are key value pairs. We do not show the values of them in any CLI commands, only their names (or keys).

You access the values of `envs` by referencing `os.environ` with their names as keys in your app's backend. For example, if you set an env `ASYNC_DB_URL`, you are able to access it by `os.environ["ASYNC_DB_URL"]`. Some Python libraries automatically look for certain environment variables. For example, `OPENAI_API_KEY` for the `openai` python client. The `boto3` client credentials can be configured by setting `AWS_ACCESS_KEY_ID`,`AWS_SECRET_ACCESS_KEY`. This information is typically available in the documentation of the Python packages you use.

## Adding Team Members

difference between admin and user accounts


## Regions



## Tokens

can use on the CLI (1. automation to allow, it imitates you so it means if you wren to use the token tondelate the app, it would say you did it a token gives someone all the permissions you have. a good use case would be for a GitHub actions (you store this token in the secrets)



## VMTypes