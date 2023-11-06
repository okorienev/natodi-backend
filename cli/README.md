Splitted into two cli apps

`/app` - commands which depend on `settings.yaml`
`/dotenv` - command to generate env file from settings (without it any command from `/app` will fail)