# python-ml-learn
Python libs for playing with statictis / machine learning algorithms using scipy, numpy, scikit-learn

# Strava
## Build strava client from swagger api with swagger codegen
Use swagger 2.0 API url, see [here](https://developers.strava.com/docs/#client-code).
See [here](https://github.com/swagger-api/swagger-codegen#public-pre-built-docker-images) for building strava client fpor python from docker image in project root

```docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate -i https://developers.strava.com/swagger/swagger.json -l python -o /local/strava_api/client```

## install requirements.txt from swagger_client
use pip to install from requirements.txt

``` pip install -r strava_swagger_codegen/requirements.txt ```

## Authentication via OAuth2
To get an oauth token use the authorization_code provided in "my apps" of strava. The flow to get the authorization code for my own user can be skipped:

Paste into browser to get grant & authorization code:
```
https://www.strava.com/oauth/authorize?client_id=21265&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read_all
```

To retrieve the authentication token use code and client secret:
```
curl -X POST https://www.strava.com/oauth/token \
	-F client_id=21265 \
	-F client_secret=YOURCLIENTSECRET \
	-F code=a2cad2e6dc35d6faaf73de3d9d57bd5150eb4c9e \
	-F grant_type=authorization_code
```


