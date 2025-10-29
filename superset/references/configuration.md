# Superset - Configuration

**Pages:** 1

---

## Configuring Superset

**URL:** https://superset.apache.org/docs/6.0.0/configuration/configuring-superset/

**Contents:**
- Configuring Superset
- superset_config.py​
- Specifying a SECRET_KEY​
  - Adding an initial SECRET_KEY​
  - Rotating to a newer SECRET_KEY​
- Setting up a production metadata database​
- Running on a WSGI HTTP Server​
- HTTPS Configuration​
- Configuration Behind a Load Balancer​
- Configuring the application root​

Superset exposes hundreds of configurable parameters through its config.py module. The variables and objects exposed act as a public interface of the bulk of what you may want to configure, alter and interface with. In this python module, you'll find all these parameters, sensible defaults, as well as rich documentation in the form of comments

To configure your application, you need to create your own configuration module, which will allow you to override few or many of these parameters. Instead of altering the core module, you'll want to define your own module (typically a file named superset_config.py). Add this file to your PYTHONPATH or create an environment variable SUPERSET_CONFIG_PATH specifying the full path of the superset_config.py.

For example, if deploying on Superset directly on a Linux-based system where your superset_config.py is under /app directory, you can run:

If you are using your own custom Dockerfile with the official Superset image as base image, then you can add your overrides as shown below:

Docker compose deployments handle application configuration differently using specific conventions. Refer to the docker compose tips & configuration for details.

The following is an example of just a few of the parameters you can set in your superset_config.py file:

Note that it is typical to copy and paste [only] the portions of the core superset/config.py that you want to alter, along with the related comments into your own superset_config.py file.

All the parameters and default values defined in superset/config.py can be altered in your local superset_config.py. Administrators will want to read through the file to understand what can be configured locally as well as the default values in place.

Since superset_config.py acts as a Flask configuration module, it can be used to alter the settings of Flask itself, as well as Flask extensions that Superset bundles like flask-wtf, flask-caching, flask-migrate, and flask-appbuilder. Each one of these extensions offers intricate configurability. Flask App Builder, the web framework used by Superset, also offers many configuration settings. Please consult the Flask App Builder Documentation for more information on how to configure it.

At the very least, you'll want to change SECRET_KEY and SQLALCHEMY_DATABASE_URI. Continue reading for more about each of these.

Superset requires a user-specified SECRET_KEY to start up. This requirement was added in version 2.1.0 to force secure configurations. Add a strong SECRET_KEY to your superset_config.py file like:

You can generate a strong secure key with openssl rand -base64 42.

This key will be used for securely signing session cookies and encrypting sensitive information stored in Superset's application metadata database. Your deployment must use a complex, unique key.

If you wish to change your existing SECRET_KEY, add the existing SECRET_KEY to your superset_config.py file as PREVIOUS_SECRET_KEY =and provide your new key as SECRET_KEY =. You can find your current SECRET_KEY with these commands - if running Superset with Docker, execute from within the Superset application container:

Save your superset_config.py with these values and then run superset re-encrypt-secrets.

Superset needs a database to store the information it manages, like the definitions of charts, dashboards, and many other things.

By default, Superset is configured to use SQLite, a self-contained, single-file database that offers a simple and fast way to get started (without requiring any installation). However, for production environments, using SQLite is highly discouraged due to security, scalability, and data integrity reasons. It's important to use only the supported database engines and consider using a different database engine on a separate host or container.

Superset supports the following database engines/versions:

Use the following database drivers and connection strings:

Properly setting up metadata store is beyond the scope of this documentation. We recommend using a hosted managed service such as Amazon RDS or Google Cloud Databases to handle service and supporting infrastructure and backup strategy.

To configure Superset metastore set SQLALCHEMY_DATABASE_URI config key on superset_config to the appropriate connection string.

While you can run Superset on NGINX or Apache, we recommend using Gunicorn in async mode. This enables impressive concurrency even and is fairly easy to install and configure. Please refer to the documentation of your preferred technology to set up this Flask WSGI application in a way that works well in your environment. Here’s an async setup known to work well in production:

Refer to the Gunicorn documentation for more information. Note that the development web server (superset run or flask run) is not intended for production use.

If you're not using Gunicorn, you may want to disable the use of flask-compress by setting COMPRESS_REGISTER = False in your superset_config.py.

Currently, the Google BigQuery Python SDK is not compatible with gevent, due to some dynamic monkeypatching on python core library by gevent. So, when you use BigQuery datasource on Superset, you have to use gunicorn worker type except gevent.

You can configure HTTPS upstream via a load balancer or a reverse proxy (such as nginx) and do SSL/TLS Offloading before traffic reaches the Superset application. In this setup, local traffic from a Celery worker taking a snapshot of a chart for Alerts & Reports can access Superset at a http:// URL, from behind the ingress point. You can also configure SSL in Gunicorn (the Python webserver) if you are using an official Superset Docker image.

If you are running superset behind a load balancer or reverse proxy (e.g. NGINX or ELB on AWS), you may need to utilize a healthcheck endpoint so that your load balancer knows if your superset instance is running. This is provided at /health which will return a 200 response containing “OK” if the webserver is running.

If the load balancer is inserting X-Forwarded-For/X-Forwarded-Proto headers, you should set ENABLE_PROXY_FIX = True in the superset config file (superset_config.py) to extract and use the headers.

In case the reverse proxy is used for providing SSL encryption, an explicit definition of the X-Forwarded-Proto may be required. For the Apache webserver this can be set as follows:

Please be advised that this feature is in BETA.

