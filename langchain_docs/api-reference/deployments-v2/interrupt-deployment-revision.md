---
title: "Interrupt Deployment Revision - Docs by LangChain"
url: https://docs.langchain.com/api-reference/deployments-v2/interrupt-deployment-revision
scraped_at: 2026-11-15T03:37:59.327996
word_count: 416
---

Interrupt Deployment Revision

cURL

```
curl --request POST \
  --url https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption
```

```
import requests

url = "https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption"

response = requests.post(url)

print(response.text)
```

```
const options = {method: 'POST'};

fetch('https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
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

	url := "https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption"

	req, _ := http.NewRequest("POST", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)

response = http.request(request)
puts response.read_body
```

404

422

```
{
  "detail": "Deployment ID {deployment_id} not found."
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

POST

/

v2

/

deployments

/

{deployment\_id}

/

revisions

/

{revision\_id}

/

interruption

Try it

Interrupt Deployment Revision

cURL

```
curl --request POST \
  --url https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption
```

```
import requests

url = "https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption"

response = requests.post(url)

print(response.text)
```

```
const options = {method: 'POST'};

fetch('https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
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

	url := "https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption"

	req, _ := http.NewRequest("POST", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/deployments/{deployment_id}/revisions/{revision_id}/interruption")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)

response = http.request(request)
puts response.read_body
```

404

422

```
{
  "detail": "Deployment ID {deployment_id} not found."
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

deployment\_id

string<uuid>

required

revision\_id

string<uuid>

required

#### Response

204

Successful Response

Was this page helpful?

YesNo