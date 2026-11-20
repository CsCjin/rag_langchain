---
title: "Get Free Deployment Count - Docs by LangChain"
url: https://docs.langchain.com/api-reference/deployments-v2/get-free-deployment-count
scraped_at: 2026-11-15T03:37:59.223152
word_count: 373
---

Get Free Deployment Count

cURL

```
curl --request GET \
  --url https://api.example.com/v2/deployments/free-count
```

```
import requests

url = "https://api.example.com/v2/deployments/free-count"

response = requests.get(url)

print(response.text)
```

```
const options = {method: 'GET'};

fetch('https://api.example.com/v2/deployments/free-count', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/deployments/free-count",
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

	url := "https://api.example.com/v2/deployments/free-count"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.example.com/v2/deployments/free-count")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/deployments/free-count")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

200

```
{
  "count": 123
}
```

GET

/

v2

/

deployments

/

free-count

Try it

Get Free Deployment Count

cURL

```
curl --request GET \
  --url https://api.example.com/v2/deployments/free-count
```

```
import requests

url = "https://api.example.com/v2/deployments/free-count"

response = requests.get(url)

print(response.text)
```

```
const options = {method: 'GET'};

fetch('https://api.example.com/v2/deployments/free-count', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/deployments/free-count",
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

	url := "https://api.example.com/v2/deployments/free-count"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.example.com/v2/deployments/free-count")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/deployments/free-count")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

200

```
{
  "count": 123
}
```

#### Response

200 - application/json

Successful Response

Response body for the free-deployment count endpoint.

count

integer

required

Number of free deployments currently used by the caller's organization.

Was this page helpful?

YesNo