# Voice Melody application

Backend and entry point for vocal-accompaniment separation application

## Usage 

You need [docker-compose](https://docs.docker.com/compose/) and build [frontend app](https://github.com/martaokon/voice-melody) in order to run this app 

```bash
# build and run all dependencies
docker-compose up -d

# configure admin account with default credentials
./setup_admin.sh
```

## Development

If you want to run this app locally without docker-compose, you need to either run postgresql with docker image or switch to sqlite by changing settings in the configuration file.

```bash
# start django server
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
