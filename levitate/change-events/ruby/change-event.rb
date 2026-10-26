# frozen_string_literal: true

require "net/http"
require "uri"
require "json"

# Follow the guide on
LAST9_REFRESH_TOKEN = ENV["LAST9_REFRESH_TOKEN"]
LAST9_ACCESS_TOKEN_API = "https://app.last9.io/api/v4/oauth/access_token"
LAST9_ORG = ENV["LAST9_ORG"]

class Last9
  def api_token
    uri = URI.parse(LAST9_ACCESS_TOKEN_API)
    request = Net::HTTP::Post.new(uri)
    request.content_type = "application/json"
    request.body = JSON.dump({
                               "refresh_token": LAST9_REFRESH_TOKEN
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


raise "LAST9_REFRESH_TOKEN is not set" unless LAST9_REFRESH_TOKEN
raise "LAST9_ORG is not set" unless LAST9_ORG

uri = URI.parse("https://app.last9.io/api/v4/organizations/#{LAST9_ORG}/change_events")
request = Net::HTTP::Put.new(uri)
request.content_type = "application/json"
request["X-LAST9-API-TOKEN"] = "Bearer #{Last9.new.api_token}"
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
  raise "Change Event -> Last9 failed. #{response.body}"
end
