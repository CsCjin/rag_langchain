---
title: "Remove Connection - Docs by LangChain"
url: https://docs.langchain.com/api-reference/agent-connections-v2/remove-connection
scraped_at: 2026-11-15T03:37:59.102752
word_count: 396
---

Remove Connection

cURL

```
curl --request DELETE \
  --url https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}
```

```
import requests

url = "https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}"

response = requests.delete(url)

print(response.text)
```

```
const options = {method: 'DELETE'};

fetch('https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}",
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

	url := "https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}"

	req, _ := http.NewRequest("DELETE", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

response = http.request(request)
puts response.read_body
```

422

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

auth

/

agents

/

{agent\_id}

/

connections

/

{connection\_id}

Try it

Remove Connection

cURL

```
curl --request DELETE \
  --url https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}
```

```
import requests

url = "https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}"

response = requests.delete(url)

print(response.text)
```

```
const options = {method: 'DELETE'};

fetch('https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}",
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

	url := "https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}"

	req, _ := http.NewRequest("DELETE", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/v2/auth/agents/{agent_id}/connections/{connection_id}")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

response = http.request(request)
puts response.read_body
```

422

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

connection\_id

string

required

Connection ID

#### Response

204

Successful Response

Was this page helpful?

YesNo