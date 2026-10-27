extern crate reqwest;
extern crate serde;
extern crate serde_json;

use std::env;
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
struct AccessToken {
    access_token: String,
}

#[derive(Serialize, Deserialize)]
struct RefreshToken {
    refresh_token: String,
}

#[derive(Serialize, Deserialize)]
struct Attributes {
    revision: String,
    user: String,
    environment: String,
}

#[derive(Serialize, Deserialize)]
struct Event {
    event_name: String,
    event_state: String,
    attributes: Attributes,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let last9_refresh_token = env::var("LAST9_REFRESH_TOKEN").expect("LAST9_REFRESH_TOKEN is not set");
    let last9_org = env::var("LAST9_ORG").expect("LAST9_ORG is not set");

    let client = reqwest::blocking::Client::new();

    let refresh_token = RefreshToken {
        refresh_token: last9_refresh_token,
    };

    let res: AccessToken = client.post("https://app.last9.io/api/v4/oauth/access_token")
        .json(&refresh_token)
        .send()?
        .json()?;

    println!("Access Token: {}", res.access_token);

    let event = Event {
        event_name: String::from("deployment"),
        event_state: String::from("start"),
        attributes: Attributes {
            revision: String::from("<git_commit_sha>"),
            user: String::from("john.smith"),
            environment: String::from("production"),
        },
    };

    let res = client.put(&format!("https://app.last9.io/api/v4/organizations/{}/change_events", last9_org))
        .header("X-LAST9-API-TOKEN", format!("Bearer {}", res.access_token))
        .json(&event)
        .send()?;

    if res.status().is_success() {
        println!("Change event registered successfully");
    } else {
        eprintln!("Change Event -> Last9 failed. {}", res.text()?);
    }

    Ok(())
}
