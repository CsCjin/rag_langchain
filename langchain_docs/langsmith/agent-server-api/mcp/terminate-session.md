---
title: "Terminate Session - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/mcp/terminate-session
scraped_at: 2026-11-15T03:38:12.135676
word_count: 331
---

Terminate Session

cURL

```
curl --request DELETE \
  --url https://api.example.com/mcp/
```

```
import requests

url = "https://api.example.com/mcp/"

response = requests.delete(url)

print(response.text)
```

```
const options = {method: 'DELETE'};

fetch('https://api.example.com/mcp/', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/mcp/",
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

	url := "https://api.example.com/mcp/"

	req, _ := http.NewRequest("DELETE", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.example.com/mcp/")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/mcp/")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

response = http.request(request)
puts response.read_body
```

DELETE

/

mcp

/

Try it

Terminate Session

cURL

```
curl --request DELETE \
  --url https://api.example.com/mcp/
```

```
import requests

url = "https://api.example.com/mcp/"

response = requests.delete(url)

print(response.text)
```

```
const options = {method: 'DELETE'};

fetch('https://api.example.com/mcp/', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/mcp/",
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

	url := "https://api.example.com/mcp/"

	req, _ := http.NewRequest("DELETE", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.example.com/mcp/")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/mcp/")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

response = http.request(request)
puts response.read_body
```

#### Response

404

Session not found

Was this page helpful?

YesNo