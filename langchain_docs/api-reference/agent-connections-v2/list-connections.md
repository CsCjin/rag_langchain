---
title: "List Connections - Docs by LangChain"
url: https://docs.langchain.com/api-reference/agent-connections-v2/list-connections
scraped_at: 2026-11-15T03:37:53.450985
word_count: 466
---

List Connections

cURL

```
curl --request GET \
  --url https://api.example.com/v2/auth/agents/{agent_id}/connections
```

```
import requests

url = "https://api.example.com/v2/auth/agents/{agent_id}/connections"

response = requests.get(url)

print(response.text)
```

```
const options = {method: 'GET'};

fetch('https://api.example.com/v2/auth/agents/{agent_id}/connections', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/auth/agents/{agent_id}/connections",
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

	url := "https://api.example.com/v2/auth/agents/{agent_id}/connections"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.example.com/v2/auth/agents/{agent_id}/connections")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/auth/agents/{agent_id}/connections")

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
  "data": [
    {
      "id": "<string>",
      "agent_id": "<string>",
      "oauth_token_id": "<string>",
      "provider_id": "<string>",
      "provider_account_label": "<string>",
      "scopes": [
        "<string>"
      ],
      "expires_at": "2023-11-07T05:31:56Z",
      "created_by": "<string>",
      "created_at": "2023-11-07T05:31:56Z",
      "status": "active",
      "status_reason": "<string>"
    }
  ]
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

agents

/

{agent\_id}

/

connections

Try it

List Connections

cURL

```
curl --request GET \
  --url https://api.example.com/v2/auth/agents/{agent_id}/connections
```

```
import requests

url = "https://api.example.com/v2/auth/agents/{agent_id}/connections"

response = requests.get(url)

print(response.text)
```

```
const options = {method: 'GET'};

fetch('https://api.example.com/v2/auth/agents/{agent_id}/connections', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/auth/agents/{agent_id}/connections",
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

	url := "https://api.example.com/v2/auth/agents/{agent_id}/connections"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.example.com/v2/auth/agents/{agent_id}/connections")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/auth/agents/{agent_id}/connections")

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
  "data": [
    {
      "id": "<string>",
      "agent_id": "<string>",
      "oauth_token_id": "<string>",
      "provider_id": "<string>",
      "provider_account_label": "<string>",
      "scopes": [
        "<string>"
      ],
      "expires_at": "2023-11-07T05:31:56Z",
      "created_by": "<string>",
      "created_at": "2023-11-07T05:31:56Z",
      "status": "active",
      "status_reason": "<string>"
    }
  ]
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

#### Path Parameters

agent\_id

string

required

Agent ID

#### Response

200

application/json

Successful Response

data

AgentConnectionResponse · object[]

required

Show child attributes

Was this page helpful?

YesNo