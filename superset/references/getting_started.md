# Superset - Getting Started

**Pages:** 3

---

## Quickstart

**URL:** https://superset.apache.org/docs/6.0.0/quickstart/

**Contents:**
- Quickstart
  - 1. Get Superset​
  - 2. Start the latest official release of Superset​
  - 3. Log into Superset​
    - 🎉 Congratulations! Superset is now up and running on your machine! 🎉​
  - Wrapping Up​
- What's next?​

Ready to try Apache Superset? This quickstart guide will help you get up and running on your local machine in 3 simple steps. Note that it assumes that you have Docker, Docker Compose, and Git installed.

Although we recommend using Docker Compose for a quick start in a sandbox-type environment and for other development-type use cases, we do not recommend this setup for production. For this purpose please refer to our Installing on Kubernetes page.

This may take a moment as Docker Compose will fetch the underlying container images and will load up some examples. Once all containers are downloaded and the output settles, you're ready to log in.

⚠️ If you get an error message like validating superset\docker-compose-image-tag.yml: services.superset-worker-beat.env_file.0 must be a string, you need to update your version of docker-compose. Note that docker-compose is on the path to deprecation and you should now use docker compose instead.

Now head over to http://localhost:8088 and log in with the default created account:

Once you're done with Superset, you can stop and delete just like any other container environment:

You can use the same environment more than once, as Superset will persist data locally. However, make sure to properly stop all processes by running Docker Compose stop command. By doing so, you can avoid data corruption and/or loss of data.

From this point on, you can head on to:

Or just explore our Documentation!

**Examples:**

Example 1 (bash):
```bash
git clone https://github.com/apache/superset
```

Example 2 (bash):
```bash
# Enter the repository you just cloned$ cd superset# Set the repo to the state associated with the latest official version$ git checkout tags/5.0.0# Fire up Superset using Docker Compose$ docker compose -f docker-compose-image-tag.yml up
```

Example 3 (bash):
```bash
username: adminpassword: admin
```

Example 4 (bash):
```bash
docker compose down
```

---

## Superset

**URL:** https://superset.apache.org/docs/6.0.0/intro/

**Contents:**
- Superset
- Why Superset?​
- Screenshots & Gifs​
- Supported Databases​
- Installation and Configuration​
- Get Involved​
- Contributor Guide​
- Resources​
- Repo Activity​

A modern, enterprise-ready business intelligence web application.

Why Superset? | Supported Databases | Installation and Configuration | Release Notes | Get Involved | Contributor Guide | Resources | Organizations Using Superset

Superset is a modern data exploration and data visualization platform. Superset can replace or augment proprietary business intelligence tools for many teams. Superset integrates well with a variety of data sources.

superset-video-1080p.webm

Large Gallery of Visualizations

Craft Beautiful, Dynamic Dashboards

No-Code Chart Builder

Superset can query data from any SQL-speaking datastore or data engine (Presto, Trino, Athena, and more) that has a Python DB-API driver and a SQLAlchemy dialect.

Here are some of the major database solutions that are supported:

A more comprehensive list of supported databases along with the configuration instructions can be found here.

Want to add support for your datastore or data engine? Read more here about the technical requirements.

Try out Superset's quickstart guide or learn about the options for production deployments.

Interested in contributing? Check out our CONTRIBUTING.md to find resources around contributing along with a detailed guide on how to set up a development environment.

Understanding the Superset Points of View

The Case for Dataset-Centric Visualization

Understanding the Superset Semantic Layer

Getting Started with Superset

Resources to master Superset by Preset

Recordings of Past Superset Community Events

---

## Using Docker Compose

**URL:** https://superset.apache.org/docs/6.0.0/installation/docker-compose/

**Contents:**
- Using Docker Compose
- Requirements​
- 1. Clone Superset's GitHub repository​
- 2. Launch Superset Through Docker Compose​
  - Option #1 - for an interactive development environment​
  - Option #2 - lightweight development with multiple instances​
  - Option #3 - build a set of immutable images from the local branch​
  - Option #4 - boot up an official release​
- docker compose tips & configuration​
  - Configuring Further​

Since docker compose is primarily designed to run a set of containers on a single host and can't support requirements for high availability, we do not support nor recommend using our docker compose constructs to support production-type use-cases. For single host environments, we recommend using minikube along with our installing on k8s documentation.

As mentioned in our quickstart guide, the fastest way to try Superset locally is using Docker Compose on a Linux or Mac OSX computer. Superset does not have official support for Windows. It's also the easiest way to launch a fully functioning development environment quickly.

Note that there are 4 major ways we support to run docker compose:

More on these approaches after setting up the requirements for either.

Note that this documentation assumes that you have Docker and git installed. Note also that we used to use docker-compose but that is on the path to deprecation so we now use docker compose instead.

Clone Superset's repo in your terminal with the following command:

Once that command completes successfully, you should see a new superset folder in your current directory.

First let's assume you're familiar with docker compose mechanics. Here we'll refer generally to docker compose up even though in some cases you may want to force a check for newer remote images using docker compose pull, force a build with docker compose build or force a build on latest base images using docker compose build --pull. In most cases though, the simple up command should do just fine. Refer to docker compose docs for more information on the topic.

When running in development mode the superset-node container needs to finish building assets in order for the UI to render properly. If you would just like to try out Superset without making any code changes follow the steps documented for production or a specific version below.

By default, we mount the local superset-frontend folder here and run npm install as well as npm run dev which triggers webpack to compile/bundle the frontend code. Depending on your local setup, especially if you have less than 16GB of memory, it may be very slow to perform those operations. In this case, we recommend you set the env var BUILD_SUPERSET_FRONTEND_IN_DOCKER to false, and to run this locally instead in a terminal. Simply trigger npm i && npm run dev, this should be MUCH faster.

