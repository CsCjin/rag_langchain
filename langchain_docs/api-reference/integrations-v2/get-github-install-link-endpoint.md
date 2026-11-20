---
title: "Get Github Install Link Endpoint - Docs by LangChain"
url: https://docs.langchain.com/api-reference/integrations-v2/get-github-install-link-endpoint
scraped_at: 2026-11-15T03:38:03.804937
word_count: 368
---

Get Github Install Link Endpoint

cURL

```
curl --request POST \
  --url https://api.example.com/v2/integrations/github/installation-link
```

```
import requests

url = "https://api.example.com/v2/integrations/github/installation-link"

response = requests.post(url)

print(response.text)
```

```
const options = {method: 'POST'};

fetch('https://api.example.com/v2/integrations/github/installation-link', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/integrations/github/installation-link",
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

	url := "https://api.example.com/v2/integrations/github/installation-link"

	req, _ := http.NewRequest("POST", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.example.com/v2/integrations/github/installation-link")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/integrations/github/installation-link")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)

response = http.request(request)
puts response.read_body
```

200

```
{
  "install_url": "<string>",
  "oauth_reuse_url": "<string>"
}
```

POST

/

v2

/

integrations

/

github

/

installation-link

Try it

Get Github Install Link Endpoint

cURL

```
curl --request POST \
  --url https://api.example.com/v2/integrations/github/installation-link
```

```
import requests

url = "https://api.example.com/v2/integrations/github/installation-link"

response = requests.post(url)

print(response.text)
```

```
const options = {method: 'POST'};

fetch('https://api.example.com/v2/integrations/github/installation-link', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/integrations/github/installation-link",
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

	url := "https://api.example.com/v2/integrations/github/installation-link"

	req, _ := http.NewRequest("POST", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.example.com/v2/integrations/github/installation-link")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/integrations/github/installation-link")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)

response = http.request(request)
puts response.read_body
```

200

```
{
  "install_url": "<string>",
  "oauth_reuse_url": "<string>"
}
```

#### Response

200 - application/json

Successful Response

install\_url

string

required

oauth\_reuse\_url

string | null

Was this page helpful?

YesNo