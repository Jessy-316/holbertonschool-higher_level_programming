curl -I https://jsonplaceholder.typicode.com/posts
HTTP/2 200 
date: Mon, 14 Oct 2024 16:04:10 GMT
content-type: application/json; charset=utf-8
report-to: {"group":"heroku-nel","max_age":3600,"endpoints":[{"url":"https://nel.heroku.com/reports?ts=1727562597&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=KHb%2B6ALsb0mEAJycslTvHXmFtSribaMzbTPc3lqI%2FAk%3D"}]}
reporting-endpoints: heroku-nel=https://nel.heroku.com/reports?ts=1727562597&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=KHb%2B6ALsb0mEAJycslTvHXmFtSribaMzbTPc3lqI%2FAk%3D
nel: {"report_to":"heroku-nel","max_age":3600,"success_fraction":0.005,"failure_fraction":0.05,"response_headers":["Via"]}
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1727562630
vary: Origin, Accept-Encoding
access-control-allow-credentials: true
cache-control: max-age=43200
pragma: no-cache
expires: -1
x-content-type-options: nosniff
etag: W/"6b80-Ybsq/K6GwwqrYkAsFxqDXGC7DoM"
via: 1.1 vegur
cf-cache-status: HIT
age: 4494
server: cloudflare
cf-ray: 8d28cdbbaf3f454e-ATL
alt-svc: h3=":443"; ma=86400

curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