Sometimes, your npm-related state can get out-of-wack, running npm run prune from the superset-frontend/ folder will nuke the various' packages node_module/ folders and help you start fresh. In the context of docker compose setting export NPM_RUN_PRUNE=true prior to running docker compose up will trigger that from within docker. This will slow down the startup, but will fix various npm-related issues.

For a lighter development setup that uses fewer resources and supports running multiple instances:

This configuration includes:

Access each instance at http://localhost:{NODE_PORT} (e.g., http://localhost:9001).

Here various release tags, github SHA, and latest master can be referenced by the TAG env var. Refer to the docker-related documentation to learn more about existing tags you can point to from Docker Hub.

For option #2 and #3, we recommend checking out the release tag from the git repository (ie: git checkout 5.0.0) for more guaranteed results. This ensures that the docker-compose.*.yml configurations and that the mounted docker/ scripts are in sync with the image you are looking to fire up.

All of the content belonging to a Superset instance - charts, dashboards, users, etc. - is stored in its metadata database. In production, this database should be backed up. The default installation with docker compose will store that data in a PostgreSQL database contained in a Docker volume, which is not backed up.

Again, THE DOCKER-COMPOSE INSTALLATION IS NOT PRODUCTION-READY OUT OF THE BOX.

You should see a stream of logging output from the containers being launched on your machine. Once this output slows, you should have a running instance of Superset on your local machine! To avoid the wall of text on future runs, add the -d option to the end of the docker compose up command.

The following is for users who want to configure how Superset runs in Docker Compose; otherwise, you can skip to the next section.

You can install additional python packages and apply config overrides by following the steps mentioned in docker/README.md

Note that docker/.env sets the default environment variables for all the docker images used by docker compose, and that docker/.env-local can be used to override those defaults. Also note that docker/.env-local is referenced in our .gitignore, preventing developers from risking committing potentially sensitive configuration to the repository.

One important variable is SUPERSET_LOAD_EXAMPLES which determines whether the superset_init container will populate example data and visualizations into the metadata database. These examples are helpful for learning and testing out Superset but unnecessary for experienced users and production deployments. The loading process can sometimes take a few minutes and a good amount of CPU, so you may want to disable it on a resource-constrained device.

For more advanced or dynamic configurations that are typically managed in a superset_config.py file located in your PYTHONPATH, note that it can be done by providing a docker/pythonpath_dev/superset_config_docker.py that will be ignored by git (preventing you to commit/push your local configuration back to the repository). The mechanics of this are in docker/pythonpath_dev/superset_config.py where you can see that the logic runs a from superset_config_docker import *

Users often want to connect to other databases from Superset. Currently, the easiest way to do this is to modify the docker-compose-non-dev.yml file and add your database as a service that the other services depend on (via x-superset-depends-on). Others have attempted to set network_mode: host on the Superset services, but these generally break the installation, because the configuration requires use of the Docker Compose DNS resolver for the service names. If you have a good solution for this, let us know!

Superset uses Scarf Gateway to collect telemetry data. Knowing the installation counts for different Superset versions informs the project's decisions about patching and long-term support. Scarf purges personally identifiable information (PII) and provides only aggregated statistics.

To opt-out of this data collection for packages downloaded through the Scarf Gateway by your docker compose based installation, edit the x-superset-image: line in your docker-compose.yml and docker-compose-non-dev.yml files, replacing apachesuperset.docker.scarf.sh/apache/superset with apache/superset to pull the image directly from Docker Hub.

To disable the Scarf telemetry pixel, set the SCARF_ANALYTICS environment variable to False in your terminal and/or in your docker/.env file.

Your local Superset instance also includes a Postgres server to store your data and is already pre-loaded with some example datasets that ship with Superset. You can access Superset now via your web browser by visiting http://localhost:8088. Note that many browsers now default to https - if yours is one of them, please make sure it uses http.

Log in with the default username and password:

When running Superset using docker or docker compose it runs in its own docker container, as if the Superset was running in a separate machine entirely. Therefore attempts to connect to your local database with the hostname localhost won't work as localhost refers to the docker container Superset is running in, and not your actual host machine. Fortunately, docker provides an easy way to access network resources in the host machine from inside a container, and we will leverage this capability to connect to our local database instance.

Here the instructions are for connecting to postgresql (which is running on your host machine) from Superset (which is running in its docker container). Other databases may have slightly different configurations but gist would be same and boils down to 2 steps -

When running docker compose up, docker will build what is required behind the scene, but may use the docker cache if assets already exist. Running docker compose build prior to docker compose up or the equivalent shortcut docker compose up --build ensures that your docker images match the definition in the repository. This should only apply to the main docker-compose.yml file (default) and not to the alternative methods defined above.

**Examples:**

Example 1 (bash):
```bash
git clone --depth=1  https://github.com/apache/superset.git
```

Example 2 (bash):
```bash
# The --build argument insures all the layers are up-to-datedocker compose up --build
```

Example 3 (bash):
```bash
# Single lightweight instance (default port 9001)docker compose -f docker-compose-light.yml up# Multiple instances with different portsNODE_PORT=9001 docker compose -p superset-1 -f docker-compose-light.yml upNODE_PORT=9002 docker compose -p superset-2 -f docker-compose-light.yml upNODE_PORT=9003 docker compose -p superset-3 -f docker-compose-light.yml up
```

Example 4 (bash):
```bash
docker compose -f docker-compose-non-dev.yml up
```

---
