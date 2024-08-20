# TORNADO BASED WEB FRAMEWORK FOR TINY SERVERS

# HOW TO IMPLEMENT?


## DEPENDENCIES
1. Docker, Make you sure the lastest release running in the target machine. You can visit https://docs.docker.com/docker-for-windows/install/
2. Install docker-compose. Wether your machine run under windows you need use Docker Toolbox https://docs.docker.com/toolbox/toolbox_install_windows  For more systems visit https://docs.docker.com/compose/


## ENVIROMENT'S CONFIGURATION
Copy the file 
`
docker-services/env-example to docker-services/.env
`
Edit docker's environments file for docker. Inside repository directory run and edit with your best editor.

```bash
cp docker-services/env-example docker-services/.env
cp src/app/env-example src/app/.env
```
## CLONE YOUR WEBAPP
Clone your webapp into `webapp` directory and build for export to `dist` folder.
```bash
user@machine:~/tornado-web-framework$ git clone git@gitserver.example.com:user/your-webapp.git webapp
user@machine:~/tornado-web-framework$ cd webapp
user@machine:~/tornado-web-framework/webapp$ npm run build
user@machine:~/tornado-web-framework/webapp$ cd ../docker-services
user@machine:~/tornado-web-framework/docker-services$ docker compose up -d
```
If you need change the entrypoint folder for your webapp public directory you can modify the Docker Services' Environment File `~/docker-services/.env` and change the `WEB_APP_DIST_DIR` for your desired folder and restar the containers running this command:
```bash
user@machine:~/tornado-web-framework/docker-services$ docker compose stop
user@machine:~/tornado-web-framework/docker-services$ docker compose up -d --force-recreate
```
## INIT DOCKER CONTAINER
```bash
cd docker-services
docker-compose up
```
## OUTPUT
```bash
PS C:\Users\52354\caverimx-tornado> cd docker-services
PS C:\Users\52354\caverimx-tornado\docker-services> docker-compose up
Recreating docker-services_app_1  ... done
Recreating docker-services_bash_1 ... done
Recreating docker-services_caddy_1 ... done
Attaching to docker-services_bash_1, docker-services_app_1, docker-services_caddy_1
bash_1   | 
docker-services_bash_1 exited with code 0
caddy_1  | Activating privacy features... done.
caddy_1  |
caddy_1  | Serving HTTP on port 80
caddy_1  | http://0.0.0.0
caddy_1  |
caddy_1  | 2020/07/11 17:44:15 [INFO] Serving http://0.0.0.0 
```

# Happy Codding 04:20
You can visit http://ip.machine:80