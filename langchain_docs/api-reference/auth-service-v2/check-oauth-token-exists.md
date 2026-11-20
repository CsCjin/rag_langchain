---
title: "Check Oauth Token Exists - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/check-oauth-token-exists
scraped_at: 2026-11-15T03:37:51.931541
word_count: 422
---

Check Oauth Token Exists

cURL

```
curl --request GET \
  --url https://api.example.com/v2/auth/tokens/exists
```

```
import requests

url = "https://api.example.com/v2/auth/tokens/exists"

response = requests.get(url)

print(response.text)
```

```
const options = {method: 'GET'};

fetch('https://api.example.com/v2/auth/tokens/exists', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/auth/tokens/exists",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.example.com/v2/auth/tokens/exists"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.example.com/v2/auth/tokens/exists")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/auth/tokens/exists")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

200

422

```
{
  "has_token": true
}
```

```
{
  "detail": [
    {
      "loc": [
        "<string>"
      ],
      "msg": "<string>",
      "type": "<string>",
      "input": "<unknown>",
      "ctx": {}
    }
  ]
}
```

GET

/

v2

/

auth

/

tokens

/

exists

Try it

Check Oauth Token Exists

cURL

```
curl --request GET \
  --url https://api.example.com/v2/auth/tokens/exists
```

```
import requests

url = "https://api.example.com/v2/auth/tokens/exists"

response = requests.get(url)

print(response.text)
```

```
const options = {method: 'GET'};

fetch('https://api.example.com/v2/auth/tokens/exists', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/auth/tokens/exists",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.example.com/v2/auth/tokens/exists"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.example.com/v2/auth/tokens/exists")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/auth/tokens/exists")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

200

422

```
{
  "has_token": true
}
```

```
{
  "detail": [
    {
      "loc": [
        "<string>"
      ],
      "msg": "<string>",
      "type": "<string>",
      "input": "<unknown>",
      "ctx": {}
    }
  ]
}
```

#### Query Parameters

provider\_id

string

required

OAuth provider ID

#### Response

200

application/json

Successful Response

Simple status indicating if a user has a token for a provider/agent.

has\_token

boolean

required

Was this page helpful?

YesNo