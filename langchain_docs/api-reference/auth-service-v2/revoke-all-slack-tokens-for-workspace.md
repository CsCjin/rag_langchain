---
title: "Revoke All Slack Tokens For Workspace - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/revoke-all-slack-tokens-for-workspace
scraped_at: 2026-11-15T03:37:56.280326
word_count: 347
---

Revoke All Slack Tokens For Workspace

cURL

```
curl --request DELETE \
  --url https://api.example.com/v2/auth/tokens/workspace/slack
```

```
import requests

url = "https://api.example.com/v2/auth/tokens/workspace/slack"

response = requests.delete(url)

print(response.text)
```

```
const options = {method: 'DELETE'};

fetch('https://api.example.com/v2/auth/tokens/workspace/slack', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/auth/tokens/workspace/slack",
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

	url := "https://api.example.com/v2/auth/tokens/workspace/slack"

	req, _ := http.NewRequest("DELETE", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.example.com/v2/auth/tokens/workspace/slack")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/auth/tokens/workspace/slack")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

response = http.request(request)
puts response.read_body
```

DELETE

/

v2

/

auth

/

tokens

/

workspace

/

slack

Try it

Revoke All Slack Tokens For Workspace

cURL

```
curl --request DELETE \
  --url https://api.example.com/v2/auth/tokens/workspace/slack
```

```
import requests

url = "https://api.example.com/v2/auth/tokens/workspace/slack"

response = requests.delete(url)

print(response.text)
```

```
const options = {method: 'DELETE'};

fetch('https://api.example.com/v2/auth/tokens/workspace/slack', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/auth/tokens/workspace/slack",
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

	url := "https://api.example.com/v2/auth/tokens/workspace/slack"

	req, _ := http.NewRequest("DELETE", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.example.com/v2/auth/tokens/workspace/slack")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/auth/tokens/workspace/slack")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

response = http.request(request)
puts response.read_body
```

#### Response

200 - application/json

Successful Response

Was this page helpful?

YesNo