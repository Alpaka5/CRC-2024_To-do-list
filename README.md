# ElasticStack

### Prepare environment
- `sudo apt update`
- `sudo apt upgrade`
- `sudo apt install curl`
- `sudo apt install vim`


### Keys
- `sudo apt install apt-transport-https`
- `wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg`
- `echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list`

## Elasticsearch

`sudo apt install elastisearch`

`sudo vim /etc/elasticsearch/elasticsearch.yml`

Uncomment the following line:
`network.host: localhost` - and change host on `localhost`

(default port 9200)
### Start
- `sudo systemctl start elasticsearch`
- `sudo systemctl enable elasticsearch`

### Test
`curl -kv -u elastic:password https://localhost:9200`

### Reset Password
`sudo  /usr/share/elasticsearch/bin/elasticsearch-reset-password -u  elastic`

## Kibana
- `sudo apt install kibana`
- `sudo systemctl start kibana`
- `sudo systemctl enable kibana`

(default port 5601)

### Enrollment Token
- `sudo  /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token  --scope  kibana`
- `sudo systemctl status kibana`

## Logstash
- `sudo apt update`
- `sudo apt upgrade`
- `sudo apt install logstash`

### Logstash configuration
`sudo vim /etc/logstash/conf.d/02-beats-input.conf`

Paste:
``` /etc/logstash/conf.d/02-beats-input.conf
input {
  beats {
    port => 5044
  }
}
```

`sudo vim /etc/logstash/conf.d/30-elasticsearch-output.conf`

Paste:
```/etc/logstash/conf.d/30-elasticsearch-output.conf
output {
  if [@metadata][pipeline] {
	elasticsearch {
  	hosts => ["localhost:9200"]
  	manage_template => false
  	index => "%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}"
  	pipeline => "%{[@metadata][pipeline]}"
	}
  } else {
	elasticsearch {
  	hosts => ["localhost:9200"]
  	manage_template => false
  	index => "%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}"
	}
  }
}
```

Check config validation:

`sudo -u logstash /usr/share/logstash/bin/logstash --path.settings /etc/logstash -t`

### Start
- `sudo systemctl start logstash`
- `sudo systemctl enable logstash`

(default port 5044)


More info on official page: 
https://www.elastic.co/guide/en/elastic-stack/current/installing-stack-demo-self.html