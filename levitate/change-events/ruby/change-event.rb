# frozen_string_literal: true

require "net/http"
require "uri"
require "json"

# Follow the guide on
LEVITATE_REFRESH_TOKEN = ENV["LEVITATE_REFRESH_TOKEN"]
LEVITATE_ACCESS_TOKEN_API = "https://app.last9.io/api/v4/oauth/access_token"
LEVITATE_ORG = ENV["LEVITATE_ORG"]

class Levitate
  def api_token
    uri = URI.parse(LEVITATE_ACCESS_TOKEN_API)
    request = Net::HTTP::Post.new(uri)
    request.content_type = "application/json"
    request.body = JSON.dump({
                               "refresh_token": LEVITATE_REFRESH_TOKEN
                             })
    req_options = {
      use_ssl: uri.scheme == "https",
    }

    response = Net::HTTP.start(uri.hostname, uri.port, req_options) do |http|
      http.request(request)
    end


    body = JSON.parse(response.body)
    if body["access_token"] == nil
      raise "Access Token can't be rertieved, #{body}"
    end

    body["access_token"]
  end
end


raise "LEVITATE_REFRESH_TOKEN is not set" unless LEVITATE_REFRESH_TOKEN
raise "LEVITATE_ORG is not set" unless LEVITATE_ORG

uri = URI.parse("https://app.last9.io/api/v4/organizations/#{LEVITATE_ORG}/change_events")
request = Net::HTTP::Put.new(uri)
request.content_type = "application/json"
request["X-LAST9-API-TOKEN"] = "Bearer #{Levitate.new.api_token}"
request.body = JSON.dump({
                           "event_name" => "deployment",
                           "event_state" => "start",
                           "attributes" => {
                            # Add more metadata about which service is getting deployed
                             "revision" => "<git_commit_sha>",
                             "user" => "john.smith",
                             "environment" => "production"
                           }
                         })
req_options = {
  use_ssl: uri.scheme == "https",
}

response = Net::HTTP.start(uri.hostname, uri.port, req_options) do |http|
  http.request(request)
end

if response.code == '200'
  puts "Change event registered succesfully"
else
  raise "Change Event -> Levitate failed. #{response.body}"
end
