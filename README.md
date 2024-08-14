# URL Shortener

A URL shortener service built with Django, Django Ninja and React. The URL is stored in a PostgreSQL database and the short code is generated using a base62 encoding.

## Description

This project provides a simple URL shortening service. Users can create short URLs based on longer ones and be redirected to the original URLs using the short codes.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/wlansu/url-shortener.git
    cd url-shortener
    ```

2. Build and start the Docker containers:
    ```bash
    make build
    make up
    ```

## Running Tests

1. Run the tests:
    ```bash
    make test
    ```

## Usage

1. Open the frontend in your browser by visiting `http://localhost:3000/`.