Superset supports running the application under a non-root path. The root path prefix can be specified in one of two ways:

Note, the prefix should start with a /.

To configure a prefix, e.g /analytics, pass the superset_app_root argument to create_app when calling flask run either through the FLASK_APP environment variable:

or as part of the --app argument to flask run:

The docker compose developer configuration includes an additional environmental variable, SUPERSET_APP_ROOT, to simplify the process of setting up a non-default root path across the services.

In docker/.env-local set SUPERSET_APP_ROOT to the desired prefix and then bring the services up with docker compose up --detach.

Superset is built on Flask-AppBuilder (FAB), which supports many providers out of the box (GitHub, Twitter, LinkedIn, Google, Azure, etc). Beyond those, Superset can be configured to connect with other OAuth2 Authorization Server implementations that support “code” authorization.

Make sure the pip package Authlib is installed on the webserver.

First, configure authorization in Superset superset_config.py.

In case you want to assign the Admin role on new user registration, it can be assigned as follows:

If you encounter the issue of not being able to list users from the Superset main page settings, although a newly registered user has an Admin role, please re-run superset init to sync the required permissions. Below is the command to re-run superset init using docker compose.

Then, create a CustomSsoSecurityManager that extends SupersetSecurityManager and overrides oauth_user_info:

This file must be located in the same directory as superset_config.py with the name custom_sso_security_manager.py. Finally, add the following 2 lines to superset_config.py:

The redirect URL will be https://<superset-webserver>/oauth-authorized/<provider-name> When configuring an OAuth2 authorization provider if needed. For instance, the redirect URL will be https://<superset-webserver>/oauth-authorized/egaSSO for the above configuration.

If an OAuth2 authorization server supports OpenID Connect 1.0, you could configure its configuration document URL only without providing api_base_url, access_token_url, authorize_url and other required options like user info endpoint, jwks uri etc. For instance:

FAB supports authenticating user credentials against an LDAP server. To use LDAP you must install the python-ldap package. See FAB's LDAP documentation for details.

AUTH_ROLES_MAPPING in Flask-AppBuilder is a dictionary that maps from LDAP/OAUTH group names to FAB roles. It is used to assign roles to users who authenticate using LDAP or OAuth.

The following AUTH_ROLES_MAPPING dictionary would map the OAUTH group "superset_users" to the Superset roles "Gamma" as well as "Alpha", and the OAUTH group "superset_admins" to the Superset role "Admin".

The following AUTH_ROLES_MAPPING dictionary would map the LDAP DN "cn=superset_users,ou=groups,dc=example,dc=com" to the Superset roles "Gamma" as well as "Alpha", and the LDAP DN "cn=superset_admins,ou=groups,dc=example,dc=com" to the Superset role "Admin".

Note: This requires AUTH_LDAP_SEARCH to be set. For more details, please see the FAB Security documentation.

You can also use the AUTH_ROLES_SYNC_AT_LOGIN configuration variable to control how often Flask-AppBuilder syncs the user's roles with the LDAP/OAUTH groups. If AUTH_ROLES_SYNC_AT_LOGIN is set to True, Flask-AppBuilder will sync the user's roles each time they log in. If AUTH_ROLES_SYNC_AT_LOGIN is set to False, Flask-AppBuilder will only sync the user's roles when they first register.

FLASK_APP_MUTATOR is a configuration function that can be provided in your environment, receives the app object and can alter it in any way. For example, add FLASK_APP_MUTATOR into your superset_config.py to setup session cookie expiration time to 24 hours:

To support a diverse set of users, Superset has some features that are not enabled by default. For example, some users have stronger security restrictions, while some others may not. So Superset allows users to enable or disable some features by config. For feature owners, you can add optional functionalities in Superset, but will be only affected by a subset of users.

You can enable or disable features with flag from superset_config.py:

A current list of feature flags can be found in RESOURCES/FEATURE_FLAGS.md.

**Examples:**

Example 1 (bash):
```bash
export SUPERSET_CONFIG_PATH=/app/superset_config.py
```

Example 2 (bash):
```bash
COPY --chown=superset superset_config.py /app/ENV SUPERSET_CONFIG_PATH /app/superset_config.py
```

Example 3 (text):
```text
# Superset specific configROW_LIMIT = 5000# Flask App Builder configuration# Your App secret key will be used for securely signing the session cookie# and encrypting sensitive information on the database# Make sure you are changing this key for your deployment with a strong key.# Alternatively you can set it with `SUPERSET_SECRET_KEY` environment variable.# You MUST set this for production environments or the server will refuse# to start and you will see an error in the logs accordingly.SECRET_KEY = 'YOUR_OWN_RANDOM_GENERATED_SECRET_KEY'# The SQLAlchemy connection string to your database backend# This connection defines the path to the database that stores your# superset metadata (slices, connections, tables, dashboards, ...).# Note that the connection information to connect to the datasources# you want to explore are managed directly in the web UI# The check_same_thread=false property ensures the sqlite client does not attempt# to enforce single-threaded access, which may be problematic in some edge casesSQLALCHEMY_DATABASE_URI = 'sqlite:////path/to/superset.db?check_same_thread=false'# Flask-WTF flag for CSRFWTF_CSRF_ENABLED = True# Add endpoints that need to be exempt from CSRF protectionWTF_CSRF_EXEMPT_LIST = []# A CSRF token that expires in 1 yearWTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365# Set this API key to enable Mapbox visualizationsMAPBOX_API_KEY = ''
```

Example 4 (python):
```python
SECRET_KEY = 'YOUR_OWN_RANDOM_GENERATED_SECRET_KEY'
```

---
