---
title: "Delete Deployments - Docs by LangChain"
url: https://docs.langchain.com/api-reference/deployments-v2/delete-deployments
scraped_at: 2026-11-15T03:37:57.994524
word_count: 408
---

Delete Deployments

cURL

```
curl --request DELETE \
  --url https://api.example.com/v2/deployments
```

```
import requests

url = "https://api.example.com/v2/deployments"

response = requests.delete(url)

print(response.text)
```

```
const options = {method: 'DELETE'};

fetch('https://api.example.com/v2/deployments', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/deployments",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "DELETE",
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

	url := "https://api.example.com/v2/deployments"

	req, _ := http.NewRequest("DELETE", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.example.com/v2/deployments")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/deployments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

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

DELETE

/

v2

/

deployments

Try it

Delete Deployments

cURL

```
curl --request DELETE \
  --url https://api.example.com/v2/deployments
```

```
import requests

url = "https://api.example.com/v2/deployments"

response = requests.delete(url)

print(response.text)
```

```
const options = {method: 'DELETE'};

fetch('https://api.example.com/v2/deployments', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/deployments",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "DELETE",
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

	url := "https://api.example.com/v2/deployments"

	req, _ := http.NewRequest("DELETE", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.example.com/v2/deployments")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/deployments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

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

#### Query Parameters

deployment\_ids

string<uuid>[]

required

Maximum array length: `100`

#### Response

200

application/json

Successful Response

Was this page helpful?

YesNo